import logging
import inspect
import time

from Tools import command as cd
from Tools.DevicesPools import ACPower, DCPower1, DCPower2, Multimeter, SignalGenerator
from Tools.Interfaces import JDK23
from Tools.Serial_IO import Serial_io_tool
from Tools.delay import delay
# global delay_com = "COM7"
# global delay_baudrate=115200
logging.basicConfig(level=logging.INFO)

class func_all_test:
    def __init__(self):
        pass
        self.test=autoTest_func()
        # self.DI=DI(self)
        # self.DO=DO(self)
        # self.AI=AI(self)
        # 以下是要用到的工具
        # self.serial_ECB=Serial_io_tool("COM10")
        # self.delay=delay()
        # self.delay.connect()

    class DI:
        def __init__(self):
            '''

            :param parent:
            '''

            try:
                self.delay_channl_num = ["0", "1", "2", "3", "4"]  # 这里指的是需要以及有继电器操作的支路通道号

            except Exception as e:
                logging.INFO("DI_func初始化出现错误" + e)
                logging.error(e)
                print("DI_func出现错误" + e)

        # 离散量输入的测试函数
        def test_channel(self, chan, choice):
            '''
            DI
            :param chan: 对离散量输入哪个通道进行处理
            :param state: 该通道测试状态是2表示接地，0断开，1表示28V
            tips：这里的choice当28V时怎么弄？
            :return:
            step1:delay通断控制
            step2:给ECB发送指令，获取回读值
            step3:回读值和设定进行对比，输出OK or ERROR
            '''

            try:
                #     # 先配置好外部环境-继电器
                if str(chan) in self.delay_channl_num:
                    # self.delay.send_command_singel(delay_data.DI[chan],choice)
                    print(delay_data.DI[str(chan)], choice)
                # num=delay_data.DI[str(chan)]
                # print("delay",num,choice)
            #     self.delay.send_command_singel(num,choice)
            #     #被测件指令
            #     if choice == 2 and chan == 2:
            #         sends = JDK23.DITest.CHES[str(chan)][str(choice - 2)]
            #     elif choice == 2 and chan == 3:
            #         sends = JDK23.DITest.CHES[str(chan)][str(choice - 1)]
            #     else:
            #         sends = JDK23.DITest.CHES[str(chan)][str(choice)]
            #     print(sends)
            #     #向被测件发指令
            #     # self.serial_ECB.write_data(sends)
            #     #向被测件回读
            #     #进行数据包对比
            #     # result=compare(a,b)
            #     # return result  #result是True  False，表明测试是否成功
            #     # logging.info("DI测试中{}通道的{}测试结果是{}".format(chan,choice,result))
            except Exception as e:
                logging.INFO("DI执行出现错误 {}".format(e))
                logging.error(e)
                return e

    class AI():
        def __init__(self, parent):
            self.parent = parent
            try:
                self.delay_chan_num = [0, 1, 2, 3, 4, 5, 6, 7, 15, 16]
                self.type_DcVolt = [0, 1, 2, 3, 4, 5, 6, 7]
                self.type_Res = [8, 9, 10, 11]
                self.type_phase = [12, 13, 14]
                self.type_freq = [15, 16]
                self.test=self.parent.test
                self.parent.test.AI_device_init()
            except Exception as e:
                logging.INFO("AI_func出现错误" + e)
                logging.error(e)
                print("AI_func出现错误" + e)

        # def set_freq_sine_test(self,choice):
        #     if choice == 300:
        #         v_pp = 0.5
        #     elif choice == 3000:
        #         v_pp = 1
        #     elif choice == 8000:
        #         v_pp = 3
        #     elif choice == 14640:
        #         v_pp = 5
        #     index=JDK23.AITest.CHES['{:02X}'.format(chan)][tpvf].index(str(choice))
        #     v_pp=JDK23.AITest.CHES['{:02X}'.format(chan)]['v_pp'][index]
        #     self.test.set_ac_sine(JDK23.AITest.CHES[], choice)

        def test_channel(self, chan, choice):
            '''
            :param chan: 对离散量输入哪个通道进行处理
            :param state: 该通道测试状态是0表示断开，1接地，2表示28V
            tips：这里的choice当28V时怎么弄？
            :return: result 表示输出和预期是否一致
            '''
            try:
                if choice == "1":
                    other_state = "0"
                elif choice == "0":
                    other_state = "1"
                if chan in self.delay_chan_num:
                    for x in self.delay_chan_num:
                        if x == chan:
                            pass
                        print(delay_data.AI[str(chan)], choice)  # 后期这里的继电器num需要加48
                        #     self.delay.send_command_singel(chan,choice)
                        # self.delay.send_command_singel(chan,other_state)
                if chan in self.type_DcVolt:
                    volt = convert_mv_to_V(choice, JDK23.AITest.CHES['{:02X}'.format(chan)]["unit"])
                    re = self.test.Set_dc_volt(volt)
                    self.test.set_equip_output_state("dc2", 1)
                    # self.delay.send_command_singel()
                    pass
                elif chan in self.type_freq:
                    index = JDK23.AITest.CHES['{:02X}'.format(chan)]["tpvs"].index(str(choice))
                    v_pp = JDK23.AITest.CHES['{:02X}'.format(chan)]['v_pp'][index]
                    re = self.test.set_ac_sine(v_pp, choice)
                    self.test.set_equip_output_state("generator", 1)
                    # self.delay.send_command_singel()
                elif chan in self.type_phase:
                    # self.delay.send_command_singel()
                    re = "LVDT"
                    pass
                elif chan in self.type_Res:
                    # self.delay.send_command_singel()
                    re = "res"
                    pass
                # sends = JDK23.DOTest.CHES['{:02X}'.format(chan)][str(choice)]  # 获取发送指令
                # print(sends)
                # 向被测件发指令
                # self.serial_ECB.write_data(sends)
                # 向被测件回读
                # 进行数据包对比
                # result=compare(a,b)  #返回result的值
                return re
            except Exception as e:
                logging.info("AI出现错误 ：{}".format(e))
                logging.error(e)
                print(e)
