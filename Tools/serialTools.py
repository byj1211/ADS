import serial


# 把字符串类型转换为bytes数据流进行发送，RS232命令发送函数+
def serial_sent_utf(command):
    # 从字典里获取对应的RS232命令
    var = command
    # encode()函数是编码，把字符串数据转换成bytes数据流
    ser.write(var.encode())
    data = ser.read(1024)
    # 获取指令的返回值，并且进行类型转换，转换为字符串后便可以进行字符串对比，因而便可以根据返回值进行判断是否执行特定功能
    data = str(data, encoding="utf-8")
    return data


if __name__ == '__main__':
    # 实现串口的连接
    ser = serial.Serial('COM10', 9600, writeTimeout=0, timeout=0.1)
    ser.write_termination = '\n'
    ser.read_termination = '\n'
    send_message = '*IDN?\n'.encode('utf-8')
    ser.write(send_message)
    send_message='SYSTem:BEEPer'.encode('utf-8')
    ser.write(send_message)
    recv_message = ser.read(1024).decode('utf-8')
    print(recv_message)
    # command2_utf8 = serial_sent_utf('command2_utf8')
