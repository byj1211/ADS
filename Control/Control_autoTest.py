import logging
import sys

from PyQt5.QtWidgets import QApplication

from Tools.decoratorTools import *
from Tools.AutoTestQThread import AutoTestQThread
from Tools.func_test import DI, DO
from UISet.UISet_AutoTest import AutoTestWindow
from Tools.Interfaces import JDK23
from Tools.DevicesPools import *
class Control_autoTest(AutoTestWindow):
    def __init__(self):
        super(Control_autoTest, self).__init__()
        self.auto_tabWidget.setCurrentIndex(1)  # 测试用
        self.pb_auto_test.released.connect(self.startBtn_clicked)  # 点击“Ztest on”按钮触发事件
        self.initProperty()  # 初始化属性
        self.initGroups()  # 初始化按钮组
        self.initControler()  # 初始化控制器

    def initControler(self):
        """
        初始化按钮组
        """
        # self.DI_controler =
        ...

    def initProperty(self):
        """
        初始化属性
        """
        self.groups = {}
        self.re_groups={}
    def initGroups(self):
        """
        初始化按钮组
        """
        self.initGroups_DI()  # DI
        self.initGroups_DO()  # DO
        self.initGroups_AI()  # AI
        self.initGroups_AO()  # AO

    def do_change_testItem(self, testItem: str):
        """
        跳转到对应测试项
        Args:
            testItem:测试项名称['DITest','DOTest']
        Returns:
        """
        if testItem == 'DITest':
            self.auto_tabWidget.setCurrentIndex(1)
        elif testItem == 'DOTest':
            self.auto_tabWidget.setCurrentIndex(2)
        elif testItem == 'AITest':
            self.auto_tabWidget.setCurrentIndex(3)
        elif testItem == 'AOTest':
            self.auto_tabWidget.setCurrentIndex(4)

    # DI Test
    @using_tryCatch
    def do_DI_test(self, chan: int, choice: int):
        """
        DI Test:离散量输入测试
        Args:
            chan:
            choice:
        Returns:
        """
        self.do_DI_test_FE(chan, choice)  # DI Test FrontEnd
        # self.do_DI_test_BE(chan,choice)


    @using_tryCatch
    def do_DI_test_FE(self, chan: int, choice: int):

        """
        DI的前端包括按钮点击，监视框显示发送指令
        DI Test FrontEnd
        离散量测试页面显示功能
        Args:
            chan: 通道号
            choice: 测试值 0,1,2 (2为 0/1中的一种)
        Returns:
        """
        self.initUI_DI()
        for w in self.re_groups["DI"][chan]:
            w.setText("1")
        if chan in range(0, 6):  # 遍历 0 ~ 5 通道
            if chan in [0, 1]:  # 处理通道 [0 1]
                needClickBtns = self.groups['DI'][str(chan)]  # 设置需要点击的按钮
                if choice == 0:  # 测试“地” 需要点击按钮 测试“开”则不需要
                    for btn in needClickBtns:  # 遍历按钮
                        btn.click()  # 点击
            elif chan == 2:  # 处理通道 [2]
                if choice == 0:  # 测试“开”
                    needClickBtns = self.groups['DI'][str(chan)] | {self.pb_auto_di_28VKIN5_2}
                elif choice == 1:  # 测试“28V”
                    needClickBtns = self.groups['DI'][str(chan)] | {self.pb_auto_di_28VKIN5_1}
                elif choice == 2:  # 测试“地”
                    needClickBtns = self.groups['DI'][str(chan)] | {self.pb_auto_di_28VKIN5_3}
                if choice in [1]:  # 测试“28V”
                    for btn in needClickBtns:
                        btn.click()  #
                elif choice in [2]:  # 测试“地”
                    self.pb_auto_di_28VKIN5_3.click()
            elif chan == 3:  # 处理通道 [3]
                if choice == 0:  # 测试“地”
                    needClickBtns = self.groups['DI'][str(chan)] | {self.pb_auto_di_28VDIN2_3}
                elif choice == 1:  # 测试“开”
                    needClickBtns = self.groups['DI'][str(chan)] | {self.pb_auto_di_28VDIN2_2}
                elif choice == 2:  # 测试“28V”
                    needClickBtns = self.groups['DI'][str(chan)] | {self.pb_auto_di_28VDIN2_1}
                if choice in [0]:  # 测试“地”
                    for btn in needClickBtns:  # 点击按钮
                        btn.click()
                elif choice in [1, 2]:  # 测试“开”和“28V"
                    self.pb_auto_di_28VDIN2_1.click()
            elif chan in [4, 5]:  # 处理通道 [4,5]
                needClickBtns = self.groups['DI'][str(chan)]  # 设置需要点击按钮
                if choice == 1:  # 测试”地“时 需要点击
                    for btn in needClickBtns:  # 点击按钮
                        btn.click()
            BtnsInfos = ""  # 测试用
            for c in needClickBtns:  # 测试用
                BtnsInfos = BtnsInfos + "  " + c.objectName().split('_')[-1] + ":"+ c.text()  # 测试用
            # 获取发送指令
            if choice == 2 and chan == 2:
                sends = JDK23.DITest.CHES[str(chan)][str(choice - 2)]
            elif choice == 2 and chan == 3:
                sends = JDK23.DITest.CHES[str(chan)][str(choice - 1)]
            else:
                sends = JDK23.DITest.CHES[str(chan)][str(choice)]
            # 显示发送指令
            self.pte_di_insIn.setPlainText(f"chan{chan} : {choice} : {sends} {BtnsInfos}")  # 测试用
            logging.debug(f"chan{chan} : {choice} : {sends} {BtnsInfos}")
        else:  # 恢复原状
            self.pte_di_insIn.setPlainText('')  # 清空
            self.pb_auto_di_28VDIN2_2.click()  # 恢复原状
            self.pb_auto_di_28VKIN5_2.click()  # 恢复原状


    def do_DI_test_BE(self,chan,choice):
        '''
        DI Test 后端的执行代码
        :param chan: 0-5的通道号
        :param choice: 0  接地  1 断开  2  28V
        :return:
        '''
        pass
        # 获取发送指令
        # if choice == 2 and chan == 2:
        #     sends = JDK23.DITest.CHES[str(chan)][str(choice - 2)]
        # elif choice == 2 and chan == 3:
        #     sends = JDK23.DITest.CHES[str(chan)][str(choice - 1)]
        # else:
        #     sends = JDK23.DITest.CHES[str(chan)][str(choice)]
        # dcp=DCPower1()
        # dcp.connect()
        # print(chan,type(chan))
        # sendmessage='volt '+str(chan)
        # print(sendmessage)
        # dcp.write(sendmessage)
        # dcp.write('outp 1')
