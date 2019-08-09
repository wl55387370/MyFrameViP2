# -*- coding:utf-8 -*-
# @Time    :2019/7/1 0001 16:38
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: yanxuan-refund.py
# @Software: PyCharm


import requests
import json
import threading
import time
import pymysql

def get_t():
    return int(time.time()*1000)

def login(acc_pass):
    headers = {
        'Authorization': '',
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/1.02.1904090 MicroMessenger/6.7.3 Language/zh_CN webview/",
        # 'Host': 'yanxuan.t.iwubida.com',
        # 'Referer': 'http://yanxuan.t.iwubida.com/login',
        # 'Accept': 'application/json, text/plain, */*',
        # 'Origin' : 'http://yanxuan.t.iwubida.com'

    }
    #acc_pass = json.dumps(acc_pass)
    print (acc_pass)
    # response = requests.post("http://yanxuan.t.iwubida.com/api/yx/company/session/create_token?", data=acc_pass, headers=headers)
    response = requests.post("http://yanxuan.t.iwubida.com/api/yx/company/session/create_token?", data=acc_pass)
    return response.json().get('result')

def order_page(Authorization,user_ID = 0):
    headers = {
        'Authorization': Authorization,
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/1.02.1904090 MicroMessenger/6.7.3 Language/zh_CN webview/",
        # 'Accept': 'application/json, text/plain, */*',
        # 'Referer': 'http://yanxuan.t.iwubida.com/user_order/user_order_manage'

    }


    data = {
        'startDate' : time.strftime("%Y-%m-%d", time.localtime()),
        'endDate' : time.strftime("%Y-%m-%d", time.localtime()),
        'page' : 0,
        'size' : 10,
        'queryStatus': 'underway',
        't' : get_t()
    }
    print (data)
    response = requests.get("http://yanxuan.t.iwubida.com/api/yx/company/order/page?", params=data,
                             headers=headers)

    r_list = response.json().get('results')
    """
    获得需要退款的列表
    根据userId来筛选想要退款的列表
    列表生成式（）
    """
    return [x.get('orderId') for x in r_list if x.get('userId') == user_ID]

def to_refund(orderID,Authorization):
    headers = {
        'Authorization': Authorization,
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/1.02.1904090 MicroMessenger/6.7.3 Language/zh_CN webview/",
        # 'Host': 'yanxuan.t.iwubida.com',
        # 'Referer': 'http://yanxuan.t.iwubida.com/user_order/user_order_datail',
        # 'Accept': 'application/json, text/plain, */*',
        # 'Origin': 'http://yanxuan.t.iwubida.com',
        'Content-Type' : 'application/json;charset=UTF-8'
    }
    data = {
        'orderId' : orderID,
        'reason' : "测试退款"
    }

    response = requests.post("http://yanxuan.t.iwubida.com/api/yx/company/order/refund?t={}".format(get_t()), json=data,
                             headers=headers)
    print (response.json())

if __name__=="__main__":

    acc_pass ={'accountName':'admin', 'password':'123456'}

    Authorization = login(acc_pass)

    user_ID = 45

    refundList = order_page(Authorization,user_ID)

    print (refundList)

    for i in refundList:

        to_refund(i,Authorization)

    print ("退款完毕")