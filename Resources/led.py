# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         自定义圆形指示灯控件
# Description:
# Author:       lgk
# Date:         2018/7/05
#-------------------------------------------------------------------------------

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QAbstractButton, QSpinBox, QColorDialog, QFrame, QVBoxLayout, QPushButton, \
    QGroupBox, QGridLayout, QLabel, QMainWindow, QSizePolicy, QHBoxLayout, QSplitter

allAttributes =   [  'colorOnBegin', 'colorOnEnd', 'colorOffBegin', 'colorOffEnd', 'colorBorderIn', 'colorBorderOut',
                     'radiusBorderOut', 'radiusBorderIn', 'radiusCircle']
allDefaultVal =   [ QColor(0, 240, 0), QColor(0, 160, 0), QColor(0, 68, 0), QColor(0, 28, 0), QColor(140, 140, 140), QColor(100, 100, 100),
                    500, 450, 400]
allLabelNames =   [ u'灯亮圆心颜色：', u'灯亮边缘颜色：', u'灯灭圆心颜色：', u'灯灭边缘颜色：', u'边框内测颜色：', u'边框外侧颜色：',
                    u'边框外侧半径：', u'边框内侧半径：', u'中间圆灯半径：']

class MyLed(QAbstractButton):
    def __init__(self, parent=None):
        super(MyLed, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setMinimumSize(24, 24)
        self.setCheckable(True)
        self.scaledSize = 1000.0    #为方便计算，将窗口短边值映射为1000
        self.setLedDefaultOption()

    def setLedDefaultOption(self):
        for attr, val in zip(allAttributes, allDefaultVal):
            setattr(self, attr, val)
        self.update()

    def setLedOption(self, opt='colorOnBegin', val=QColor(0,240,0)):
        if hasattr(self, opt):
            setattr(self, opt, val)
            self.update()

    def resizeEvent(self, evt):
        self.update()

    def paintEvent(self, evt):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(Qt.black, 1))

        realSize = min(self.width(), self.height())                         #窗口的短边
        painter.translate(self.width()/2.0, self.height()/2.0)              #原点平移到窗口中心
        painter.scale(realSize/self.scaledSize, realSize/self.scaledSize)   #缩放，窗口的短边值映射为self.scaledSize
        gradient = QRadialGradient(QPointF(0, 0), self.scaledSize/2.0, QPointF(0, 0))   #辐射渐变

        #画边框外圈和内圈
        for color, radius in [(self.colorBorderOut, self.radiusBorderOut),  #边框外圈
                               (self.colorBorderIn, self.radiusBorderIn)]:   #边框内圈
            gradient.setColorAt(1, color)
            painter.setBrush(QBrush(gradient))
            painter.drawEllipse(QPointF(0, 0), radius, radius)

        # 画内圆
        gradient.setColorAt(0, self.colorOnBegin if self.isChecked() else self.colorOffBegin)
        gradient.setColorAt(1, self.colorOnEnd if self.isChecked() else self.colorOffEnd)
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(QPointF(0, 0), self.radiusCircle, self.radiusCircle)

class MyColorBox(QFrame):
    sigColorChanged = pyqtSignal(QColor)
    def __init__(self, parent=None, height=20, color=QColor(0,240,0)):
        super(MyColorBox, self).__init__(parent)
        self.setFixedHeight(height)
        self.setAutoFillBackground(True)
        self.setPalette(QPalette(color))
        self.setFrameStyle(QFrame.Panel | QFrame.Sunken)

    def mousePressEvent(self, *args, **kwargs):
        color = QColorDialog.getColor(initial=self.palette().color(QPalette.Window))
        if color.isValid():
            self.setPalette(QPalette(color))
            self.sigColorChanged.emit(color)

    def setColor(self, color):
        self.setPalette(QPalette(color))

class MyRadiusCtrl(QSpinBox):
    def __init__(self, parent=None, initVal=500):
        super(MyRadiusCtrl, self).__init__(parent)
        self.setRange(1, 500)
        self.setValue(initVal)

