from PyQt5.QtCore import QObject, pyqtSignal

class MyObject(QObject):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # 将信号与lambda表达式绑定
        self.my_signal.connect(lambda msg: self.handler(msg))

    def handler(self, msg):
        line = input("Received signal. Enter input: "+msg)
        print("You entered:", line)

# 创建对象
obj = MyObject()

# 发射信号
obj.my_signal.emit("Hello")

# 无限循环，等待信号触发
while True:
    pass
