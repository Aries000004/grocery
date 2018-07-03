
import scrapy
import json

from scrapy import Request

from weiboSpider.items import WeiboUserItem


class WeoboSpider(scrapy.Spider):

    name = 'weibo'
    user_url = r'https://m.weibo.cn/api/container/getIndex?uid={uid}&containerid=100505{uid}'
    uids = [
        '1831216671', # 黄磊
        '1749127163', # 雷军
    ]

    def start_requests(self):
        for uid in self.uids:
            yield Request(self.user_url.format(uid=uid), callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        if data['ok']:
            userInfo = data['data']['userInfo']
            user_item = WeiboUserItem()
            # 需要的字段
            need_params = (
                'id',  # 用户 id
                'screen_name', # 用户名
                'profile_image_url',  #
                'statuses_count',
                'verified',
                'gender',  # 性别
                'verified_type',
                'verified_type_ext',
                'verified_reason',  # 微博认证
                'close_blue_v',
                'description',   # 个人简介
                'follow_count',  # 关注的用户数
                'followers_count',  # 粉丝数
                'cover_image_phone',
                'avatar_hd', # 头像
            )

            for key in need_params:
                user_item[key] = userInfo.get(key)

            return user_item
