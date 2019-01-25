#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
import scrapy
import requests
from bs4 import BeautifulSoup
import re
from ..items import TutorialItem
from scrapy import Request
class JdSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["lianjia.com"]
    start_urls = [
        "https://km.lianjia.com/ershoufang/106102006135.html"
    ]

    def parse(self, response):
        headers1 = {'User-Agent': 'ua.random'}
        domain = 'https://km.lianjia.com/ershoufang/'  # 为了之后拼接子域名爬取详细信息

        for i in range(1, 2):  # 爬取399页，想爬多少页直接修改替换掉400，不要超过总页数就好
            res = requests.get('https://km.lianjia.com/ershoufang/pg' + str(i), headers=headers1)  # 爬取拼接域名
            soup = BeautifulSoup(res.text, 'html.parser')  # 使用html筛选器
            # print(soup)
            for j in range(0, 3):  # 网站每页呈现30条数据，循环爬取
                url1 = soup.select('.item')[j]['data-houseid']  # 选中class=prop-title下的a标签里的第j个元素的href子域名内容
                url = domain + url1 + '.html'
                try:
                    yield scrapy.Request(url, callback=self.parse_history)
                except:
                    continue

    def parse_history(self,response):
        item = {}  # 构造字典，作为之后的返回内容
        soup = BeautifulSoup(response.body, 'html.parser')
        try:
            item['type'] = soup.find('div', class_="room").get_text()
            item['total'] = soup.find('span', class_="total").get_text()
            item['local'] = soup.find('div', class_="areaName").get_text()
            item['local']=re.sub('\xa0','',item['local'])
            item['title'] = soup.find('h1', class_="main").get_text()
            item['price'] = soup.find('span', class_="unitPriceValue").get_text()
            item['area'] = soup.find('div', class_="area").get_text()
            yield item
        except Exception as e:
            print(e)

