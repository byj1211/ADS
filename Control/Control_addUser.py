import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox

from Tools.sqlTools import DBCon
from UISet.UISet_AddUser import AddUserWindow


class Control_addUser(AddUserWindow):
    def __init__(self, parent=None):
        super(Control_addUser, self).__init__(parent)
        self.setWindowModality(Qt.ApplicationModal)#应用程序模态，将阻塞与其关联的父窗口和其他兄弟窗口

    # 点击清理表格内容
    def cleanAll(self):
        """
        清空输入框中内容
        """
        self.le_id.clear()
        self.le_username.clear()
        self.le_mobile.clear()
        self.le_depart.clear()
        self.le_password.clear()
        self.cb_gender.setCurrentIndex(0)

    # 添加用户事件
    # @disp_error
    def addUser(self):
        """
        点击pb_addUser时，触发该函数
        :return:
        """
        try:
            uname = self.le_id.text()  # 获取le_username中的文本数据
            passwd = self.le_password.text()  # 获取le_password中的文本数据
            name = self.le_username.text()  # 获取le_name中的文本数据
            sex = self.cb_gender.currentText()  # 获取le_sex中的文本数据
            tel = self.le_mobile.text()  # 获取le_tel中的文本数据
            depart = self.le_depart.text()  # 获取le_depart中的文本数据
            flag = self.isVaild(uname, passwd, name, sex, tel, depart)  # 获取是否输入是否合法
            if flag == 'Vaild':  # 如果合法，直接增加到数据库中
                DBCon().insterItem(uname, passwd, name, sex, tel, depart)  # 增加到数据库中

                self.mymessage = QMessageBox()  # 创建一个弹窗
                self.mymessage.setWindowTitle('创建成功')  # 设置弹窗显示的主题
                self.mymessage.setText('创建成功！')  # 设置弹窗显示的内容
                self.mymessage.setIcon(QMessageBox.Information)  # 设置默认的窗口类型，
                self.mymessage.setWindowFlag(Qt.FramelessWindowHint)  # 设置窗口无边框
                # self.mymessage.setStandardButtons(QMessageBox.Ok | QMessageBox.No)  # 设置默认的按钮类型
                # self.mymessage.setObjectName('mymessagestyle')  # 设置stylesheet

                # ####弹窗样式设置
                self.mymessage.setStyleSheet('''
                                                        QMessageBox QLabel{font-family:"Arial";color:rgb(255, 255, 255);font-size:18px;}
                                                        QMessageBox{background-color:rgb(80,80,80);border:1px solid rgb(0,0,0);border-radius:4px;}
                                                    ''')
                self.mymessage.show()  # 显示弹窗
                self.close()  # 关闭创建用户页面

            else:  # 输入不合法，根据原因，修改提示信息
                hintText = "请重新输入！"  # 设置初始提示信息
                if flag == 'UsernameIsEmpty':  # 如果是账户ID为空
                    hintText = '账户ID不能为空！'
                elif flag == 'PasswordIsEmpty':  # 如果密码为空
                    hintText = '密码不能为空！'
                elif flag == 'UserIsExist':  # 如果用户已存在
                    hintText = '用户已存在，请重新输入！'
                self.mymessage = QMessageBox()
                self.mymessage.setWindowTitle('创建失败')  # 弹跳窗口显示的主题
                self.mymessage.setText(hintText)  # 将提示信息放到窗口里
                self.mymessage.setIcon(QMessageBox.Critical)  # 设置默认的窗口类型，
                self.mymessage.setWindowFlag(Qt.FramelessWindowHint)
                # 弹窗样式设置
                self.mymessage.setStyleSheet('''
                                                        QMessageBox QLabel{font-family:"Arial";color:rgb(255, 255, 255);font-size:18px;}
                                                        QMessageBox{background-color:rgb(80,80,80);border:1px solid rgb(0,0,0);border-radius:4px;}
                                                    ''')
                self.mymessage.show()  # 显示该窗口

        except Exception as e:
            print(e)

    # ------------ 判断输入是否合法-------------------
    def isVaild(self, uname, passwd, name, sex, tel, depart):
        """
        判断输入是否合法
        :param uname:
        :param passwd:
        :param name:
        :param sex:
        :param tel:
        :param depart:
        :return:
        """
        print(uname, passwd, name, sex, tel, depart)
        if uname == '':  # 如果账户ID为空，则返回'UsernameIsEmpty'
            return 'UsernameIsEmpty'
        elif uname == 'admin':
            return 'UserIsExist'
        elif passwd == '':  # 如果密码为空，则返回'PasswordIsEmpty'
            return 'PasswordIsEmpty'
        else:  # 账户ID和密码都不为空，进行数据库查询
            isExist = DBCon().searchItem(uname)  # 进行数据库查询，是否已经存在
            if isExist:  # 如果已经存在，则返回'UserIsExist'
                return 'UserIsExist'
            # 其他情况返回'Vaild'
            return "Vaild"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ContorlAddUserWindow = Control_addUser()
    ContorlAddUserWindow.show()
    sys.exit(app.exec_())