class ConfigWnd(QFrame):
    def __init__(self, parent=None):
        super(ConfigWnd, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setFrameStyle(QFrame.Box|QFrame.Sunken)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.createColorParaGroupBox(), 0)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(self.createRadiusParaGroupBox(), 0)
        mainLayout.addStretch()
        mainLayout.addSpacing(20)
        self.restoreDefaultBtn = QPushButton(u'恢复默认设置')
        mainLayout.addWidget(self.restoreDefaultBtn, 0)
        mainLayout.addSpacing(10)
        self.animateBtn = QPushButton(u'开始动画')
        self.animateBtn.setCheckable(True)
        mainLayout.addWidget(self.animateBtn, 0)

    def createColorParaGroupBox(self):
        colorParaGroupBox = QGroupBox(u"颜色参数设置", self)
        layout = QGridLayout(colorParaGroupBox)
        layout.setSpacing(10)

        self.allColorBoxCtrls = []
        for name, color, row in zip(allLabelNames[:6], allDefaultVal[:6], range(6)):
            layout.addWidget(QLabel(name), row, 0)
            colorBox = MyColorBox(color=color)
            layout.addWidget(colorBox, row, 1)
            self.allColorBoxCtrls.append(colorBox)

        layout.setColumnStretch(0, 0)
        layout.setColumnStretch(1, 1)
        return colorParaGroupBox

    def createRadiusParaGroupBox(self):
        radiusParaGroupBox = QGroupBox(u"半径设置（1～500）", self)
        layout = QGridLayout(radiusParaGroupBox)
        layout.setSpacing(10)

        self.allRadiusCtrls = []
        for name, radius, row in zip(allLabelNames[6:], allDefaultVal[6:], range(3)):
            layout.addWidget(QLabel(name), row, 0)
            radiusCtrl = MyRadiusCtrl(initVal=radius)
            layout.addWidget(radiusCtrl, row, 1)
            self.allRadiusCtrls.append(radiusCtrl)

        layout.setColumnStretch(0, 0)
        layout.setColumnStretch(1, 1)
        return radiusParaGroupBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.initSlotFunc()
        self.cnt = 0
        self.show()

    def initUI(self):
        self.resize(580, 350)
        self.setWindowTitle(u'自定义圆形指示灯控件')

        mainSplitter = self.createSplitter(style=Qt.Horizontal, parent=self, width=4)

        self.configWnd = ConfigWnd(mainSplitter)

        rightSplitter = self.createSplitter(style=Qt.Vertical, parent=mainSplitter, width=4)

        rightTopWnd = self.createSubWnd(rightSplitter)
        rightTopLayout = QVBoxLayout(rightTopWnd)
        rightTopLayout.setContentsMargins(60, 60, 60, 60)
        self.ledSingle = MyLed()
        self.ledSingle.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        rightTopLayout.addWidget(self.ledSingle)

        rightBottomWnd = self.createSubWnd(rightSplitter)
        rightBottomLayout = QHBoxLayout(rightBottomWnd)
        rightBottomLayout.setContentsMargins(10, 10, 10, 10)
        self.ledGroup = []
        for i in range(8):
            led = MyLed()
            led.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.ledGroup.append(led)
            rightBottomLayout.addWidget(led)

        self.setSplitterStrechFactor(rightSplitter, 1, 0)
        self.setSplitterStrechFactor(mainSplitter, 0, 1)
        self.setCentralWidget(mainSplitter)

    def createSplitter(self, style=Qt.Horizontal, parent=None, width=3):
        splitter = QSplitter(style, parent)
        splitter.setHandleWidth(width)
        return splitter

    def setSplitterStrechFactor(self, splitter=None, factor1=1, factor2=1): #设置分割条两部分的比例
        splitter.setStretchFactor(0, factor1)
        splitter.setStretchFactor(1, factor2)

    def createSubWnd(self, parent=None):
        wnd = QFrame(parent)
        wnd.setFrameStyle(QFrame.Box | QFrame.Sunken)
        return wnd

    def initSlotFunc(self):
        self.configWnd.restoreDefaultBtn.clicked.connect(self.slotRestoreDefault)
        map(lambda x: x.sigColorChanged.connect(self.slotattributeChanged), self.configWnd.allColorBoxCtrls)   #设定每个颜色控件的槽函数
        map(lambda x: x.valueChanged.connect(self.slotattributeChanged), self.configWnd.allRadiusCtrls)        #设定每个半径控件的槽函数
        self.configWnd.animateBtn.clicked.connect(self.slotAnimation)
        self.timer = QTimer()
        self.timer.timeout.connect(self.slotTimeout) #动画定时器

    def slotattributeChanged(self, val):
        allCtrls = self.configWnd.allColorBoxCtrls + self.configWnd.allRadiusCtrls
        idx = allCtrls.index(self.sender())
        self.ledSingle.setLedOption(allAttributes[idx], val)

    def slotRestoreDefault(self):
        for colorBox, val in zip(self.configWnd.allColorBoxCtrls, allDefaultVal[:6]):
            colorBox.setColor(val)

        for radiusCtrl, val in zip(self.configWnd.allRadiusCtrls, allDefaultVal[6:]):
            radiusCtrl.setValue(val)

        self.ledSingle.setLedDefaultOption()

    def slotAnimation(self):
        if self.configWnd.animateBtn.isChecked():
            self.cnt = 0
            self.configWnd.animateBtn.setText(u'停止动画')
            self.timer.start(300)
        else:
            self.configWnd.animateBtn.setText(u'开始动画')
            self.timer.stop()

    def slotTimeout(self):
        self.cnt = self.cnt % 256
        ledBits = QString('%1').arg(self.cnt, 8, 2, fillChar=QChar('0'))    #将数值转换为二进制字符串
        for ledBit, led in zip(ledBits, self.ledGroup):
            led.setChecked(ledBit=='1')
        self.cnt += 1

def main():
    app = QApplication(sys.argv)
    mainWnd = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()