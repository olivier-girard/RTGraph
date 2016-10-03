# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PosterWindow.ui'
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

class Ui_PosterWindow(object):
    def setupUi(self, PosterWindow):
        PosterWindow.setObjectName(_fromUtf8("PosterWindow"))
        PosterWindow.resize(2122, 1464)
        PosterWindow.setStyleSheet(_fromUtf8("\n"
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
        self.centralwidget = QtGui.QWidget(PosterWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.cosmicray = QtGui.QLabel(self.centralwidget)
        self.cosmicray.setGeometry(QtCore.QRect(110, 130, 521, 721))
        self.cosmicray.setText(_fromUtf8(""))
        self.cosmicray.setScaledContents(True)
        self.cosmicray.setObjectName(_fromUtf8("cosmicray"))
        self.schema = QtGui.QLabel(self.centralwidget)
        self.schema.setGeometry(QtCore.QRect(730, 110, 521, 471))
        self.schema.setText(_fromUtf8(""))
        self.schema.setScaledContents(True)
        self.schema.setObjectName(_fromUtf8("schema"))
        self.track_muon = QtGui.QLabel(self.centralwidget)
        self.track_muon.setGeometry(QtCore.QRect(1580, 870, 441, 341))
        self.track_muon.setText(_fromUtf8(""))
        self.track_muon.setScaledContents(True)
        self.track_muon.setObjectName(_fromUtf8("track_muon"))
        self.track_electron = QtGui.QLabel(self.centralwidget)
        self.track_electron.setGeometry(QtCore.QRect(1580, 520, 441, 341))
        self.track_electron.setText(_fromUtf8(""))
        self.track_electron.setScaledContents(True)
        self.track_electron.setObjectName(_fromUtf8("track_electron"))
        self.detector = QtGui.QLabel(self.centralwidget)
        self.detector.setGeometry(QtCore.QRect(660, 670, 431, 411))
        self.detector.setText(_fromUtf8(""))
        self.detector.setScaledContents(True)
        self.detector.setObjectName(_fromUtf8("detector"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(880, 610, 431, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 501, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(850, 40, 311, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 681, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.signal = QtGui.QLabel(self.centralwidget)
        self.signal.setGeometry(QtCore.QRect(1120, 680, 431, 401))
        self.signal.setText(_fromUtf8(""))
        self.signal.setScaledContents(True)
        self.signal.setObjectName(_fromUtf8("signal"))
        PosterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(PosterWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PosterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PosterWindow)
        QtCore.QMetaObject.connectSlotsByName(PosterWindow)

    def retranslateUi(self, PosterWindow):
        PosterWindow.setWindowTitle(_translate("PosterWindow", "Poster", None))
        self.label.setText(_translate("PosterWindow", "          How to Detect cosmic ray ?", None))
        self.label_2.setText(_translate("PosterWindow", "          Cosmic ray, what is it?", None))
        self.label_3.setText(_translate("PosterWindow", "How they break down ?", None))
        self.label_4.setText(_translate("PosterWindow", "It\'sparticules coming from space whose decomposed through the atmosphere ", None))

