#-*- encoding: UTF-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
import xlrd
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
    db = DBHelper()
    data = xlrd.open_workbook('C:\\Users\\cs\\Downloads\\201903211800.xls')
    # 获取第一张工作表（通过索引的方式）
    table = data.sheets()[0]
    # data_list用来存放数据
    data_list = []
    # 将table中第一行的数据读取并添加到data_list中
    nrows = table.nrows
    for x in range(nrows):
        z = table.row_values(x)
        print(z)
        db.insertbaomingrenshu(z[0],z[1],z[2])
    # 打印出第一行的全部数据
    # for item in data_list:
    #     print(item)
