import logging

import serial

class delay_data:
    '''
    类是实现进行某个测试项对应操作的继电器通道，有疑问看电路原理图
    '''
    DI_0 = [36,42,43,37,47,45]
    DI_1 = [39,40,35,37,33,46,48]
    DI_2 = [19,18,20,22,21,17]
    DI_3 = [26,23,24]
    DI_4 = [25]
    #注意：启动监视器1、2的继电器编号是错的，硬件上没有通道5的  Flash写能

    DI_5 = []
    DI = {}
    DI["0"] = DI_0
    DI["1"] = DI_1
    DI["2"] = DI_2
    DI["3"] = DI_3
    DI["4"] = DI_4
    DI["5"] = DI_5
#chan表示通道，delay_num是继电器的卡号
#结构为 chan:delay_num
    AI={"0":15,"1":16,"2":14,"3":9,"4":10,"5":13,"6":11,"7":12,"15":41,"16":42}
class delay:
    # signal_read=pyqtSignal(str)
    def __init__(self):
        self.serial = None
        self.name="delay"
        self.port="COM3"
        self.baudrate=115200
        # self.resource=None
    def connect(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate)
            logging.info("{} is connecting...".format(self.name))
            self.send_command_mode_all_off()
            return True
        except Exception as e:
            logging.info("{} is disconnect...".format(self.name))
            logging.error(e)
            return False
    def send_command_mode_all_off(self):
        try:
            if not self.serial:
                self.connect()
            command=b"0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\r\n"
            self.serial.write(command)
            response = self.serial.readline()
            print(response)
            return response
        except Exception as e:
            logging.info("{} can't write to...".format(self.name))
            logging.error(e)

    def send_command_mode_all_on(self):
        try:
            if not self.serial:
                self.connect()
            command = b"0,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f\r\n"
            self.serial.write(command)
            response = self.serial.readline()
            print(response)
            return response
        except Exception as e:
            logging.info("{} can't write to...".format(self.name))
            logging.error(e)


    #num是继电器序号，state是继电器通断状态，用1表示连接，0表示断开
    def send_command_singel(self,num,state):
        try:
            if not self.serial:
                self.connect()
            data = "1,{},{}\r\n".format(str(num), str(state))
            command = data.encode('utf-8')
            self.serial.write(command)
            response = self.serial.readline()
            print(response)
            return response
        except Exception as e:
            logging.info("{} can't write to...".format(self.name))
            logging.error(e)

    #设置一排继电器的开关状态
    def send_command_pai(self,pai_num,state):
        try:
            if not self.serial:
                self.connect()
            data = "2,{},{}\r\n".format(str(pai_num), str(state))
            command = data.encode('utf-8')
            self.serial.write(command)
            response = self.serial.readline()
            print(response)
            return response
        except Exception as e:
            logging.info("{} can't write to...".format(self.name))
            logging.error(e)

    def close(self):
        try:
            if self.serial:
                self.serial.close()
                logging.info("{} is closed...".format(self.name))
        except Exception as e:
            logging.info("{} is disconnect...".format(self.name))
            logging.error(e)
    def __del__(self):
        self.close()