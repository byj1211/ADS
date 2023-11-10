import sys

from PyQt5.QtWidgets import QApplication

from UISet.UISet_AdminMainMenus import AdminMainMenusWindow
from Control.Control_addUser import Control_addUser


class Control_adminMenus(AdminMainMenusWindow):
    def __init__(self, parent=None):
        super(Control_adminMenus, self).__init__(parent)

        # self.pb_createUser.clicked.connect(self.a)
        # 初始化按钮
        # self.pb_autoTest.setEnabled(False)
        # self.pb_manualTest.setEnabled(False)
        # self.pb_testReport.setEnabled(False)

    def on_clicked_pb_createUser(self):
        """
        点击创建用户按钮 执行该函数
        """
        self.window = Control_addUser()  # 新建用户窗口
        self.window.show()  # 显示窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ControladminWindow = Control_adminMenus()
    ControladminWindow.show()
    sys.exit(app.exec_())