class autoTest_func:
    def __init__(self):
        try:
            #以下是要用到的工具
            # self.serial_ECB=Serial_io_tool("COM10")
            # self.delay1=delay()
            # self.delay1.connect()
            # self.delay2
            self.devices = {
                'ac': ACPower(),
                'dc1': DCPower1(),
                'dc2': DCPower2(),
                'meter': Multimeter(),
                'generator': SignalGenerator()
            }
            self.devices["ac"].connect()
            self.devices["dc1"].connect()
            self.devices["dc2"].connect()
            self.devices["meter"].connect()
            self.devices["generator"].connect()
            self.power_supply()
            self.devices_init()
        except Exception as e:
            logging.INFO("auto_Test出现错误" + e)
            logging.error(e)
            print("auto_Test出现错误" + e)


    def AI_device_init(self):
        '''
        针对模拟量输入测试进行设备初始化
        1.ITCHpower 电流输出量程设定为1mA
        2.电源输出模式为CV
        :return:
        '''
        self.devices["dc2"].write(cd.dc_ITCH.OUTP_mode+"VOLT")
        self.devices["dc2"].write(cd.dc_ITCH.set_curr_range+"0.001")  #设置电流输出量程为1mA（由于电源输出功率恒定）


    def devices_init(self):
        '''
        对设备的初始化操作，比如:
        1.面板锁定，禁止手动操作
        2.设置为远程操控

        后续继续添加基础设定
        :return:
        '''
        try:
            self.devices["ac"].write(cd.ac_kikusui.local_button_lock)
            self.devices["dc1"].write(cd.ac_kikusui.local_button_lock)
            self.devices["dc2"].write(cd.dc_ITCH.SYST_control)
            self.devices["dc2"].write(cd.dc_ITCH.V_range)
            # self.devices["dc2"].write(cd.dc_ITCH.A_range)
            self.devices["meter"].write(cd.SYST_query)
            self.devices["generator"].connect()  #目前暂无禁用面板操作
        except Exception as e:
            logging.info("设备初始化出现问题{}".format(e))
            logging.error(e)

    def set_equip_output_state(self,name:str,state:int):
        '''
        改变指定某台设备的输出状态，
        :param name: "ac","dc1","dc2"，“meter”,"generator"
        :param state: 1表示输出打开，0表示输出关闭
        :return:
        '''
        if state==1:
            self.devices[name].write(cd.output_on)
        elif state==0:
            self.devices[name].write(cd.output_off)

    def meas_curr(self):
        """
        实现从万用表回读电流的功能
        :return:  返回电流值（未经处理）
        """
        try:
            meas = self.devices["meter"]
            meas.write(cd.Multimeter.set_func_curr_dc)
            meas.write(cd.Multimeter.set_range_meas)
            meas_freq1 = meas.query(cd.Multimeter.meas_curr_dc)
            # meas_volt = convert_voltage(meas_freq1)
            return meas_freq1
        except Exception as e:
            logging.INFO("func-DO出出现错误 ：{}".format(e))
            logging.error(e)
            print("func-DO出出现错误 ：{}".format(e))
    def Set_dc_volt(self,volt):
        try:
            power=self.devices["dc2"]

            power.write(cd.dc_ITCH.V_set+str(volt))
            a=power.query(cd.dc_ITCH.V_meas)
            return convert_voltage(a)
        except Exception as e:
            logging.INFO("func-AI_SetPower_volt出出现错误 ：{}".format(e))
            logging.error(e)
            print("func-AI_SetPower_volt出出现错误 ：{}".format(e))
    def meas_freq(self):
        """
        实现从万用表回读频率的功能
        :return:  返回频率值
        """
        try:
            meas = self.devices["meter"]
            meas.write(cd.Multimeter.set_func_freq)
            meas.write(cd.Multimeter.set_range_meas)
            meas_freq1 = meas.query(cd.Multimeter.meas_freq)
            # meas_volt = convert_voltage(meas_freq1)
            return meas_freq1
        except Exception as e:
            logging.INFO("func-DO出出现错误 ：{}".format(e))
            logging.error(e)
            print("func-DO出出现错误 ：{}".format(e))
    def meas_volt(self):
        """
        实现从万用表回读电压的功能
        :return:  返回电压值，经过处理的例2.00V
        """
        try:
            meas = self.devices["meter"]
            meas.write(cd.Multimeter.set_func_volt_dc)
            meas.write(cd.Multimeter.set_range_meas)
            meas_volt1 = meas.query(cd.Multimeter.meas_volt_dc)
            meas_volt = convert_voltage(meas_volt1)
            return meas_volt
        except Exception as e:
            logging.INFO("func-DO出出现错误 ：{}".format(e))
            logging.error(e)
            print("func-DO出出现错误 ：{}".format(e))

    #实现上电后基础对被测件、信号调理箱供电
    def power_supply(self):
        ac = self.devices["ac"]
        ac.write(cd.ac_kikusui.set_ac115)
        ac.write(cd.ac_kikusui.set_freq400)
        dc1 = self.devices["dc1"]
        dc1.write(cd.dc_kikusui.set_dc_28)

    from typing import Union

    def check_str(self,a: Union[str, int,float]) -> str:
        if isinstance(a, str):
            return a
        else:
            return str(a)

    def set_ac_sine(self,v_pp,freq):
        '''
        实现信号发生器产生特定P-P值，频率的交流输出（默认正弦波）
        :param v_pp:
        :param freq:
        :return:
        '''
        try:
            v_pp=self.check_str(v_pp)
            freq=self.check_str(freq)
            generator=self.devices["generator"]
            generator.write(cd.signal_generator.channel_c1_sine)
            generator.write(cd.signal_generator.channel_c1_offset)
            generator.write(cd.signal_generator.channel_c1_phase)
            generator.write(cd.signal_generator.channel_c1_vpp+v_pp)
            generator.write(cd.signal_generator.channel_c1_freq+freq)
            generator.write(cd.output_on)
            time.sleep(0.5)
            re=generator.query(cd.signal_generator.query_c1)
            current_function = inspect.currentframe().f_code.co_name
            return re
        except Exception as e:
            logging.error(f"{current_function} 出现错误: {e}")
            logging.INFO(f"{current_function} 出现错误: {e}")

