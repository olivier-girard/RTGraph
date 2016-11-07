# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LiveWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1348, 920)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet(_fromUtf8("\n"
"/*\n"
"    Android Material Dark\n"
"    COLOR_DARK     = #212121 Grey 900\n"
"    COLOR_MEDIUM   = #424242 Grey 800\n"
"    COLOR_MEDLIGHT = #757575 Grey 600\n"
"    COLOR_LIGHT    = #DDDDDD White\n"
"    COLOR_ACCENT   = #3F51B5 Indigo 500\n"
"*/\n"
"\n"
"* {\n"
"    background:qlineargradient(spread:pad, x1:0.517, y1:0.25, x2:1, y2:1, stop:0.211207 rgba(0, 0, 0, 255), stop:0.456897 rgba(39, 103, 106, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #757575;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3F51B5;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #757575;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
"    border: 1px solid #757575;\n"
"    background: #757575;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -7px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: 1px solid #757575;\n"
"    background: #212121;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 32px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 32px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #424242;\n"
"    border: 1px solid #757575;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border-width: 0px 1px 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-width: 1px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background:#424242;\n"
"    border: 1px solid #757575;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    position: absolute;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    left: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    top: 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: top left;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"}\n"
"\n"
"QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"    border: 1px solid #757575;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"    background: #424242;\n"
"}\n"
"\n"
"QAbstractButton:pressed {\n"
"    background: #757575;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    show-decoration-selected: 1;\n"
"    selection-background-color: #3F51B5;\n"
"    selection-color: #DDDDDD;\n"
"    alternate-background-color: #424242;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: 1px solid #757575;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #212121;\n"
"    border: 1px solid #757575;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QHeaderView::section:selected, QHeaderView::section::checked {\n"
"    background: #424242;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #757575;\n"
"}\n"
"\n"
"QTabBar {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #424242;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 1px solid #757575;\n"
"    background: #424242;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #757575;\n"
"    background: #424242;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #757575;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
"    border: 1px solid #757575;\n"
"    background: #424242;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #757575;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #757575;\n"
"    background: #424242;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
"    background: #3F51B5;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
"    background: #424242;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 1px;\n"
"    background-color: #3F51B5;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #424242;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    border: 1px;\n"
"    color: #3F51B5;\n"
"}"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.EnergieDep = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EnergieDep.setFont(font)
        self.EnergieDep.setObjectName(_fromUtf8("EnergieDep"))
        self.gridLayout_2.addWidget(self.EnergieDep, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.EventType = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.EventType.setFont(font)
        self.EventType.setObjectName(_fromUtf8("EventType"))
        self.gridLayout_2.addWidget(self.EventType, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.display = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        self.display.setMinimumSize(QtCore.QSize(1330, 0))
        self.display.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.display.setFont(font)
        self.display.setStyleSheet(_fromUtf8("QTabWidget::tab-bar {\n"
"left:0px;\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"\n"
"QTabBar::tab:selected {\n"
"border-color: rgb(77, 77, 77);\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 5px solid qlineargradient(spread:pad, x1:0.176, y1:1, x2:0.797, y2:1, stop:0 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:1 rgba(137, 108, 26, 255));\n"
"border-bottom:5px solid qlineargradient(spread:pad, x1:0.176, y1:1, x2:0.797, y2:1, stop:0 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:1 rgba(137, 108, 26, 255));\n"
"border-left:5px solid qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:1 rgba(137, 108, 26, 255));\n"
"border-right:5px solid qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:1 rgba(137, 108, 26, 255)) ;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"background:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 148, 114, 69), stop:0.375 rgba(0, 0, 0, 255), stop:0.452889 rgba(71, 72, 0, 145), stop:0.466983 rgba(1, 128, 99, 228), stop:0.503158 rgba(72, 69, 20, 130), stop:0.505423 rgba(72, 61, 20, 130), stop:0.55 rgba(72, 72, 0, 255), stop:0.668103 rgba(0, 0, 0, 255), stop:0.685345 rgba(72, 72, 0, 69), stop:0.905172 rgba(72, 57, 0, 130));\n"
"border: 3px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-right-radius: 40px;\n"
"min-width: 33ex;\n"
"padding: 10px;\n"
"color:rgb(0, 0, 0);\n"
"}"))
        self.display.setIconSize(QtCore.QSize(16, 16))
        self.display.setUsesScrollButtons(True)
        self.display.setDocumentMode(False)
        self.display.setTabsClosable(False)
        self.display.setMovable(False)
        self.display.setObjectName(_fromUtf8("display"))
        self.tracker = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracker.sizePolicy().hasHeightForWidth())
        self.tracker.setSizePolicy(sizePolicy)
        self.tracker.setMinimumSize(QtCore.QSize(1318, 0))
        self.tracker.setObjectName(_fromUtf8("tracker"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tracker)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.plttracker = GraphicsLayoutWidget(self.tracker)
        self.plttracker.setMinimumSize(QtCore.QSize(1040, 0))
        self.plttracker.setObjectName(_fromUtf8("plttracker"))
        self.gridLayout_5.addWidget(self.plttracker, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.display.addTab(self.tracker, _fromUtf8(""))
        self.threed = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threed.sizePolicy().hasHeightForWidth())
        self.threed.setSizePolicy(sizePolicy)
        self.threed.setMinimumSize(QtCore.QSize(1318, 0))
        self.threed.setObjectName(_fromUtf8("threed"))
        self.gridLayout_4 = QtGui.QGridLayout(self.threed)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.plt3d = GLViewWidget(self.threed)
        self.plt3d.setObjectName(_fromUtf8("plt3d"))
        self.gridLayout_4.addWidget(self.plt3d, 0, 0, 1, 1)
        self.display.addTab(self.threed, _fromUtf8(""))
        self.histogram = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram.sizePolicy().hasHeightForWidth())
        self.histogram.setSizePolicy(sizePolicy)
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.gridLayout_8 = QtGui.QGridLayout(self.histogram)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.plthistogram = GraphicsLayoutWidget(self.histogram)
        self.plthistogram.setObjectName(_fromUtf8("plthistogram"))
        self.gridLayout_7.addWidget(self.plthistogram, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.display.addTab(self.histogram, _fromUtf8(""))
        self.frequency = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequency.sizePolicy().hasHeightForWidth())
        self.frequency.setSizePolicy(sizePolicy)
        self.frequency.setObjectName(_fromUtf8("frequency"))
        self.gridLayout_10 = QtGui.QGridLayout(self.frequency)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.pltfrequency = GraphicsLayoutWidget(self.frequency)
        self.pltfrequency.setObjectName(_fromUtf8("pltfrequency"))
        self.gridLayout_9.addWidget(self.pltfrequency, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.display.addTab(self.frequency, _fromUtf8(""))
        self.channel = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channel.sizePolicy().hasHeightForWidth())
        self.channel.setSizePolicy(sizePolicy)
        self.channel.setObjectName(_fromUtf8("channel"))
        self.gridLayout_12 = QtGui.QGridLayout(self.channel)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.pltchannel = GraphicsLayoutWidget(self.channel)
        self.pltchannel.setObjectName(_fromUtf8("pltchannel"))
        self.gridLayout_11.addWidget(self.pltchannel, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.display.addTab(self.channel, _fromUtf8(""))
        self.Integration_tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Integration_tab.sizePolicy().hasHeightForWidth())
        self.Integration_tab.setSizePolicy(sizePolicy)
        self.Integration_tab.setObjectName(_fromUtf8("Integration_tab"))
        self.gridLayout_13 = QtGui.QGridLayout(self.Integration_tab)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.integview = GraphicsLayoutWidget(self.Integration_tab)
        self.integview.setObjectName(_fromUtf8("integview"))
        self.gridLayout_3.addWidget(self.integview, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.display.addTab(self.Integration_tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.display, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAll_pannel = QtGui.QAction(MainWindow)
        self.actionAll_pannel.setCheckable(False)
        self.actionAll_pannel.setEnabled(True)
        self.actionAll_pannel.setObjectName(_fromUtf8("actionAll_pannel"))
        self.actionHistogram = QtGui.QAction(MainWindow)
        self.actionHistogram.setObjectName(_fromUtf8("actionHistogram"))
        self.actionTracker = QtGui.QAction(MainWindow)
        self.actionTracker.setObjectName(_fromUtf8("actionTracker"))
        self.actionChannels = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionChannels.setFont(font)
        self.actionChannels.setObjectName(_fromUtf8("actionChannels"))
        self.actionAll = QtGui.QAction(MainWindow)
        self.actionAll.setObjectName(_fromUtf8("actionAll"))

        self.retranslateUi(MainWindow)
        self.display.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Live Window", None))
        self.EnergieDep.setText(_translate("MainWindow", "0", None))
        self.label.setText(_translate("MainWindow", "Energie deposit:  ", None))
        self.label_2.setText(_translate("MainWindow", "Event type:  ", None))
        self.EventType.setText(_translate("MainWindow", "TextLabel", None))
        self.display.setTabText(self.display.indexOf(self.tracker), _translate("MainWindow", "2D track", None))
        self.display.setTabText(self.display.indexOf(self.threed), _translate("MainWindow", "3D track", None))
        self.display.setTabText(self.display.indexOf(self.histogram), _translate("MainWindow", "Angle", None))
        self.display.setTabText(self.display.indexOf(self.frequency), _translate("MainWindow", "Frequency", None))
        self.display.setTabText(self.display.indexOf(self.channel), _translate("MainWindow", "Channel", None))
        self.display.setTabText(self.display.indexOf(self.Integration_tab), _translate("MainWindow", "Integration", None))
        self.actionAll_pannel.setText(_translate("MainWindow", "All pannel", None))
        self.actionHistogram.setText(_translate("MainWindow", "Histogram", None))
        self.actionTracker.setText(_translate("MainWindow", "Tracker", None))
        self.actionChannels.setText(_translate("MainWindow", "Channels", None))
        self.actionAll.setText(_translate("MainWindow", "All", None))

from pyqtgraph import GraphicsLayoutWidget
from pyqtgraph.opengl import GLViewWidget
