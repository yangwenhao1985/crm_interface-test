# -*- coding:utf-8 -*-
__author__ = 'Michael'
import unittest
import requests
import json
from common import method
import time
TOKEN = 0
class extend2(unittest.TestCase):
    def setUp(self):
        times = int(time.time())
        self.times_str = str(times)
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    def test_0_getStaffSignIn(self):
        u"获取考勤记录,日期无效"
        url = self.url + "/api/attendance/getStaffSignIn?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/attendance/getStaffSignIn"
        global TOKEN
        TOKEN = method.generate_app_token("18801409523", "Y+a1dRVSmYh\/GAow9N6xdQ==")
        cookie = {"token": TOKEN}
        paramter = {"date": ""}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10286)

    def test_1_myCourseArrangement(self):
        u"我的排课，时间类型无效"
        url = self.url + "/api/user/myCourseArrangement?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/user/myCourseArrangement"
        cookie = {"token": TOKEN}
        paramter = {"time_type": "3"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10144)

    def test_2_getMyDaily(self):
        u"获取我的日报，日期无效"
        url = self.url + "/api/daily/getMyDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/getMyDaily"
        cookie = {"token": TOKEN}
        paramter = {"date": ""}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10286)

    def test_3_addDaily(self):
        u"添加日报，日期无效"
        url = self.url + "/api/daily/addDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/addDaily"
        cookie = {"token": TOKEN}
        paramter = {"date": "", "work_plan": "yeah yeah yeah", "work_summary": "yeah yeah yeah"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10286)

    def test_4_addDaily(self):
        u"添加日报，工作总结无效"
        url = self.url + "/api/daily/addDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/addDaily"
        cookie = {"token": TOKEN}
        paramter = {"date": "2017-06-25", "work_plan": "yeah yeah yeah", "work_summary": ""}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10496)

    def test_5_addDaily(self):
        u"添加日报，工作计划无效"
        url = self.url + "/api/daily/addDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/addDaily"
        cookie = {"token": TOKEN}
        paramter = {"date": "2017-06-25", "work_plan": "go go go", "work_summary": "oh my god"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10495)

    def test_6_modifyDaily(self):
        u"修改日报，日报id无效"
        url = self.url + "/api/daily/modifyDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/modifyDaily"
        cookie = {"token": TOKEN}
        paramter = {"daily_id": "", "date": "2017-06-26", "work_plan": "NO NO NO", "work_summary": "NO NO NO"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10489)

    def test_7_modifyDaily(self):
        u"修改日报，日报日期无效"
        url = self.url + "/api/daily/modifyDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/modifyDaily"
        cookie = {"token": TOKEN}
        paramter = {"daily_id": "1977", "date": "", "work_plan": "NO NO NO", "work_summary": "NO NO NO"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10286)

    def test_8_modifyDaily(self):
        u"修改日报，工作总结无效"
        url = self.url + "/api/daily/modifyDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/modifyDaily"
        cookie = {"token": TOKEN}
        paramter = {"daily_id": "1977", "date": "2017-06-26", "work_plan": "NO NO NO", "work_summary": ""}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10496)

    def test_9_modifyDaily(self):
        u"修改日报，工作计划无效"
        url = self.url + "/api/daily/modifyDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/modifyDaily"
        cookie = {"token": TOKEN}
        paramter = {"daily_id": "1977", "date": "2017-06-26", "work_plan": "", "work_summary": "yes yes yes"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10497)


if __name__ == "__main__":
    unittest.main()