import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow

from UI.py import UI_UserMainMenus as UI


class UserMainMenusWindow(QMainWindow, UI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UserMainMenusWindow, self).__init__(parent)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)  # 设置无法修改大小
        self.setupUi(self)  # 设置UI

        # 屏幕居中
        screen = QDesktopWidget().screenGeometry()  # 获取屏幕的大小
        self.top = int((screen.width() - self.width()) / 2)  # 顶部坐标
        self.left = int((screen.height() - self.height()) / 2)  # 左侧坐标
        self.setGeometry(self.top, self.left, self.width(), self.height())  # 设置居中

    # 给测试项绑定事件
    def on_clicked_pb_inspectProtect(self):
        ...

    def on_clicked_autoTest(self):
        ...

    def on_clicked_manualTest(self):
        ...

    def on_clicked_pb_testReport(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UserMainMenusWindow = UserMainMenusWindow()
    UserMainMenusWindow.show()
    sys.exit(app.exec_())
