# -*- coding:utf-8 -*-
__author__ = 'Michael'
import requests
from common import method
import unittest
import json
from nose_parameterized import parameterized
TOKEN = 0
class test3(unittest.TestCase):
    def setUp(self):
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    @parameterized.expand(input=method.read_excel("WEB","/call/ajax_get_call_list"))
    def test_0_ajax_get_call_list(self,paramter,code):
        u"获取通话记录的列表"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        global TOKEN
        TOKEN = method.generate_web_token()
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/time_table/ajax_get_time_table_list"))
    def test_1_ajax_get_time_table_list(self,paramter,code):
        u"获取排课信息列表"
        uri = "/time_table/ajax_get_time_table_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/venues/ajax_get_venues_list_by_category_id_and_date"))
    def test_2_ajax_get_venues_list_by_category_id_and_date(self,paramter,code):
        u"根据科目获取场馆列表"
        uri = "/venues/ajax_get_venues_list_by_category_id_and_date"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/class/ajax_get_class_list_by_venues_id_and_date"))
    def test_3_ajax_get_class_list_by_venues_id_and_date(self,paramter,code):
        u"通过场馆和周几获取班级列表（排课）"
        uri = "/class/ajax_get_class_list_by_venues_id_and_date"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/time_table/ajax_get_coach_list"))
    def test_4_ajax_get_coach_list(self,paramter,code):
        u"获取教练列表"
        uri = "/time_table/ajax_get_coach_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/time_table/ajax_save_time_table"))
    def test_5_ajax_save_time_table(self,paramter,code):
        u"保存排课"
        uri = "/time_table/ajax_save_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/time_table/ajax_submit_check_time_table"))
    def test_6_ajax_submit_check_time_table(self,paramter,code):
        u"添加或修改排课时提交审批"
        uri = "/time_table/ajax_submit_check_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/time_table/ajax_copy_time_table"))
    def test_7_ajax_copy_time_table(self,paramter,code):
        u"复制排课，10285：指定的月份已经排课"
        uri = "/time_table/ajax_copy_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])



if __name__ == "__main__":
    unittest.main()