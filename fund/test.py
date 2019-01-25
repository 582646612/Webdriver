#-*- encoding: UTF-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
from dbinsert import DBHelper
from data import allfund

def parse(num):
    url='http://fund.eastmoney.com/'+num+'.html'
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.select('[class~=infoOfFund]')[0].select('td')
    type =items[0].get_text()
    return  type
if __name__ == '__main__':
    # y=allfund
    # z=[]
    # for x in y:
    #     db = DBHelper()
    #     data=db.Select(x)
    #     if data is None:
    #         z.append(x)
    x= "UPDATE fund SET type = %s WHERE code =%s "
    y=('2017-07-1', '004775')
    print(x('2017-07-1', '004775'))