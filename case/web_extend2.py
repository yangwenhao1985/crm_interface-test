# -*- coding:utf-8 -*-
__author__ = 'michael'
import requests
import unittest
import json
from common import method
TOKEN = 0
class extend2(unittest.TestCase):
    def setUp(self):
        self.url = "http://qa.education.hy-sport.cn"

    def tearDown(self):
        pass

    def test_0_ajax_delete_venues_by_venues_ids(self):
        u"删除场馆,场馆ID无效"
        uri = "/venues/ajax_delete_venues_by_venues_ids"
        url = self.url + uri
        global TOKEN
        TOKEN = method.generate_web_token()
        cookie = {"token": TOKEN}
        paramter = {"venues_ids": ""}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10125)

    def test_1_ajax_get_user_list(self):
        u"获取用户列表，公司ID无效"
        uri = "/user/ajax_get_user_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148)

    def test_2_ajax_get_user_list(self):
        u"获取用户列表，页数无效"
        uri = "/user/ajax_get_user_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"page": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10119)

    def test_3_ajax_get_user_list(self):
        u"获取用户列表，每页条数无效"
        uri = "/user/ajax_get_user_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"page_size": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10120)

    def test_4_ajax_get_user(self):
        u"获取账号详情，用户ID无效"
        uri = "/user/ajax_get_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10139)

    def test_5_ajax_get_department_list(self):
        u"获取账号的部门列表，公司ID无效"
        uri = "/user/ajax_get_department_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148)

    def test_6_ajax_get_role_list_by_department_id(self):
        u"获取职位列表通过部门id，公司ID无效"
        uri = "/user/ajax_get_role_list_by_department_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "", "department_id": "5"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148)

    def test_7_ajax_get_role_list_by_department_id(self):
        u"获取职位列表通过部门id"
        uri = "/user/ajax_get_role_list_by_department_id"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17", "department_id": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10324)

    def test_8_ajax_get_superior_leader_list(self):
        u"获取上级列表，公司ID无效"
        uri = "/user/ajax_get_superior_leader_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "", "role_id": "9"}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148)

    def test_9_ajax_get_superior_leader_list(self):
        u"获取上级列表，角色ID无效"
        uri = "/user/ajax_get_superior_leader_list"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"company_id": "17", "role_id": ""}
        response = requests.get(url, params=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10137)

    def test_A_ajax_modify_user(self):
        u"修改用户帐号信息,用户ID无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10139)

    def test_B_ajax_modify_user(self):
        u"修改用户帐号信息，姓名无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10112)

    def test_C_ajax_modify_user(self):
        u"修改用户帐号信息，角色ID无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10137)

    def test_D_ajax_modify_user(self):
        u"修改用户帐号信息，级别ID无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10321)

    def test_E_ajax_modify_user(self):
        u"修改用户帐号信息，部门ID无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10324)

    def test_F_ajax_modify_user(self):
        u"修改用户帐号信息，头像ID无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10111)

    def test_G_ajax_modify_user(self):
        u"修改用户帐号信息，微信号无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10116)

    def test_H_ajax_modify_user(self):
        u"修改用户帐号信息，性别无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10163)

    def test_I_ajax_modify_user(self):
        u"修改用户帐号信息，邮箱无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10117)

    def test_J_ajax_modify_user(self):
        u"修改用户帐号信息，公司ID无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10148)

    def test_K_ajax_modify_user(self):
        u"修改用户帐号信息，上级无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": ""}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10158)

    def test_L_ajax_modify_user(self):
        u"修改用户帐号信息，科目ID无效"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "15212344321", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10123)

    def test_M_ajax_modify_user(self):
        u"修改用户帐号信息，手机号已经存在"
        uri = "/user/ajax_modify_user"
        url = self.url + uri
        cookie = {"token": TOKEN}
        paramter = {"uid": "3096", "name": "michael", "role_id": "9", "level_id": "21", "department_id": "5", "birthday": "",
                    "phone": "18701458751", "avatar_id": "698520", "sex_id": "1", "weixin_num": "234234234324", "email": "234233@qq.com",
                    "company_id": "17", "address": "", "emergency_contact": "", "phone1": "", "height": "", "nation_id": "", "weight":"",
                    "education_level_id": "", "education_experience": "", "category_ids": "1|2", "english_level_id": "",
                    "computer_level_id": "", "fid": "43"}
        response = requests.post(url, data=paramter, cookies=cookie)
        text = response.content
        dic = json.loads(text)
        self.assertEqual(dic["errcode"], 10135)


if __name__ == "__main__":
    unittest.main()