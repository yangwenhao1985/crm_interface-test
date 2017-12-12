# -*- coding:utf-8 -*-
__author__ = 'Michael'
import requests
import unittest
from common import method
import json
from nose_parameterized import parameterized
TOKEN = 0
class test2(unittest.TestCase):
    def setUp(self):
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_get_user_information_by_uid"))
    def test_0_ajax_get_user_information_by_uid(self,paramter,code):
        u"获取账号详情"
        uri = "/user/ajax_get_user_information_by_uid"
        url = self.url + uri
        global TOKEN
        TOKEN = method.generate_web_token()
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    # def test_1_ajax_reset_passwd(self):
    #     u"重置账号密码,10169发送短信的次数超过了限制"
    #     uri = "/user/ajax_reset_passwd"
    #     url = self.url + uri
    #     cookie = {"token": TOKEN}
    #     paramter = {"phone": "18701458751", "type": "3"}
    #     response = requests.post(url, data=paramter, cookies=cookie)
    #     text = response.content
    #     dic = json.loads(text)
    #     self.assertEqual(dic["errcode"], 0)

    # def test_2_ajax_user_enable_or_disable(self):
    #     u"账户禁用和启用"
    #     uri = "/user/ajax_user_enable_or_disable"
    #     url = self.url + uri
    #     cookie = {"token": TOKEN}
    #     paramter = {"uid": "3097", "status": "0"}
    #     response = requests.post(url, data=paramter, cookies=cookie)
    #     text = response.content
    #     dic = json.loads(text)
    #     self.assertEqual(dic["errcode"], 0)

    @parameterized.expand(input=method.read_excel("WEB","/venues/ajax_add_venues"))
    def test_3_ajax_add_venues(self,paramter,code):
        u"添加场馆,10403场馆已存在，10488地址已经存在"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/news/ajax_upload_image"))
    def test_4_ajax_upload_image(self,paramter,code):
        u"上传图片"
        uri = "/news/ajax_upload_image"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],  code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_add_user"))
    def test_5_ajax_add_user(self,paramter,code):
        u"添加用户帐号信息,10135：手机号已存在"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/student/ajax_get_student_list"))
    def test_6_ajax_get_student_list(self,paramter,code):
        u"获取学员列表"
        uri = "/student/ajax_get_student_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/sign_up/ajax_get_sign_up_list"))
    def test_7_ajax_get_sign_up_list(self,paramter,code):
        u"获取报名列表"
        uri = "/sign_up/ajax_get_sign_up_list"
        url = self.url + uri
        dandan_token = method.get_token_for_dandan()
        cookie = {"token": dandan_token}
        response = requests.get(url, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/daily/ajax_get_daily_list"))
    def test_8_ajax_get_daily_list(self,paramter,code):
        u"获取日报列表"
        uri = "/daily/ajax_get_daily_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/daily/ajax_get_daily"))
    def test_9_ajax_get_daily(self,paramter,code):
        u"查看日报"
        uri = "/daily/ajax_get_daily"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])


if __name__ == "__main__":
    unittest.main()