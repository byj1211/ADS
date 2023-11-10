"""
Created on 2020/11/27
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: QuitThread
@description:
"""

import sys
import time
from PyQt5.QtCore import pyqtSignal, QThread, QCoreApplication, QTimer


class T1(QThread):
    signal = pyqtSignal(str, int)

    def run(self):
        print('thread id', QThread.currentThread().objectName())
        for i in range(0, 20):
            if not self.isInterruptionRequested():
                self.signal.emit('0', i)
                print(f'emit 0 {i} ')

                time.sleep(2)
        print('thread quit')


class T2(QThread):

    def __init__(self, a, b):
        super(T2, self).__init__()
        self.a = a
        self.b = b
        print('init T2')

    def run(self):
        print(self.a, self.b)


def func1(a, b):
    t2 = T2(a, b)
    t2.start()


if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    t1 = T1()
    t1.signal.connect(func1)
    t1.run()
    # 3秒后退出

    # QTimer.singleShot(3000, t1.requestInterruption)
    sys.exit(app.exec_())
