import json
import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import requests
import json
import time
import mysql.connector

from dbinsert import DBHelper
def get_data(x):
    orc_url ='http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=yearzf&code='+str(x)
    res = requests.get(orc_url).text
    # print(res)
    # soup = BeautifulSoup(res.text, "html.parser")
    # items = soup.find_all('li',class_='title')
    pattern = re.compile("<tr><td.*?class='tdgray'>.*?</td><td class='.*?'>(.*?)</td><td class='.*?'>(.*?)</td><td class='.*?'>(.*?)</td><td class='.*?'>(.*?)</td><td class='.*?'>(.*?)</td><td class='.*?'>(.*?)</td><td class='.*?>(.*?)</td><td class='.*?'>(.*?)</td></tr>", re.S)
    items = re.findall(pattern, res)
    return items[1]
if __name__ == '__main__':

    x=['310318','000011','050011','310318','530015','539001','163407','005156','180008','000809']
    y=['股票型','混合型','债券型','指数型','ETF','QDII','LOF','FOF','货币型','理财型']
    db = DBHelper()
    for i in range(0,10):
        try:
            print(i)
            item = get_data(x[i])
            print(item)
            db.insertyeardata(y[i],item)
        except Exception as e:
            print(e)

