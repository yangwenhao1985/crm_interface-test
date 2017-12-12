# -*- coding:utf-8 -*-
__author__ = 'Michael'
import unittest
import requests
import json
from common import method
import time
TOKEN = 0 #身份验证
NOT_ATTENDANCE_RULE_TOKEN = 0
class extend1(unittest.TestCase):
    def setUp(self):
        times = int(time.time())
        self.times_str = str(times)
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    def test_0_getCustomerList(self):
        u"获取客户列表时，时间无效"
        url = self.url + "/api/customer/getCustomerList?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/customer/getCustomerList"
        global TOKEN
        TOKEN = method.generate_app_token("18801409523", "Y+a1dRVSmYh\/GAow9N6xdQ==")
        cookie = {"token": TOKEN}
        paramter = {"position": "110", "page_size": "100"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10188)

    def test_1_getCustomerList(self):
        u"获取客户列表时，数据条数无效"
        url = self.url + "/api/customer/getCustomerList?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/customer/getCustomerList"
        cookie = {"token": TOKEN}
        paramter = {"position": "2017-06-20 15:45:04", "page_size": "0"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10120)

    def test_2_getAttendAnceInfo(self):
        u"获取考勤信息，辅导老师没有考勤规则"
        url = self.url + "/api/attendance/getAttendAnceInfo?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/getAttendAnceInfo"
        global NOT_ATTENDANCE_RULE_TOKEN
        NOT_ATTENDANCE_RULE_TOKEN = method.generate_app_token("18801410855", "Y+a1dRVSmYh/GAow9N6xdQ==")
        cookie = {"token": NOT_ATTENDANCE_RULE_TOKEN}
        paramter = {}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10517)

    def test_3_staffSignIn(self):
        u"员工签到考勤,考勤地址无效"
        url = self.url + "/api/attendance/staffSignIn?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignIn"
        cookie = {"token": TOKEN}
        address = ""
        paramter = {"scene": address, "longitude": "116.487488", "latitude": "40.002678"}
        img = open("E:\\demo1\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10500)

    def test_4_staffSignIn(self):
        u"员工签到考勤，经度无效"
        url = self.url + "/api/attendance/staffSignIn?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignIn"
        cookie = {"token": TOKEN}
        address = "aaa"
        paramter = {"scene": address, "longitude": "", "latitude": "40.002678"}
        img = open("E:\\demo1\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10194)

    def test_5_staffSignIn(self):
        u"员工签到考勤，纬度无效"
        url = self.url + "/api/attendance/staffSignIn?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignIn"
        cookie = {"token": TOKEN}
        address = "aaa"
        paramter = {"scene": address, "longitude": "20.002678", "latitude": ""}
        img = open("E:\\demo1\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10195)

    def test_6_staffSignIn(self):
        u"员工签到，员工没有考勤规则"
        url = self.url + "/api/attendance/staffSignIn?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignIn"
        cookie = {"token": NOT_ATTENDANCE_RULE_TOKEN}
        address = "aaa"
        paramter = {"scene": address, "longitude": "20.002678", "latitude": "40.000904"}
        img = open("E:\\demo1\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10517)

    def test_7_staffSignBack(self):
        u"员工签退考勤，签到id无效"
        url = self.url + "/api/attendance/staffSignBack?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignBack"
        cookie = {"token": TOKEN}
        address = "interface auto"
        paramter = {"scene": address, "longitude": "116.487488", "latitude": "40.002678", "staff_sign_id": ""}
        img = open("E:\\demo1\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10501)

    def test_8_staffSignBack(self):
        u"员工签退考勤，经度无效"
        url = self.url + "/api/attendance/staffSignBack?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignBack"
        cookie = {"token": TOKEN}
        paramter = {"scene": "aaa", "longitude": "", "latitude": "40.002678", "staff_sign_id": "123"}
        img = open("E:\\demo1\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10194)

    def test_9_staffSignBack(self):
        u"员工签退考勤，纬度无效"
        url = self.url + "/api/attendance/staffSignBack?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/staffSignBack"
        cookie = {"token": TOKEN}
        paramter = {"scene": "aaa", "longitude": "23.333333", "latitude": "", "staff_sign_id": "123"}
        img = open("E:\\demo1\\resouce\\12345.jpg", "rb")
        files = {"scene_img": img}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie, files=files)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10195)


if __name__ == "__main__":
    unittest.main()
