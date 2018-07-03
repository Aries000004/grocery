
import json
from collections import defaultdict

import scrapy

from weiboSpider.items import WeiboFansSpider


class WeiboFans(scrapy.Spider):

    name = 'fans'

    def start_requests(self):
        uid = '1749127163'

        url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_1831216671&luicode=10000011&lfid=1076031831216671'

        for i in range(1, 20):
            if i > 1:
                url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_1831216671&luicode=10000011&lfid=1076031831216671&since_id=%s'
                url = url % str(i)
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        res = json.loads(response.text)
        item = WeiboFansSpider()

        # cards 列表
        cards = res.get('data').get('cards')
        # 粉丝分类, 及对应的分类下的 前几个
        group_name_fans = defaultdict(list)
        for fans_group in cards:
            id = fans_group.get('card_group')[0].get('user').get('id')
            screen_name = fans_group.get('card_group')[0].get('user').get('screen_name')

            group_name_fans[fans_group.get('title')].append((id, screen_name))

        return group_name_fans
