import logging
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

#，用于处理字符串和进行校验和计算。
class SendString:
    def __init__(self, string):
        self.string = string
        self.slice_string = self.string.split(' ')
        self.length = len(self.slice_string)
        self.cal_length()
        self.cal_checksum()

    def __repr__(self):
        return self.string
#校验和处理
    def cal_checksum(self):
        sum = 0
        for i in self.slice_string[:self.length - 1]:
            sum = sum + int(i, 16)
        res = 0xff & sum
        checksum = 256 - res
        str_checksum = '{:02X}'.format(checksum)
        self.slice_string[-1] = str_checksum
        return_data = " ".join(self.slice_string)
        self.string = return_data

    def cal_length(self):
        str_length = '{:02X}'.format(self.length)
        self.slice_string[2] = str_length
        return_data = " ".join(self.slice_string)
        self.string = return_data

    def set_TestData(self, val, ratio, low=5, high=6, rd=4):
        res = int(val * ratio)
        res = 0xFFFF & res
        low_data = '{:02X}'.format(res % 256)
        high_data = '{:02X}'.format(res // 256)
        self.slice_string[low] = low_data
        self.slice_string[high] = high_data
        self.string = ' '.join(self.slice_string)
        self.cal_length()
        self.cal_checksum()
        return self

    def cal_TestData(self, ratio, low=5, high=6, rd=4):
        low_data = int(self.slice_string[low], 16)
        high_data = int(self.slice_string[high], 16)
        testData = (high_data * 256 + low_data)
        if testData > 32765:
            testData = -(0xFFFF - testData + 1)
        testData = testData / ratio
        testData = round(testData, rd)
        return testData


class RecvString:
    def __init__(self, string):
        self.string = string
        self.slice_string = self.string.split(' ')
        self.length = len(self.slice_string)
        # self.cal_length()
        # self.cal_checksum()

    def __repr__(self):
        return self.string

    def cal_checksum(self):
        sum = 0
        for i in self.slice_string[:self.length - 1]:
            sum = sum + int(i, 16)
        res = 0xff & sum
        checksum = 256 - res
        str_checksum = '{:02X}'.format(checksum)
        self.slice_string[-1] = str_checksum
        return_data = " ".join(self.slice_string)
        self.string = return_data

    def cal_length(self):
        str_length = '{:02X}'.format(self.length)
        self.slice_string[2] = str_length
        return_data = " ".join(self.slice_string)
        self.string = return_data

    def cal_TestData(self, ratio, low=5, high=6, rd=4):
        low_data = int(self.slice_string[low], 16)
        high_data = int(self.slice_string[high], 16)
        testData = (high_data * 256 + low_data) / ratio
        testData = round(testData, rd)
        return testData


class JDK23:
    #   0   1   2   3   4   5   6   7
    # 0：    包头
    # 1：    包头
    # 2：    长度
    # 3：    指令号
    # 4：    备用
    # 5：    备用
    # 6：    备用
    # 7：    校验和
    class HandShake:  # 0x00
        STRING = SendString("AA 55 08 00 00 00 00 xx")  # AA 55 08 00 00 00 00 F9

    class CPUTest:  # 0x01
        STRING = SendString("AA 55 08 01 00 00 00 xx")  # AA 55 08 01 00 00 00 F8

    class PSUTest:  # 0x02
        STRING = SendString("AA 55 08 02 00 00 00 xx")  # AA 55 08 02 00 00 00 F7

    class CMTest:  # 0x03
        STRING = SendString("AA 55 08 03 00 00 00 xx")  # AA 55 08 03 00 00 00 F6

    class IOSTest:  # 0x04
        STRING = SendString("AA 55 08 04 00 00 00 xx")  # AA 55 08 04 00 00 00 F5

    class DITest:  # 0x05
        #   0   1   2   3   4   5   6   7
        # 0：    包头
        # 1：    包头
        # 2：    长度
        # 3：    指令号
        # 4：    通道号
        # 5：    输入值
        # 6：    备用
        # 7：    校验和
        Chanel_nums = 5

        CH0_00 = SendString("AA 55 08 05 00 00 00 XX")
        CH0_01 = SendString("AA 55 08 05 00 01 00 XX")
        CH1_00 = SendString("AA 55 08 05 01 00 00 XX")
        CH1_01 = SendString("AA 55 08 05 01 01 00 XX")
        CH2_00 = SendString("AA 55 08 05 02 00 00 XX")
        CH2_01 = SendString("AA 55 08 05 02 01 00 XX")
        CH3_00 = SendString("AA 55 08 05 03 00 00 XX")
        CH3_01 = SendString("AA 55 08 05 03 01 00 XX")
        CH4_00 = SendString("AA 55 08 05 04 00 00 XX")
        CH4_01 = SendString("AA 55 08 05 04 01 00 XX")
        CH5_00 = SendString("AA 55 08 05 05 00 00 XX")
        CH5_01 = SendString("AA 55 08 05 05 01 00 XX")

        CHES = dict()
        CHES['0'] = {"0": CH0_00, "1": CH0_01}
        CHES['1'] = {"0": CH1_00, "1": CH1_01}
        CHES['2'] = {"0": CH2_00, "1": CH2_01}
        CHES['3'] = {"0": CH3_00, "1": CH3_01}
        CHES['4'] = {"0": CH4_00, "1": CH4_01}
        CHES['5'] = {"0": CH5_00, "1": CH5_01}
        # CHES['0']['0']=CH0_00

    class DOTest:  # 0x06
        #   0   1   2   3   4   5   6   7
        # 0：    包头
        # 1：    包头
        # 2：    长度
        # 3：    指令号
        # 4：    通道号
        # 5：    输出值
        # 6：    备用
        # 7：    校验和
        CH00_00, CH00_01 = SendString("AA 55 08 06 00 00 00 XX"), SendString("AA 55 08 06 00 01 00 XX")
        CH01_00, CH01_01 = SendString("AA 55 08 06 01 00 00 XX"), SendString("AA 55 08 06 01 01 00 XX")
        CH02_00, CH02_01 = SendString("AA 55 08 06 02 00 00 XX"), SendString("AA 55 08 06 02 01 00 XX")
        CH03_00, CH03_01 = SendString("AA 55 08 06 03 00 00 XX"), SendString("AA 55 08 06 03 01 00 XX")
        CH04_00, CH04_01 = SendString("AA 55 08 06 04 00 00 XX"), SendString("AA 55 08 06 04 01 00 XX")
        CH05_00, CH05_01 = SendString("AA 55 08 06 05 00 00 XX"), SendString("AA 55 08 06 05 01 00 XX")
        CH06_00, CH06_01 = SendString("AA 55 08 06 06 00 00 XX"), SendString("AA 55 08 06 06 01 00 XX")
        CH07_00, CH07_01 = SendString("AA 55 08 06 07 00 00 XX"), SendString("AA 55 08 06 07 01 00 XX")
        CH08_00, CH08_01 = SendString("AA 55 08 06 08 00 00 XX"), SendString("AA 55 08 06 08 01 00 XX")
        CH09_00, CH09_01 = SendString("AA 55 08 06 09 00 00 XX"), SendString("AA 55 08 06 09 01 00 XX")
        CH0A_00, CH0A_01 = SendString("AA 55 08 06 0A 00 00 XX"), SendString("AA 55 08 06 0A 01 00 XX")
        CH0B_00, CH0B_01 = SendString("AA 55 08 06 0B 00 00 XX"), SendString("AA 55 08 06 0B 01 00 XX")
        CH0C_00, CH0C_01 = SendString("AA 55 08 06 0C 00 00 XX"), SendString("AA 55 08 06 0C 01 00 XX")
        CH0D_00, CH0D_01 = SendString("AA 55 08 06 0D 00 00 XX"), SendString("AA 55 08 06 0D 01 00 XX")
        CH0E_00, CH0E_01 = SendString("AA 55 08 06 0E 00 00 XX"), SendString("AA 55 08 06 0E 01 00 XX")
        CH0F_00, CH0F_01 = SendString("AA 55 08 06 0F 00 00 XX"), SendString("AA 55 08 06 0F 01 00 XX")
        CH10_00, CH10_01 = SendString("AA 55 08 06 10 00 00 XX"), SendString("AA 55 08 06 10 01 00 XX")
        CH11_00, CH11_01 = SendString("AA 55 08 06 11 00 00 XX"), SendString("AA 55 08 06 11 01 00 XX")
        CH12_00, CH12_01 = SendString("AA 55 08 06 12 00 00 XX"), SendString("AA 55 08 06 12 01 00 XX")
        CH13_00, CH13_01 = SendString("AA 55 08 06 13 00 00 XX"), SendString("AA 55 08 06 13 01 00 XX")
        CH14_00, CH14_01 = SendString("AA 55 08 06 14 00 00 XX"), SendString("AA 55 08 06 14 01 00 XX")

        # 字典
        CHES = dict()
        CHES['00'] = {"0": CH00_00, "1": CH00_01}
        CHES['01'] = {"0": CH01_00, "1": CH01_01}
        CHES['02'] = {"0": CH02_00, "1": CH02_01}
        CHES['03'] = {"0": CH03_00, "1": CH03_01}
        CHES['04'] = {"0": CH04_00, "1": CH04_01}
        CHES['05'] = {"0": CH05_00, "1": CH05_01}
        CHES['06'] = {"0": CH06_00, "1": CH06_01}
        CHES['07'] = {"0": CH07_00, "1": CH07_01}
        CHES['08'] = {"0": CH08_00, "1": CH08_01}
        CHES['09'] = {"0": CH09_00, "1": CH09_01}
        CHES['0A'] = {"0": CH0A_00, "1": CH0A_01}
        CHES['0B'] = {"0": CH0B_00, "1": CH0B_01}
        CHES['0C'] = {"0": CH0C_00, "1": CH0C_01}
        CHES['0D'] = {"0": CH0D_00, "1": CH0D_01}
        CHES['0E'] = {"0": CH0E_00, "1": CH0E_01}
        CHES['0F'] = {"0": CH0F_00, "1": CH0F_01}
        CHES['10'] = {"0": CH10_00, "1": CH10_01}
        CHES['11'] = {"0": CH11_00, "1": CH11_01}
        CHES['12'] = {"0": CH12_00, "1": CH12_01}
        CHES['13'] = {"0": CH13_00, "1": CH13_01}
        CHES['14'] = {"0": CH14_00, "1": CH14_01}

    class AITest:  # 0x07
        # 0:包头
        # 1:包头
        # 2:长度
        # 3:指令号
        # 4:通道号
        # 5:测试值1
        # 6:测试值2
        # 7:备用
        # 8:校验和
        CH00 = {  # ECS指令测试输入
            'chanN': 0x00, 'err': 0.100, 'ratio_1': 1000, 'unit': 'V',
            'tpvs': ['0.5', '2.0', '3.5', '4.5'],  # Ztest point value string style 测试点 字符串格式
            'tpvf': [0.5, 2.0, 3.5, 4.5],  # Ztest point value float style 测试点 浮点格式
            'tps': []  # Ztest point sendstring # 测试点 发送字符串格式
        }  # ECS指令测试输入
        for i in range(4):
            CH00['tps'].append(SendString("AA 55 09 07 00 00 00 00 XX").set_TestData(CH00['tpvf'][i], CH00['ratio_1']))
        # CH00['0.5'] = SendString("AA 55 09 07 00 00 00 00 XX").set_TestData(0.5, CH00['ratio_1'])
        # CH00['2.0'] = SendString("AA 55 09 07 00 00 00 00 XX").set_TestData(2.0, CH00['ratio_1'])
        # CH00['3.5'] = SendString("AA 55 09 07 00 00 00 00 XX").set_TestData(3.5, CH00['ratio_1'])
        # CH00['4.5'] = SendString("AA 55 09 07 00 00 00 00 XX").set_TestData(4.5, CH00['ratio_1'])

        CH01 = {  # 转速变化测试
            'chanN': 0x01, 'err': 0.1, 'ratio_1': 1000, 'unit': 'V',
            'tpvs': ['0.5', '2.0', '3.5', '4.5'],  # Ztest point value string style 测试点 字符串格式
            'tpvf': [0.5, 2.0, 3.5, 4.5],  # Ztest point value float style 测试点 浮点格式
            'tps': []  # Ztest point sendstring # 测试点 发送字符串格式
        }  # 转速变化测试
        for i in range(4):
            CH01['tps'].append(SendString("AA 55 09 07 01 00 00 00 XX").set_TestData(CH01['tpvf'][i], CH01['ratio_1']))
        # CH01['0.5'] = SendString("AA 55 09 07 01 00 00 00 XX").set_TestData(0.5, CH01['ratio_1'])
        # CH01['2.0'] = SendString("AA 55 09 07 01 00 00 00 XX").set_TestData(2.0, CH01['ratio_1'])
        # CH01['3.5'] = SendString("AA 55 09 07 01 00 00 00 XX").set_TestData(3.5, CH01['ratio_1'])
        # CH01['4.5'] = SendString("AA 55 09 07 01 00 00 00 XX").set_TestData(4.5, CH01['ratio_1'])

        CH02 = {  # 起动电压监视
            'chanN': 0x02, 'err': 0.333, 'ratio_1': 1000, 'unit': 'V',
            'tpvs': ['20', '24', '26', '28'],
            'tpvf': [20, 24, 26, 28],
            'tps': []
        }  # 起动电压监视
        for i in range(4):
            CH02['tps'].append(SendString("AA 55 09 07 02 00 00 00 XX").set_TestData(CH02['tpvf'][i], CH02['ratio_1']))
        # CH02['20'] = SendString("AA 55 09 07 02 00 00 00 XX").set_TestData(20, CH02['ratio_1'])
        # CH02['24'] = SendString("AA 55 09 07 02 00 00 00 XX").set_TestData(24, CH02['ratio_1'])
        # CH02['26'] = SendString("AA 55 09 07 02 00 00 00 XX").set_TestData(26, CH02['ratio_1'])
        # CH02['28'] = SendString("AA 55 09 07 02 00 00 00 XX").set_TestData(28, CH02['ratio_1'])

        CH03 = {  # 排气温度1
            'chanN': 0x03, 'err': 0.66, 'ratio_1': 100, 'unit': 'mV',
            'tpvs': ['-2.6', '20', '40', '52.4'],
            'tpvf': [-2.6, 20, 40, 52.4],
            'tps': []
        }  # 排气温度1
        for i in range(4):
            CH03['tps'].append(SendString("AA 55 09 07 03 00 00 00 XX").set_TestData(CH03['tpvf'][i], CH03['ratio_1']))
        # CH03['-2.6'] = SendString("AA 55 09 07 03 00 00 00 XX").set_TestData(-2.6, CH03['ratio_1'])
        # CH03['20'] = SendString("AA 55 09 07 03 00 00 00 XX").set_TestData(20, CH03['ratio_1'])
        # CH03['40'] = SendString("AA 55 09 07 03 00 00 00 XX").set_TestData(40, CH03['ratio_1'])
        # CH03['52.4'] = SendString("AA 55 09 07 03 00 00 00 XX").set_TestData(52.4, CH03['ratio_1'])

        CH04 = {  # 排气温度2
            'chanN': 0x04, 'err': 0.66, 'ratio_1': 100, 'unit': 'mV',
            'tpvs': ['-2.6', '20', '40', '52.4'],
            'tpvf': [-2.6, 20, 40, 52.4],
            'tps': [],
        }  # 排气温度2
        for i in range(4):
            CH04['tps'].append(SendString("AA 55 09 07 04 00 00 00 XX").set_TestData(CH04['tpvf'][i], CH04['ratio_1']))
        # CH04['-2.6'] = SendString("AA 55 09 07 04 00 00 00 XX").set_TestData(-2.6, CH04['ratio_1'])
        # CH04['20'] = SendString("AA 55 09 07 04 00 00 00 XX").set_TestData(20, CH04['ratio_1'])
        # CH04['40'] = SendString("AA 55 09 07 04 00 00 00 XX").set_TestData(40, CH04['ratio_1'])
        # CH04['52.4'] = SendString("AA 55 09 07 04 00 00 00 XX").set_TestData(52.4, CH04['ratio_1'])

        CH05 = {  # 环境压力传感器
            'chanN': 0x05, 'err': 0.29, 'ratio_1': 100, 'unit': 'mV',
            'tpvs': ['0', '10', '25', '40'],
            'tpvf': [0, 10, 25, 40],
            'tps': []
        }  # 环境压力传感器
        for i in range(4):
            CH05['tps'].append(SendString("AA 55 09 07 05 00 00 00 XX").set_TestData(CH05['tpvf'][i], CH05['ratio_1']))
        # CH05['0'] = SendString("AA 55 09 07 05 00 00 00 XX").set_TestData(0, CH05['ratio_1'])
        # CH05['10'] = SendString("AA 55 09 07 05 00 00 00 XX").set_TestData(10, CH05['ratio_1'])
        # CH05['25'] = SendString("AA 55 09 07 05 00 00 00 XX").set_TestData(25, CH05['ratio_1'])
        # CH05['40'] = SendString("AA 55 09 07 05 00 00 00 XX").set_TestData(40, CH05['ratio_1'])

        CH06 = {  # 总压传感器
            'chanN': 0x06, 'err': 0.34, 'ratio_1': 100, 'unit': 'mV',
            'tpvs': ['0', '10', '25', '40'],
            'tpvf': [0, 10, 25, 40],
            'tps': []
        }  # 总压传感器
        # @todo 测试值为10时，校验和为100? 字符串为 AA 55 09 07 06 E8 03 00 100
        for i in range(4):
            CH06['tps'].append(SendString("AA 55 09 07 06 00 00 00 XX").set_TestData(CH06['tpvf'][i], CH06['ratio_1']))
        # CH06['0'] = SendString("AA 55 09 07 06 00 00 00 XX").set_TestData(0, CH06['ratio_1'])
        # CH06['10'] = SendString("AA 55 09 07 06 00 00 00 XX").set_TestData(10, CH06['ratio_1'])
        # CH06['25'] = SendString("AA 55 09 07 06 00 00 00 XX").set_TestData(25, CH06['ratio_1'])
        # CH06['40'] = SendString("AA 55 09 07 06 00 00 00 XX").set_TestData(40, CH06['ratio_1'])

        CH07 = {  # 压差传感器
            'chanN': 0x07, 'err': 0.33, 'ratio_1': 100, 'unit': 'mV',
            'tpvs': ['0', '10', '25', '40'],
            'tpvf': [0, 10, 25, 40],
            'tps': []
        }  # 压差传感器
        for i in range(4):
            CH07['tps'].append(SendString("AA 55 09 07 07 00 00 00 XX").set_TestData(CH07['tpvf'][i], CH07['ratio_1']))
        # CH07['0'] = SendString("AA 55 09 07 07 00 00 00 XX").set_TestData(0, CH07['ratio_1'])
        # CH07['10'] = SendString("AA 55 09 07 07 00 00 00 XX").set_TestData(10, CH07['ratio_1'])
        # CH07['25'] = SendString("AA 55 09 07 07 00 00 00 XX").set_TestData(25, CH07['ratio_1'])
        # CH07['40'] = SendString("AA 55 09 07 07 00 00 00 XX").set_TestData(40, CH07['ratio_1'])

        CH08 = {  # 滑油温度
            'chanN': 0x08, 'err': 1.59, 'ratio_1': 1, 'unit': 'Ω',
            'tpvs': ['68', '110', '160', '208'],
            'tpvf': [68, 110, 160, 208],
            'tps': []
        }  # 滑油温度
        for i in range(4):
            CH08['tps'].append(SendString("AA 55 09 07 08 00 00 00 XX").set_TestData(CH08['tpvf'][i], CH08['ratio_1']))
        # CH08['68'] = SendString("AA 55 09 07 08 00 00 00 XX").set_TestData(68, CH08['ratio_1'])
        # CH08['110'] = SendString("AA 55 09 07 08 00 00 00 XX").set_TestData(110, CH08['ratio_1'])
        # CH08['160'] = SendString("AA 55 09 07 08 00 00 00 XX").set_TestData(160, CH08['ratio_1'])
        # CH08['208'] = SendString("AA 55 09 07 08 00 00 00 XX").set_TestData(208, CH08['ratio_1'])

        CH09 = {  # APU进口温度
            'chanN': 0x09, 'err': 1.59, 'ratio_1': 1, 'unit': 'Ω',
            'tpvs': ['68', '110', '160', '208'],
            'tpvf': [68, 110, 160, 208],
            'tps': []
        }  # APU进口温度
        for i in range(4):
            CH09['tps'].append(SendString("AA 55 09 07 09 00 00 00 XX").set_TestData(CH09['tpvf'][i], CH09['ratio_1']))
        # CH09['68'] = SendString("AA 55 09 07 09 00 00 00 XX").set_TestData(68, CH09['ratio_1'])
        # CH09['110'] = SendString("AA 55 09 07 09 00 00 00 XX").set_TestData(110, CH09['ratio_1'])
        # CH09['160'] = SendString("AA 55 09 07 09 00 00 00 XX").set_TestData(160, CH09['ratio_1'])
        # CH09['208'] = SendString("AA 55 09 07 09 00 00 00 XX").set_TestData(208, CH09['ratio_1'])

        CH0A = {  # 燃油温度
            'chanN': 0x0A, 'err': 1.59, 'ratio_1': 1, 'unit': 'Ω',
            'tpvs': ['68', '110', '160', '208'],
            'tpvf': [68, 110, 160, 208],
            'tps': []
        }  # 燃油温度
        for i in range(4):
            CH0A['tps'].append(SendString("AA 55 09 07 0A 00 00 00 XX").set_TestData(CH0A['tpvf'][i], CH0A['ratio_1']))
        # CH0A['68'] = SendString("AA 55 09 07 0A 00 00 00 XX").set_TestData(68, CH0A['ratio_1'])
        # CH0A['110'] = SendString("AA 55 09 07 0A 00 00 00 XX").set_TestData(110, CH0A['ratio_1'])
        # CH0A['160'] = SendString("AA 55 09 07 0A 00 00 00 XX").set_TestData(160, CH0A['ratio_1'])
        # CH0A['208'] = SendString("AA 55 09 07 0A 00 00 00 XX").set_TestData(208, CH0A['ratio_1'])

        CH0B = {  # 冷端补偿温度
            'chanN': 0x0B, 'err': None, 'ratio_1': 1, 'unit': 'Ω', 'range': [1000, 1155],
            'tpvs': ['0'],
            'tpvf': [0],
            'tps': []
        }  # 冷端补偿温度
        CH0B['tps'].append(SendString("AA 55 09 07 0B 00 00 00 XX").set_TestData(0, 0))


#-----------------以下是byj新添用信号发生器代替LVDT板卡的代码---------------------------------------


        # @todo LVDT
        CH0C = {  # IGV LVDT
            'chanN': 0x0C, 'err': 0.045, 'ratio_1': 1000, 'unit': None,
            'tpvs': ['-0.3', '-0.1', '0.1', '0.3'],
            'tpvf': [-0.3, -0.1, 0.1, 0.3],
            'tps': []
        }  # IGV LVDT
        for i in range(4):
            CH0C['tps'].append(SendString("AA 55 09 07 0C 00 00 00 XX").set_TestData(CH0C['tpvf'][i], CH0C['ratio_1']))

        CH0D = {  # SCV LVDT
            'chanN': 0x0D, 'err': 0.045, 'ratio_1': 1000, 'unit': None,
            'tpvs': ['-0.516'],
            'tpvf': [-0.516],
            'tps': []
        }  # SCV LVDT
        for i in range(1):
            CH0D['tps'].append(SendString("AA 55 09 07 0D 00 00 00 XX").set_TestData(CH0D['tpvf'][i], CH0D['ratio_1']))

        CH0E = {  # FCU 旋转变压器
            'chanN': 0x0E, 'err': 3.6, 'ratio_1': 10, 'unit': '°',
            'tpvs': ['20', '40', '60', '80'],
            'tpvf': [20, 40, 60, 80],
            'tps': []
        }  # FCU 旋转变压器
        for i in range(4):
            CH0E['tps'].append(SendString("AA 55 09 07 0E 00 00 00 XX").set_TestData(CH0E['tpvf'][i], CH0E['ratio_1']))


#-----------------------以下是吴润瑾学长用LVDT板卡部分的代码------------------------------------
        # # @todo LVDT
        # CH0C = {  # IGV LVDT
        #     'chanN': 0x0C, 'err': 0.045, 'ratio_1': 1000, 'unit': None,
        #     'tpvs': ['-0.3', '-0.1', '0.1', '0.3'],
        #     'tpvf': [-0.3, -0.1, 0.1, 0.3],
        #     'tps': []
        # }  # IGV LVDT
        # for i in range(4):
        #     CH0C['tps'].append(SendString("AA 55 09 07 0C 00 00 00 XX").set_TestData(CH0C['tpvf'][i], CH0C['ratio_1']))
        #
        # CH0D = {  # SCV LVDT
        #     'chanN': 0x0D, 'err': 0.045, 'ratio_1': 1000, 'unit': None,
        #     'tpvs': ['-0.516'],
        #     'tpvf': [-0.516],
        #     'tps': []
        # }  # SCV LVDT
        # for i in range(1):
        #     CH0D['tps'].append(SendString("AA 55 09 07 0D 00 00 00 XX").set_TestData(CH0D['tpvf'][i], CH0D['ratio_1']))
        #
        # CH0E = {  # FCU 旋转变压器
        #     'chanN': 0x0E, 'err': 3.6, 'ratio_1': 10, 'unit': '°',
        #     'tpvs': ['20', '40', '60', '80'],
        #     'tpvf': [20, 40, 60, 80],
        #     'tps': []
        # }  # FCU 旋转变压器
        # for i in range(4):
        #     CH0E['tps'].append(SendString("AA 55 09 07 0E 00 00 00 XX").set_TestData(CH0E['tpvf'][i], CH0E['ratio_1']))

        CH0F = {  # 转速1
            'chanN': 0x0F, 'err': 36, 'ratio_1': 1, 'unit': 'Hz',
            "v_pp": [0.5, 1, 3, 5],
            'tpvs': ['300', '3000', '8000', '14640'],
            'tpvf': [300, 3000, 8000, 14640],
            'tps': []
        }  # 转速1
        for i in range(4):
            CH0F['tps'].append(SendString("AA 55 09 07 0F 00 00 00 XX").set_TestData(CH0F['tpvf'][i], CH0F['ratio_1']))

        CH10 = {  # 转速2
            'chanN': 0x10, 'err': 36, 'ratio_1': 1, 'unit': 'Hz',
            "v_pp": [0.5, 1, 3, 5],
            'tpvs': ['300', '3000', '8000', '14640'],
            'tpvf': [300, 3000, 8000, 14640],
            'tps': []
        }  # 转速2
        for i in range(4):
            CH10['tps'].append(SendString("AA 55 09 07 10 00 00 00 XX").set_TestData(CH10['tpvf'][i], CH10['ratio_1']))

        # 合并
        CHES = dict()
        CHES['00'], CHES['01'], CHES['02'], CHES['03'], CHES['04'], CHES['05'] = CH00, CH01, CH02, CH03, CH04, CH05
        CHES['06'], CHES['07'], CHES['08'], CHES['09'], CHES['0A'], CHES['0B'] = CH06, CH07, CH08, CH09, CH0A, CH0B
        CHES['0C'], CHES['0D'], CHES['0E'], CHES['0F'], CHES['10'] = CH0C, CH0D, CH0E, CH0F, CH10

    class AOTest:  # 0x08
        CH00 = {  # AOUT_PREPS 传感器供电
            'chanN': 0x00, 'err': 0.2, 'ratio_1': 1, 'unit': 'V',
            'tpvs': ['10'],  # Ztest point value string style 测试点 字符串格式
            'tpvf': [10],  # Ztest point value float style 测试点 浮点格式
            'tps': []  # Ztest point sendstring # 测试点 发送字符串格式
        }  # AOUT_PREPS 传感器供电
        for i in range(len(CH00['tpvf'])):
            CH00['tps'].append(SendString("AA 55 09 08 00 00 00 00 XX").set_TestData(CH00["tpvf"][i], CH00['ratio_1']))

        CH01 = {  # AOUT_FLPPS 进气门供电
            'chanN': 0x01, 'err': 3, 'ratio_1': 1, 'unit': 'V',
            'tpvs': ['28'],  # Ztest point value string style 测试点 字符串格式
            'tpvf': [28],  # Ztest point value float style 测试点 浮点格式
            'tps': []  # Ztest point sendstring # 测试点 发送字符串格式
        }  # AOUT_FLPPS 进气门供电
        for i in range(len((CH01['tpvf']))):
            CH01['tps'].append(SendString("AA 55 09 08 01 00 00 00 XX").set_TestData(CH00["tpvf"][i], CH01['ratio_1']))

        CH02 = {  # LVDT_IGVPRI_STATE  IGV LVDT 初级激励
            'chanN': 0x02, 'err': 3, 'ratio_1': 1, 'unit': 'V',  # useless
            'tpvs': ['28'],  # useless
            'tpvf': [28],  # useless
            'tps': []  # useless
            # --------
            # 测试交流电 3.34+-0.3 KHz    3.1Vrms >2.4
            # --------
        }  # LVDT_IGVPRI_STATE  IGV LVDT 初级激励
        for i in range(1):
            CH02['tps'].append(SendString("AA 55 09 08 02 00 00 00 XX").set_TestData(0, CH02['ratio_1']))

        CH03 = {  # LVDT_SGVPRI_STATE   SCV LVDT 初级激励
            'chanN': 0x03, 'err': 3, 'ratio_1': 1, 'unit': 'V',  # useless
            'tpvs': ['28'],  # useless
            'tpvf': [28],  # useless
            'tps': []  # useless
            # --------
            # 测试交流电 3.34（±0.3） KHz    3.1 （>2.4）Vrms
            # --------
        }  # LVDT_SGVPRI_STATE   SCV LVDT 初级激励
        for i in range(1):
            CH03['tps'].append(SendString("AA 55 09 08 03 00 00 00 XX").set_TestData(0, CH03['ratio_1']))

        CH04 = {  # RVDT_FCUPRI_STATE    FCU旋变初级激励
            'chanN': 0x04, 'err': 3, 'ratio_1': 1, 'unit': 'V',  # useless
            'tpvs': ['28'],  # useless
            'tpvf': [28],  # useless
            'tps': []  # useless
            # --------
            # 测试交流电 3.6（±0.3） KHz    2.0 （±0.3）Vrms
            # --------
        }  # RVDT_FCUPRI_STATE    FCU旋变初级激励
        for i in range(1):
            CH04['tps'].append(SendString("AA 55 09 08 04 00 00 00 XX").set_TestData(0, CH04['ratio_1']))

        CH05 = {  # AOUT_IGVCD IGV电流驱动
            'chanN': 0x05, 'err': 2, 'ratio_1': 100, 'unit': 'mA',
            'tpvs': ['0.70', '1.00', '1.50', '2.10'],
            'tpvf': [-41.5,-18.87,64.15, 1, 1.5, 2.1],
            'tps': []
        }  # AOUT_IGVCD IGV电流驱动
        for i in range(4):
            CH05['tps'].append(SendString("AA 55 09 08 05 00 00 00 XX").set_TestData(CH05['tpvf'][i], CH05['ratio_1']))

        CH06 = {  # AOUT_FCUCD 燃油力矩马达电流驱动
            'chanN': 0x06, 'err': 6, 'ratio_1': 100, 'unit': 'mA',
            'tpvs': ['0', '0.5', '1.6', '2.5'],
            'tpvf': [0, 0.5, 1.6, 2.5],
            'tps': []
        }  # AOUT_FCUCD 燃油力矩马达电流驱动
        for i in range(4):
            CH06['tps'].append(SendString("AA 55 09 08 06 00 00 00 XX").set_TestData(CH06['tpvf'][i], CH06['ratio_1']))

        CH07 = {  # AOUT_SCVCD SCV电流驱动
            'chanN': 0x07, 'err': 2, 'ratio_1': 100, 'unit': 'mA',
            'tpvs': ['0.97','1.10','1.50','1.68'],
            'tpvf': [0.97,1.10,1.50,1.68],
            'tps': []
        }  # AOUT_SCVCD SCV电流驱动
        for i in range(4):
            CH07['tps'].append(SendString("AA 55 09 08 07 00 00 00 XX").set_TestData(CH07['tpvf'][i], CH07['ratio_1']))

        # 合并
        CHES = dict()
        CHES['00'], CHES['01'], CHES['02'], CHES['03'] = CH00, CH01, CH02, CH03
        CHES['04'], CHES['05'], CHES['06'], CHES['07'] = CH04, CH05, CH06, CH07

    class PSTest:  # 0x09
        ...

    class OPSTest:  # 0x10
        ...


class Processing:
    @staticmethod
    def cal_checksum(data):
        return data

    @staticmethod
    def cal_length(data):
        slice_data = data.split(' ')
        length = len(slice_data)
        str_length = '{:02x}'.format(length)
        slice_data[2] = str_length
        return_data = " ".join(slice_data)
        return return_data


if __name__ == '__main__':
    count = 17
    # for i in range(count):
    #     print('{:02X}'.format(i), JDK23.AITest.CHES['{:02X}'.format(i)]['tps'])
    s = SendString("AA 55 09 07 06 E8 03 00 XX")
    print(s)
    print(JDK23.AITest.CHES['06']['tps'][1].cal_TestData(100))
    print(BASE_DIR)
    # for i in range(2):
    #     print('{:02X}'.format(i), JDK23.AOTest.CHES['{:02X}'.format(i)]['tps'])
    # s1 = SendString("AA 55 09 07 00 00 00 00 XX").set_TestData(0.5, 1000)
    # print(s1)
    # s2 = SendString("AA 55 09 07 00 00 00 00 XX").set_TestData(-0.5, 1000)
    # print(s2)'{:02X}'.format(i)
    #
    # print(s1.cal_TestData(1000), s2.cal_TestData(1000))
    #
    # sendstring = SendString('AA 55 09 07 00 FC FE 00 XX')
    # sendstring.set_TestData(-2.6, 100)
    # print(sendstring.cal_TestData(100))
    # res = 0.5
    # print(res & 0XFF)
    # res =-0.5
    # print(res&0xff)
    # sendstring.set_TestData(2, 1000)
    # print(sendstring)
    # sendstring.set_TestData(3.5, 1000)
    # print(sendstring)
    # sendstring.set_TestData(4.5, 1000)
    # print(sendstring)
    # # recvstring.cal_TestData(1000)
    # # for i in dir(JDK23.DOTest):
    # #     if not i.startswith('__'):
    # #         print(getattr(JDK23.DOTest, i))
