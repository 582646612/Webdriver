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
def get_fundtheme():
    orc_url ='http://fund.jrj.com.cn/subject/list.shtml'
    res = requests.get(orc_url).text
    # soup = BeautifulSoup(res.text, "html.parser")
    # items = soup.find_all('li',class_='title')
    pattern = re.compile("<tr data_topcode=.*?><td><a href=.*? title=.*?>(.*?)</a></td><td class=.*?>(.*?)%</td><td class=.*?>(.*?)%</td><td class=.*?>(.*?)%</td><td class=.*?>(.*?)%</td><td><a href=.*? title=.*?>(.*?)</a></td><td class=.*?>(.*?)%</td>",re.S)

    items = re.findall(pattern, res)
    return items
if __name__ == '__main__':
    y=get_fundtheme()
    db = DBHelper()
    for i in y:
        try:
            print(i)
        except Exception as e:
            print(e)

