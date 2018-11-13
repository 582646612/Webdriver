#coding:utf-8
from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import time,os
import csv



class Common(BaseView):
    skipBtn=(By.ID, 'com.tal.kaoyan:id/tv_skip')

#跳过APP启动后的banner
    def check_skipBtn(self):
        logging.info('========check_skipBtn========')
        try:
            skipBtn=self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skip button')
        else:
            skipBtn.click()

#获取屏幕大小
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

#向左滑动
    def swipeLeft(self):
        logging.info('swipeLeft')
        l= self.get_size()
        x1 = int(l[0]*0.9)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        self.swipe(x1,y1,x2,y1,1000)

#向下滑动
    def swipeUp(self):
        l= self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.9)
        y2 = int(l[1]*0.3)
        self.swipe(x1,y1,x1,y2,2000)


#获取时间
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H:%M:%S")
        return self.now

#获取截图
    def getScreenshot(self, module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module, time)

        logging.info('get %s screenshot'%module)
        self.driver.get_screenshot_as_file(image_file)

# 登录后出现的隐私条款弹窗
    term_agree=(By.ID, 'com.tal.kaoyan:id/tv_agree')
    def check_privateTerm(self):
        logging.info('===check_privateTerm===')
        try:
            element=self.driver.find_element(*self.term_agree)
        except NoSuchElementException:
            pass
        else:
            logging.info('agree private term')
            element.click()

# 获取data文件夹数据
    def get_csv_data(self, csv_file,line):
        logging.info('=====get_csv_data=====')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index, row in enumerate(reader,1):
                if index == line:
                    return row





if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    # com.check_skipBtn()
    com.swipeLeft()
    com.getScreenshot('startApp')

