# -*- coding:utf-8 -*-
__author__ = 'Michael'
import unittest
import requests
import json
from common import method
import time
TOKEN = 0
class extend3(unittest.TestCase):
    def setUp(self):
        times = int(time.time())
        self.times_str = str(times)
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    def test_0_getUnderlingListForDaily(self):
        u"获取汇报给我的日报列表"
        url = self.url + "/api/daily/getUnderlingListForDaily?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/daily/getUnderlingListForDaily"
        global TOKEN
        TOKEN = method.generate_app_token("18801409523", "Y+a1dRVSmYh\/GAow9N6xdQ==")
        cookie = {"token": TOKEN}
        paramter = {"date": "dddd"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10286)

    def test_1_getStudentListByPhone(self):
        u"学员补卡：查询学生信息，手机号无效"
        url = self.url + "/api/student/getStudentListByPhone?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/student/getStudentListByPhone"
        cookie = {"token": TOKEN}
        paramter = {"phone": ""}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10110)

    def test_2_sendCode(self):
        u"发送短信，手机号无效"
        url = self.url + "/api/user/sendCode?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/user/sendCode"
        cookie = {"token": TOKEN}
        paramter = {"phone": "", "source": "3"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10110)

    def test_3_sendCode(self):
        u"发送短信，用户不存在"
        url = self.url + "/api/user/sendCode?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/user/sendCode"
        cookie = {"token": TOKEN}
        paramter = {"phone": "18701458753", "source": "3"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10142)

    def test_4_upCard(self):
        u"补卡,学生id无效"
        url = self.url + "/api/student/upCard?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/student/upCard"
        cookie = {"token": TOKEN}
        paramter = {"sms_code": "2432", "student_id": "", "card_num": "cf16e09a", "source": "3", "phone": "18701458751"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10118)

    def test_5_upCard(self):
        u"补卡，卡号无效"
        url = self.url + "/api/student/upCard?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/student/upCard"
        cookie = {"token": TOKEN}
        paramter = {"sms_code": "2432", "student_id": "44088", "card_num": "", "source": "3", "phone": "18701458751"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10179)

    def test_6_upCard(self):
        u"补卡，请求来源无效"
        url = self.url + "/api/student/upCard?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
        uri = "/api/student/upCard"
        cookie = {"token": TOKEN}
        paramter = {"sms_code": "2432", "student_id": "44088", "card_num": "cf16e09a", "source": "", "phone": "18701458751"}
        sign = method.generate_sign(paramter, self.times_str, uri)
        time_str = "&" + "t" + "=" + self.times_str
        str = "&v=2.9.1&rc_id=1"
        sign_str = "&" + "sign" + "=" + sign
        url = url + time_str + str + sign_str
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10154)



if __name__ == "__main__":
    unittest.main()