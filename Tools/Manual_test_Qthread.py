import logging
import time

from PyQt5.QtCore import pyqtSignal, QThread
from Tools.func_test import func_all_test
from Tools.Interfaces import JDK23
from Tools.func_test import DO,AI,AO,DI
logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Manual_testQthread(QThread):
    signal_thread_finished=pyqtSignal()
    signal_change_item=pyqtSignal(str)
    def __init__(self,button,testname,para):
        super(Manual_testQthread, self).__init__()
        self.testname=testname
        self.daemon = True
        self.flag = True
        self.bt=button
        self.test = {
            "AI": {
                "5vdc": self.AI_5vdc_test,
                "28vdc": self.AI_28vdc_test,
                "mvdc": self.AI_mvdc_test,
                "ac": self.AI_ac_test,
                "r": self.AI_r_test
            },
            "AO": []
        }

    def AI_r_test(self):
        pass
    def AI_ac_test(self):
        pass

    def AI_mvdc_test(self):
        pass

    def AI_28vdc_test(self):
        pass

    def AI_5vdc_test(self):
        test_name = self.testname.split("_")[1]
        chanel = self.testname.split("_")[2]
        choices = JDK23.AITest.CHES['{:02X}'.format(chanel)]['tpvf']
        for choice in choices:
            idx = JDK23.AITest.CHES['{:02X}'.format(chanel)]['tpvf'].index(choice)
            sends = JDK23.AITest.CHES['{:02X}'.format(chanel)]['tps'][idx]  # 获取发送指令
            print(choice,sends)
            #delay 设置为全关



    def run(self) -> None:
        if self.flag==True:
            print("manual thread is runing ")
            self.bt.setText("A")
            time.sleep(5)
            self.signal_thread_finished.emit()
    def stop_thread(self):
        self.flag=False
        self.quit()
        print("manual thread has stop ")
        return self.bt
    def sort_out_testItem(self,testname):
        print(testname)