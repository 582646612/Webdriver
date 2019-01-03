# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
from dbhelper import DBHelper
class TutorialPipeline(object):
    def process_item(self, item, spider):
        # 获取当前工作目录
        # 从内存以追加的方式打开文件，并写入对应的数据

        self.db = DBHelper()


        # 插入数据库
        self.db.insert(item)
        return item
        # with open('news.txt', 'a') as f:
        #     f.write(item['totalprice']+'\t')
        #     f.write(item['price'] + '\t')
        #     f.write(item['mianji'] + '\t')
        #     f.write(item['fangxing'] + '\t')
        #     f.write(item['local']+ '\t')
        #     f.write(item['title']+ '\r')
        # print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
        # return item
