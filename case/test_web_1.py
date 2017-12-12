# -*- coding:utf-8 -*-
__author__ = 'Michael'
import requests
import unittest
import json
from common import method
from nose_parameterized import parameterized
TOKEN = 0
class test1(unittest.TestCase):
    def setUp(self):
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_login"))
    def test_0_login(self,paramter,code):
        u"CRM后台登陆"
        uri = "/user/ajax_login"
        url = self.url + uri
        response = requests.post(url, data=paramter)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/venues/ajax_get_venues_list"))
    def test_1_ajax_get_venues_list(self,paramter,code):
        u"获取场馆列表"
        uri = "/venues/ajax_get_venues_list"
        url = self.url + uri
        global TOKEN
        TOKEN = method.generate_web_token()
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/venues/ajax_modify_venues_by_venues_id"))
    def test_2_ajax_modify_venues_by_venues_id(self,paramter,code):
        u"修改场馆信息"
        uri = "/venues/ajax_modify_venues_by_venues_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/venues/ajax_delete_venues_by_venues_ids"))
    def test_3_ajax_delete_venues_by_venues_ids(self,paramter,code):
        u"删除场馆,场馆ID为361，因为场馆有班级，所以返回10424"
        uri = "/venues/ajax_delete_venues_by_venues_ids"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_get_user_list"))
    def test_4_ajax_get_user_list(self,paramter,code):
        u"获取用户列表"
        uri = "/user/ajax_get_user_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_get_user"))
    def test_5_ajax_get_user(self,paramter,code):
        u"获取账号详情"
        uri = "/user/ajax_get_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_get_department_list"))
    def test_6_ajax_get_department_list(self,paramter,code):
        u"获取账号的部门列表"
        uri = "/user/ajax_get_department_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_get_role_list_by_department_id"))
    def test_7_ajax_get_role_list_by_department_id(self,paramter,code):
        u"获取职位列表通过部门id"
        uri = "/user/ajax_get_role_list_by_department_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_get_superior_leader_list"))
    def test_8_ajax_get_superior_leader_list(self,paramter,code):
        u"获取上级列表"
        uri = "/user/ajax_get_superior_leader_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("WEB","/user/ajax_modify_user"))
    def test_9_ajax_modify_user(self,paramter,code):
        u"修改用户帐号信息"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])


if __name__ == "__main__":
    unittest.main()