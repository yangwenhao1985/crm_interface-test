# -*- coding:utf-8 -*-
__author__ = 'Michael'
import unittest
import time
import requests
import json
from common import method
from nose_parameterized import parameterized
STAFF_SIGN_ID = 0 #员工签到ID
TOKEN = 0 #身份验证
class test1(unittest.TestCase):
    def setUp(self):
        times = int(time.time())
        self.times_str = str(times)
        self.url = "http://qa.education.hy-sport.cn"
        self.path = "E:\\crm_interface-test\\resouce\\interface_data.xlsx"

    def tearDown(self):
        pass

    @parameterized.expand(input=method.read_excel("APP","/api/user/login"))
    def test_0_login(self,paramter,code):
        """APP端登陆接口"""
        url = self.url + "/api/user/login?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/user/login"
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("APP","/api/user/loginOut"))
    def test_1_loginOut(self,paramter,code):
        """APP端退出登陆接口"""
        url = self.url + "/api/user/loginOut?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        global TOKEN
        TOKEN = method.generate_app_token("18801409523", "Y+a1dRVSmYh\/GAow9N6xdQ==")
        cookie = {"token": TOKEN}
        uri = "/api/user/loginOut"
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("APP","/api/system/upgrade"))
    def test_2_upgrade(self,paramter,code):
        """APP升级接口"""
        url = self.url + "/api/system/upgrade?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/system/upgrade"
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("APP","/api/customer/getCustomerList"))
    def test_3_getCustomerList(self,paramter,code):
        """获取客户列表"""
        url = self.url + "/api/customer/getCustomerList?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/customer/getCustomerList"
        cookie = {"token": TOKEN}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("APP","/api/attendance/getAttendAnceInfo"))
    def test_4_getAttendAnceInfo(self,paramter,code):
        """获取考勤信息"""
        url = self.url + "/api/attendance/getAttendAnceInfo?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/getAttendAnceInfo"
        cookie = {"token": TOKEN}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("APP","/api/attendance/staffSignIn"))
    def test_5_staffSignIn(self,paramter,code):
        """员工签到考勤"""
        url = self.url + "/api/attendance/staffSignIn?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignIn"
        cookie = {"token": TOKEN}
        img = open("E:\\crm_interface-test\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        global STAFF_SIGN_ID
        if dic["errcode"] == 0:
            STAFF_SIGN_ID = dic["data"]
        self.assertEqual(dic["errcode"], code["errcode"])

    def test_6_staffSignBack(self):
        """员工签退考勤"""
        url = self.url + "/api/attendance/staffSignBack?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignBack"
        cookie = {"token": TOKEN}
        address = "interface auto"
        paramter = {"scene": address, "longitude": "116.487488", "latitude": "40.002678", "staff_sign_id": STAFF_SIGN_ID}
        img = open("E:\\crm_interface-test\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 0)

if __name__ == "__main__":
    unittest.main()