#delay串口的波特率于232串口的波特率不一样是否OK
def convert_voltage(voltage):
    voltage = str(voltage)
    if 'E' in voltage:
        voltage_parts = voltage.split('E')
        voltage_main = float(voltage_parts[0])
        voltage_exponent = int(voltage_parts[1])
        if voltage_exponent >= -3:
            voltage_unit = 'V'
            voltage_main *= 10**voltage_exponent
        elif voltage_exponent >= -6:
            voltage_unit = 'mV'
            voltage_main *= 10**(voltage_exponent + 3)
        else:
            voltage_unit = 'uV'
            voltage_main *= 10**(voltage_exponent + 6)
        return str(round(voltage_main,3)) + voltage_unit
    else:
        return voltage + "V"



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

#对发给被测件的数据报和被测件返回的数据包进行对比
class compare:
    def __init__(self,send_ECB_message,ECB_return_messang):
        '''

        :param send_ECB_message:
        :param ECB_return_messang:
        '''
        pass
class DO(func_all_test):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        try:
            # self.serial_ECB=Serial_io_tool("COM10")

            self.devices = {
                'ac': ACPower(),
                'dc1': DCPower1(),
                'dc2': DCPower2(),
                'meter': Multimeter(),
                'generator': SignalGenerator()
            }
            self.power_supply()
        except Exception as e:
            logging.INFO("DI_func出现错误"+e)
            logging.error(e)
            print("DI_func出现错误"+e)

    # 离散量输入的测试函数
    def test_channel(self, chan, choice):
        '''
        :param chan: 对离散量输入哪个通道进行处理
        :param state: 该通道测试状态是0表示断开，1接地，2表示28V
        tips：这里的choice当28V时怎么弄？
        :return:
        '''
        try:
            # sends = JDK23.DOTest.CHES['{:02X}'.format(chan)][str(choice)]  # 获取发送指令
            # print(sends)
            # 向被测件发指令
            # self.serial_ECB.write_data(sends)
            # 向被测件回读
            # 进行数据包对比
            # compare(a,b)
            meas=self.devices["meter"]
            meas.write(cd.Multimeter.set_func_volt_dc)
            meas_volt1=meas.query(cd.Multimeter.meas_volt_dc)
            meas_volt=convert_voltage(meas_volt1)
            dic = {'device': str(meas_volt), 'device2': str(meas_volt)}
            print(dic)
            return dic
        except Exception as e:
            logging.INFO("离散量输出出现错误 ：{}".format(e))
            logging.error(e)
            current_function = inspect.currentframe().f_code.co_name
            logging.error(f"{current_function} 出现错误: {e}")
            logging.INFO(f"{current_function} 出现错误: {e}")

    def power_supply(self):
        ac = self.devices["ac"]
        ac.write(cd.ac_kikusui.set_ac115)
        ac.write(cd.ac_kikusui.set_freq400)
        dc1 = self.devices["dc1"]
        dc1.write(cd.dc_kikusui.set_dc_28)
