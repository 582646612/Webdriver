import unittest
import paramunittest
import readConfig as readConfig
import Log
import common
import configHttp as ConfigHttp
import json

queryAccountBill_xls = common.get_xls("userCase.xlsx", "queryAccountBill")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*queryAccountBill_xls)

class queryAccountBill(unittest.TestCase):
    def setParameters(self,case_name,method,token,phoneNumber,billTime,status,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.phoneNumber = str(phoneNumber)
        self.billTime = str(billTime)
        self.status = str(status)
        self.msg = str(msg)
        self.ret = None
        self.info = None

    def description(self):
        self.case_name

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"测试开始前准备")

    def testqueryAccountBill(self):
        # set url
        self.url = common.get_url_from_xml('queryAccountBill')
        configHttp.set_url(self.url)
        print("第一步：设置url  ")

        # get visitor token
        if self.token == '0':
            token = localReadConfig.get_headers("token_v")
        elif self.token == '1':
            token = None

        # set headers
        header = {"token": str(token)}
        configHttp.set_headers(header)
        print("第二步：设置header(token等)")

        # set params
        data = {"phoneNumber": self.phoneNumber,
                "billTime":self.billTime}
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.ret = configHttp.get()
        print("第四步：发送请求：")
        if self.ret.status_code == 200:
            print('调用成功，返回200')
        else:
            print('调用失败')

        print("第五步：检查结果")
        self.checkResult()


    def tearDown(self):
        print("测试结束，输出log完结\n\n")


    def checkResult(self):

        if self.ret.text != '':
            self.info = self.ret.json()
            common.show_return_msg(self.ret)
            value = common.get_value_from_return_json(self.info, "status")
            self.assertEqual(value, self.status)
            value = common.get_value_from_return_json(self.info, "msg")
            self.assertEqual(value, self.msg)
        else:
            print("返回空")

