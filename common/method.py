# -*- coding:utf-8 -*-
__author__ = 'Michael'
import requests
import hashlib
import time
import json
import operator
import xlrd
def generate_sign(post_data, times_str, uri):
    rc_key = "2718b9b2d90ee5b42eea46412de0454e"
    param_str = ""
    num = 0
    get_data = {"cid": "ab837d90-429d-47bd-befb-9ec05a6bf8eb", "did": "373a34a8-2862-383e-8f29-111712273746",
                "os": "Android", "osv": "4.4.4", "t": times_str, "v": "2.9.1", "c": "official", "rc_id": "1"}
    paramter = {}
    paramter.update(get_data)
    paramter.update(post_data)
    list_key = []
    for key in paramter:
        list_key.append(key)
    list_key.sort()
    for i in list_key:
        param_str += i + "=" + paramter[i]
        if not operator.eq(i,list_key[-1]):
            param_str += "&"
    sign_str = uri + param_str + rc_key
    sign_str_encode = sign_str.encode("utf-8")
    sign = hashlib.sha1(sign_str_encode).hexdigest()
    return sign

def generate_app_token(phone, passwd):
    times = int(time.time())
    times_str = str(times)
    paramter = {"phone": phone, "passwd": passwd}
    uri = "/api/user/login"
    sign = generate_sign(paramter, times_str, uri)
    url = "http://qa.education.hy-sport.cn/api/user/login?c=official&cid=ab837d90-429d-47bd-befb-9ec05a6bf8eb&did=373a34a8-2862-383e-8f29-111712273746&os=Android&osv=4.4.4"
    time_str = "&" + "t" + "=" + times_str
    sys_str = "&v=2.9.1&rc_id=1"
    sign_str = "&" + "sign" + "=" + sign
    url = url + time_str + sys_str + sign_str
    response = requests.post(url, data=paramter)
    text = response.content
    dic = json.loads(text)
    return dic["data"]["token"]

def generate_web_token(): #获取运营经理的token
    url = "http://qa.education.hy-sport.cn/user/ajax_login"
    paramter = {"phone": "18600000006", "passwd": "123456qwe"}
    response = requests.post(url, data=paramter)
    text = response.content
    dic = json.loads(text)
    token = dic["data"]["token"]
    return token

def get_token_for_dandan(): #获取丹丹账号的token
    url = "http://qa.education.hy-sport.cn/user/ajax_login"
    paramter = {"phone": "18500564388", "passwd": "123456qwe"}
    response = requests.post(url, data=paramter)
    text = response.content
    dic = json.loads(text)
    token = dic["data"]["token"]
    return token

def read_excel(sheet_name,uri,path = "E:\\crm_interface-test\\resouce\\interface_data.xlsx"):
    with xlrd.open_workbook(path) as data:
        table = data.sheet_by_name(sheet_name)
        nrows = table.nrows
        param_list = []
        for i in range(nrows):
            if table.row_values(i)[0] == uri:
                param = eval(table.row_values(i)[1])
                code = eval(table.row_values(i)[2])
                tup1 = (param,code)
                param_list.append(tup1)
        # print(param_list)
        return param_list

if __name__ == "__main__":
    read_excel("APP","/api/user/login")