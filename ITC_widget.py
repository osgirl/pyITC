# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Oxford_ITC_gui.ui'
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

class Ui_OxfordITC(object):
    def setupUi(self, OxfordITC):
        OxfordITC.setObjectName(_fromUtf8("OxfordITC"))
        OxfordITC.resize(448, 355)
        self.horizontalLayout_5 = QtGui.QHBoxLayout(OxfordITC)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.groupBox = QtGui.QGroupBox(OxfordITC)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.btn_open_connection = QtGui.QPushButton(self.groupBox)
        self.btn_open_connection.setObjectName(_fromUtf8("btn_open_connection"))
        self.horizontalLayout_6.addWidget(self.btn_open_connection)
        self.btn_close_connection = QtGui.QPushButton(self.groupBox)
        self.btn_close_connection.setObjectName(_fromUtf8("btn_close_connection"))
        self.horizontalLayout_6.addWidget(self.btn_close_connection)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.label_2 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.disp_current_temp = QtGui.QLabel(self.groupBox)
        self.disp_current_temp.setObjectName(_fromUtf8("disp_current_temp"))
        self.horizontalLayout.addWidget(self.disp_current_temp)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.check_live_temp = QtGui.QCheckBox(self.groupBox)
        self.check_live_temp.setObjectName(_fromUtf8("check_live_temp"))
        self.horizontalLayout.addWidget(self.check_live_temp)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_read_temp = QtGui.QPushButton(self.groupBox)
        self.btn_read_temp.setObjectName(_fromUtf8("btn_read_temp"))
        self.horizontalLayout.addWidget(self.btn_read_temp)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.label_3 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.spin_set_temp = QtGui.QSpinBox(self.groupBox)
        self.spin_set_temp.setMinimum(5)
        self.spin_set_temp.setMaximum(300)
        self.spin_set_temp.setObjectName(_fromUtf8("spin_set_temp"))
        self.horizontalLayout_2.addWidget(self.spin_set_temp)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.check_auto_heat = QtGui.QCheckBox(self.groupBox)
        self.check_auto_heat.setObjectName(_fromUtf8("check_auto_heat"))
        self.horizontalLayout_3.addWidget(self.check_auto_heat)
        self.check_auto_PID = QtGui.QCheckBox(self.groupBox)
        self.check_auto_PID.setObjectName(_fromUtf8("check_auto_PID"))
        self.horizontalLayout_3.addWidget(self.check_auto_PID)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.label_6 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.spin_man_heat = QtGui.QDoubleSpinBox(self.groupBox)
        self.spin_man_heat.setMaximum(99.9)
        self.spin_man_heat.setSingleStep(0.1)
        self.spin_man_heat.setObjectName(_fromUtf8("spin_man_heat"))
        self.horizontalLayout_4.addWidget(self.spin_man_heat)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addWidget(self.groupBox)

        self.retranslateUi(OxfordITC)
        QtCore.QMetaObject.connectSlotsByName(OxfordITC)

    def retranslateUi(self, OxfordITC):
        OxfordITC.setWindowTitle(_translate("OxfordITC", "Oxford ITC 503S", None))
        self.groupBox.setTitle(_translate("OxfordITC", "Oxford ITC 503S", None))
        self.label_8.setText(_translate("OxfordITC", "Connection", None))
        self.btn_open_connection.setText(_translate("OxfordITC", "Open", None))
        self.btn_close_connection.setText(_translate("OxfordITC", "Close", None))
        self.label_2.setText(_translate("OxfordITC", "Current temperature", None))
        self.disp_current_temp.setText(_translate("OxfordITC", "273", None))
        self.label.setText(_translate("OxfordITC", "K", None))
        self.check_live_temp.setText(_translate("OxfordITC", "live", None))
        self.btn_read_temp.setText(_translate("OxfordITC", "Read", None))
        self.label_3.setText(_translate("OxfordITC", "Temperature Control", None))
        self.label_4.setText(_translate("OxfordITC", "Set Temperature", None))
        self.label_5.setText(_translate("OxfordITC", "K", None))
        self.check_auto_heat.setText(_translate("OxfordITC", "Auto Heater", None))
        self.check_auto_PID.setText(_translate("OxfordITC", "Auto PID", None))
        self.label_6.setText(_translate("OxfordITC", "Manual Heater Control", None))
        self.label_7.setText(_translate("OxfordITC", "%", None))
