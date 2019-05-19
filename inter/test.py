#coding=utf8
from inter.httpkeys import HTTP

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


from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
import  time

imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')
doctor = ImportDoctor(imp)

client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl',doctor=doctor)

res = client.service.getWeatherbyCityName('长沙')
print(res)
time.sleep(1)
res = client.service.getWeatherbyCityName('北京')
print(res)
time.sleep(1)
res = client.service.getWeatherbyCityName('上海')
print(res)