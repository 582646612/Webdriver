#coding:utf-8
import unittest
import os
import HTMLTestRunner
import time

from baidu_search import BaiduSearch
from test_get_pagetitle import GetPageTitle
# suite=unittest.TestSuite()
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_search2'))
# suite.addTest(GetPageTitle('test_get_pagehome'))

# suite = unittest.TestSuite()
# suite.makeSuite(BaiduSearch)

# test_dir = './'
# suite = unittest.defaultTestLoader.discover(test_dir,pattern='*.py')

suite = unittest.TestLoader().discover('testsuits')

if __name__=='__main__':
    # 设置报告文件保存路径
    report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
    # 获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 设置报告名称格式
    HtmlFile = report_path + now + "HTMLtemplate.html"
    fp = file(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)