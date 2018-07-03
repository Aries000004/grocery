
import scrapy
import json
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule, CrawlSpider

from weiboSpider.items import WeibospiderItem


class WeoboSpider(scrapy.Spider):

    name = 'weibo'
    uid = '1831216671'

    start_urls = {
        r'https://m.weibo.cn/api/container/getIndex?uid=%s&containerid=100505%s' % (uid, uid)
    }


    def start_requests(self):
        pass

    def parse(self, response):
        data = json.loads(response.text)
        userInfo = data['data']['userInfo']
        id = userInfo['id']
        name = userInfo['screen_name']
        # 简介  职业 代表作
        intro = userInfo['verified_reason']
        # 他的关注 数量
        follow_count = userInfo['follow_count']
        # 他的粉丝数量
        followers_count = userInfo['followers_count']
        pass






