# coding=utf8
from common.Excel import Reader, Writer
from inter.httpkeys import HTTP
import inspect


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
            print("waring:框架暂时只支持3个参数！")


if __name__ == "__main__":
    print("整个框架使用该入口执行")
    reader = Reader()
    # http = HTTP()
    reader.open_excel('./lib/HTTP接口用例.xls')
    sheetname = reader.get_sheets()
    print(sheetname)

    writer = Writer()
    writer.copy_open('./lib/HTTP接口用例.xls', './lib/result-HTTP接口用例.xls')
    # sheetname = writer.get_sheets()

    http = HTTP(writer)

    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        writer.set_sheet(sheet)
        writer.clo = 7
        for i in range(reader.rows):
            writer.row = i
            line = reader.readline()
            print(line)
            try:
                runCases(http, line)
            except Exception as e:
                pass
    writer.save_close()
