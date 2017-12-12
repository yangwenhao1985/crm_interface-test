# -*- coding:utf-8 -*-
__author__ = 'Michael'
import requests
import unittest
import json
from common import method
TOKEN = 0
class extend1(unittest.TestCase):
    def setUp(self):
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    def test_0_login(self):
        u"CRM后台登陆，手机号无效"
        uri = "/user/ajax_login"
        url = self.url + uri
        paramter = {"phone": "", "passwd": "123456qwe"}
        response = requests.post(url, data=paramter)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10110)

    def test_1_login(self):
        u"CRM后台登陆，密码无效"
        uri = "/user/ajax_login"
        url = self.url + uri
        paramter = {"phone": "18600000006", "passwd": ""}
        response = requests.post(url, data=paramter)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10138)

    def test_2_login(self):
        u"CRM后台登陆，用户不存在"
        uri = "/user/ajax_login"
        url = self.url + uri
        paramter = {"phone": "18701451100", "passwd": "123456qwe"}
        response = requests.post(url, data=paramter)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10142)

    def test_3_ajax_get_venues_list(self):
        u"获取场馆列表，公司ID无效"
        uri = "/venues/ajax_get_venues_list"
        url = self.url + uri
        global TOKEN
        TOKEN = method.generate_web_token()
        cookie = {"token": TOKEN}
        paramter = {"company_id": "", "status": "-1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148)

    def test_4_ajax_get_venues_list(self):
        u"获取场馆列表，科目无效"
        uri = "/venues/ajax_get_venues_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17", "status": "-1", "category_ids": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10402)

    def test_5_ajax_get_venues_list(self):
        u"获取场馆列表，状态无效"
        uri = "/venues/ajax_get_venues_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17", "status": "",}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10164)

    def test_6_ajax_modify_venues_by_venues_id(self):
        u"修改场馆，场馆ID无效"
        uri = "/venues/ajax_modify_venues_by_venues_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "", "name": "测试专用", "address": "北京香山小场馆", "longitude": "116.1847657600",
                    "latitude": "39.9888019700", "status": "0", "category_ids": "1|2|3|4|5"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10125)

    def test_7_ajax_modify_venues_by_venues_id(self):
        u"修改场馆，场馆名称无效"
        uri = "/venues/ajax_modify_venues_by_venues_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "416", "name": "", "address": "北京香山小场馆", "longitude": "116.1847657600",
                    "latitude": "39.9888019700", "status": "0", "category_ids": "1|2|3|4|5"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10112)

    def test_8_ajax_modify_venues_by_venues_id(self):
        u"修改场馆，场馆地址无效"
        uri = "/venues/ajax_modify_venues_by_venues_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "416", "name": "测试专用", "address": "", "longitude": "116.1847657600",
                    "latitude": "39.9888019700", "status": "0", "category_ids": "1|2|3|4|5"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10115)

    def test_9_ajax_modify_venues_by_venues_id(self):
        u"修改场馆，场馆经度无效"
        uri = "/venues/ajax_modify_venues_by_venues_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "416", "name": "测试专用", "address": "北京香山小场馆", "longitude": "",
                    "latitude": "39.9888019700", "status": "0", "category_ids": "1|2|3|4|5"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10194)

    def test_A_ajax_modify_venues_by_venues_id(self):
        u"修改场馆，场馆纬度无效"
        uri = "/venues/ajax_modify_venues_by_venues_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "416", "name": "测试专用", "address": "北京香山小场馆", "longitude": "116.1847657600",
                    "latitude": "", "status": "0", "category_ids": "1|2|3|4|5"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10195)

    def test_B_ajax_modify_venues_by_venues_id(self):
        u"修改场馆，分类id无效"
        uri = "/venues/ajax_modify_venues_by_venues_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "416", "name": "测试专用", "address": "北京香山小场馆", "longitude": "116.1847657600",
                    "latitude": "39.9888019700", "status": "0", "category_ids": ""}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10402)

    def test_C_ajax_modify_venues_by_venues_id(self):
        u"修改场馆，状态无效"
        uri = "/venues/ajax_modify_venues_by_venues_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "416", "name": "测试专用", "address": "北京香山小场馆", "longitude": "116.1847657600",
                    "latitude": "39.9888019700", "status": "", "category_ids": "1|2|3|4|5"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10164)

if __name__ == "__main__":
    unittest.main()