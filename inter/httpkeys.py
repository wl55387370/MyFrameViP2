# coding=utf8
import requests,jsonpath,json
from common import logger

class HTTP():
    """
    http协议接口测试的关键字类
    提供调用http接口的各种方法
    提供接口测试结果断言的各种方法
    """

    def __init__(self,w):
        # 在创建对象的时候初始化session
        self.session = requests.session()
        # 设置请求的基本url
        self.url = ""
        self.params = {}
        self.result = None
        self.jsonres = None
        self.json = {}
        self.writer=w
        self.session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'

    def seturl(self, u):
        # 设置请求的基本url
        self.url = u + "/"
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.url))

    def removeheader(self, key):
        # 从请求的头里面删除key的值
        try:
            self.session.headers.pop(key)
        except Exception as e:
            logger.exception(e)

        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.session.headers))

    def addheader(self, key, value):
        # 往请求的头里添加一个键值对
        value = self.__get_value(value)
        self.session.headers[key] = value
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo+1, str(self.session.headers))

    def post(self, path, params=None):
        # 解析参数为一个dict
        # 调用post方法,请求接口
        self.__get_params(params)
        self.result = self.session.post(self.url + path, data=self.params)
        logger.info(self.result.text)
        self.jsonres = json.loads(self.__to_json(self.result.text))
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo+1, str(self.jsonres))


    def get(self, path, params=None):
        # 调用get,请求接口
        self.result = self.session.get(self.url + path + '?' + params)
        self.jsonres = json.loads(self.__to_json(self.result.text))
        self.writer.write(self.writer.row, self.writer.clo, "PASS")
        self.writer.write(self.writer.row, self.writer.clo+1, str(self.jsonres))


    def __to_json(self, res):
        # get方法不是纯json格式
        return res[res.find('{'):res.rfind('}') + 1]

    def __get_params(self, p):

        # 每一次解析参数之前先清空参数dict
        self.params.clear()
        if p is None or p=='':
            return self.params
            # return {}
        # 分割每一个键值队
        pp = p.split('&')
        # 遍历每一个键值队
        for s in pp:
            # 分割每一个参数的键和值
            ppp = s.split('=')
            # self.params[ppp[0]] = ppp[1]
            try:
                self.params[ppp[0]] = ppp[1]
            except Exception as e:
                self.params[ppp[0]] = None

        return self.params

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
