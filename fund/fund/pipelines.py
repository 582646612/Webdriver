# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .spiders.dbhelper import DBHelper
class FundPipeline(object):
    def process_item(self, item, spider):
        self.db = DBHelper()

        # 插入数据库
        self.db.updatefuninfo(item)
        return item
