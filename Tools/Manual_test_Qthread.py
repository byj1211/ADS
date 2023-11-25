import logging
import time
from Tools.data_all import all_data
import PyQt5.QtCore
from PyQt5.QtCore import pyqtSignal, QThread
from Tools.func_test import func_all_test
from Tools.Interfaces import JDK23
from Tools.func_test import DO,AI,AO,DI,AI_test
logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
#调度线程
class Manual_testQthread(QThread):
    signal_thread_finished=pyqtSignal(str,int)
    signal_change_item=pyqtSignal(str)
    signal_revolt=pyqtSignal(str)
    signal_re_sends=pyqtSignal(str,str)   #re sends ,state
    def __init__(self,test_typr,chan,set_volt,all_func_test):
        super(Manual_testQthread, self).__init__()
        logging.info(" Now is runing {} channel is {}, set_volt is {}".format(test_typr,chan,set_volt))
        # self.testname=testname
        self.test_sigle=all_func_test  #tools - control all devices
        self.test_type=test_typr
        self.chan=chan
        self.set_volt=set_volt
        self.daemon = True
        self.flag = True
        self.test_func = {
            "AI": {
                "5vdc": "AI_5vdc_test",
                "28vdc": "AI_28vdc_test",
                "mvdc": "AI_mvdc_test",
                "ac": "AI_ac_test",
                "r": "AI_r_test"
            },
            "AO": []
        }
        print("have into manual test")




    def run(self) -> None:
        if self.flag==True:
            print("manual thread is runing ")
            if self.test_type=="AI":
                ai_type=all_data["AI"]["sort_class"][int(self.chan)]
                func_str=self.test_func["AI"][str(ai_type)]
                exe_func=getattr(self.test_sigle,func_str)
                exe_func(self.chan,self.set_volt)
            time.sleep(3)
            self.signal_thread_finished.emit(self.test_type,self.chan)
    def stop_thread(self):
        self.flag=False
        self.quit()
        print("manual thread has stop ")
    def sort_out_testItem(self,testname):
        print(testname)