import sys

from PyQt5.QtWidgets import QApplication

from Tools.DevicesPools import ACPower
from UISet.UISet_ManualTest import ManualTestWindow


class Control_manualTest(ManualTestWindow):
    def __init__(self, parent=None):
        super(Control_manualTest, self).__init__(parent)
        self.ac=ACPower()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ContorlAutoTestWindow = Control_manualTest()
    ContorlAutoTestWindow.show()
    sys.exit(app.exec_())
