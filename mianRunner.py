# coding=utf8
from common.Excel import Reader, Writer
from inter.httpkeys import HTTP
from inter.soapkeys import SOAP
import inspect,time
from common import logger,config
from common.mysql import Mysql
from common.mail import Mail
from common.excelresult import Res

def runCases(http, line):
    """
    执行每一行用例的方法
    :param line: 参数列表
    :return: 无
    """
    if len(line[0]) > 0 or len(line[1]) > 0:
        # 分组信息不用执行
        pass
    else:
        # 执行用例
        #
        # if line[3] == "post":
        #     http.post(line[4],line[5])
        #     return
        #
        # if line[3] == "seturl":
        #     http.seturl(line[4])
        #     return
        #
        # if line[3] == "assertequals":
        #     http.assertequals(line[4],line[5])
        #     return
        #
        # if line[3] == "removeheader":
        #     http.removeheader(line[4])
        #     return
        #
        # if line[3] == "addheader":
        #     http.addheader(line[4],line[5])
        #     return
        #
        # if line[3] == "savejson":
        #     http.savejson(line[4],line[5])
        #     return
        func = getattr(http, line[3])
        p = inspect.getfullargspec(func).__str__()
        p = p[p.find('args=') + 5:p.find(', varargs')]
        p = eval(p)
        p.remove('self')

        if len(p) == 0:
            func()
        elif len(p) == 1:
            func(line[4])
        elif len(p) == 2:
            func(line[4], line[5])
        elif len(p) == 3:
            func(line[4], line[5], line[6])
        else:
            logger.warn("waring:框架暂时只支持3个参数！")


if __name__ == "__main__":
    logger.info("整个框架使用该入口执行")
    #运行用例之前，初始化配置，初始化数据库
    config.get_config('./lib/conf.properties')
    mysql = Mysql()
    mysql.init_mysql('./lib/userinfo.sql')

    #开始读取用例
    reader = Reader()
    # http = HTTP()
    # reader.open_excel('./lib/HTTP接口用例.xls')
    reader.open_excel('./lib/SOAP.xls')
    sheetname = reader.get_sheets()
    logger.info(sheetname)

    writer = Writer()
    # writer.copy_open('./lib/HTTP接口用例.xls', './lib/result-HTTP接口用例.xls')
    writer.copy_open('./lib/SOAP.xls', './lib/result-SOAP.xls')
    # sheetname = writer.get_sheets()

    #获取开始时间
    t = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    #设置shet页
    writer.set_sheet(sheetname[0])
    # 写入结果文件
    writer.write(1,3,t)

    #识别接口类型
    reader.readline()
    line = reader.readline()
    if line[1] =='HTTP':

        http = HTTP(writer)
    else:
        http = SOAP(writer)
    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        writer.set_sheet(sheet)
        writer.clo = 7
        for i in range(reader.rows):
            writer.row = i
            line = reader.readline()
            logger.info(line)
            try:
                runCases(http, line)
            except Exception as e:
                # pass
                logger.exception(e)

    writer.set_sheet(sheetname[0])
    # 获取结束时间
    t = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # 设置shet页

    # 写入结果文件
    writer.write(1, 4, t)
    writer.save_close()

    res = Res()
    # result = res.get_res('./lib/result-HTTP接口用例.xls')
    result = res.get_res('./lib/result-SOAP.xls')
    print(result)


    mail = Mail()
    mail.mail_info['mail_subject'] = result['title']
    mailtxt= config.config['mailtxt']
    mailtxt = mailtxt.replace('title',result['title'])
    mailtxt = mailtxt.replace('status', result['status'])
    mailtxt = mailtxt.replace('runtype', result['runtype'])
    mailtxt = mailtxt.replace('passrate', result['passrate'])
    mailtxt = mailtxt.replace('starttime', result['starttime'])
    mailtxt = mailtxt.replace('casecount', result['casecount'])
    mailtxt = mailtxt.replace('endtime', result['endtime'])

    if result['status'] =='Fail':
        mailtxt = mailtxt.replace('#00d800','red')

    config.config['mailtxt']=mailtxt

    #附件的路径，如果有多个就用，分割
    # mail.mail_info['filepaths'] = ['./lib/result-HTTP接口用例.xls']
    # mail.mail_info['filenames'] = ['result-HTTP.xls']
    mail.mail_info['filepaths'] = ['./lib/result-SOAP.xls']
    mail.mail_info['filenames'] = ['result-SOAP.xls']
    mail.send(config.config['mailtxt'])