class DI(func_all_test):
    def __init__(self, parent):
        '''

        :param parent:
        '''
        super().__init__()
        self.parent = parent
        try:
            self.delay_channl_num=["0","1","2","3","4"]  #这里指的是需要以及有继电器操作的支路通道号

        except Exception as e:
            logging.INFO("DI_func初始化出现错误"+e)
            logging.error(e)
            print("DI_func出现错误"+e)

    #离散量输入的测试函数
    def test_channel(self,chan,choice):
        '''
        DI
        :param chan: 对离散量输入哪个通道进行处理
        :param state: 该通道测试状态是2表示接地，0断开，1表示28V
        tips：这里的choice当28V时怎么弄？
        :return:
        step1:delay通断控制
        step2:给ECB发送指令，获取回读值
        step3:回读值和设定进行对比，输出OK or ERROR
        '''

        try:
        #     # 先配置好外部环境-继电器
            if chan in self.delay_channl_num:
                # self.delay.send_command_singel(delay_data.DI[chan],choice)
                print(chan,choice)
            # num=delay_data.DI[str(chan)]
            # print("delay",num,choice)
        #     self.delay.send_command_singel(num,choice)
        #     #被测件指令
        #     if choice == 2 and chan == 2:
        #         sends = JDK23.DITest.CHES[str(chan)][str(choice - 2)]
        #     elif choice == 2 and chan == 3:
        #         sends = JDK23.DITest.CHES[str(chan)][str(choice - 1)]
        #     else:
        #         sends = JDK23.DITest.CHES[str(chan)][str(choice)]
        #     print(sends)
        #     #向被测件发指令
        #     # self.serial_ECB.write_data(sends)
        #     #向被测件回读
        #     #进行数据包对比
        #     # result=compare(a,b)
        #     # return result  #result是True  False，表明测试是否成功
        #     # logging.info("DI测试中{}通道的{}测试结果是{}".format(chan,choice,result))
        except Exception as e:
            logging.INFO("DI执行出现错误 {}".format(e))
            logging.error(e)
            return e


