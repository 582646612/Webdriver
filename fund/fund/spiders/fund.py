#-*- encoding: UTF-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
from ..items import FundItem
from scrapy import Request
from db import allfund
class FundSpider(scrapy.Spider):
    name = "funding"
    allowed_domains = ["eastmoney.com"]
    start_urls = ["http://fund.eastmoney.com/001716.html"]
    print('--------------')
    def parse(self,response):
        item=allfund
        for x in item:
            url = 'http://fund.eastmoney.com/' + x + '.html'
            try:
                yield scrapy.Request(url, callback=self.parse_history)
            except:
                continue

    def parse_history(self,response):
        item = {}  # 构造字典，作为之后的返回内容
        soup = BeautifulSoup(response.body, 'html.parser')
        tags = soup.find_all('dd')
        items = soup.select('[class~=infoOfFund]')[0].select('td')
        try:
            item['code'] = soup.find('span',class_='fix_fcode').get_text()
            # item['name'] = soup.find('span', class_='fix_fname').get_text()
            # item['unit_value'] = tags[3].find_all('span')[0].string
            # item['sum_value'] =tags[6].find_all('span')[0].string
            # item['local']=tags[3].find_all('span')[1].string
            # item['near_month'] = tags[1].find_all('span')[1].string
            # item['near_three_month'] = tags[4].find_all('span')[1].string
            # item['near_six_month'] = tags[7].find_all('span')[1].string
            # item['near_year'] =tags[2].find_all('span')[1].string
            # item['near_three_year'] =tags[5].find_all('span')[1].string
            # item['from_found'] =tags[8].find_all('span')[1].string
            # item['manager'] =items[2].get_text()
            # item['type'] =items[0].get_text()
            # item['company'] =items[4].get_text()
            # item['scale'] =items[1].get_text()
            item['establish'] =items[3].get_text()
            yield item
        except Exception as e:
            print(e)

'''最近一年、两年、三年、五年及成立以来收益率排名同类基金的前1/4
最近三个月、六个月收益率排名同类基金的前1/3'''