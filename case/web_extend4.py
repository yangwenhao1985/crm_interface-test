# -*- coding:utf-8 -*-
__author__ = 'HeYu'
import unittest
from common import method
import json
import requests
TOKEN = 0
class extend4(unittest.TestCase):
    def setUp(self):
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    def test_0_ajax_get_user_information_by_uid(self):
        u"获取账号详情id为空时"
        uri = "/user/ajax_get_user_information_by_uid"
        url = self.url + uri
        global TOKEN
        TOKEN = method.generate_web_token()
        cookie = {"token": TOKEN}
        paramter = {"uid": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10139)

    def test_1_ajax_reset_passwd(self):
        u"重置账号密码，手机号无效"
        uri = "/user/ajax_reset_passwd"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"phone": "", "type": "3"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10110)

    def test_2_ajax_reset_passwd(self):
        u"重置账号密码,发送短信类型为空"
        uri = "/user/ajax_reset_passwd"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"phone": "18701458751", "type": ""}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10144)

    def test_3_ajax_reset_passwd(self):
        u"重置账号密码,手机号不存在"
        uri = "/user/ajax_reset_passwd"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"phone": "13699999999", "type": "3"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10172)

    def test_4_ajax_add_venues(self):
        u"添加场馆,名称为空"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "", "address": "soho", "longitude": "116.3999900000",
                    "latitude": "59.8797577200", "category_ids": "1", "status": "0"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10112)

    def test_5_ajax_add_venues(self):
        u"添加场馆,地址为空"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "DaChang", "address": "", "longitude": "116.3999900000",
                    "latitude": "59.8797577200", "category_ids": "1", "status": "0"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10115)

    def test_6_ajax_add_venues(self):
        u"添加场馆,经度为空"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "DaChang", "address": "soho", "longitude": "",
                    "latitude": "59.8797577200", "category_ids": "1", "status": "0"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10194)

    def test_7_ajax_add_venues(self):
        u"添加场馆,纬度为空"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "DaChang", "address": "soho", "longitude": "116.3999900000",
                    "latitude": "", "category_ids": "1", "status": "0"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10195)

    def test_8_ajax_add_venues(self):
        u"添加场馆,科目为空"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "DaChang", "address": "soho", "longitude": "116.3999900000",
                    "latitude": "59.8797577200", "category_ids": "", "status": "0"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10402)

    def test_9_ajax_add_venues(self):
        u"添加场馆,场馆状态为空"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "DaChang", "address": "soho", "longitude": "116.3999900000",
                    "latitude": "59.8797577200", "category_ids": "1", "status": ""}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10164)

    def test_A_ajax_add_venues(self):
        u"添加场馆,科目为空"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "DaChang", "address": "soho", "longitude": "116.3999900000",
                    "latitude": "59.8797577200", "category_ids": "", "status": "0"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10402)

    def test_B_ajax_add_venues(self):
        u"添加场馆,名称已存在"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "test_venues3", "address": "sohosoho", "longitude": "116.3999900000",
                    "latitude": "59.8797577200", "category_ids": "1", "status": "0"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10403)

    def test_C_ajax_add_venues(self):
        u"添加场馆,地点已存在"
        uri = "/venues/ajax_add_venues"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"name": "DaChang", "address": "soho", "longitude": "116.3999900000",
                    "latitude": "59.8797577200", "category_ids": "", "status": "0"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10488)

    def test_D_ajax_add_user(self):
        u"添加用户帐号信息,头像为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10111)

    def test_E_ajax_add_user(self):
        u"添加用户帐号信息,名字为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10112)

    def test_F_ajax_add_user(self):
        u"添加用户帐号信息,手机号为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10110)

    def test_G_ajax_add_user(self):
        u"添加用户帐号信息,微信号为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10116)

    def test_H_ajax_add_user(self):
        u"添加用户帐号信息,公司为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148)

    def test_I_ajax_add_user(self):
        u"添加用户帐号信息,部门为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10324)

    def test_J_ajax_add_user(self):
        u"添加用户帐号信息,角色为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10137)

    def test_K_ajax_add_user(self):
        u"添加用户帐号信息,上级为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10158)

    def test_L_ajax_add_user(self):
        u"添加用户帐号信息,级别为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10321)

    def test_M_ajax_add_user(self):
        u"添加用户帐号信息,性别为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10163)

    def test_N_ajax_add_user(self):
        u"添加用户帐号信息,邮箱为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "18701458756", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": ""}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10117)

    def test_O_ajax_add_user(self):
        u"添加用户帐号信息,名字为空"
        uri = "/user/ajax_add_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"avatar_id": "698876", "name": "jack", "phone": "17600207135", "weixin_num": "rxwindows", "company_id": "17",
                    "department_id": "5", "role_id": "8", "manage_company_ids": "", "category_ids": "", "fid": "43", "level_id": "21",
                    "sex_id": "1", "email": "112@qq.com"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10135)

    def test_P_ajax_get_student_list(self):
        u"获取学员列表 关键字不存在"
        uri = "/student/ajax_get_student_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"keyword": "战狼", "company_id": "17"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10128)

    def test_Q_ajax_get_student_list(self):
        u"获取学员列表 公司为空"
        uri = "/student/ajax_get_student_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"keyword": "", "company_id": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148)

    def test_R_ajax_get_student_list(self):
        u"获取学员列表 起止日期不存在"
        uri = "/student/ajax_get_student_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"keyword": "", "company_id": "17","birth_begin_date":"abc"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10241)

    def test_S_ajax_get_student_list(self):
        u"获取学员列表 终止日期不存在"
        uri = "/student/ajax_get_student_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"keyword": "", "company_id": "17","birth_end_date":"abc"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10242)

    def test_T_ajax_get_student_list(self):
        u"获取学员列表  辅导老师不存在"
        uri = "/student/ajax_get_student_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"keyword": "", "company_id": "17","service_teacher_keyword":"abc"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10541)

    def test_U_ajax_get_student_list(self):
        u"获取学员列表  每页存在学员数错误"
        uri = "/student/ajax_get_student_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"keyword": "", "company_id": "17", "page_size": "abc"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10120)

    def test_V_ajax_get_student_list(self):
        u"获取学员列表  每页存在学员数错误"
        uri = "/student/ajax_get_student_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"keyword": "", "company_id": "17", "is_need_total_page": "99"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10165)

    def test_W_ajax_get_sign_up_list(self):
        u"获取报名列表 公司不存在"
        uri = "/sign_up/ajax_get_sign_up_list"
        url = self.url + uri
        dandan_token = method.get_token_for_dandan()
        cookie = {"token": dandan_token}
        parmter = {"company_id":"99"}
        response = requests.get(url,params=parmter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10148)

    def test_X_ajax_get_sign_up_list(self):
        u"获取报名列表 起始日期不存在"
        uri = "/sign_up/ajax_get_sign_up_list"
        url = self.url + uri
        dandan_token = method.get_token_for_dandan()
        cookie = {"token": dandan_token}
        parmter = {"begin_date":"abc"}
        response = requests.get(url,params=parmter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10241)

    def test_Y_ajax_get_sign_up_list(self):
        u"获取报名列表 终止日期日期不存在"
        uri = "/sign_up/ajax_get_sign_up_list"
        url = self.url + uri
        dandan_token = method.get_token_for_dandan()
        cookie = {"token": dandan_token}
        parmter = {"end_date":"abc"}
        response = requests.get(url,params=parmter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10242)

    def test_Z_ajax_get_sign_up_list(self):
        u"获取报名列表 page为空"
        uri = "/sign_up/ajax_get_sign_up_list"
        url = self.url + uri
        dandan_token = method.get_token_for_dandan()
        cookie = {"token": dandan_token}
        parmter = {"page":""}
        response = requests.get(url,params=parmter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10119)

    def test_ajax_get_sign_up_list(self):
        u"获取报名列表 每页展示跳数错误"
        uri = "/sign_up/ajax_get_sign_up_list"
        url = self.url + uri
        dandan_token = method.get_token_for_dandan()
        cookie = {"token": dandan_token}
        parmter = {"page_size":"abc"}
        response = requests.get(url,params=parmter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10220)

    def test_ajax_get_sign_up_list(self):
        u"获取报名列表 获取不存在的页数"
        uri = "/sign_up/ajax_get_sign_up_list"
        url = self.url + uri
        dandan_token = method.get_token_for_dandan()
        cookie = {"token": dandan_token}
        parmter = {"is_need_total_page":"99"}
        response = requests.get(url,params=parmter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10165)

    def test_ajax_get_daily_list(self):
        u"获取日报列表  公司为空"
        uri = "/daily/ajax_get_daily_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        patamter = {"company_id": "", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=patamter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10148)

    def test_ajax_get_daily_list(self):
        u"获取日报列表  当前页为空"
        uri = "/daily/ajax_get_daily_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        patamter = {"company_id": "17", "page": "", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=patamter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10119)

    def test_ajax_get_daily_list(self):
        u"获取日报列表  每页展示条数为空"
        uri = "/daily/ajax_get_daily_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        patamter = {"company_id": "17", "page": "1", "page_size": "", "is_need_total_page": "1"}
        response = requests.get(url, params=patamter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10148)

    def test_ajax_get_daily_list(self):
        u"获取日报列表  总页数为空"
        uri = "/daily/ajax_get_daily_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        patamter = {"company_id": "17", "page": "1", "page_size": "15", "is_need_total_page": ""}
        response = requests.get(url, params=patamter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10165)

    def test_ajax_get_daily_list(self):
        u"获取日报列表  关键字不存在"
        uri = "/daily/ajax_get_daily_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        patamter = {"company_id": "17","keyword":"abc", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=patamter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10128)

    def test_ajax_get_daily_list(self):
        u"获取日报列表  起始日期不存在"
        uri = "/daily/ajax_get_daily_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        patamter = {"company_id": "17","begin_date":"abc", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=patamter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10241)

    def test_ajax_get_daily_list(self):
        u"获取日报列表  终止日期不存在"
        uri = "/daily/ajax_get_daily_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        patamter = {"company_id": "17","end_date":"abc", "page": "1", "page_size": "15", "is_need_total_page": "1"}
        response = requests.get(url, params=patamter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"],10242)

    def test_ajax_get_daily(self):
        u"查看日报  ID为空"
        uri = "/daily/ajax_get_daily"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"daily_id": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 0)

if __name__ == "__main__":
    unittest.main()