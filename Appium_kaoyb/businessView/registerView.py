#coding:utf-8
from common.desired_caps import appium_desired
from common.common_fun import Common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging
import random
from time import sleep

class RegisterView(Common):
    #登录页面注册按钮
    registerBtn = (By.ID, 'com.tal.kaoyan:id/login_register_text')

    #头像设置相关元素
    add_portait = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    image_choice = (By.ID, 'com.tal.kaoyan:id/item_image')
    saveBtn = (By.ID, 'com.tal.kaoyan:id/save')

    #注册信息相关元素
    username_loc = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    password_loc = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    email_loc = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    registerNow = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    #目标院校
    select_school = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_school')
    select_schools=(By.NAME,"添加院校")
    cities = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')

    #目标专业
    choose_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    pro_master = (By.ID, 'com.tal.kaoyan:id/activity_marjorsubject_zhuanye')
    majors = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_spe = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')

    #点击进入考研帮
    perfectInfoBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')
    recommend_forum = (By.ID, 'com.tal.kaoyan:id/regist_recommend_forum_commit')

    #个人中心元素
    my_account = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username = (By.ID, 'com.tal.kaoyan:id/com.tal.kaoyan:id/activity_usercenter_username')


    def register_action(self, newname, newpass, newemail):
        self.check_skipBtn()

        logging.info('=======register action=======')
        self.driver.find_element(*self.registerBtn).click()
        #设置头像
        logging.info('set portait')
        # self.driver.find_element(*self.add_portait).click()
        # self.driver.find_elements(*self.image_choice)[2].click()
        # self.driver.find_element(*self.saveBtn).click()


        #设置用户名
        logging.info('set username %s' %newname)
        self.driver.find_element(*self.username_loc).send_keys(newname)

        # 设置密码
        logging.info('set password %s' %newpass)
        self.driver.find_element(*self.password_loc).send_keys(newpass)

        # 设置邮箱
        logging.info('set email %s' %newemail)
        self.driver.find_element(*self.email_loc).send_keys(newemail)

        #点击注册按钮
        logging.info('点击立即注册')
        self.driver.find_element(*self.registerNow).click()

        try:
            self.driver.find_element(*self.select_school)
        except NoSuchElementException:
            logging.error('register Fail!')
            self.getScreenshot('register Fail!')
            return False
        else:
            self.add_target_info()
            self.check_privateTerm()

            #注册结果判断
            if self.check_registerStatus():
                return True
            else:
                return False

    def add_target_info(self):
        logging.info('======target_info======')

        logging.info('choose university')
        self.driver.find_element(*self.select_school).click()

        sleep(7)
        self.swipeUp()

        self.driver.find_elements(*self.cities)[9].click()

        self.swipeUp()
        self.driver.find_elements(*self.university)[0].click()
        sleep(7)
        logging.info('choose major')
        self.driver.find_element(*self.choose_major).click()
        self.driver.find_element(*self.pro_master).click()
        self.driver.find_elements(*self.majors)[2].click()
        self.driver.find_elements(*self.major_group)[0].click()
        self.driver.find_elements(*self.major_spe)[8].click()

        logging.info('click enter')
        self.driver.find_element(*self.perfectInfoBtn).click()
        self.driver.find_element(*self.recommend_forum).click()

    def check_register_status(self):
        logging.info('======check_register_status======')
        try:
            for i in range(2):
                self.driver.find_element(*self.my_account).click()
            self.driver.find_element(*self.username).click()
        except NoSuchElementException:
            logging.error('register Fail!')
            self.getScreenshot('register Fail')
            return False
        else:
            logging.info('register success!')
            self.getScreenshot('register_success')
            return True

if __name__ == '__main__':
    driver = appium_desired()
    register = RegisterView(driver)

    newname = 'william' + str(random.randint(1, 1000)) + 'sss'
    newpass = 'test' + '@' + str(random.randint(1, 1000))
    newemail = 'hellolove' + str(random.randint(1, 1000)) + '@163.com'

    register.register_action(newname, newpass, newemail)

# adb uninstall io.appium.android.ime





