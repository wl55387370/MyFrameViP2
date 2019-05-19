# coding=utf8
import pymysql


# 处理.sql备份文件为SQL语句
def __read_sql_file(file_path):
    # 打开SQL文件到f
    sql_list = []
    with open(file_path, 'r', encoding='utf8') as f:
        # 逐行读取和处理SQL文件
        for line in f.readlines():
            # 如果是配置数据库的SQL语句，就去掉末尾的换行
            if line.startswith('SET'):
                sql_list.append(line.replace('\n', ''))
            # 如果是删除表的语句，则改成删除表中的数据
            elif line.startswith('DROP'):
                sql_list.append(line.replace('DROP', 'TRUNCATE').replace(' IF EXISTS', '').replace('\n', ''))
            # 如果是插入语句，也删除末尾的换行
            elif line.startswith('INSERT'):
                sql_list.append(line.replace('\n', ''))
                # 如果是删除语句，也删除末尾的换行
            elif line.startswith('delete') or line.startswith('DELETE'):
                sql_list.append(line.replace('\n', ''))
            # 如果是其他语句，就忽略
            else:
                pass
    return sql_list


mysql_config = {
    'mysqluser': "root",
    'mysqlpassword': "123456",
    'mysqlport': 3306,
    'mysqlhost': 'localhost',
    'mysqldb': 'test_project',
    'mysqlcharset': "utf8"
}

# 创建连接，执行语句的时候是在这个连接
connect = pymysql.connect(
    user=mysql_config['mysqluser'],
    password=mysql_config['mysqlpassword'],
    port=mysql_config['mysqlport'],
    host=mysql_config['mysqlhost'],
    db=mysql_config['mysqldb'],
    charset=mysql_config['mysqlcharset']
)

# 获取游标
cursor = connect.cursor()
print("正在恢复%s数据库")
# 一行一行执行SQL语句
# 第一种方法
for sql in __read_sql_file("C:\\Users\\Administrator\\Desktop\\userinfo.sql"):
    cursor.execute(sql)
    connect.commit()
# ====第二种方法
# cursor.execute("delete from userinfo where username like 'Tes%'or linkname like '测试账号'")
# result = cursor.fetchall()
# print(result)
#
# connect.commit()
# 关闭游标和连接
cursor.close()
connect.close()
