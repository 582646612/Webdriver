#coding:utf-8
import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings  #导入seetings配置
import time
import mysql.connector

class DBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="123",  # 数据库密码
        database="test"
        )
        self.mycursor = self.mydb.cursor()

    def insert(self,item):
        loctime= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        sql = "INSERT INTO `price_sh` (`total`, `price`, `area`, `type`, `local`, `title`, `created_time`) VALUES"
        value=str((item['total'], item['price'], item['area'],item['type'], item['local'], item['title'], loctime))
        self.mycursor.execute(sql+value)
        self.mydb.commit()


if __name__ == '__main__':
    db = DBHelper()
    item={'type': '3室2厅高楼层/共24层', 'local': '所在区域五华顺城', 'area': '129.15平米暂无数据', 'total': '235', 'title': '南北通透朝南看金马坊朝北看南屏街，视野开阔阳光充足', 'price': '18196元/平米'}
    db.insert(item)
