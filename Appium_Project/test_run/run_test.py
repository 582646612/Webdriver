import unittest
from HTMLTestRunnerCN import HTMLTestRunner
import time
from common.send_email import *


#指定测试用例和测试报告路径
testcase_dir='../test_case'
report_dir='../reports'

#加载测试用例
discover=unittest.defaultTestLoader.discover(testcase_dir, pattern='test_register.py')

#定义报告的文件格式
now = time.strftime('%Y-%m-%d %H:%M:%S')
report_name = report_dir+'/'+now+' test_report.html'

#运行用例并生成报告
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='Kyb Test Report', description='Kyb app Android Test Report')
    logging.info('start running testcase...')
    runner.run(discover)
f.close()

print('find latest report...')
latest_report=latest_report(report_dir)

print('start send email...')
sendEmail(latest_report)

print('email sent!')