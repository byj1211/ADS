import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow

from UI.py import UI_Login as UI


class LoginWindow(QMainWindow, UI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)  # 设置无法修改大小
        self.setupUi(self)  # 设置UI

        # 屏幕居中
        screen = QDesktopWidget().screenGeometry()  # 获取屏幕的大小
        self.top = int((screen.width() - self.width()) / 2)  # 顶部坐标
        self.left = int((screen.height() - self.height()) / 2)  # 左侧坐标
        self.setGeometry(self.top, self.left, self.width(), self.height())  # 设置居中


    def slot_pb_login(self):
        # print("123")
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LoginWindow = LoginWindow()
    LoginWindow.show()
    sys.exit(app.exec_())
