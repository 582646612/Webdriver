# coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from common.send_email import *
import os

#指定测试用例和测试报告路径
testcase_dir='../test_case'
report_dir='D:/Webdriver/Appium_Project/reports'

#加载测试用例
discover=unittest.defaultTestLoader.discover(testcase_dir, pattern='test_register.py')

#定义报告的文件格式
now = time.strftime('%Y-%m-%d_%H_%M_%S')
report_name = report_dir+'/'+now+' test_report.html'
print (report_name)
#运行用例并生成报告
with open(report_name, 'w') as f:
    runner = HTMLTestRunner(stream=f, title='Kyb Test Report', description='Kyb app Android Test Report')
    logging.info('start running testcase...')
    runner.run(discover)
f.close()

print('find latest report...')
latest_report=latest_report(report_dir)

print('start send email...')
sendEmail(latest_report)

print('email sent!')