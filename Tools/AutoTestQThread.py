import logging
import time

from PyQt5.QtCore import pyqtSignal, QThread
from Tools.func_test import func_all_test
from Tools.Interfaces import JDK23
from Tools.func_test import DO,AI,AO,DI
logging.getLogger(__name__)
from Tools.AI_demo import do_AI_test_FUNC


class AutoTestQThread(QThread):
    DITestSignal = pyqtSignal(int, int)  # channel, value
    DOTestSignal = pyqtSignal(int, int)  # channel, value
    AITestSignal = pyqtSignal(int, float)  # channel, value
    AOTestSignal = pyqtSignal(int, float)
    ChangeSignal = pyqtSignal(str)  # testItem
    InterruptSignal = pyqtSignal()
    RecvDataSignal = pyqtSignal(str)

    def __init__(self):
        super(AutoTestQThread, self).__init__()
        self.daemon = True
        self.flag = True
        self.all_func_test=func_all_test()
        self.AI=self.all_func_test.AI(self.all_func_test)
        self.DI=self.all_func_test.DI()
        # self.DO=DO(self.all_func_test)
        # self.AO=AO(func_all_test)
    def do_DI_Test(self):
        chansCount = 5
        choices = [0, 1]
        if self.flag:
            logging.info('Change to DITest')
            self.ChangeSignal.emit('DITest')
            time.sleep(1)
            logging.info('DI Test start')
            for i in range(0, chansCount + 1):
                if self.flag:
                    if i == 2:
                        for choice in [0, 1, 2]:
                            self.DITestSignal.emit(i, choice)
                            self.DI.test_channel(i,choice)
                            if i != chansCount:  # 0~5
                                logging.info(
                                    f'DI testing channel {i}, testValue {choice - 2 if choice == 2 else choice}')
                                time.sleep(1)
                    elif i == 3:
                        for choice in [0, 1, 2]:
                            self.DITestSignal.emit(i, choice)
                            self.DI.test_channel(i,choice)
                            if i != chansCount+1:
                                logging.info(
                                    f'DI testing channel {i}, testValue {choice - 1 if choice == 2 else choice}')
                                time.sleep(1)
                    else:
                        for choice in choices:
                            self.DITestSignal.emit(i, choice)
                            self.DI.test_channel(i,choice)
                            if i != chansCount+1:
                                logging.info(f'DI testing channel {i}, testValue {choice}')
                                time.sleep(1)
                else:
                    self.InterruptSignal.emit()
                    logging.info('Interrupt DI Test!')
                    return
            logging.info('DI Test end')
            time.sleep(1)
        else:
            self.InterruptSignal.emit()
            logging.info('Interrupt DI Test!')
            return

    def do_DO_Test(self):
        choices = [0, 1]
        chanCount = 20
        if self.flag:
            logging.info('Change to DOTest')
            self.ChangeSignal.emit('DOTest')
            time.sleep(1)
            logging.info('DO Test start')
            for i in range(chanCount + 1):
                if self.flag:
                    for choice in choices:
                        self.DOTestSignal.emit(i, choice)

                        if i != chanCount:
                            logging.info(f'DO testing channel {i}, testValue {choice}')
                            time.sleep(1)
                else:
                    self.InterruptSignal.emit()
                    logging.info('Interrupt DO Test!')
                    return
            logging.info('DO Test end')
            time.sleep(1)
        else:
            self.InterruptSignal.emit()
            logging.info('Interrupt DO Test!')
            return

    def do_AI_Test(self):
        chansCount = 16
        if self.flag:
            logging.info('Change to AITest')
            self.ChangeSignal.emit('AITest')
            time.sleep(1)
            logging.info('AI Test start')
            for i in range(chansCount + 1):
                choices = JDK23.AITest.CHES['{:02X}'.format(i)]['tpvf']
                for choice in choices:
                    if self.flag:
                        self.AITestSignal.emit(i, choice) # 1 # UI
                        recv_data = self.AI.test_channel(i, choice)# 3 device # 4
                        print(recv_data)
                        self.RecvDataSignal.emit(recv_data) # 5
                        if i != chansCount+1:
                            logging.info(f'AI testing channel {i}, testValue {choice}')
                            time.sleep(1)

                    else:
                        self.InterruptSignal.emit()
                        logging.info('Interrupt AI Test!')
                        return
            logging.info('AI Test end')
            time.sleep(1)
        else:
            self.InterruptSignal.emit()
            logging.info('Interrupt AI Test!')
            return

    def do_AO_Test(self):
        chansCount = 7

        if self.flag:
            logging.info('Change to AOTest')
            self.ChangeSignal.emit('AOTest')
            time.sleep(1)
            logging.info('AO Test start')
            for i in range(chansCount + 1):
                if i == 7:
                    self.AOTestSignal.emit(7, 0)  # 退出
                    continue
                choices = JDK23.AOTest.CHES['{:02X}'.format(i)]['tpvf']
                for choice in choices:
                    if self.flag:
                        self.AOTestSignal.emit(i, choice)
                        recv_data = AO().test_channel(i, choice)# 3 device # 4
                        print(recv_data)
                        self.RecvDataSignal.emit(recv_data) # 5
                        if i != chansCount:
                            logging.info(f'AO testing channel {i}, testValue {choice}')
                            time.sleep(1)
                    else:
                        self.InterruptSignal.emit()
                        logging.info('Interrupt AO Test!')
                        return
            logging.info('AO Test end')
            time.sleep(1)
        else:
            self.InterruptSignal.emit()
            logging.info('Interrupt AO Test!')
            return

    def run(self) -> None:
        self.do_DI_Test()
        # self.do_DO_Test()
        self.do_AI_Test()
        # self.do_AO_Test()


if __name__ == '__main__':
    a = AutoTestQThread()
    a.daemon = True
    a.run()
