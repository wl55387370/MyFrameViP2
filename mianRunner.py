# coding=utf8
from common.Excel import Reader, Writer
from inter.httpkeys import HTTP


def runCases(http,line):
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

        if line[3] == "post":
            http.post(line[4],line[5])
            return

        if line[3] == "seturl":
            http.seturl(line[4])
            return

        if line[3] == "assertequals":
            http.assertequals(line[4],line[5])
            return

        if line[3] == "removeheader":
            http.removeheader(line[4])
            return

        if line[3] == "addheader":
            http.addheader(line[4],line[5])
            return

        if line[3] == "savejson":
            http.savejson(line[4],line[5])
            return


if __name__ == "__main__":
    print("整个框架使用该入口执行")
    reader = Reader()
    http = HTTP()
    reader.open_excel('./lib/HTTP接口用例.xls')
    sheetname = reader.get_sheets()
    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        for i in range(reader.rows):
            line = reader.readline()
            print(line)
            runCases(http,line)
