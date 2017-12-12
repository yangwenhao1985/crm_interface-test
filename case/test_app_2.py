# -*- coding:utf-8 -*-
__author__ = 'Michael'
import unittest
import time
import requests
import json
from common import method
from nose_parameterized import parameterized
TOKEN = 0
class test2(unittest.TestCase):
    def setUp(self):
        times = int(time.time())
        self.times_str = str(times)
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    @parameterized.expand(input=method.read_excel("APP","/api/attendance/getVisitCustomerInfo"))
    def test_0_getVisitCustomerInfo(self,paramter,code):
        u"获取正在拜访的客户"
        url = self.url + "/api/attendance/getVisitCustomerInfo?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/getVisitCustomerInfo"
        global TOKEN
        TOKEN = method.generate_app_token("18801409523", "Y+a1dRVSmYh\/GAow9N6xdQ==")
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

    @parameterized.expand(input=method.read_excel("APP","/api/attendance/getStaffSignIn"))
    def test_1_getStaffSignIn(self,paramter,code):
        u"获取考勤记录"
        url = self.url + "/api/attendance/getStaffSignIn?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/getStaffSignIn"
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

    @parameterized.expand(input=method.read_excel("APP","/api/user/myCourseArrangement"))
    def test_2_myCourseArrangement(self,paramter,code):
        u"我的排课"
        url = self.url + "/api/user/myCourseArrangement?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/user/myCourseArrangement"
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

    @parameterized.expand(input=method.read_excel("APP","/api/user/myAllCourseArrangement"))
    def test_3_myAllCourseArrangement(self,paramter,code):
        u"获取教练全部一周的排课"
        url = self.url + "/api/user/myAllCourseArrangement?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/user/myAllCourseArrangement"
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

    @parameterized.expand(input=method.read_excel("APP","/api/daily/getMyDaily"))
    def test_4_getMyDaily(self,paramter,code):
        u"获取我的日报"
        url = self.url + "/api/daily/getMyDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/getMyDaily"
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

    @parameterized.expand(input=method.read_excel("APP","/api/daily/addDaily"))
    def test_5_addDaily(self,paramter,code):
        u"添加日报,10495：日报已经存在"
        url = self.url + "/api/daily/addDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/addDaily"
        cookie = {"token": TOKEN}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("APP","/api/daily/modifyDaily"))
    def test_6_modifyDaily(self,paramter,code):
        u"修改日报"
        url = self.url + "/api/daily/modifyDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/modifyDaily"
        cookie = {"token": TOKEN}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("APP","/api/daily/getUnderlingListForDaily"))
    def test_7_getUnderlingListForDaily(self,paramter,code):
        u"获取汇报给我的日报列表"
        url = self.url + "/api/daily/getUnderlingListForDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/getUnderlingListForDaily"
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

    @parameterized.expand(input=method.read_excel("APP","/api/student/getStudentListByPhone"))
    def test_8_getStudentListByPhone(self,paramter,code):
        u"学员补卡：查询学生信息"
        url = self.url + "/api/student/getStudentListByPhone?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/student/getStudentListByPhone"
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

    @parameterized.expand(input=method.read_excel("APP","/api/user/sendCode"))
    def test_9_sendCode(self,paramter,code):
        u"发送短信，短信发送次数到了，返回10169"
        url = self.url + "/api/user/sendCode?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/user/sendCode"
        cookie = {"token": TOKEN}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])

    @parameterized.expand(input=method.read_excel("APP","/api/student/upCard"))
    def test_A_upCard(self,paramter,code):
        u"补卡,无法获取返回的验证码，验证码错误返回10178"
        url = self.url + "/api/student/upCard?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/student/upCard"
        cookie = {"token": TOKEN}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], code["errcode"])


if __name__ == "__main__":
    unittest.main()

