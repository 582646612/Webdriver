#_*_coding:utf-8_*_

import scrapy
import re
from bs4 import BeautifulSoup as bs
from ..items import ZhilianItem

class mapSpider(scrapy.Spider):
    name = 'zhilian_map'
    start_urls = ['http://www.gx211.com/collegemanage/content45_03.shtml']


    def parse(self, response):
        for i in range(45, 1000):
            url = 'http://www.gx211.com/collegemanage/content' + str(i) + '_03.shtml'
            try:
                yield scrapy.Request(url, callback=self.parse_history)
            except:
                continue


    def parse_history(self, response):
        item = {}
        try:
            school = response.css('h1 a::text').extract()[0]
            item['name'] = school
            yield item
        except Exception as e:
            print(e)


