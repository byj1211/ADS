# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_UserMainMenus.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1187, 741)
        MainWindow.setStyleSheet("background-color: rgb(58, 58,58);\n"
"QLineEdit{\n"
"    color:white;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1181, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lb_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_title.setStyleSheet("font-family:Arial;\n"
"                                            font-size:50px;\n"
"                                            background-color:rgb(0,0,0);\n"
"                                            color:rgb(255, 255, 255);\n"
"                                            padding:30px;\n"
"                                            border-radius:10px;\n"
"                                        ")
        self.lb_title.setObjectName("lb_title")
        self.horizontalLayout_2.addWidget(self.lb_title)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.lb_subtitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_subtitle.setStyleSheet("color: #ffffff;\n"
"                                            background-color: rgb(40,40, 60);\n"
"                                            border-radius:5px;\n"
"                                            text-align:center;\n"
"                                            font-size:40px;\n"
"                                            font-family:Arial;\n"
"                                            padding: 5px;\n"
"                                            width:200px;\n"
"                                            border-radius:10px;\n"
"                                        ")
        self.lb_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_subtitle.setObjectName("lb_subtitle")
        self.horizontalLayout_2.addWidget(self.lb_subtitle)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 6)
        self.horizontalLayout_2.setStretch(4, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pb_inspectProtect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_inspectProtect.setStyleSheet("QPushButton{\n"
"                                            color: #ffffff;\n"
"                                            background-color: rgb(0,0, 0);\n"
"                                            border-radius:5px;\n"
"                                            text-align:center;\n"
"                                            font-size:18pt;\n"
"                                            font-family:Arial;\n"
"                                            border:2px solid rgb(67,83,140);\n"
"                                            height:400px;\n"
"                                            }\n"
"                                            QPushButton:hover{\n"
"                                            font-size:20pt;\n"
"                                            font-weight:bold;\n"
"                                            border-width:4px;\n"
"                                            border-radius:10px;\n"
"                                            }\n"
"                                            QPushButton:disabled {\n"
"                                            background-color:rgb(205,205,205);\n"
"                                            color:rgb(0,0,0);\n"
"                                            }\n"
"                                        ")
        self.pb_inspectProtect.setObjectName("pb_inspectProtect")
        self.horizontalLayout.addWidget(self.pb_inspectProtect)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.pb_autoTest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_autoTest.setEnabled(True)
        self.pb_autoTest.setStyleSheet("QPushButton{\n"
"                                            color: #ffffff;\n"
"                                            background-color: rgb(0,0, 0);\n"
"                                            border-radius:5px;\n"
"                                            text-align:center;\n"
"                                            font-size:18pt;\n"
"                                            font-family:Arial;\n"
"                                            border:2px solid rgb(67,83,140);\n"
"                                            height:400px;\n"
"                                            }\n"
"                                            QPushButton:hover{\n"
"                                            font-size:20pt;\n"
"                                            font-weight:bold;\n"
"                                            border-width:4px;\n"
"                                            border-radius:10px;\n"
"                                            }\n"
"                                            QPushButton:disabled {\n"
"                                            background-color:rgb(205,205,205);\n"
"                                            color:rgb(0,0,0);\n"
"                                            }\n"
"                                        ")
        self.pb_autoTest.setDefault(False)
        self.pb_autoTest.setObjectName("pb_autoTest")
        self.horizontalLayout.addWidget(self.pb_autoTest)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.pb_manualTest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_manualTest.setEnabled(True)
        self.pb_manualTest.setStyleSheet("QPushButton{\n"
"                                            color: #ffffff;\n"
"                                            background-color: rgb(0,0, 0);\n"
"                                            border-radius:5px;\n"
"                                            text-align:center;\n"
"                                            font-size:18pt;\n"
"                                            font-family:Arial;\n"
"                                            border:2px solid rgb(67,83,140);\n"
"                                            height:400px;\n"
"                                            }\n"
"                                            QPushButton:hover{\n"
"                                            font-size:20pt;\n"
"                                            font-weight:bold;\n"
"                                            border-width:4px;\n"
"                                            border-radius:10px;\n"
"                                            }\n"
"                                            QPushButton:disabled {\n"
"                                            background-color:rgb(205,205,205);\n"
"                                            color:rgb(0,0,0);\n"
"\n"
"                                            }\n"
"                                        ")
        self.pb_manualTest.setObjectName("pb_manualTest")
        self.horizontalLayout.addWidget(self.pb_manualTest)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.pb_testReport = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_testReport.setEnabled(True)
        self.pb_testReport.setStyleSheet("QPushButton{\n"
"                                            color: #ffffff;\n"
"                                            background-color: rgb(0,0, 0);\n"
"                                            border-radius:5px;\n"
"                                            text-align:center;\n"
"                                            font-size:18pt;\n"
"                                            font-family:Arial;\n"
"                                            border:2px solid rgb(67,83,140);\n"
"                                            height:400px;\n"
"                                            }\n"
"                                            QPushButton:hover{\n"
"                                            font-size:20pt;\n"
"                                            font-weight:bold;\n"
"                                            border-width:4px;\n"
"                                            border-radius:10px;\n"
"                                            }\n"
"                                            QPushButton:disabled {\n"
"                                            background-color:rgb(205,205,205);\n"
"                                            color:rgb(0,0,0);\n"
"                                            }\n"
"                                        ")
        self.pb_testReport.setObjectName("pb_testReport")
        self.horizontalLayout.addWidget(self.pb_testReport)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 2)
        self.horizontalLayout.setStretch(8, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("background-color:rgb(0,0,0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pb_inspectProtect.clicked.connect(MainWindow.on_clicked_pb_inspectProtect) # type: ignore
        self.pb_autoTest.clicked.connect(MainWindow.on_clicked_autoTest) # type: ignore
        self.pb_manualTest.clicked.connect(MainWindow.on_clicked_manualTest) # type: ignore
        self.pb_testReport.clicked.connect(MainWindow.on_clicked_pb_testReport) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户界面"))
        self.lb_title.setText(_translate("MainWindow", "辅助动力装置电子控制试验主菜单"))
        self.lb_subtitle.setText(_translate("MainWindow", "用户"))
        self.pb_inspectProtect.setText(_translate("MainWindow", "设备自检\n"
"&&\n"
"保护设定\n"
" "))
        self.pb_autoTest.setText(_translate("MainWindow", "硬件\n"
"自动测试"))
        self.pb_manualTest.setText(_translate("MainWindow", "手动测试"))
        self.pb_testReport.setText(_translate("MainWindow", "测试报告"))
