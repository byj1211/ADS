import sys

from PyQt5.QtWidgets import QApplication

from Control.Control_Login import Control_Login


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ContorlLoginWindow = Control_Login()
    ContorlLoginWindow.show()
    sys.exit(app.exec_())
