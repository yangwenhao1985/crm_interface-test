# -*- coding:utf-8 -*-
__author__ = 'yangwenhao'
import requests
import unittest
import json
from common import method
TOKEN = 0
class extend3(unittest.TestCase):
    def setUp(self):
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    def test_0_ajax_get_call_list(self):
        u"获取通话记录的列表---公司ID无效"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        global TOKEN
        TOKEN = method.generate_web_token()
        cookie = {"token": TOKEN}
        paramter = {"company_id": "", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148,msg=dic["errmsg"])

    def test_1_ajax_get_call_list(self):
        u"获取通话记录的列表---关键字无效"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17","keyword":"一二三四五六七八九十一", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        #print dic
        self.assertEqual(dic["errcode"], 10128,msg=dic["errmsg"])

    def test_2_ajax_get_call_list(self):
        u"获取通话记录的列表---开始时间无效"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17","begin_date":"2017-02-32","end_date":"2017-03-02", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        #print dic
        self.assertEqual(dic["errcode"],10126 ,msg=dic["errmsg"])

    def test_3_ajax_get_call_list(self):
        u"获取通话记录的列表---结束时间无效"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17","begin_date":"2017-02-02","end_date":"2017-02-32", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        #print dic
        self.assertEqual(dic["errcode"],10127 ,msg=dic["errmsg"])

    def test_4_ajax_get_call_list(self):
        u"获取通话记录的列表---通话状态无效"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17","status":"abc", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        #print dic
        self.assertEqual(dic["errcode"],10164 ,msg=dic["errmsg"])

    def test_5_ajax_get_call_list(self):
        u"获取通话记录的列表---当前页数无效"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17", "page": "0", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        #print dic
        self.assertEqual(dic["errcode"],10119 ,msg=dic["errmsg"])

    def test_6_ajax_get_call_list(self):
        u"获取通话记录的列表---当前页数无效"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17", "page": "1", "page_size": "abc", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        #print dic
        self.assertEqual(dic["errcode"],10120 ,msg=dic["errmsg"])

    def test_7_ajax_get_call_list(self):
        u"获取通话记录的列表---是否需要总页数无效"
        uri = "/call/ajax_get_call_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17", "page": "1", "page_size": "15", "is_need_total_page": "abc"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        #print dic
        self.assertEqual(dic["errcode"],10165 ,msg=dic["errmsg"])

    def test_8_ajax_get_time_table_list(self):
        u"获取排课信息列表---开始时间无效"
        uri = "/time_table/ajax_get_time_table_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"begin_date": "2017-02-33", "end_date": "2017-03","page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter,cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10241,msg=dic["errmsg"])

    def test_9_ajax_get_time_table_list(self):
        u"获取排课信息列表---结束时间无效"
        uri = "/time_table/ajax_get_time_table_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"begin_date": "2017-08", "end_date": "2017-131","page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter,cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10242,msg=dic["errmsg"])

    def test_A_ajax_get_time_table_list(self):
        u"获取排课信息列表---页数无效"
        uri = "/time_table/ajax_get_time_table_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"begin_date": "2017-08", "end_date": "2017-10","page": "0", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter,cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10119,msg=dic["errmsg"])

    def test_B_ajax_get_time_table_list(self):
        u"获取排课信息列表---每页条数无效"
        uri = "/time_table/ajax_get_time_table_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"begin_date": "2017-08", "end_date": "2017-10","page": "1", "page_size": "0", "is_need_total_page": "1"}
        response = requests.get(url, params=paramter,cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10120,msg=dic["errmsg"])

    def test_C_ajax_get_time_table_list(self):
        u"获取排课信息列表---每页条数无效"
        uri = "/time_table/ajax_get_time_table_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"begin_date": "2017-08", "end_date": "2017-10","page": "1", "page_size": "15", "is_need_total_page": "2"}
        response = requests.get(url, params=paramter,cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10165,msg=dic["errmsg"])

    def test_D_ajax_get_venues_list_by_category_id_and_date(self):
        u"根据科目获取场馆列表---科目ID无效"
        uri = "/venues/ajax_get_venues_list_by_category_id_and_date"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"category_id": "0", "date": "2017-07"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10123,msg=dic["errmsg"])

    def test_E_ajax_get_venues_list_by_category_id_and_date(self):
        u"根据科目获取场馆列表---科目ID无效"
        uri = "/venues/ajax_get_venues_list_by_category_id_and_date"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"category_id": "1", "date": "abc"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10286,msg=dic["errmsg"])

    def test_F_ajax_get_class_list_by_venues_id_and_date(self):
        u"通过场馆和周几获取班级列表（排课）---场馆ID无效"
        uri = "/class/ajax_get_class_list_by_venues_id_and_date"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "", "date": "2017-07", "category_id": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10125,msg=dic["errmsg"])

    def test_G_ajax_get_class_list_by_venues_id_and_date(self):
        u"通过场馆和周几获取班级列表（排课）---日期无效"
        uri = "/class/ajax_get_class_list_by_venues_id_and_date"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "34", "date": "abc", "category_id": "1"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10286,msg=dic["errmsg"])

    def test_H_ajax_get_class_list_by_venues_id_and_date(self):
        u"通过场馆和周几获取班级列表（排课）---科目ID无效"
        uri = "/class/ajax_get_class_list_by_venues_id_and_date"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "34", "date": "2017-02", "category_id": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10123,msg=dic["errmsg"])

    def test_I_ajax_get_coach_list(self):
        u"获取教练列表---科目ID无效"
        uri = "/time_table/ajax_get_coach_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"category_id": "0","keyword":"12345678901"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10123,msg=dic["errmsg"])

    def test_J_ajax_get_coach_list(self):
        u"获取教练列表---科目ID无效"
        uri = "/time_table/ajax_get_coach_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"category_id": "1","keyword":"1234567890111111111111111111111111111111111"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10128,msg=dic["errmsg"])

    def test_K_ajax_save_time_table(self):
        u"保存排课---日期无效"
        uri = "/time_table/ajax_save_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "341", "coach_id": "3106", "date": "abc", "class_ids": "6124|6100"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10286,msg=dic["errmsg"])

    def test_L_ajax_save_time_table(self):
        u"保存排课---教练ID无效"
        uri = "/time_table/ajax_save_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "341", "coach_id": "abc", "date": "2017-02", "class_ids": "6124|6100"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10131,msg=dic["errmsg"])

    def test_M_ajax_save_time_table(self):
        u"保存排课---场馆ID无效"
        uri = "/time_table/ajax_save_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "", "coach_id": "33", "date": "2017-02", "class_ids": "6124|6100"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10125,msg=dic["errmsg"])

    def test_N_ajax_save_time_table(self):
        u"保存排课---班级ID无效"
        uri = "/time_table/ajax_save_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "341", "coach_id": "33", "date": "2017-02", "class_ids": "6124|6100|||||"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10182,msg=dic["errmsg"])

    def test_O_ajax_save_time_table(self):
        u"保存排课---排课审批中不能保存"
        uri = "/time_table/ajax_save_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"venues_id": "341", "coach_id": "33", "date": "2017-12", "class_ids": "6124|6100"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10282,msg=dic["errmsg"])

    def test_P_ajax_submit_check_time_table(self):
        u"添加或修改排课时提交审批---排课表ID无效"
        uri = "/time_table/ajax_submit_check_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"time_table_id": ""}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10280,msg=dic["errmsg"])

    def test_Q_ajax_copy_time_table(self):
        u"复制排课---指定的月份已经排课"
        uri = "/time_table/ajax_copy_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"new_date": "2017-10", "old_date": "2017-07"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10285,msg=dic["errmsg"])

    def test_R_ajax_copy_time_table(self):
        u"复制排课---新时间无效"
        uri = "/time_table/ajax_copy_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"new_date": "2017-10-11", "old_date": "2017-07"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10293,msg=dic["errmsg"])

    def test_S_ajax_copy_time_table(self):
        u"复制排课---旧时间无效"
        uri = "/time_table/ajax_copy_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"new_date": "2017-10", "old_date": "2017-07-11"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10294,msg=dic["errmsg"])

    def test_T_ajax_copy_time_table(self):
        u"复制排课---新时间无效"
        uri = "/time_table/ajax_copy_time_table"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"new_date": "2017-12", "old_date": "2022-07"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10284,msg=dic["errmsg"])

if __name__ == "__main__":
    unittest.main()