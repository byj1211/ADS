import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.py import UI_ManualTest as UI
from Tools.data_all import tab_change, all_data

class ManualTestWindow(QMainWindow, UI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ManualTestWindow, self).__init__(parent)
        self.setupUi(self)  # 设置UI
        self.tab_name=None
        self.showMaximized()
        self.pb_auto_test.setVisible(False)

        self.button_click=False
        # 绑定电源上电的按钮
        self.PushButton_115.setEnabled(True)
        self.PushButton_115.setCheckable(True)
        self.PushButton_115.toggled.connect(self.power_on_style)

        self.PushButton_28.setEnabled(True)
        self.PushButton_28.setCheckable(True)
        self.PushButton_28.toggled.connect(self.power_on_style)
        self.PushButton_signal_generaor.setEnabled(True)
        self.PushButton_signal_generaor.setCheckable(True)
        self.PushButton_signal_generaor.toggled.connect(self.power_on_style)
        self.PushButton_28_test.setEnabled(True)
        self.PushButton_28_test.setCheckable(True)
        self.PushButton_28_test.toggled.connect(self.power_on_style)
        # self.PushButton_115.clicked.connect(self.on_clicked_pb_115_test)
        # self.PushButton_28.clicked.connect(self.on_clicked_pb_man_test)
        # self.PushButton_signal_generaor.clicked.connect(self.on_clicked_pb_man_test)
        # self.PushButton_28_test.clicked.connect(self.on_clicked_pb_man_test)
        self.auto_tabWidget.currentChanged.connect(self.on_click_tabChange)
        # 启动器默认为开
        self.pb_auto_di_28VKIN5_2.click()
        self.pb_auto_di_28VDIN2_2.click()

        # # 下拉框文本居中
        self.cm_auto_ai_AIN_PT100_9.lineEdit().setAlignment(Qt.AlignCenter)
        self.cm_auto_ai_AIN_PT100_8.lineEdit().setAlignment(Qt.AlignCenter)
        self.cm_auto_ai_AIN_PT100_7.lineEdit().setAlignment(Qt.AlignCenter)
        self.cm_auto_ai_AIN_CTSENSOR_3.lineEdit().setAlignment(Qt.AlignCenter)

        # 设置控制测试表格的列宽
        self.auto_cor_ins_table.setColumnWidth(0, 100)
        self.auto_cor_ins_table.setColumnWidth(1, 400)
        self.auto_cor_ins_table.setColumnWidth(2, 600)
        self.auto_cor_ins_table.setColumnWidth(3, 240)
        # 设置树的列宽
        self.test_auto_treeWidget.setColumnWidth(0, 200)
        self.test_auto_treeWidget.setColumnWidth(1, 100)
        self.button_init()
        # 表格设置为只读
        for row in range(self.auto_cor_ins_table.rowCount()):
            for col in range(4):  # Columns 0 and 1
                item = self.auto_cor_ins_table.item(row, col)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.func_button_style_change=[self.power_on_style,self.sends_style_change,self.DI_style_change,self.DO_style_change,self.AI_style_change
                                       ,self.AO_style_change,self.carProtect_style_change]
    def set_single_buttonOff_stylesheet(self,bt):
        current_style = bt.styleSheet()
        new_style = f"{current_style} QPushButton {{ background-color: transparent; }}"
        for item in all_data["AI"]["control_button"]:
            name = all_data["AI"]["control_button"][item]
            button = getattr(self, all_data["AI"]["control_button"][item])
            button.setCheckable(True)
            # 禁用所有标签页
        for i in range(self.auto_tabWidget.count()):
            self.auto_tabWidget.setTabEnabled(i, True)
        bt.setStyleSheet(new_style)
        bt.setChecked(False)
        bt.setCheckable(True)

    def AI_style_change(self, checked):
        current_style = self.sender().styleSheet()
        if checked:
            new_style = f"{current_style} QPushButton {{ background-color: #c23616; color:white}}"
            self.sender().setStyleSheet(new_style)
            # 禁用剩余的按钮
            for item in all_data["AI"]["control_button"]:
                name=all_data["AI"]["control_button"][item]
                button = getattr(self, all_data["AI"]["control_button"][item])
                if button != self.sender():
                    button.setCheckable(False)
            # 禁用所有标签页
            for i in range(self.auto_tabWidget.count()):
                if i==4:
                    continue
                self.auto_tabWidget.setTabEnabled(i, False)
            self.test_auto_treeWidget.setEnabled(False)
        else:
            new_style = f"{current_style} QPushButton {{ background-color: transparent; }}"
            for item in all_data["AI"]["control_button"]:
                button = getattr(self, all_data["AI"]["control_button"][item])
                button.setCheckable(True)
            # 禁用所有标签页
            for i in range(self.auto_tabWidget.count()):
                self.auto_tabWidget.setTabEnabled(i, True)
                self.test_auto_treeWidget.setEnabled(True)
        self.sender().setStyleSheet(new_style)
    # 设置TEST ON按钮点击切换文本、颜色

    # ------------以下仅是对AIbutton进行button绑定，DI、DO的button绑定已通过槽绑定
    def button_init(self):
        for item in all_data["AI"]["control_button"]:
            button=getattr(self,all_data["AI"]["control_button"][item])
            button.toggled.connect(self.AI_style_change)
            button.setEnabled(True)
            button.setCheckable(True)
    def sends_style_change(self):
        pass
    def DI_style_change(self):
        pass

    def DO_style_change(self):
        pass



    def AO_style_change(self):
        pass

    def carProtect_style_change(self):
        pass

    def on_click_tabChange(self):
        self.tab_name=tab_change[self.auto_tabWidget.currentIndex()][0]
        print(self.tab_name)

    def power_on_style(self,checked):
        print("have get into"+str(checked))
        current_style = self.sender().styleSheet()
        if checked:
                new_style = f"{current_style} QPushButton {{ background-color: red; color:white}}"
                self.sender().setText('Output\nON')
                self.sender().setStyleSheet(new_style)

        else:
                self.sender().setText('Output\nOFF')
                new_style = f"{current_style} QPushButton {{ background-color: white; color:black}}"
                self.button_click = False
        self.sender().setStyleSheet(new_style)

    def on_clicked_pb_115_test(self):
        current_style = self.sender().styleSheet()
        if not self.button_click:
            if self.sender().isChecked():
                # self.sender().setChecked(True)
                new_style = f"{current_style} QPushButton {{ background-color: red; color:white}}"

                # self.sender().setStyleSheet("QPushButton{\n"
                #               "        background-color: #ff6345;\n"
                #               "}\n")
                self.sender().setText('Output\nON')
                self.button_click = True
            else:
                print("no clicked")
        else:
            self.sender().setText('Output\nOFF')
            new_style = f"{current_style} QPushButton {{ background-color: white; color:black}}"
            self.button_click = False
        self.sender().setStyleSheet(new_style)

    # 开关按钮
    def switch(self):
        # print(self.sender().isChecked())
        if self.sender().isChecked():
            self.sender().setText('地')
            self.sender().setStyleSheet(
                'QPushButton{text-align : right;background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, '
                'stop:0 green, stop:0.495 green, stop:0.505 white,'
                ' stop:1 white);color:black;font:14pt "Arial";border:3px solid rgb(29,63,91);'
                'border-radius:10px;padding-right:15px;padding-left:20px;padding-top:5px;padding-bottom:5px;}QPushButton:pressed{color:rgb(85, 170, 255);}')

        else:
            self.sender().setText('开')
            self.sender().setStyleSheet(
                'QPushButton{text-align : left;background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, '
                'stop:0 white, stop:0.495 white, stop:0.505 red, '
                'stop:1 red);color:black;font: 14pt "Arial";border:3px solid rgb(29,63,91);'
                'border-radius:10px;padding-right:15px;padding-left:20px;padding-top:5px;padding-bottom:5px;}QPushButton:pressed{color:rgb(85, 170, 255);}')

    def switch28(self):
        # print(self.sender().text())
        if self.sender().isChecked():
            self.sender().setText('28V')
            self.sender().setStyleSheet(
                'QPushButton{text-align : right;background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, '
                'stop:0 green, stop:0.495 green, stop:0.505 white,'
                ' stop:1 white);color:black;font:14pt "Arial";border:3px solid rgb(29,63,91);'
                'border-radius:10px;padding-right:5px;padding-left:15px;padding-top:5px;padding-bottom:5px;}QPushButton:pressed{color:rgb(85, 170, 255);}')

        else:
            self.sender().setText('开')
            # print(self.sender().text())
            self.sender().setStyleSheet(
                'QPushButton{text-align : left;background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, '
                'stop:0 white, stop:0.495 white, stop:0.505 red, '
                'stop:1 red);color:black;font: 14pt "Arial";border:3px solid rgb(29,63,91);'
                'border-radius:10px;padding-right:15px;padding-left:20px;padding-top:5px;padding-bottom:5px;}QPushButton:pressed{color:rgb(85, 170, 255);}')

    def clickedToTabWidget(self):
        # 获取父节点的序号，发送给tab控件
        # item = self.test_treeWidget.currentIndex()
        # self.tabWidget.setCurrentIndex(item.parent().row())
        # 获取当前点击节点的第一列内容
        txt = self.test_auto_treeWidget.currentItem().text(0)
        # print(txt)
        # 点击的是父节点，则直接按自己的序号完成跳转
        if txt in ["控制指令测试", "离散量输入测试", "离散量输出驱动测试", "模拟量输入测试", "模拟量输出测试", "超转保护与停车测试"]:
            fatherItem = self.test_auto_treeWidget.currentIndex()
            self.auto_tabWidget.setCurrentIndex(fatherItem.row())
        # 对子节点，获取父节点序号后完成跳转
        else:
            childItem = self.test_auto_treeWidget.currentIndex().parent()
            self.auto_tabWidget.setCurrentIndex(childItem.row())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ManualTest = ManualTestWindow()
    ManualTest.show()
    sys.exit(app.exec_())
