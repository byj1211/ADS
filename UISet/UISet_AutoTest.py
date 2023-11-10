import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.py.UI_AutoTest import Ui_MainWindow


class AutoTestWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AutoTestWindow, self).__init__(parent)
        # self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)  # 设置无法修改大小
        self.setupUi(self)  # 设置UI
        # 全屏显示
        self.showMaximized()

        # 隐藏send按钮
        self.pb_auto_con_insSend.setVisible(False)
        self.pb_auto_di_insSend.setVisible(False)
        self.pb_auto_do_insSend.setVisible(False)
        self.pb_auto_ai_insSend.setVisible(False)
        self.pte_auto_ao_insSend.setVisible(False)
        self.pte_auto_op_insSend.setVisible(False)

        # 启动器绑定事件
        # self.pb_auto_di_28VKIN5_1.clicked.connect(self.choose)
        # print(self.pb_auto_di_28VKIN5_1.isChecked())
        # self.pb_auto_di_28VKIN5_2.clicked.connect(self.choose)
        # self.pb_auto_di_28VDIN2_1.clicked.connect(self.choose)
        # self.pb_auto_di_28VDIN2_2.clicked.connect(self.choose)

        # 启动器默认为开
        self.pb_auto_di_28VKIN5_2.click()
        self.pb_auto_di_28VDIN2_2.click()

        # 下拉框文本居中
        # self.cm_auto_ai_AIN_PT100_1.lineEdit().setAlignment(Qt.AlignCenter)
        # self.cm_auto_ai_AIN_PT100_2.lineEdit().setAlignment(Qt.AlignCenter)
        # self.cm_auto_ai_AIN_PT100_3.lineEdit().setAlignment(Qt.AlignCenter)
        # self.cm_auto_ai_AIN_CTSENSOR.lineEdit().setAlignment(Qt.AlignCenter)

        # 设置控制测试表格的列宽
        self.auto_cor_ins_table.setColumnWidth(0, 100)
        self.auto_cor_ins_table.setColumnWidth(1, 400)
        self.auto_cor_ins_table.setColumnWidth(2, 600)
        self.auto_cor_ins_table.setColumnWidth(3, 240)
        # 设置树的列宽
        self.test_auto_treeWidget.setColumnWidth(0, 200)
        self.test_auto_treeWidget.setColumnWidth(1, 100)

        # 表格设置为只读
        for row in range(self.auto_cor_ins_table.rowCount()):
            for col in range(4):  # Columns 0 and 1
                item = self.auto_cor_ins_table.item(row, col)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    # 设置TEST ON按钮点击切换文本、颜色
    def on_clicked_pb_auto_test(self):
        if self.pb_auto_test.isChecked():
            self.pb_auto_test.setText('TEST\nOFF')
        else:
            self.pb_auto_test.setText('TEST\nON')

    #
    #     # # 启动器绑定事件pb_auto_di_28VKIN5
    #     self.pb_auto_di_28VKIN5_1.clicked.connect(self.choose)
    #     # self.pb_auto_di_28VKIN5_2.clicked.connect(self.choose)
    #     # self.pb_auto_di_28VDIN2_1.clicked.connect(self.choose)
    #     # self.pb_auto_di_28VDIN2_2.clicked.connect(self.choose)
    # def on_clicked_pb_auto_test(self):
    #     if self.sender().isChecked():
    #         self.sender().setText('TEST\nOFF')
    #     else:
    #         self.sender().setText('TEST\nON')

    # def choose(self):
    #     print(self.sender().isChecked())
    #     print("11")
    #     if self.sender().isChecked():
    #         self.sender().setText("123")
    #         # self.sender().setStyleSheet('QPushButton:checked{color:red;}')
    #     else:
    #         print("22")
    #         # self.sender().setText("为")
    #         # self.sender().setStyleSheet('QPushButton{color:white}')

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


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     AutoTestWindow = AutoTestWindow()
#     AutoTestWindow.show()
#     sys.exit(app.exec_())
