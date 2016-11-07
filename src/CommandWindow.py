# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CommandWindow.ui'
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

class Ui_CommandWindow(object):
    def setupUi(self, CommandWindow):
        CommandWindow.setObjectName(_fromUtf8("CommandWindow"))
        CommandWindow.resize(1333, 915)
        CommandWindow.setMinimumSize(QtCore.QSize(1333, 760))
        CommandWindow.setMaximumSize(QtCore.QSize(1333, 915))
        CommandWindow.setStyleSheet(_fromUtf8("\n"
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
"    color: #424242;\n"
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
"    background: orange;\n"
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
"QComboBox:editable {\n"
"    background: white;\n"
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
"    border: yes;\n"
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
"}\n"
"QPushButton {\n"
"    color: rgb(181, 206, 206);\n"
"    border-width: 2px;\n"
"    border-color:rgb(177, 173, 163);\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    border-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(CommandWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setText(_fromUtf8(""))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(1300, 700))
        self.frame.setMaximumSize(QtCore.QSize(1300, 700))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_25 = QtGui.QGridLayout(self.frame)
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.automatic_bt = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.automatic_bt.sizePolicy().hasHeightForWidth())
        self.automatic_bt.setSizePolicy(sizePolicy)
        self.automatic_bt.setMinimumSize(QtCore.QSize(50, 0))
        self.automatic_bt.setMaximumSize(QtCore.QSize(1280, 16777215))
        self.automatic_bt.setBaseSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.automatic_bt.setFont(font)
        self.automatic_bt.setObjectName(_fromUtf8("automatic_bt"))
        self.horizontalLayout_2.addWidget(self.automatic_bt)
        self.gridLayout_25.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.gridLayout_24 = QtGui.QGridLayout()
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_SensorPos = QtGui.QLineEdit(self.frame)
        self.lineEdit_SensorPos.setObjectName(_fromUtf8("lineEdit_SensorPos"))
        self.gridLayout.addWidget(self.lineEdit_SensorPos, 11, 2, 1, 6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_14 = QtGui.QLabel(self.frame)
        self.label_14.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout.addWidget(self.label_14)
        self.spinBox_Acq = QtGui.QSpinBox(self.frame)
        self.spinBox_Acq.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_Acq.setFont(font)
        self.spinBox_Acq.setMinimum(1)
        self.spinBox_Acq.setMaximum(10000)
        self.spinBox_Acq.setProperty("value", 100)
        self.spinBox_Acq.setObjectName(_fromUtf8("spinBox_Acq"))
        self.horizontalLayout.addWidget(self.spinBox_Acq)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.CurrentEven = QtGui.QLCDNumber(self.frame)
        self.CurrentEven.setMinimumSize(QtCore.QSize(181, 30))
        self.CurrentEven.setObjectName(_fromUtf8("CurrentEven"))
        self.gridLayout_5.addWidget(self.CurrentEven, 1, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
"\n"
""))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_5.addWidget(self.label_13, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 4, 2, 1, 1)
        self.btnSavedPause = QtGui.QPushButton(self.frame)
        self.btnSavedPause.setMinimumSize(QtCore.QSize(68, 60))
        self.btnSavedPause.setMaximumSize(QtCore.QSize(68, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnSavedPause.setFont(font)
        self.btnSavedPause.setStyleSheet(_fromUtf8("background-image:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/pause.png);"))
        self.btnSavedPause.setText(_fromUtf8(""))
        self.btnSavedPause.setObjectName(_fromUtf8("btnSavedPause"))
        self.gridLayout.addWidget(self.btnSavedPause, 2, 7, 1, 1)
        self.btnSavedLeft = QtGui.QPushButton(self.frame)
        self.btnSavedLeft.setMinimumSize(QtCore.QSize(70, 60))
        self.btnSavedLeft.setMaximumSize(QtCore.QSize(70, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnSavedLeft.setFont(font)
        self.btnSavedLeft.setStyleSheet(_fromUtf8("background:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/left.png);"))
        self.btnSavedLeft.setText(_fromUtf8(""))
        self.btnSavedLeft.setObjectName(_fromUtf8("btnSavedLeft"))
        self.gridLayout.addWidget(self.btnSavedLeft, 2, 8, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_7 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
"\n"
""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_8.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
"\n"
"\n"
""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_8.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_8.addWidget(self.label_11, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 5, 1, 1, 1)
        self.btnSavedRight = QtGui.QPushButton(self.frame)
        self.btnSavedRight.setMinimumSize(QtCore.QSize(68, 60))
        self.btnSavedRight.setMaximumSize(QtCore.QSize(68, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnSavedRight.setFont(font)
        self.btnSavedRight.setStyleSheet(_fromUtf8("background:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/right.png);"))
        self.btnSavedRight.setText(_fromUtf8(""))
        self.btnSavedRight.setObjectName(_fromUtf8("btnSavedRight"))
        self.gridLayout.addWidget(self.btnSavedRight, 2, 9, 1, 1)
        self.btnSavedStart = QtGui.QPushButton(self.frame)
        self.btnSavedStart.setMinimumSize(QtCore.QSize(70, 60))
        self.btnSavedStart.setMaximumSize(QtCore.QSize(70, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnSavedStart.setFont(font)
        self.btnSavedStart.setStyleSheet(_fromUtf8("background:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/played.png);"))
        self.btnSavedStart.setText(_fromUtf8(""))
        self.btnSavedStart.setObjectName(_fromUtf8("btnSavedStart"))
        self.gridLayout.addWidget(self.btnSavedStart, 2, 6, 1, 1)
        self.pushButton_LIVE = QtGui.QPushButton(self.frame)
        self.pushButton_LIVE.setMinimumSize(QtCore.QSize(100, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.310345, QtGui.QColor(156, 143, 137, 133))
        gradient.setColorAt(0.378572, QtGui.QColor(104, 117, 126, 145))
        gradient.setColorAt(0.392241, QtGui.QColor(135, 143, 88, 130))
        gradient.setColorAt(0.479796, QtGui.QColor(136, 129, 116, 208))
        gradient.setColorAt(0.537455, QtGui.QColor(185, 214, 223, 69))
        gradient.setColorAt(0.543862, QtGui.QColor(51, 38, 12, 69))
        gradient.setColorAt(0.592552, QtGui.QColor(52, 52, 52, 130))
        gradient.setColorAt(0.597677, QtGui.QColor(17, 42, 49))
        gradient.setColorAt(0.74569, QtGui.QColor(48, 48, 48, 69))
        gradient.setColorAt(0.891088, QtGui.QColor(101, 95, 60, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_LIVE.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_LIVE.setFont(font)
        self.pushButton_LIVE.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.pushButton_LIVE.setObjectName(_fromUtf8("pushButton_LIVE"))
        self.gridLayout.addWidget(self.pushButton_LIVE, 0, 2, 2, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
"\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 4, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_19 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
"\n"
""))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_6.addWidget(self.label_19, 0, 0, 1, 1)
        self.current_event = QtGui.QLCDNumber(self.frame)
        self.current_event.setObjectName(_fromUtf8("current_event"))
        self.gridLayout_6.addWidget(self.current_event, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 4, 5, 1, 5)
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setMinimumSize(QtCore.QSize(0, 10))
        self.line_2.setStyleSheet(_fromUtf8("background:qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0.0948276 rgba(136, 106, 22, 255), stop:0.185345 rgba(40, 5, 5, 255), stop:0.376179 rgba(223, 215, 102, 255), stop:0.399142 rgba(137, 108, 26, 255), stop:0.407725 rgba(204, 181, 74, 255), stop:0.420601 rgba(202, 174, 68, 255), stop:0.424893 rgba(166, 140, 41, 255), stop:0.429185 rgba(14, 14, 11, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.625 rgba(187, 156, 51, 255), stop:0.698276 rgba(168, 142, 42, 255), stop:0.814655 rgba(218, 202, 86, 255), stop:0.853448 rgba(208, 187, 73, 255), stop:0.931034 rgba(22, 26, 1, 255), stop:0.987069 rgba(187, 156, 51, 255));"))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 8, 1, 1, 9)
        self.sensorLoadbtn = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.sensorLoadbtn.setFont(font)
        self.sensorLoadbtn.setStyleSheet(_fromUtf8("background:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 148, 114, 69), stop:0.375 rgba(0, 0, 0, 255), stop:0.452889 rgba(71, 72, 0, 145), stop:0.466983 rgba(1, 128, 99, 228), stop:0.503158 rgba(72, 69, 20, 130), stop:0.505423 rgba(72, 61, 20, 130), stop:0.55 rgba(72, 72, 0, 255), stop:0.668103 rgba(0, 0, 0, 255), stop:0.685345 rgba(72, 72, 0, 69), stop:0.905172 rgba(72, 57, 0, 130));\n"
""))
        self.sensorLoadbtn.setObjectName(_fromUtf8("sensorLoadbtn"))
        self.gridLayout.addWidget(self.sensorLoadbtn, 11, 8, 1, 2)
        self.label_logo = QtGui.QLabel(self.frame)
        self.label_logo.setEnabled(True)
        self.label_logo.setMaximumSize(QtCore.QSize(16777215, 120000))
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))
        self.gridLayout.addWidget(self.label_logo, 0, 1, 4, 1)
        self.setupLoadbtn = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.setupLoadbtn.setFont(font)
        self.setupLoadbtn.setStyleSheet(_fromUtf8("background:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 148, 114, 69), stop:0.375 rgba(0, 0, 0, 255), stop:0.452889 rgba(71, 72, 0, 145), stop:0.466983 rgba(1, 128, 99, 228), stop:0.503158 rgba(72, 69, 20, 130), stop:0.505423 rgba(72, 61, 20, 130), stop:0.55 rgba(72, 72, 0, 255), stop:0.668103 rgba(0, 0, 0, 255), stop:0.685345 rgba(72, 72, 0, 69), stop:0.905172 rgba(72, 57, 0, 130));\n"
""))
        self.setupLoadbtn.setObjectName(_fromUtf8("setupLoadbtn"))
        self.gridLayout.addWidget(self.setupLoadbtn, 9, 8, 1, 2)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.radioButton_electron_sd = QtGui.QRadioButton(self.frame)
        self.radioButton_electron_sd.setText(_fromUtf8(""))
        self.radioButton_electron_sd.setAutoExclusive(True)
        self.radioButton_electron_sd.setObjectName(_fromUtf8("radioButton_electron_sd"))
        self.buttonGroup_2 = QtGui.QButtonGroup(CommandWindow)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.radioButton_electron_sd)
        self.gridLayout_4.addWidget(self.radioButton_electron_sd, 0, 1, 1, 1)
        self.radioButton_highelectron_sd = QtGui.QRadioButton(self.frame)
        self.radioButton_highelectron_sd.setText(_fromUtf8(""))
        self.radioButton_highelectron_sd.setAutoExclusive(True)
        self.radioButton_highelectron_sd.setObjectName(_fromUtf8("radioButton_highelectron_sd"))
        self.buttonGroup_2.addButton(self.radioButton_highelectron_sd)
        self.gridLayout_4.addWidget(self.radioButton_highelectron_sd, 3, 1, 1, 1)
        self.electron_Ind_sd = QtGui.QLCDNumber(self.frame)
        self.electron_Ind_sd.setStyleSheet(_fromUtf8(""))
        self.electron_Ind_sd.setObjectName(_fromUtf8("electron_Ind_sd"))
        self.gridLayout_4.addWidget(self.electron_Ind_sd, 0, 2, 1, 1)
        self.radioButton_All_sd = QtGui.QRadioButton(self.frame)
        self.radioButton_All_sd.setText(_fromUtf8(""))
        self.radioButton_All_sd.setAutoExclusive(True)
        self.radioButton_All_sd.setObjectName(_fromUtf8("radioButton_All_sd"))
        self.buttonGroup_2.addButton(self.radioButton_All_sd)
        self.gridLayout_4.addWidget(self.radioButton_All_sd, 4, 1, 1, 1)
        self.radioButton_muon_sd = QtGui.QRadioButton(self.frame)
        self.radioButton_muon_sd.setText(_fromUtf8(""))
        self.radioButton_muon_sd.setAutoExclusive(True)
        self.radioButton_muon_sd.setObjectName(_fromUtf8("radioButton_muon_sd"))
        self.buttonGroup_2.addButton(self.radioButton_muon_sd)
        self.gridLayout_4.addWidget(self.radioButton_muon_sd, 1, 1, 1, 1)
        self.radioButton_disintegration_sd = QtGui.QRadioButton(self.frame)
        self.radioButton_disintegration_sd.setText(_fromUtf8(""))
        self.radioButton_disintegration_sd.setAutoExclusive(True)
        self.radioButton_disintegration_sd.setObjectName(_fromUtf8("radioButton_disintegration_sd"))
        self.buttonGroup_2.addButton(self.radioButton_disintegration_sd)
        self.gridLayout_4.addWidget(self.radioButton_disintegration_sd, 2, 1, 1, 1)
        self.disintegration_Ind_sd = QtGui.QLCDNumber(self.frame)
        self.disintegration_Ind_sd.setObjectName(_fromUtf8("disintegration_Ind_sd"))
        self.gridLayout_4.addWidget(self.disintegration_Ind_sd, 2, 2, 1, 1)
        self.muon_Ind_sd = QtGui.QLCDNumber(self.frame)
        self.muon_Ind_sd.setObjectName(_fromUtf8("muon_Ind_sd"))
        self.gridLayout_4.addWidget(self.muon_Ind_sd, 1, 2, 1, 1)
        self.highelectron_Ind_sd = QtGui.QLCDNumber(self.frame)
        self.highelectron_Ind_sd.setObjectName(_fromUtf8("highelectron_Ind_sd"))
        self.gridLayout_4.addWidget(self.highelectron_Ind_sd, 3, 2, 1, 1)
        self.ALL_Ind_sd = QtGui.QLCDNumber(self.frame)
        self.ALL_Ind_sd.setObjectName(_fromUtf8("ALL_Ind_sd"))
        self.gridLayout_4.addWidget(self.ALL_Ind_sd, 4, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 5, 5, 1, 5)
        self.spinBox_Event = QtGui.QSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.spinBox_Event.setFont(font)
        self.spinBox_Event.setMinimum(1)
        self.spinBox_Event.setMaximum(10000000)
        self.spinBox_Event.setObjectName(_fromUtf8("spinBox_Event"))
        self.gridLayout.addWidget(self.spinBox_Event, 2, 5, 1, 1)
        self.lineEdit_SetupFile = QtGui.QLineEdit(self.frame)
        self.lineEdit_SetupFile.setObjectName(_fromUtf8("lineEdit_SetupFile"))
        self.gridLayout.addWidget(self.lineEdit_SetupFile, 9, 2, 1, 6)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.btnLivePause = QtGui.QPushButton(self.frame)
        self.btnLivePause.setMinimumSize(QtCore.QSize(68, 60))
        self.btnLivePause.setMaximumSize(QtCore.QSize(68, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnLivePause.setFont(font)
        self.btnLivePause.setStyleSheet(_fromUtf8("background-image:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img//pause.png);"))
        self.btnLivePause.setText(_fromUtf8(""))
        self.btnLivePause.setObjectName(_fromUtf8("btnLivePause"))
        self.gridLayout_7.addWidget(self.btnLivePause, 0, 1, 1, 1)
        self.btnLiveStart = QtGui.QPushButton(self.frame)
        self.btnLiveStart.setMinimumSize(QtCore.QSize(70, 60))
        self.btnLiveStart.setMaximumSize(QtCore.QSize(70, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnLiveStart.setFont(font)
        self.btnLiveStart.setStyleSheet(_fromUtf8("background:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/played.png);"))
        self.btnLiveStart.setText(_fromUtf8(""))
        self.btnLiveStart.setObjectName(_fromUtf8("btnLiveStart"))
        self.gridLayout_7.addWidget(self.btnLiveStart, 0, 0, 1, 1)
        self.btnLiveLeft = QtGui.QPushButton(self.frame)
        self.btnLiveLeft.setMinimumSize(QtCore.QSize(70, 60))
        self.btnLiveLeft.setMaximumSize(QtCore.QSize(70, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnLiveLeft.setFont(font)
        self.btnLiveLeft.setStyleSheet(_fromUtf8("background:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/left.png);"))
        self.btnLiveLeft.setText(_fromUtf8(""))
        self.btnLiveLeft.setObjectName(_fromUtf8("btnLiveLeft"))
        self.gridLayout_7.addWidget(self.btnLiveLeft, 0, 2, 1, 1)
        self.btnLiveRight = QtGui.QPushButton(self.frame)
        self.btnLiveRight.setMinimumSize(QtCore.QSize(68, 60))
        self.btnLiveRight.setMaximumSize(QtCore.QSize(68, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnLiveRight.setFont(font)
        self.btnLiveRight.setStyleSheet(_fromUtf8("background:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/right.png);"))
        self.btnLiveRight.setText(_fromUtf8(""))
        self.btnLiveRight.setObjectName(_fromUtf8("btnLiveRight"))
        self.gridLayout_7.addWidget(self.btnLiveRight, 0, 3, 1, 1)
        self.btnLiveStopacq = QtGui.QPushButton(self.frame)
        self.btnLiveStopacq.setMinimumSize(QtCore.QSize(68, 60))
        self.btnLiveStopacq.setMaximumSize(QtCore.QSize(68, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnLiveStopacq.setFont(font)
        self.btnLiveStopacq.setStyleSheet(_fromUtf8("background:url(/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/stop.png);"))
        self.btnLiveStopacq.setText(_fromUtf8(""))
        self.btnLiveStopacq.setObjectName(_fromUtf8("btnLiveStopacq"))
        self.gridLayout_7.addWidget(self.btnLiveStopacq, 0, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 2, 2, 1, 1)
        self.pushButton_SavedData = QtGui.QPushButton(self.frame)
        self.pushButton_SavedData.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_SavedData.setFont(font)
        self.pushButton_SavedData.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.pushButton_SavedData.setObjectName(_fromUtf8("pushButton_SavedData"))
        self.gridLayout.addWidget(self.pushButton_SavedData, 0, 4, 2, 7)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radioButton_highelectron = QtGui.QRadioButton(self.frame)
        self.radioButton_highelectron.setInputMethodHints(QtCore.Qt.ImhNone)
        self.radioButton_highelectron.setText(_fromUtf8(""))
        self.radioButton_highelectron.setAutoExclusive(True)
        self.radioButton_highelectron.setObjectName(_fromUtf8("radioButton_highelectron"))
        self.buttonGroup = QtGui.QButtonGroup(CommandWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButton_highelectron)
        self.gridLayout_3.addWidget(self.radioButton_highelectron, 3, 0, 1, 1)
        self.radioButton_muon = QtGui.QRadioButton(self.frame)
        self.radioButton_muon.setText(_fromUtf8(""))
        self.radioButton_muon.setAutoExclusive(True)
        self.radioButton_muon.setObjectName(_fromUtf8("radioButton_muon"))
        self.buttonGroup.addButton(self.radioButton_muon)
        self.gridLayout_3.addWidget(self.radioButton_muon, 1, 0, 1, 1)
        self.radioButton_All = QtGui.QRadioButton(self.frame)
        self.radioButton_All.setText(_fromUtf8(""))
        self.radioButton_All.setAutoExclusive(True)
        self.radioButton_All.setObjectName(_fromUtf8("radioButton_All"))
        self.buttonGroup.addButton(self.radioButton_All)
        self.gridLayout_3.addWidget(self.radioButton_All, 4, 0, 1, 1)
        self.ALL_Ind = QtGui.QLCDNumber(self.frame)
        self.ALL_Ind.setObjectName(_fromUtf8("ALL_Ind"))
        self.gridLayout_3.addWidget(self.ALL_Ind, 4, 2, 1, 1)
        self.radioButton_disintegration = QtGui.QRadioButton(self.frame)
        self.radioButton_disintegration.setText(_fromUtf8(""))
        self.radioButton_disintegration.setAutoExclusive(True)
        self.radioButton_disintegration.setObjectName(_fromUtf8("radioButton_disintegration"))
        self.buttonGroup.addButton(self.radioButton_disintegration)
        self.gridLayout_3.addWidget(self.radioButton_disintegration, 2, 0, 1, 1)
        self.disintegration_Ind = QtGui.QLCDNumber(self.frame)
        self.disintegration_Ind.setObjectName(_fromUtf8("disintegration_Ind"))
        self.gridLayout_3.addWidget(self.disintegration_Ind, 2, 2, 1, 1)
        self.electron_Ind = QtGui.QLCDNumber(self.frame)
        self.electron_Ind.setEnabled(True)
        self.electron_Ind.setStyleSheet(_fromUtf8(""))
        self.electron_Ind.setObjectName(_fromUtf8("electron_Ind"))
        self.gridLayout_3.addWidget(self.electron_Ind, 0, 2, 1, 1)
        self.muon_Ind = QtGui.QLCDNumber(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.muon_Ind.setFont(font)
        self.muon_Ind.setObjectName(_fromUtf8("muon_Ind"))
        self.gridLayout_3.addWidget(self.muon_Ind, 1, 2, 1, 1)
        self.highelectron_Ind = QtGui.QLCDNumber(self.frame)
        self.highelectron_Ind.setObjectName(_fromUtf8("highelectron_Ind"))
        self.gridLayout_3.addWidget(self.highelectron_Ind, 3, 2, 1, 1)
        self.radioButton_electron = QtGui.QRadioButton(self.frame)
        self.radioButton_electron.setText(_fromUtf8(""))
        self.radioButton_electron.setAutoExclusive(True)
        self.radioButton_electron.setObjectName(_fromUtf8("radioButton_electron"))
        self.buttonGroup.addButton(self.radioButton_electron)
        self.gridLayout_3.addWidget(self.radioButton_electron, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 5, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 11, 1, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_15 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_9.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.frame)
        self.label_17.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_9.addWidget(self.label_17, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_9.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
"\n"
""))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_9.addWidget(self.label_18, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_9, 5, 4, 1, 1)
        self.lineEdit_DataPath = QtGui.QLineEdit(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.517, 0.25, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.211207, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.456897, QtGui.QColor(39, 103, 106))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lineEdit_DataPath.setPalette(palette)
        self.lineEdit_DataPath.setObjectName(_fromUtf8("lineEdit_DataPath"))
        self.gridLayout.addWidget(self.lineEdit_DataPath, 6, 5, 1, 4)
        self.DataLoadbtn = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.DataLoadbtn.setFont(font)
        self.DataLoadbtn.setStyleSheet(_fromUtf8("background:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 148, 114, 69), stop:0.375 rgba(0, 0, 0, 255), stop:0.452889 rgba(71, 72, 0, 145), stop:0.466983 rgba(1, 128, 99, 228), stop:0.503158 rgba(72, 69, 20, 130), stop:0.505423 rgba(72, 61, 20, 130), stop:0.55 rgba(72, 72, 0, 255), stop:0.668103 rgba(0, 0, 0, 255), stop:0.685345 rgba(72, 72, 0, 69), stop:0.905172 rgba(72, 57, 0, 130));\n"
""))
        self.DataLoadbtn.setObjectName(_fromUtf8("DataLoadbtn"))
        self.gridLayout.addWidget(self.DataLoadbtn, 6, 9, 1, 1)
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.lineEdit_SaveAs = QtGui.QLineEdit(self.frame)
        self.lineEdit_SaveAs.setObjectName(_fromUtf8("lineEdit_SaveAs"))
        self.gridLayout_11.addWidget(self.lineEdit_SaveAs, 0, 0, 1, 1)
        self.lineEdit_Dossier = QtGui.QLineEdit(self.frame)
        self.lineEdit_Dossier.setObjectName(_fromUtf8("lineEdit_Dossier"))
        self.gridLayout_11.addWidget(self.lineEdit_Dossier, 1, 0, 1, 1)
        self.load_save_classify_data = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.load_save_classify_data.setFont(font)
        self.load_save_classify_data.setStyleSheet(_fromUtf8("background:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 148, 114, 69), stop:0.375 rgba(0, 0, 0, 255), stop:0.452889 rgba(71, 72, 0, 145), stop:0.466983 rgba(1, 128, 99, 228), stop:0.503158 rgba(72, 69, 20, 130), stop:0.505423 rgba(72, 61, 20, 130), stop:0.55 rgba(72, 72, 0, 255), stop:0.668103 rgba(0, 0, 0, 255), stop:0.685345 rgba(72, 72, 0, 69), stop:0.905172 rgba(72, 57, 0, 130));\n"
""))
        self.load_save_classify_data.setObjectName(_fromUtf8("load_save_classify_data"))
        self.gridLayout_11.addWidget(self.load_save_classify_data, 1, 1, 1, 1)
        self.load_save_as = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.load_save_as.setFont(font)
        self.load_save_as.setStyleSheet(_fromUtf8("background:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 148, 114, 69), stop:0.375 rgba(0, 0, 0, 255), stop:0.452889 rgba(71, 72, 0, 145), stop:0.466983 rgba(1, 128, 99, 228), stop:0.503158 rgba(72, 69, 20, 130), stop:0.505423 rgba(72, 61, 20, 130), stop:0.55 rgba(72, 72, 0, 255), stop:0.668103 rgba(0, 0, 0, 255), stop:0.685345 rgba(72, 72, 0, 69), stop:0.905172 rgba(72, 57, 0, 130));\n"
""))
        self.load_save_as.setObjectName(_fromUtf8("load_save_as"))
        self.gridLayout_11.addWidget(self.load_save_as, 0, 1, 1, 1)
        self.load_USB_board_file = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.load_USB_board_file.setFont(font)
        self.load_USB_board_file.setStyleSheet(_fromUtf8("background:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 148, 114, 69), stop:0.375 rgba(0, 0, 0, 255), stop:0.452889 rgba(71, 72, 0, 145), stop:0.466983 rgba(1, 128, 99, 228), stop:0.503158 rgba(72, 69, 20, 130), stop:0.505423 rgba(72, 61, 20, 130), stop:0.55 rgba(72, 72, 0, 255), stop:0.668103 rgba(0, 0, 0, 255), stop:0.685345 rgba(72, 72, 0, 69), stop:0.905172 rgba(72, 57, 0, 130));\n"
""))
        self.load_USB_board_file.setObjectName(_fromUtf8("load_USB_board_file"))
        self.gridLayout_11.addWidget(self.load_USB_board_file, 2, 1, 1, 1)
        self.spinBox_USB_board = QtGui.QSpinBox(self.frame)
        self.spinBox_USB_board.setMinimum(1)
        self.spinBox_USB_board.setMaximum(10000000)
        self.spinBox_USB_board.setProperty("value", 100000)
        self.spinBox_USB_board.setObjectName(_fromUtf8("spinBox_USB_board"))
        self.gridLayout_11.addWidget(self.spinBox_USB_board, 3, 0, 1, 2)
        self.USB_board_file = QtGui.QLineEdit(self.frame)
        self.USB_board_file.setObjectName(_fromUtf8("USB_board_file"))
        self.gridLayout_11.addWidget(self.USB_board_file, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_11, 6, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(192, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 4, 1, 1)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_12 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_10.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_10.addWidget(self.label_22, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_10.addWidget(self.label_23, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_10, 6, 1, 1, 1)
        self.line = QtGui.QFrame(self.frame)
        self.line.setMinimumSize(QtCore.QSize(10, 313))
        self.line.setStyleSheet(_fromUtf8("color:rgb(20, 153, 255);\n"
"background:qlineargradient(spread:reflect, x1:0, y1:1, x2:1, y2:1, stop:0.0948276 rgba(136, 106, 22, 255), stop:0.185345 rgba(40, 5, 5, 255), stop:0.376179 rgba(223, 215, 102, 255), stop:0.399142 rgba(137, 108, 26, 255), stop:0.407725 rgba(204, 181, 74, 255), stop:0.420601 rgba(202, 174, 68, 255), stop:0.424893 rgba(166, 140, 41, 255), stop:0.429185 rgba(14, 14, 11, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.625 rgba(187, 156, 51, 255), stop:0.698276 rgba(168, 142, 42, 255), stop:0.814655 rgba(218, 202, 86, 255), stop:0.853448 rgba(208, 187, 73, 255), stop:0.931034 rgba(22, 26, 1, 255), stop:0.987069 rgba(187, 156, 51, 255));"))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 3, 7, 1)
        self.rotation_saved = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rotation_saved.setFont(font)
        self.rotation_saved.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.310345 rgba(156, 143, 137, 133), stop:0.378572 rgba(104, 117, 126, 145), stop:0.392241 rgba(135, 143, 88, 130), stop:0.479796 rgba(136, 129, 116, 208), stop:0.537455 rgba(185, 214, 223, 69), stop:0.543862 rgba(51, 38, 12, 69), stop:0.592552 rgba(52, 52, 52, 130), stop:0.597677 rgba(17, 42, 49, 255), stop:0.74569 rgba(48, 48, 48, 69), stop:0.891088 rgba(101, 95, 60, 69));\n"
""))
        self.rotation_saved.setObjectName(_fromUtf8("rotation_saved"))
        self.gridLayout.addWidget(self.rotation_saved, 4, 4, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_24, 0, 0, 1, 1)
        self.poster = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.poster.setFont(font)
        self.poster.setObjectName(_fromUtf8("poster"))
        self.gridLayout_25.addWidget(self.poster, 11, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        CommandWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(CommandWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CommandWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CommandWindow)
        QtCore.QMetaObject.connectSlotsByName(CommandWindow)

    def retranslateUi(self, CommandWindow):
        CommandWindow.setWindowTitle(_translate("CommandWindow", "MainWindow", None))
        self.label_20.setText(_translate("CommandWindow", "ERROR MESSAGE", None))
        self.automatic_bt.setText(_translate("CommandWindow", "Automatic mode", None))
        self.lineEdit_SensorPos.setText(_translate("CommandWindow", "/home/lphe/cosmic_analysis/python-scripts/RTGraph/cfg_TrackerDemo/geometry_full_tracker_approx.csv", None))
        self.label_14.setText(_translate("CommandWindow", "Acquisition buffer :", None))
        self.label_5.setText(_translate("CommandWindow", "Setup file :", None))
        self.label_13.setText(_translate("CommandWindow", "  Event Id :", None))
        self.label_7.setText(_translate("CommandWindow", "Electron", None))
        self.label_8.setText(_translate("CommandWindow", "Muon", None))
        self.label_9.setText(_translate("CommandWindow", "Disintegration", None))
        self.label_10.setText(_translate("CommandWindow", "Large energy deposit", None))
        self.label_11.setText(_translate("CommandWindow", "ALL", None))
        self.pushButton_LIVE.setText(_translate("CommandWindow", "Live data", None))
        self.label_2.setText(_translate("CommandWindow", "Go Event num", None))
        self.label_19.setText(_translate("CommandWindow", "Event id :", None))
        self.sensorLoadbtn.setText(_translate("CommandWindow", "Load", None))
        self.setupLoadbtn.setText(_translate("CommandWindow", "Load", None))
        self.lineEdit_SetupFile.setText(_translate("CommandWindow", "/home/lphe/cosmic_analysis/python-scripts/RTGraph/cfg_TrackerDemo/setup.yaml", None))
        self.pushButton_SavedData.setText(_translate("CommandWindow", "Saved data", None))
        self.label_4.setText(_translate("CommandWindow", "Sensor position file:", None))
        self.label_15.setText(_translate("CommandWindow", "Muon", None))
        self.label_17.setText(_translate("CommandWindow", "Large energy deposit", None))
        self.label_6.setText(_translate("CommandWindow", "Electron", None))
        self.label_16.setText(_translate("CommandWindow", "Disintegration", None))
        self.label_18.setText(_translate("CommandWindow", "ALL", None))
        self.lineEdit_DataPath.setText(_translate("CommandWindow", "/home/lphe/scifi-data/vata64-data/Pebs_cp-from-tell22/signal_shortfile.csv", None))
        self.DataLoadbtn.setText(_translate("CommandWindow", "Load", None))
        self.lineEdit_SaveAs.setText(_translate("CommandWindow", "/home/lphe/cosmic_analysis/python-scripts/RTGraph/SavedData/data.csv", None))
        self.lineEdit_Dossier.setText(_translate("CommandWindow", "/home/lphe/cosmic_analysis/python-scripts/RTGraph/SavedData/data/", None))
        self.load_save_classify_data.setText(_translate("CommandWindow", "Load", None))
        self.load_save_as.setText(_translate("CommandWindow", "Load", None))
        self.load_USB_board_file.setText(_translate("CommandWindow", "Load", None))
        self.USB_board_file.setText(_translate("CommandWindow", "test", None))
        self.label_3.setText(_translate("CommandWindow", "Saved data :", None))
        self.label_12.setText(_translate("CommandWindow", "Save selected data path:", None))
        self.label_22.setText(_translate("CommandWindow", "USB Board root file", None))
        self.label.setText(_translate("CommandWindow", "Save live data:", None))
        self.label_23.setText(_translate("CommandWindow", "USB Board N event", None))
        self.rotation_saved.setText(_translate("CommandWindow", "3D view Rotation", None))
        self.poster.setText(_translate("CommandWindow", "POSTER", None))

