import sys
import threading
import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication

from Tools.DevicesPools import *
from UISet.UISet_InsProtect import inspectProtectWindow


class Control_insPro(inspectProtectWindow):
    styleChangeSignal = pyqtSignal(list, bool)

    def __init__(self, parent=None):
        super(Control_insPro, self).__init__(parent)
        self.styleChangeSignal.connect(self.changestyle)
        self.devices = {
            'ac': ACPower(),
            'dc1': DCPower1(),
            'dc2': DCPower2(),
            'meter': Multimeter(),
            'generator': SignalGenerator()
        }
        self.devices_ui = [
            [self.cb_ins_115ac],
            [self.cb_ins_28dc1],
            [self.cb_ins_28dc2, self.cb_ins_card],
            [self.cb_ins_dataget, self.cb_ins_currget],
            [self.cb_ins_asg, self.cb_ins_dsg],
            [self.cb_ins_dcard, self.cb_ins_LR, self.cb_ins_429, self.cb_ins_232]
        ]
        self.pb_ins_confirm.clicked.connect(self.thread_on_clicked_pb_ins)
        self.pb_pro.clicked.connect(self.thread_on_clicked_pb_pro)

    def thread_on_clicked_pb_ins(self):
        self.thread = threading.Thread(target=self.on_clicked_pb_ins)
        self.thread.start()

    def on_clicked_pb_ins(self):
        for i, e in enumerate(self.devices.values()):
            flag = e.isExist()
            self.styleChangeSignal.emit(self.devices_ui[i], flag)
            print(i,flag)

        self.styleChangeSignal.emit(self.devices_ui[5], True)  # 最后四个选项

    def thread_on_clicked_pb_pro(self):
        self.thread = threading.Thread(target=self.on_clicked_pb_pro)
        self.thread.start()

    def on_clicked_pb_pro(self):
        dc_overcurr = self.le_pro_dc_overcur.text()
        dc_overvolt = self.le_pro_dc_overvolt.text()
        ac_mode = 'low' if self.rb_pro_adc_low.isChecked() else 'high'
        ac_overcurr = self.le_pro_ac_overcur.text()
        ac_overvolt = self.le_pro_ac_overvolt.text()
        ac_undervolt = self.le_pro_ac_lowvolt.text()
        ac_overpower = self.le_pro_ac_overPpro.text()
        self.devices['dc1'].write('CURR:PROT ' + dc_overcurr)
        self.devices['dc1'].write('VOLT:PROT ' + dc_overvolt)
        self.devices['ac'].write('VOLT:RANG:LOW')

    def changestyle(self, uis, flag):
        for i, e in enumerate(uis):
            if flag:
                e.setChecked(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ContorlAutoTestWindow = Control_insPro()
    ContorlAutoTestWindow.show()
    sys.exit(app.exec_())
