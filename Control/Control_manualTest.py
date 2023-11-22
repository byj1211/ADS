import datetime
import sys

import pyvisa
from PyQt5.QtWidgets import QApplication
from Tools.Manual_test_Qthread import Manual_testQthread
from Tools.DevicesPools import ACPower
from UISet.UISet_ManualTest import ManualTestWindow
from Tools.func_test import autoTest_func,ThreadPowerOn

class Control_manualTest(ManualTestWindow):
    def __init__(self, parent=None):
        super(Control_manualTest, self).__init__(parent)
        self.PushButton_115.toggled.connect(self.test_output_on)
        self.PushButton_28.toggled.connect(self.test_output_on)
        self.PushButton_signal_generaor.toggled.connect(self.test_output_on)
        self.PushButton_28_test.toggled.connect(self.test_output_on)
        self.pushButton_equip_outp_on={"ac":self.PushButton_115,"dc1":self.PushButton_28,"generator":self.PushButton_signal_generaor,
                            "dc2":self.PushButton_28_test}
#-----------这部分是自动上电线程的设置-----------------------------------
        global autoTest_func1
        autoTest_func1=None
        # autoTest_func1 = autoTest_func()
        # self.thread_power_on= ThreadPowerOn(autoTest_func1)
        # self.thread_power_on.signal_send_data_UI.connect(self.write_power_on_return_data)
        # self.thread_power_on.finish.connect(self.stop_thread)
        # self.thread_power_on.aoto_test.devices_init_autoTest()
        # self.thread_power_on.start_thread()
        #
        # self.auto_tabWidget.currentChanged.connect(self.tab_change)

#--------------公共变量的定义--------------------------------------------
        self.power_on_re_linedit={"ac115_volt":self.le_man_115v_vOUT_2,"ac115_curr":self.le_man_115v_cOUT_2,
                                  "ac115_freq":self.le_man_115v_fOUT_2,
                                  "dc28_volt":self.le_man_28v_vOUT_2,"dc28_curr":self.le_man_28v_cOUT_2,
                                  "ac_volt":self.le_man_speed_ampOUT_2,"ac_freq":self.le_man_speed_fOUT_2,
                                  "dc_volt":self.test_28_v_read,"dc_curr":self.test_28_c_read}
        self.AI_button_init_all()

        self.manuel_thread =None

    def AI_button_init(self):
        for key, button in self.AI_button.items():
            button.setEnabled(True)
            button.setCheckable(True)
            button.toggled.connect(self.AI_button_style_change)
            button.toggled.connect(self.AI_button_start_thread)
    def AI_button_init_all(self):
        self.AI_button_init()
    def AI_thread_off(self):
        bt=self.manuel_thread.stop_thread()
        self.set_single_buttonOff_stylesheet(bt)
        self.manuel_thread=None
    def AI_button_start_thread(self,checked):
        if checked:
            if self.manuel_thread==None:
                reverse_dict = {val: key for key, val in self.AI_button.items()}
                test_name=reverse_dict.get(self.sender())
                para=self.dsb_auto_ai_AIN_EDT_3.text()
                self.manuel_thread=Manual_testQthread(self.sender(),test_name,para)
                self.manuel_thread.signal_thread_finished.connect(self.AI_thread_off)
                self.manuel_thread.start()
                self.sender().setCheckable(False)
        # else:
        #     if self.manuel_thread!=None:
        #         self.manuel_thread.stop_thread()
        #         self.manuel_thread=None
    def stop_thread(self):
        print("guanbi")
        self.thread_power_on=None

    def write_power_on_return_data(self,name,data):
        self.power_on_re_linedit[name].setText(data)

    def tab_change(self,sender):
        '''

        :param sender:
        :return:
        '''
        # sender = self.sender()
        print("---------------------------")
        index=sender
        print(index)
        if index==0:
            if self.thread_power_on==None:
                self.thread_power_on = ThreadPowerOn(autoTest_func1)
                self.thread_power_on.signal_send_data_UI.connect(self.write_power_on_return_data)
                self.thread_power_on.finish.connect(self.stop_thread)
                self.thread_power_on.start_thread()
                # self.thread_power_on.start_thread()
                # print(datetime.datetime.now())
            #
            # if not self.thread_power_on.is_running:
            #     # print(sender.currentIndex())
            #     self.thread_power_on.is_running=True
            #     # self.thread_power_on.start_thread()
        else:
                pass
        if index!=0:
            if self.thread_power_on !=None:
                self.thread_power_on.stop()
            else:
                pass
    def test_output_on(self,checked):
        '''

        :param checked:
        :return:
        '''
        sender = self.sender()
        for key, button in self.pushButton_equip_outp_on.items():
            if button == sender:
                euip_name=key
                break
            else:
                euip_name=""
        if checked:
            autoTest_func1.set_equip_output_state(euip_name,1)
        else:
            autoTest_func1.set_equip_output_state(euip_name,0)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ContorlAutoTestWindow = Control_manualTest()
    ContorlAutoTestWindow.show()

    sys.exit(app.exec_())

# global a=["dsb_auto_ai_AIN_EDT_3"]