class AI(func_all_test):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        try:
            self.delay_chan_num=[0,1,2,3,4,5,6,7,15,16]
            self.type_DcVolt=[0,1,2,3,4,5,6,7]
            self.type_Res=[8,9,10,11]
            self.type_phase=[12,13,14]
            self.type_freq=[15,16]
            self.test.AI_device_init()
        except Exception as e:
            logging.INFO("AI_func出现错误"+e)
            logging.error(e)
            print("AI_func出现错误"+e)
    # def set_freq_sine_test(self,choice):
    #     if choice == 300:
    #         v_pp = 0.5
    #     elif choice == 3000:
    #         v_pp = 1
    #     elif choice == 8000:
    #         v_pp = 3
    #     elif choice == 14640:
    #         v_pp = 5
    #     index=JDK23.AITest.CHES['{:02X}'.format(chan)][tpvf].index(str(choice))
    #     v_pp=JDK23.AITest.CHES['{:02X}'.format(chan)]['v_pp'][index]
    #     self.test.set_ac_sine(JDK23.AITest.CHES[], choice)


    def test_channel(self, chan, choice):
        '''
        :param chan: 对离散量输入哪个通道进行处理
        :param state: 该通道测试状态是0表示断开，1接地，2表示28V
        tips：这里的choice当28V时怎么弄？
        :return: result 表示输出和预期是否一致
        '''
        try:
            if choice=="1":
                other_state="0"
            elif choice=="0":
                other_state="1"
            if chan in self.delay_chan_num:
                for x in self.delay_chan_num:
                    if x==chan:
                        pass
                    print(delay_data.AI[chan],choice)  #后期这里的继电器num需要加48
                    #     self.delay.send_command_singel(chan,choice)
                    # self.delay.send_command_singel(chan,other_state)
            if chan in self.type_DcVolt:
                volt=convert_mv_to_V(choice,JDK23.AITest.CHES['{:02X}'.format(chan)]["unit"])
                re=self.test.Set_dc_volt(volt)
                self.test.set_equip_output_state("dc2",1)
                # self.delay.send_command_singel()
                pass
            elif chan in self.type_freq:
                index = JDK23.AITest.CHES['{:02X}'.format(chan)]["tpvs"].index(str(choice))
                v_pp = JDK23.AITest.CHES['{:02X}'.format(chan)]['v_pp'][index]
                re=self.test.set_ac_sine(v_pp,choice)
                self.test.set_equip_output_state("generator",1)
                # self.delay.send_command_singel()
            elif chan in self.type_phase:
                # self.delay.send_command_singel()
                re="LVDT"
                pass
            elif chan in self.type_Res:
                # self.delay.send_command_singel()
                re="res"
                pass
            # sends = JDK23.DOTest.CHES['{:02X}'.format(chan)][str(choice)]  # 获取发送指令
            # print(sends)
            # 向被测件发指令
            # self.serial_ECB.write_data(sends)
            # 向被测件回读
            # 进行数据包对比
            # result=compare(a,b)  #返回result的值
            return re
        except Exception as e:
            logging.info("离散量输出出现错误 ：{}".format(e))
            logging.error(e)
            print(e)

class AO(func_all_test):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        try:
            # self.delay=delay()
            # self.delay.connect()
            self.chan_volt=[0,1]
            self.chan_curr=[5,6,7]
            self.chan_lvdt=[2,3,4]
            current_function = inspect.currentframe().f_code.co_name
        except Exception as e:
            logging.error(f"{current_function} 出现错误: {e}")
            logging.INFO(f"{current_function} 出现错误: {e}")

    def test_channel(self,chan,choice):
        '''

        :param chan:
        :param choice:
        :return:
        step1:ATE发送数据包给ECB
        step2:ECB读取、输出、发送
        step3:设备采集ATE对应通道输出
        step4:采集值与期望值对比
        '''
        sends = JDK23.DOTest.CHES['{:02X}'.format(chan)][str(choice)]  # 获取发送指令
        print(sends)
        # 向被测件发指令
        # self.serial_ECB.write_data(sends)
        # 向被测件回读
        if chan in self.chan_volt:
            re=self.test.meas_volt()
        elif chan in self.chan_curr:
            re=self.test.meas_curr()
        elif chan in self.chan_lvdt:
            pass
        # 进行数据包对比
        # result=compare(a,b)  #返回result的值
        return re


def convert_mv_to_V(volt,unit):
    if "m" in unit:
        volt_con=round(float(volt)/1000,5)
    elif unit=="V":
        volt_con=volt
    else:
        logging.info("将mV转换成V出现异常，传入参数为"+str(volt)+str( unit))
    return volt_con


if __name__ == '__main__':
    b=func_all_test()
    a =AI(b)
    for chan in [15, 16]:
        for choice in JDK23.AITest.CHES['{:02X}'.format(chan)]["tpvs"]:
            index = JDK23.AITest.CHES['{:02X}'.format(chan)]["tpvs"].index(str(choice))
            v_pp = JDK23.AITest.CHES['{:02X}'.format(chan)]['v_pp'][index]
            print(index, choice, v_pp)

            a.test_channel(chan,choice)
            time.sleep(0.1)