#------------------以下代码为真正实现的功能，需要时可解开注释--------------------
        # try:
        #     di=DI()
        #     result=di.test_channel(chan,choice)
        #     for x in self.re_groups["DI"][chan]:
        #         x.setText(str(result))
        # except Exception as e:
        #     logging.info("DI 执行后端出现 {}".format(e))
        #     logging.error(e)
    # DO Test
    @using_tryCatch
    def do_DO_test(self, chan: int, choice: int):
        """
        DO Test:离散量驱动输出测试
        Args:
            chan: 通道号
            choice: 测试值 0,1
        Returns:
        """
        self.do_DO_test_FE(chan, choice)  # DO Test FrontEnd
        # self.do_DO_test_BE(chan,choice)
    @using_tryCatch
    def do_DO_test_BE(self, chan: int, choice: int):
        '''

        :param chan:
        :param choice:
        :return:
        '''
        a=DO()
        print("channel{}".format(chan))
        re_volt=a.test_channel(chan,choice)
        print("mult回读的电压"+str(re_volt))
        for x in self.re_groups["DO"][chan+1]:
            x.setText(re_volt)
        #
    @using_tryCatch
    def do_DO_test_FE(self, chan: int, choice: int):
        """
        DO Test FrontEnd
        离散量驱动输出测试页面显示功能
        Args:
            chan: 通道号
            choice: 测试值 0,1
        Returns:
        """
        self.initUI_DO()
        if chan in range(0, 21):  # 遍历 0 ~ 20 通道
            for i in self.groups['DO'][str(chan)]:  # 点击需要点击的按钮
                if choice == 1:
                    i.click()  # 点击

            sends = JDK23.DOTest.CHES['{:02X}'.format(chan)][str(choice)]  # 获取发送指令
            print('{:02X}  {}'.format(chan,str(choice)))
            print(sends)
            self.pte_auto_do_insIn.setPlainText(f"chan{'{:02X}'.format(chan)} : {choice} : {sends}")  # 测试用
            logging.debug(f"chan{'{:02X}'.format(chan)} : {choice} : {sends}")  #
        else:
            self.pte_auto_do_insIn.setPlainText('')  # 清空

    # AI Test
    @using_tryCatch
    def do_AI_test_UI(self, chan: int, choice: float):
        self.do_AI_test_FE(chan, choice)  # AI Test FrontEnd

    def do_AI_test_FE(self, chan: int, choice: float):
        self.initUI_AI()
        if chan in range(0, 17):
            idx = JDK23.AITest.CHES['{:02X}'.format(chan)]['tpvf'].index(choice)
            sends = JDK23.AITest.CHES['{:02X}'.format(chan)]['tps'][idx]  # 获取发送指令
            self.pte_auto_ai_insIN.setPlainText(f"chan{'{:02X}'.format(chan)} : {choice} : {sends}")  # 测试用
            logging.debug(f"chan {chan} : {choice} : {sends} [{idx}]")
            for i in self.groups['AI'][str(chan)]:
                i.setValue(choice)
                i.setStyleSheet("background-color: green;")
        else:
            self.pte_auto_ai_insIN.setPlainText("")

    # AO Test
    @using_tryCatch
    def do_AO_test(self, chan: int, choice: float):
        self.do_AO_test_FE(chan, choice)  # AO Test FrontEnd

    def do_AO_test_FE(self, chan: int, choice: float):
        self.initUI_AO()
        if chan in range(0, 8):
            idx = JDK23.AOTest.CHES['{:02X}'.format(chan)]['tpvf'].index(choice)
            sends = JDK23.AOTest.CHES['{:02X}'.format(chan)]['tps'][idx]  # 获取发送指令
            self.pte_auto_ao_insIN.setPlainText(f"chan{'{:02X}'.format(chan)} : {choice} : {sends}")  # 测试用
            logging.debug(f"chan {chan} : {choice} : {sends} [{idx}]")
            for i in self.groups['AO'][str(chan)]:
                i.setText(str(choice))
                i.setStyleSheet("background-color: green;font-size:20px;")
        else:
            self.pte_auto_ao_insIN.setPlainText("")

    # def getRecvData(self,dic):
    #     for key,value in dic.items():
    #         if key =='device1':
    #             self.pte_auto_ai_insIN.setPlainText(value)
    #         elif key=='device2':
    #             self.pte_auto_ai_insOUT.setPlainText(value)

    def getRecvData(self, reback):
        print(reback)
    def startBtn_clicked(self):
        """
        点击开始测试按钮 触发函数
        Returns:
        """
        self.initGroups()  # 初始按钮组
        if self.pb_auto_test.isChecked():  # 如果点击 开始运行
            self.autothread = AutoTestQThread()  # 定义
            self.autothread.DITestSignal.connect(self.do_DI_test)  # 绑定信号与槽函数
            self.autothread.DOTestSignal.connect(self.do_DO_test)  # 绑定信号与槽函数
            self.autothread.AITestSignal.connect(self.do_AI_test_UI)  # 绑定信号与槽函数
            self.autothread.RecvDataSignal.connect(self.getRecvData)

            self.autothread.AOTestSignal.connect(self.do_AO_test)  # 绑定信号与槽函数
            self.autothread.InterruptSignal.connect(self.do_interrupt)  # 绑定信号与槽函数
            self.autothread.ChangeSignal.connect(self.do_change_testItem)  # 绑定信号与槽函数
            self.autothread.finished.connect(
                lambda: (self.pb_auto_test.click() if self.pb_auto_test.isChecked() else ...))  # 绑定信号与槽函数
            self.autothread.start()  # 开始运行
        else:  # 结束运行
            # self.pb_auto_test.click()
            self.autothread.flag = False  # 设置为False 结束运行

    def initGroups_DI(self):
        # 初始化DI
        #通道号0-5
        #这里的控件组合都没有加上启动监视器1和2
        self.groups = {'DI': {}}
        self.re_groups={"DI":{}}
        self.groups['DI']['0'] = {
            self.btn_auto_di_DKIN1, self.btn_auto_di_DKIN2, self.btn_auto_di_DKIN3,
            self.btn_auto_di_DKIN4, self.btn_auto_di_DKIN5, self.btn_auto_di_DKIN6,
        }
        self.groups['DI']['1'] = {
            self.btn_auto_di_DKIN7, self.btn_auto_di_DKIN8, self.btn_auto_di_DKIN9,
            self.btn_auto_di_DKIN10, self.btn_auto_di_DKIN11, self.btn_auto_di_DKIN12, self.btn_auto_di_DKIN13,
        }
        self.groups['DI']['2']   = {
            self.btn_auto_di_28VKIN1, self.btn_auto_di_28VKIN2, self.btn_auto_di_28VKIN3,
            self.btn_auto_di_28VDIN1, self.btn_auto_di_28VKIN4,
        }
        self.groups['DI']['3'] = {
            self.btn_auto_di_28VDIN3, self.btn_auto_di_28VDIN4,
        }
        self.groups['DI']['4'] = {
            self.btn_auto_di_RDKIN1,
        }
        self.groups['DI']['5'] = {
            self.btn_auto_di_RDKIN2,
        }
        self.groups['DI']['ALL'] = set()
        for i in range(6):
            self.groups['DI']['ALL'] = self.groups['DI']['ALL'] | self.groups['DI'][str(i)]
        self.re_groups["DI"][0]=[
            self.le_auto_di_DKIN1r,self.le_auto_di_DKIN2r,self.le_auto_di_DKIN3r,
            self.le_auto_di_DKIN4r,self.le_auto_di_DKIN5r,
            self.le_auto_di_DKIN6r
        ]
        self.re_groups["DI"][1]=[
            self.le_auto_di_lDKIN7r,self.le_auto_di_DKIN8r,self.le_auto_di_DKIN9r,self.le_auto_di_DKIN10r
            ,self.le_auto_di_DKIN11r,self.le_auto_di_DKIN12r,self.le_auto_di_DKIN13r
        ]
        self.re_groups["DI"][2]=[
            self.le_auto_di_28VKIN1r,self.le_auto_di_28VKIN2r,self.le_auto_di_28VKIN3r,
            self.le_auto_di_28VDIN1r,self.le_auto_di_28VKIN4r
        ]
        self.re_groups["DI"][3]=[
            self.le_auto_di_28VDIN4r,self.le_auto_di_28VDIN3r
        ]
        self.re_groups["DI"][4]=[
            self.le_auto_di_APUr
        ]
        self.re_groups["DI"][5] = [
            self.le_auto_di_RDKIN2r
        ]
        self.re_groups['DI']['ALL'] = set()
        for i in range(6):
            self.re_groups['DI']['ALL'] = self.re_groups['DI']['ALL'] | set(self.re_groups['DI'][i])
    def initGroups_DO(self):
        """
        初始化DO
        Returns:
        """
        self.groups['DO'] = {"DO":{}}
        self.groups['DO']['0'], self.groups['DO']['1'], = {self.pb_auto_do_28VKOUT1}, {self.pb_auto_do_28VKOUT2}
        self.groups['DO']['2'], self.groups['DO']['3'], = {self.pb_auto_do_28VKOUT3}, {self.pb_auto_do_28VKOUT4}
        self.groups['DO']['4'], self.groups['DO']['5'], = {self.pb_auto_do_28VKOUT5}, {self.pb_auto_do_28VKOUT6}
        self.groups['DO']['6'], self.groups['DO']['7'], = {self.pb_auto_do_28VKOUT7}, {self.pb_auto_do_28VKOUT8}
        self.groups['DO']['8'], self.groups['DO']['9'], = {self.pb_auto_do_28VKOUT9}, {self.pb_auto_do_28VKOUT10}
        self.groups['DO']['10'], self.groups['DO']['11'], = {self.pb_auto_do_28VKOUT11}, {self.pb_auto_do_28VKOUT12}
        self.groups['DO']['12'], self.groups['DO']['13'], = {self.pb_auto_do_28VKOUT13}, {self.pb_auto_do_28VKOUT14}
        self.groups['DO']['14'], self.groups['DO']['15'], = {self.pb_auto_do_DKOUT1}, {self.pb_auto_do_DKOUT2}
        self.groups['DO']['16'], self.groups['DO']['17'], = {self.pb_auto_do_DKOUT3}, {self.pb_auto_do_DKOUT4}
        self.groups['DO']['18'], self.groups['DO']['19'], = {self.pb_auto_do_DKOUT5}, {self.pb_auto_do_DKOUT6}
        self.groups['DO']['20'] = {self.pb_auto_do_DKOUT7}
        self.groups['DO']['ALL'] = set()
        for i in range(21):
            self.groups['DO']['ALL'] = self.groups['DO']['ALL'] | self.groups['DO'][str(i)]
        #对回读的lineedit组件按照通道号组成、排序
        self.re_groups["DO"]={"DO":{}}
        self.re_groups['DO']['ALL'] = set()
        for i in range(1, 15):
            # print( getattr(self, f"le_auto_do_28VKOUT{i}"))
            self.re_groups["DO"][i] =[ getattr(self, f"le_auto_do_28VKOUT{i}")]
        for i in range(1, 8):
            self.re_groups["DO"][i+14] = [getattr(self, f"le_auto_do_DKOUT{i}")]
        for i in range(1,22):
            self.re_groups['DO']['ALL'] = self.re_groups['DO']['ALL'] | set(self.re_groups['DO'][i])
    def initGroups_AI(self):
        self.groups['AI'] = {}
        self.groups['AI']['0'] = {self.dsb_auto_ai_AIN_EDT}
        self.groups['AI']['1'] = {self.dsb_auto_ai_AIN_NVT}
        self.groups['AI']['2'] = {self.dsb_auto_ai_AIN_SVM}
        self.groups['AI']['3'] = {self.dsb_auto_ai_AIN_KTM_1}
        self.groups['AI']['4'] = {self.dsb_auto_ai_AIN_KTM_2}
        self.groups['AI']['5'] = {self.dsb_auto_ai_AIN_KTM_3}
        self.groups['AI']['6'] = {self.dsb_auto_ai_AIN_KTM_4}
        self.groups['AI']['7'] = {self.dsb_auto_ai_AIN_KTM_5}
        self.groups['AI']['8'] = {self.dsb_auto_ai_AIN_PT100_1}
        self.groups['AI']['9'] = {self.dsb_auto_ai_AIN_PT100_2}
        self.groups['AI']['10'] = {self.dsb_auto_ai_AIN_PT100_3}
        self.groups['AI']['11'] = {self.dsb_auto_ai_AIN_CTSENSOR}
        self.groups['AI']['12'] = {self.dsb_auto_ai_IGV_IN, self.dsb_auto_ai_IGV_incentive}
        self.groups['AI']['13'] = {self.dsb_auto_ai_SCV_IN, self.dsb_auto_ai_SCV_incentive}
        self.groups['AI']['14'] = {self.dsb_auto_ai_FCU_IN, self.dsb_auto_ai_FCU_incentive}
        self.groups['AI']['15'] = {self.dsb_auto_ai_AIN_FRE_N1}
        self.groups['AI']['16'] = {self.dsb_auto_ai_AIN_FRE_N2}

        self.groups['AI']['ALL'] = set()
        for i in range(12):
            self.groups['AI']['ALL'] = self.groups['AI']['ALL'] | self.groups['AI'][str(i)]

    def initGroups_AO(self):
        self.groups['AO'] = {}
        self.groups['AO']['0'] = {self.le_auto_ao_AOUT_PREPS}
        self.groups['AO']['1'] = {self.le_auto_ao_AOUT_FLPPS}
        self.groups['AO']['2'] = {self.le_auto_ao_LVDT_IGVPRI_STATEv, self.le_auto_ao_LVDT_IGVPRI_STATEf}
        self.groups['AO']['3'] = {self.le_auto_ao_LVDT_SGVPRI_STATEv, self.le_auto_ao_LVDT_SGVPRI_STATEf}
        self.groups['AO']['4'] = {self.le_auto_ao_RVDT_FCUPRI_STATEv, self.le_auto_ao_RVDT_FCUPRI_STATEf}
        self.groups['AO']['5'] = {self.le_auto_ao_AOUT_IGVCD}
        self.groups['AO']['6'] = {self.le_auto_ao_AOUT_FCUCD}
        self.groups['AO']['7'] = {self.le_auto_ao_AOUT_SCVCD}

        self.groups['AO']['ALL'] = set()
        for i in range(8):
            self.groups['AO']['ALL'] = self.groups['AO']['ALL'] | self.groups['AO'][str(i)]

    def do_interrupt(self):
        """
        终止测试 恢复默认状态
        Returns:
        """
        # DI
        self.initUI_DI()
        # DO
        self.initUI_DO()
        # AI
        self.initUI_AI()
        # AO
        self.initUI_AO()

    def initUI_DI(self):
        for i in self.groups['DI']['ALL']:  # 默认回到初始状态
            if i.isChecked():  # 如果是点击状态
                i.click()  # 恢复原状
        self.pb_auto_di_28VDIN2_2.click()  # 恢复
        self.pb_auto_di_28VKIN5_2.click()  # 恢复
        self.pte_di_insIn.setPlainText('')  # 清空

    def initUI_DO(self):
        for i in self.groups['DO']['ALL']:  # 默认回到初始状态
            if i.isChecked():  # 如果是点击状态
                i.click()  # 恢复原状
        self.pte_auto_do_insIn.setPlainText('')  # 清空

    def initUI_AI(self):
        for i in range(17):
            for j in self.groups['AI'][str(i)]:
                j.setValue(0)
                j.setStyleSheet("background-color:''")

        self.pte_auto_ai_insIN.setPlainText('')

    def initUI_AO(self):
        for i in range(8):
            for j in self.groups['AO'][str(i)]:
                j.setText('')
                j.setStyleSheet("background-color:'';font-size:20px;")

        self.pte_auto_ao_insIN.setPlainText('')


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        ContorlAutoTestWindow = Control_autoTest()
        ContorlAutoTestWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
