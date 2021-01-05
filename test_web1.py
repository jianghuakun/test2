#!/usr/bin/python3
from data.get_data import GetData
from util.common_util import CommonUtil
#from util.operation_header import OperationHeader
#from util.operation_json import OperationJson
import unittest
import re
import time
from selenium import webdriver
from Common.basePage import BasePage
from database.redis245 import redis245
class RunTest(unittest.TestCase):

    def setUp(self):
        self.data = GetData()
        self.com_util = CommonUtil()
        basepage = BasePage(webdriver)


        #s1=data_create_ota()
        #s1.depart_create()
        #s1.user_create()
        #s1.oss_file_create()
    #def __init__(self):



        # self.send_email = SendEmail()

    def test_01(self):
    #def go_on_run(self):
        """程序执行"""
        pass_count = []
        fail_count = []
        count1=0
        count2=0

        res = None


        # 获取用例数
        rows_count = self.data.get_case_lines()

        # 第一行索引为0

        basepage = BasePage(webdriver)
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:

                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                #request_data = self.data.get_data_for_json(i)
                request_data = self.data.get_request_data(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                action_type=self.data.get_depend_key(i)
                action_value=self.data.get_depend_field(i)
                caseID = self.data.get_ID(i)
                api_name = self.data.get_api_name(i)
                request_name = self.data.get_request_name(i)



                #params=self.data.get_params(i)
                data1={"method":method,"depend_case":depend_case,"header":header,"action_type":action_type,"action_value":action_value,"request_body":request_data}
                #print(1122,data1)
                selector1=[]
                print(action_type,action_value)
                if depend_case!=None:
                    selector1.append(depend_case)
                if action_type!=None:
                    selector1.append(action_type)
                #print(123,selector1)
                if method=="open":
                    time.sleep(2)
                    try:
                        basepage.open_browser(url)
                        self.data.write_result(i, "Pass")
                        pass_count.append(i)
                        count1 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(0, 0, "pass")
                    except:
                        self.data.write_result(i, "Fail")
                        pass_count.append(i)
                        count2 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(1, 0, "Fail")
                elif method == "sleep":
                    try:
                        basepage.my_sleep(data1["request_body"])
                        self.data.write_result(i, "Pass")
                        count1 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(0, 0, "pass")
                    except:
                        self.data.write_result(i, "Fail")
                        count2 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(1, 0, "Fail")
                elif method == "exit":
                    time.sleep(2)
                    try:
                        basepage.isdisplayed(selector1)
                        self.data.write_result(i, "Pass")
                        count1 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(0, 0, "pass")
                    except:
                        self.data.write_result(i, "Fail")
                        count2 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(1, 0, "Fail")

                elif method == "get_attribute":
                    try:
                        get_attribute=basepage.get_attribute(selector1,data1["request_body"])


                        if expect!=None:
                            if expect==get_attribute:
                                self.data.write_result(i, "Pass")
                                count1 += 1
                                with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                                    self.assertEqual(0, 0, "pass")
                            else:
                                self.data.write_result(i, get_attribute)
                                count2 += 1
                                with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                                    self.assertEqual(1, 0, "Fail")
                        else:
                            self.data.write_result(i, "Pass")
                            count1 += 1
                            with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                                self.assertEqual(0, 0, "pass")
                    except:
                        self.data.write_result(i, "Fail")
                        count2 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(1, 0, "Fail")

                elif method == "get_title":
                    try:
                        basepage.get_title()
                        self.data.write_result(i, "Pass")
                        count1 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(0, 0, "pass")
                    except:
                        self.data.write_result(i, "Fail")
                        count2 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(1, 0, "Fail")

                elif method=="click":
                    time.sleep(2)
                    try:
                        basepage.click(selector1)
                        self.data.write_result(i, "Pass")
                        count1 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(0, 0, "pass")
                    except:
                        self.data.write_result(i, "Fail")
                        count2 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(1, 0, "Fail")
                elif method=="get_text":
                    try:
                        basepage.get_text(selector1)
                        self.data.write_result(i, "Pass")
                        count1 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(0, 0, "pass")
                    except:
                        self.data.write_result(i, "Fail")
                        count2 += 1
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(1, 0, "Fail")
                elif method=="input":
                    time.sleep(2)
                    if request_name=="验证码输入":
                        print("验证码输入")
                        s1 = redis245.Cluster
                        captchas = s1.keys("*")
                        for captcha1 in captchas:
                            if ":" not in captcha1 and len(captcha1) == 32:
                                data1["request_body"] = s1.get(captcha1).replace('"','').lower()
                                try:
                                    basepage.type(selector1, data1["request_body"])
                                    self.data.write_result(i, "Pass")
                                    count1 += 1
                                    with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                                        self.assertEqual(0, 0, "pass")
                                except:
                                    self.data.write_result(i, "Fail")
                                    count2 += 1
                                    with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                                        self.assertEqual(1, 0, "Fail")
                    else:
                        try:
                            basepage.type(selector1, data1["request_body"])
                            self.data.write_result(i, "Pass")
                            count1 += 1
                            with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                                self.assertEqual(0, 0, "pass")
                        except:
                            self.data.write_result(i, "Fail")
                            count2 += 1
                            with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                                self.assertEqual(1, 0, "Fail")
                print(count1,count2)

    def tearDown(self):
        '''清除数据'''
        pass





if __name__ == '__main__':
    run = RunTest()
    run.test_01()