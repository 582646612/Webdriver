# coding:utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class GetPageTitle(unittest.TestCase):

    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器        :return:
        """
        cls.driver.quit()

    def test_get_pagehome(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        print baiduhome.get_page_title()



if __name__ == '__main__':
     unittest.main()