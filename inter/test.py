#coding=utf8
from inter.httpkeys import HTTP
import  requests


# session = requests.session()
# # session.headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
# # session.headers['Content-Type']= 'application/x-www-form-urlencoded'
# #
# # res = session.post('https://www.zhihu.com/udid',data=None)
# # print(res.text)
# # res=session.get('https://www.zhihu.com/api/v3/oauth/captcha?lang=en')
# # print(res.text)
# # session.headers['x-zse-83'] = '3_1.1'



# print(session.cookies)
# print(session.headers)

# res =session.post('https://www.zhihu.com/api/v3/oauth/sign_in',data='')
# print(res.text)
# res = session.get('https://www.zhihu.com/logout',data=None)
# print(res.text)


# if __name__ == "__main__":
    # h = {
    # #     'a':'aa',
    # #     'b':'bb'
    # # }
    # # h.pop('a')
    # s = '1+1'
    # a=eval(s)
    # print(a)

    # http = HTTP()
    # http.seturl('http://112.74.191.10:8081/inter/HTTP')
    # http.addheader('token','0d862fe621ae4bca86489a554945b202')
    # http.post('login','username=Will&password=123456')
    # http.assertequals('status','405')
    #
    # http.addheader('token', None)
    # http.post('auth')
    # http.savejson('token','token')
    # http.addheader('token','{token}')
    # http.post('login', 'username=Will&password=123456')
    # http.assertequals('status', '200')
    #
    # http.addheader('token', '{token}')
    # http.post('login', 'username=Will&password=123456')
    # http.assertequals('status', '406')
    #
    # http.post('logout')
    # http.assertequals('status', '200')


# from suds.client import Client
# from suds.xsd.doctor import ImportDoctor, Import
# import  time
#
# imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
# imp.filter.add('http://WebXml.com.cn/')
# doctor = ImportDoctor(imp)
#
# client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl',doctor=doctor)
#
# res = client.service.getWeatherbyCityName('长沙')
# print(res)
# time.sleep(1)
# res = client.service.getWeatherbyCityName('北京')
# print(res)
# time.sleep(1)
# res = client.service.getWeatherbyCityName('上海')
# print(res)
import requests,json
session = requests.session()
result = session.post("http://112.74.191.10:8081/inter/REST/auth")
token=json.loads(result.text)['token']
session.headers['token']=token

result=session.post("http://112.74.191.10:8081/inter/REST/user/register", json='{"username":"Tester","pwd":"123456","nickname":"测试账号","describe":"这是一个测试注册的账号"}')
print(result.text)