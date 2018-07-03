# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from datetime import datetime

import pymongo
from scrapy.conf import settings


class UserCreateTimePipeline(object):
    """添加创建时间"""

    def process_item(self, item, spider):
        item['create_time'] = datetime.now().strftime('%Y-%m-%d %H:%M')
        return item


# class WeibospiderPipeline(object):
#
#     def process_item(self, item, spider):
#         return item


class WeiboPymongoPipeline(object):
    """保存数据到 mongodb"""

    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONGO_HOST'],
                                   port=settings['MONGO_PORT'])
        db = conn[settings['MONGO_DATABASE']]
        self.collection = db[settings['MONGO_COLLECTION']]

    def process_item(self, item, spider):
        self.collection.update({'id': item['id']}, {'$set': dict(item)}, upsert=True)
        return item

