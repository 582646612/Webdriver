# -*- coding: utf-8 -*-

# Scrapy settings for fund project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'fund'

SPIDER_MODULES = ['fund.spiders']
NEWSPIDER_MODULE = 'fund.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES={'fund.pipelines.FundPipeline':300,}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fund (+http://www.yourdomain.com)'
#Mysql数据库的配置信息
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'test'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = '123'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用