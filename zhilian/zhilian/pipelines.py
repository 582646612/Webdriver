# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#以下两种写法保存json格式，需要在settings里面设置'coolscrapy.pipelines.JsonPipeline': 200

import codecs
import os
import json
import pymysql

import codecs
import os
import json
import pymysql

class CoolscrapyPipeline(object):#需要在setting.py里设置'coolscrapy.piplines.CoolscrapyPipeline':300
    def process_item(self, item, spider):
        # 获取当前工作目录
        base_dir = os.getcwd()
        fiename = base_dir + '/news.txt'
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a') as f:
            f.write(item['name'] + '\n')
        return item


class JsonPipeline(object):
    def process_item(self, item, spider):
        # 打开json文件，向里面以dumps的方式吸入数据
        # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如
        # :“/xe15”
        with codecs.open('news.json', 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item