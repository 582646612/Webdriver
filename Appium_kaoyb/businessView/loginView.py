#coding:utf-8
from common.desired_caps import appium_desired
from common.common_fun import Common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging


class LoginView(Common):

    username_loc=(By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_loc=(By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn_loc=(By.ID, 'com.tal.kaoyan:id/login_login_btn')
    #账号下线提醒确定按钮
    tip_commit=(By.ID, 'com.tal.kaoyan:id/tip_commit')
    #我
    my_account=(By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    #用户中心页面的用户名
    usercenter_username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    #设置按钮
    settingBtn = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    #退出登录按钮
    logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    #确定退出登录按钮
    confirmLogout = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    def login_action(self,username,password):

        self.check_skipBtn()

        logging.info('========login_action========')
        logging.info('username is: %s' %username)
        self.driver.find_element(*self.username_loc).send_keys(username)

        logging.info('password is: %s' %password)
        self.driver.find_element(*self.password_loc).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn_loc).click()

    def check_account_alert(self):
        logging.info('========check_account_alert========')
        try:
            element=self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('close alert')
            element.click()

    def check_loginStatus(self):
        logging.info('========check_loginStatus========')
        self.check_privateTerm()
        self.check_account_alert()

        try:
            self.driver.find_element(*self.my_account).click()
            self.driver.find_element(*self.my_account).click()
            self.driver.find_element(*self.usercenter_username)
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenshot('loginFail')
            return False
        else:
            logging.info('login Success!')
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('========logout_action========')
        self.driver.find_element(*self.settingBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.confirmLogout).click()



if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('helloreverie@sina.com', '1051303119Wp10')
    l.check_loginStatus()