import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow

from UI.py import UI_AddUser as UI


class AddUserWindow(QMainWindow, UI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddUserWindow, self).__init__(parent)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)  # 设置无法修改大小
        self.setupUi(self)  # 设置UI
        # try:
        #     self.cb_gender.lineEdit().setAlignment(Qt.AlignCenter)
        # except Exception as e:
        #     print(e)



        # 屏幕居中
        screen = QDesktopWidget().screenGeometry()  # 获取屏幕的大小
        self.top = int((screen.width() - self.width()) / 2)  # 顶部坐标
        self.left = int((screen.height() - self.height()) / 2)  # 左侧坐标
        self.setGeometry(self.top, self.left, self.width(), self.height())  # 设置居中

    def cleanAll(self):
        # print("1")
        pass

    def addUser(self):
        # print("2")
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    AddUserWindow = AddUserWindow()
    AddUserWindow.show()
    sys.exit(app.exec_())
