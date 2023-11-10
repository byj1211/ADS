import time

import serial
import serial.tools.list_ports


class Serial_io_tool:
    def __init__(self, port: str, baudrate=9600, bytesize=7, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_TWO,
                 timeout=None):  # timeout以s为单位，时间一到立马返回数据，不管是否读完
        """
        初始化串口连接
        :param port: 串口名
        :param baudrate: 波特率默认为 9600
        :param bytesize: 数据位默认为 7 位
        :param parity: 默认为奇校验
        :param stopbits: 停止位 2 位
        :param timeout: 超时默认为 无
        """
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        self.ser = None

    @staticmethod
    def get_port_list() -> list:
        """
        初始化 Serial_io_tool 实例时必须指定一个端口。使用这个静态方法会返回目前可用的串口设备信息，里面包含了该设备的端口和其它信息。
        :return: 返回一个可使用的端口列表，否则返回 None
        """
        # 扫描所有可用串口设备
        try:
            port_list = serial.tools.list_ports.comports()
            if bool(port_list):
                print("可用的串口设备如下：")
                for port in port_list:
                    print(port)  # COM4 - USB-SERIAL CH340 (COM4)\
                return port_list
            else:
                print("没有发现可用的串口设备")
                return None
        except Exception as e:
            print("Error: ", str(e))
            return None

    def open_port(self):
        """
        根据初始化 Serial_io_tool 时的参数打开目标端口
        :return: 成功打开返回True，否则返回 False
        """
        try:
            self.ser = serial.Serial(self.port, self.baudrate, self.bytesize, self.parity, self.stopbits,
                                     timeout=self.timeout)
            if self.ser.isOpen():
                print("Serial port {} is open".format(self.port))
            else:
                print("Serial port {} is not open".format(self.port))
        except Exception as e:
            print("Error: ", str(e))
            return False
        return True

    def is_open(self):
        return self.ser.isOpen()

    def close_port(self):
        """
        如果当前端口已经打开，则关闭端口
        """
        if self.ser is not None:
            self.ser.close()
            print("Serial port {} is closed".format(self.port))

    def write_data(self, data: str) -> str:
        """
        写入字符串数据到设备
        :param data: 要写入的字符串
        :return: 成功写入的话返回写入的字节长度，否则返回 None
        """
        if self.ser is not None:
            try:
                # 检查data类型是不是字符串
                if not isinstance(data, str):
                    data = str(data)
                """
                1. write() 方法只能发送 bytes 类型的数据，所以需要对字符串进行 encode 编码
                2. write() 方法执行完成后，会将发送的字节数作为返回值
                3. Serial() 方法可以指定写入超时时间参数：write_timeout，效果与timeout类似
                """
                str_len = self.ser.write(data.encode('UTF-8'))  # str.encode()是 Python 中字符串类型的一个方法，用于将字符串编码为字节序列。
                # print(str_len)
                return str_len
            except Exception as e:
                print("Error: ", str(e))

    def read_data(self, size: int) -> str:
        """
        读取 size 大小的字节数据
        :param size: 指定要读取的字节个数
        :return: 读取到的内容，str类型，已经提前被解码，不需要再处理
        """
        if self.ser is not None:
            try:
                """
                1. read() 方法默认一次读取一个字节，可以通过传入参数指定每次读取的字节数
                2. read() 方法会将读取的内容作为返回值，类型为 bytes
                """
                info = self.ser.read(size).decode('UTF-8')
                # print("info:" + info)
                return info
            except Exception as e:
                print("Error: ", str(e))

    def flush_input(self):
        """
        清空串口输入缓冲区
        """
        if self.ser is not None:
            self.ser.flushInput()

    def flush_output(self):
        """
        清空串口输出缓冲区
        """
        if self.ser is not None:
            self.ser.flushOutput()

    def query_data(self, data, read_size=1024) -> str:
        """
        发送指令并接收返回值
        :param data: 要发送的指令
        :param read_size: 要读取的字节大小，默认为1024
        :return: 读取到的返回值，字符串类型
        """
        self.flush_input()
        self.flush_output()
        self.write_data(data)
        time.sleep(0.1)
        response = self.read_data(read_size)
        return response
