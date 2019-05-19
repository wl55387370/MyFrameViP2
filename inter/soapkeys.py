# coding=utf8
import jsonpath,json
from common import logger
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
import  time

class SOAP():
    """
       webserive协议接口测试的关键字类
       提供调用webserive接口的各种方法
       提供接口测试结果断言的各种方法
       """

    def __init__(self, w):
        # 设置请求的基本wsdl
        self.wsdl = ""
        # self.params = []
        self.result = None
        self.jsonres = None
        self.json = {}
        self.writer = w
        self.header ={}
        self.doctor =None
        self.client =None

    def adddoctor(self,s='',n=''):
        #使用suds.client创建一个客服端，用来请求webservice服务器
        # imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
        imp = Import('http://www.w3.org/2001/XMLSchema', location=s)
        # imp.filter.add('http://WebXml.com.cn/')
        imp.filter.add(n)
        self.doctor = ImportDoctor(imp)
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.doctor))

    def setwsdl(self,wurl):
        self.wsdl=wurl
        self.client=Client('http://112.74.191.10:8081/inter/SOAP?wsdl',headers=self.header,doctor=self.doctor)
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.wsdl))


    def removeheader(self,key):
        try:
            self.header.pop(key)
        except Exception as e:
            pass
        self.client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl', headers=self.header, doctor=self.doctor)
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.header))


    def addheader(self,key,value):
        # 往请求的头里添加一个键值对
        value = self.__get_value(value)
        self.header[key] = value
        self.client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl', headers=self.header, doctor=self.doctor)
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.header))

    def callmethod(self,m,p=None):
        if p==None or p=='':
            params=[]
        else:
            try:
                value = self.__get_value(p)
                params=value.split('、')
            except Exception as e:
                params = []
        self.result = self.client.service.__getattr__(m)(*params)
        self.jsonres = json.loads(self.__to_json(self.result))
        # print(self.result)
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))

    def assertequals(self, key, value):
        """
        校验返回的json结果里面.key对应的值是否和预期的value一致
        :param key:要校验的json的键
        :param value:期望值
        :return:无
        """
        # if str(self.jsonres[key]) == value:
        #利用jsonpath断言
        if str(jsonpath.jsonpath(self.jsonres, key)[0]) == value:
            # print("PASS")
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo+1, str(jsonpath.jsonpath(self.jsonres, key)[0]))
        else:
            # print("FAIL")
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(jsonpath.jsonpath(self.jsonres, key)[0]))




    def __to_json(self, res):
        # get方法不是纯json格式
        return res[res.find('{'):res.rfind('}') + 1]





    def savejson(self, key, p):
        """
        将返回结果里面.json的key的值，保存到我们框架的p这个参数里面
        :param key:需要保存的json值的键
        :param p:保存后的参数名
        :return:无
        """
        logger.info(self.jsonres)
        # self.json[key] = self.jsonres[p]
        self.json[p] = str(jsonpath.jsonpath(self.jsonres, key)[0])
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        # self.writer.write(self.writer.row, self.writer.clo + 1, self.jsonres[key])
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.json))


    def __get_value(self, p):
        # 用{key}的形式去替换参数里面的字符串，如果没有就不替换
        for key in self.json.keys():
            p = p.replace('{' + key + '}', self.json[key])
        return p