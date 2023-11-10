import logging

import serial


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