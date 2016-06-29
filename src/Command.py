# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Command.ui'
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
        CommandWindow.resize(1016, 407)
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
"    background: #212121;\n"
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
        self.centralwidget = QtGui.QWidget(CommandWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_LIVE = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_LIVE.setFont(font)
        self.pushButton_LIVE.setObjectName(_fromUtf8("pushButton_LIVE"))
        self.gridLayout.addWidget(self.pushButton_LIVE, 0, 1, 1, 2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addLayout(self.verticalLayout, 7, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)
        self.pushButton_SavedData = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_SavedData.setFont(font)
        self.pushButton_SavedData.setObjectName(_fromUtf8("pushButton_SavedData"))
        self.gridLayout.addWidget(self.pushButton_SavedData, 0, 4, 1, 3)
        self.pushButton_Right = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Right.setFont(font)
        self.pushButton_Right.setObjectName(_fromUtf8("pushButton_Right"))
        self.gridLayout.addWidget(self.pushButton_Right, 0, 14, 1, 1)
        self.pushButton_Start = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setObjectName(_fromUtf8("pushButton_Start"))
        self.gridLayout.addWidget(self.pushButton_Start, 0, 9, 1, 1)
        self.spinBox_Event = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_Event.setMinimum(1)
        self.spinBox_Event.setMaximum(10000000)
        self.spinBox_Event.setObjectName(_fromUtf8("spinBox_Event"))
        self.gridLayout.addWidget(self.spinBox_Event, 0, 8, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 2)
        self.lineEdit_SenorPos = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_SenorPos.setObjectName(_fromUtf8("lineEdit_SenorPos"))
        self.gridLayout.addWidget(self.lineEdit_SenorPos, 7, 2, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.pushButton_Pause = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Pause.setFont(font)
        self.pushButton_Pause.setObjectName(_fromUtf8("pushButton_Pause"))
        self.gridLayout.addWidget(self.pushButton_Pause, 0, 11, 1, 1)
        self.lineEdit_DataPath = QtGui.QLineEdit(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lineEdit_DataPath.setPalette(palette)
        self.lineEdit_DataPath.setObjectName(_fromUtf8("lineEdit_DataPath"))
        self.gridLayout.addWidget(self.lineEdit_DataPath, 2, 6, 1, 1)
        self.pushButton_Left = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Left.setFont(font)
        self.pushButton_Left.setObjectName(_fromUtf8("pushButton_Left"))
        self.gridLayout.addWidget(self.pushButton_Left, 0, 13, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 7, 1, 1)
        self.lineEdit_SaveAs = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_SaveAs.setText(_fromUtf8(""))
        self.lineEdit_SaveAs.setObjectName(_fromUtf8("lineEdit_SaveAs"))
        self.gridLayout.addWidget(self.lineEdit_SaveAs, 2, 2, 1, 1)
        self.sensorLoadbtn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.sensorLoadbtn.setFont(font)
        self.sensorLoadbtn.setObjectName(_fromUtf8("sensorLoadbtn"))
        self.gridLayout.addWidget(self.sensorLoadbtn, 7, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.lineEdit_SetupFile = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_SetupFile.setObjectName(_fromUtf8("lineEdit_SetupFile"))
        self.gridLayout.addWidget(self.lineEdit_SetupFile, 8, 2, 1, 3)
        self.setupLoadbtn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.setupLoadbtn.setFont(font)
        self.setupLoadbtn.setObjectName(_fromUtf8("setupLoadbtn"))
        self.gridLayout.addWidget(self.setupLoadbtn, 8, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        CommandWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(CommandWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CommandWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CommandWindow)
        QtCore.QMetaObject.connectSlotsByName(CommandWindow)

    def retranslateUi(self, CommandWindow):
        CommandWindow.setWindowTitle(_translate("CommandWindow", "MainWindow", None))
        self.pushButton_LIVE.setText(_translate("CommandWindow", "LIVE", None))
        self.label_4.setText(_translate("CommandWindow", "Sensor position file:", None))
        self.pushButton_SavedData.setText(_translate("CommandWindow", "Saved DATA", None))
        self.pushButton_Right.setText(_translate("CommandWindow", "Right", None))
        self.pushButton_Start.setText(_translate("CommandWindow", "Start", None))
        self.label_3.setText(_translate("CommandWindow", "Data Path loaded :", None))
        self.label.setText(_translate("CommandWindow", "Save as :", None))
        self.pushButton_Pause.setText(_translate("CommandWindow", "Pause", None))
        self.pushButton_Left.setText(_translate("CommandWindow", "Left", None))
        self.label_2.setText(_translate("CommandWindow", "Event id", None))
        self.sensorLoadbtn.setText(_translate("CommandWindow", "Load", None))
        self.label_5.setText(_translate("CommandWindow", "Setup file :", None))
        self.setupLoadbtn.setText(_translate("CommandWindow", "Load", None))

