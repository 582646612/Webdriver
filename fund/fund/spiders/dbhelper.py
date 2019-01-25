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

    def insertfundvary(self,item):
        loctime= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        sql = "INSERT INTO `tech_courses` (`total`, `price`, `area`, `type`, `local`, `title`, `created_time`) VALUES"
        value=str((item['total'], item['price'], item['area'],item['type'], item['local'], item['title'], loctime))
        self.mycursor.execute(sql+value)
        self.mydb.commit()
    def insertfund(self,x,y,z):
        loctime= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        sql = "INSERT INTO `fund` (`num`, `name`, `url`,`created_time`)  VALUES"
        value=str((x,y,z, loctime))
        print(sql+value)
        self.mycursor.execute(sql+value)
        self.mydb.commit()
    def insertfundinfo(self,item):
        loctime= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        sql = "INSERT INTO `fundinfo` (`code`, `name`, `unit_value`, `sum_value`, `manager`, `type`, `company`, `scale`, `establish`, `created_time`) VALUES"
        value=str((item['code'], item['name'], item['unit_value'],item['sum_value'], item['manager'], item['type'], item['company'],item['scale'],item['establish'],loctime))
        print(sql+value)
        self.mycursor.execute(sql+value)
        self.mydb.commit()
    def Update(self,item):
        sql = "UPDATE fund SET type = %s WHERE code = %s"
        val = (item['type'], item['code'])
        print(sql,val)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def updatefuninfo(self,item):
        sql = "UPDATE fundinfo SET establish = %s WHERE code = %s"
        val = (item['establish'], item['code'])
        print(sql%val)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
if __name__ == '__main__':
    db = DBHelper()

