#coding=utf8
import jsonpath,json
from inter.httpkeys import HTTP
from common.Excel import Reader, Writer

# if __name__=="__main__":
#
#     http = HTTP()
#
#     http.get('https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php','query=1.1.1.1&co=&resource_id=6006&t=1558255414490&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery11020031084788174859712_1558255397360&_=1558255397366')

# s='{"status":"0","t":"1558255414490","set_cache_time":"","data":[{"location":"澳大利亚","titlecont":"IP地址查询","origip":"1.1.1.1","origipquery":"1.1.1.1","showlamp":"1","showLikeShare":1,"shareImage":1,"ExtendedLocation":"","OriginQuery":"1.1.1.1","tplt":"ip","resourceid":"6006","fetchkey":"1.1.1.1","appinfo":"","role_id":0,"disp_type":0}]}'
#
# jsonres  = json.loads(s)
# r = jsonpath.jsonpath(jsonres,"$.data.[0].location")
# print(r[0])
#
# print(jsonres['data'][0]['location'])

# from inter.soapkeys import SOAP
# #
# # soap =SOAP(None)
# # soap.adddoctor()
# # soap.setwsdl('http://112.74.191.10:8081/inter/SOAP?wsdl')
# # soap.callmethod('auth')
# # soap.savejson('token','token')
# # soap.addheader('token','{token}')
# # soap.callmethod('login','will、123456')
# # soap.callmethod('logout')

# from colorama import Fore, Back, Style
from colorama import Fore
# for color in ['GREEN', 'RED', 'BLUE', 'YELLOW', 'WHITE']:
for color in ['GREEN', 'RED']:
    print(getattr(Fore, color), "It's color will be", color)
    # print (getattr(Back, color), "It's color will be", color)
    # print( Style.RESET_ALL)
