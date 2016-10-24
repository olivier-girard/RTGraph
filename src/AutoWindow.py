# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoWindow.ui'
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

class Ui_AutoWindow(object):
    def setupUi(self, AutoWindow):
        AutoWindow.setObjectName(_fromUtf8("AutoWindow"))
        AutoWindow.resize(1346, 920)
        AutoWindow.setMinimumSize(QtCore.QSize(0, 0))
        AutoWindow.setStyleSheet(_fromUtf8("\n"
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
        AutoWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(AutoWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.autoplot = GraphicsLayoutWidget(self.centralwidget)
        self.autoplot.setObjectName(_fromUtf8("autoplot"))
        self.gridLayout_2.addWidget(self.autoplot, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        AutoWindow.setCentralWidget(self.centralwidget)
        self.actionAll_pannel = QtGui.QAction(AutoWindow)
        self.actionAll_pannel.setCheckable(False)
        self.actionAll_pannel.setEnabled(True)
        self.actionAll_pannel.setObjectName(_fromUtf8("actionAll_pannel"))
        self.actionHistogram = QtGui.QAction(AutoWindow)
        self.actionHistogram.setObjectName(_fromUtf8("actionHistogram"))
        self.actionTracker = QtGui.QAction(AutoWindow)
        self.actionTracker.setObjectName(_fromUtf8("actionTracker"))
        self.actionChannels = QtGui.QAction(AutoWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionChannels.setFont(font)
        self.actionChannels.setObjectName(_fromUtf8("actionChannels"))
        self.actionAll = QtGui.QAction(AutoWindow)
        self.actionAll.setObjectName(_fromUtf8("actionAll"))

        self.retranslateUi(AutoWindow)
        QtCore.QMetaObject.connectSlotsByName(AutoWindow)

    def retranslateUi(self, AutoWindow):
        AutoWindow.setWindowTitle(_translate("AutoWindow", "Auto Window", None))
        self.actionAll_pannel.setText(_translate("AutoWindow", "All pannel", None))
        self.actionHistogram.setText(_translate("AutoWindow", "Histogram", None))
        self.actionTracker.setText(_translate("AutoWindow", "Tracker", None))
        self.actionChannels.setText(_translate("AutoWindow", "Channels", None))
        self.actionAll.setText(_translate("AutoWindow", "All", None))

from pyqtgraph import GraphicsLayoutWidget
