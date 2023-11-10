import sys

from PyQt5.QtWidgets import QApplication

from UISet.UISet_UserMainMenus import UserMainMenusWindow


class Control_userMenus(UserMainMenusWindow):
    def __init__(self, parent=None):
        super(Control_userMenus, self).__init__(parent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ContorluserWindow = Control_userMenus()
    ContorluserWindow.show()
    sys.exit(app.exec_())
