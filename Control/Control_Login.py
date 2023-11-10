import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox

from Control.Control_adminMenus import Control_adminMenus
from Control.Control_userMenus import Control_userMenus
from Tools.sqlTools import DBCon
from UISet import UISet_Login


class Control_Login(UISet_Login.LoginWindow):
    def __init__(self):
        super(Control_Login, self).__init__()

    # ------------登录失败函数--------------------------
    def login_failed(self):
        """
        登录失败
        :return:
        """
        self.mymessage = QMessageBox()  # 创建提示框
        self.mymessage.setWindowTitle('登录错误')  # 弹跳窗口显示的主题
        self.mymessage.setText('用户名或密码错误!')
        self.mymessage.setIcon(QMessageBox.Information)  # 设置默认的窗口类型，
        self.mymessage.setWindowFlag(Qt.FramelessWindowHint)  # 设置无边框
        # self.mymessage.setStandardButtons(QMessageBox.Ok | QMessageBox.No)  # 设置默认的按钮类型

        # self.mymessage.setObjectName('mymessagestyle')  # 设置stylesheet
        # ####弹窗样式设置
        self.mymessage.setStyleSheet('''
                            QMessageBox QLabel{font-family:"Arial";color:rgb(255, 255, 255);font-size:18px;}
                            QMessageBox{background-color:rgb(80,80,80);border:1px solid rgb(0,0,0);border-radius:4px;}
                        ''')

        self.mymessage.show()  # 显示窗口

    # ----------------登录成功函数---------------------
    def login_successed(self, userType):
        """
        登录成功
        :param userType:用户类型
        :return:
        """
        if userType == 'admin':
            self.mainmenus = Control_adminMenus()
        else:
            self.mainmenus = Control_userMenus()
        self.mainmenus.show()

    # ----------点击登录时判断是否登录成功函数-----------------------
    def slot_pb_login(self):
        """
        点击登录按钮触发该函数
        :return:
        """
        uname = self.le_username.text()  # 获取le_username里的文本信息
        passwd = self.le_password.text()  # 获取le_password里的文本信息
        flag = DBCon().searchItem(uname, passwd)  # 从数据库中获取是否存在该用户
        if flag:  # 如果存在，即登录成功
            userType = DBCon().isSuperUser(uname, passwd)  # 得到该用户权限，创建主窗口
            self.login_successed(userType)
        else:  # 登陆失败 ，提示弹窗
            self.login_failed()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ContorlLoginWindow = Control_Login()
    ContorlLoginWindow.show()
    sys.exit(app.exec_())
