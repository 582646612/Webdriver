#coding:utf-8
from framework.base_page import BasePage


class NewsHomePage(BasePage):
    # 点击体育新闻入口
    sports_link = "xpath=>//*[@id='channel-all']/div/ul/li[5]/a"

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)

class SportNewsHomePage(BasePage):
    # NBA
    nba_link = "xpath=>//*[@id='channel-submenu']/div/span[2]/a[1]"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)