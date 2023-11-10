import sqlite3

# 若无该数据库，则创建Sqlite数据库并打开
# 若有，则直接打开数据库
from Tools.Interfaces import BASE_DIR

sqlFile = BASE_DIR+r'\Resources\test.db'  # 数据库文件名


superusername = 'admin'  # 超级用户名
superpassword = '88888888'  # 超级用户名的密码


class DBCon:
    def init(self):  # 初始化数据库 将admin:88888888加入到初始数据库
        try:
            conn = self.getDBConn()  # 打开数据库
            cursor = conn.cursor()  # 获取该数据库的游标
            # 执行一条SQL语句，创建user表:
            cursor.execute(
                'CREATE TABLE User (ID INTEGER Primary KEY, Username TEXT, Password TEXT,Name TEXT,Sex INTEGER ,Tel TEXT, Depart TEXT)')  # 创建数据表
            sql = f"INSERT INTO User (Username, Password,Name,Sex,Tel,Depart) VALUES ({superusername}, {superpassword},'admin','admin','admin','admin')"  # 将admin:88888888增加到数据库里的sql语句
            cursor.execute(sql)  # 执行该sql语句
            cursor.close()  # 关闭Cursor:
            conn.commit()  # 提交事务:
            conn.close()  # 关闭Connection
        except Exception as e:
            print(f'错误文件是:{e.__traceback__.tb_frame.f_globals["__file__"]}\t'
                  f'错误所在行数 line at : {e.__traceback__.tb_lineno}\n错误是', e)


    def getDBConn(self):
        conn = sqlite3.connect(sqlFile)  # 获得数据库的连接对象
        return conn

    def insterItem(self, uname, passwd, name, sex, tel, depart):
        """
        增
        :param uname:
        :param passwd:
        :param name:
        :param sex:
        :param tel:
        :param depart:
        :return:
        """
        try:
            conn = self.getDBConn()  # 打开数据库
            cursor = conn.cursor()  # 获取该数据库的游标
            sql = f'insert into User (Username,Password,Name,Sex,Tel,Depart)VALUES("{uname}","{passwd}","{name}","{sex}","{tel}","{depart}")'  # 构造sql语句
            result = cursor.execute(sql)  # 执行sql语句
            print(sql)
            if result != None:  # 插入成功
                print("insert successed!")
            else:  # 插入失败
                print("insert failed!")
            conn.commit()  # 提交事务
            conn.close()  # 关闭Connection
        except Exception as e:
            print(f'错误文件是:{e.__traceback__.tb_frame.f_globals["__file__"]}\t'
                  f'错误所在行数 line at : {e.__traceback__.tb_lineno}\n错误是', e)

    def searchItem(self, uname, passwd=None):
        """
        查
        :param uname:
        :param passwd:
        :return:
        """
        try:
            if passwd is None:  # 只有用户名，没有密码，用于注册
                conn = self.getDBConn()  # 连接数据库
                cursor = conn.cursor()  # 获得游标
                sql = f'select * from User where username="{uname}" and password="{passwd}"'  # 拼接sql语句
                # print(sql)
                cursor.execute(sql)  # 执行sql语句
                data = cursor.fetchall()  # 获得查询后的数据
                cursor.close()  # 关闭Cursor
                conn.close()  # 关闭Connection
                if len(data) != 0:  # 如果有返回数据，则表示查找到用户，返回True
                    return True
                else:
                    return False  # 没找到则返回False
            else:  # 既有用户名也有密码，用于登录。
                conn = self.getDBConn()  # 连接数据库
                cursor = conn.cursor()  # 获得游标
                sql = f'select * from User where username="{uname}" and password="{passwd}"'
                # print(sql)
                cursor.execute(sql)  # 执行sql语句
                data = cursor.fetchall()  # 获得查询后的数据
                cursor.close()  # 关闭Cursor
                conn.close()  # 关闭Connection
                if len(data) != 0:  # 如果有返回数据，则表示查找到用户，返回True
                    return True
                else:
                    return False  # 没找到则返回False
        except Exception as e:
            print(f'错误文件是:{e.__traceback__.tb_frame.f_globals["__file__"]}\t'
                  f'错误所在行数 line at : {e.__traceback__.tb_lineno}\n错误是', e)
            return False

    def isSuperUser(self, uname, passwd):
        """
        判断是否为超级用户
        :param uname:
        :param passwd:
        :return:
        """
        if uname == superusername and passwd == superpassword:  # 是超级用户
            return 'admin'
        else:  # 不是超级用户
            return 'other'


if __name__ == '__main__':
    print(sqlFile)
    conn = sqlite3.connect(sqlFile)  # 获得数据库的连接对象
    print(conn)
    # DBCon().init()
    # DBCon().insterItem('1', '1', '1', '1', '1', '1')
    # DBCon().insterItem('1', '1', '1', '1', '1', '1')
