# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nicholas\Documents\GitHub\PYSAT\src\New PYSAT_Gui\mainwindow_normalization.ui'
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

class pysat_ui(object):
    def normalization(self, MainWindow):
        self.Normalization = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Normalization.setFont(font)
        self.Normalization.setObjectName(_fromUtf8("Normalization"))
        self.verticalLayout_27 = QtGui.QVBoxLayout(self.Normalization)
        self.verticalLayout_27.setMargin(11)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(_fromUtf8("verticalLayout_27"))
        self.verticalLayout_26 = QtGui.QVBoxLayout()
        self.verticalLayout_26.setMargin(11)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(_fromUtf8("verticalLayout_26"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.norm_label = QtGui.QLabel(self.Normalization)
        self.norm_label.setObjectName(_fromUtf8("norm_label"))
        self.horizontalLayout_2.addWidget(self.norm_label)
        self.norm_spinBox_9 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_9.setMaximum(1000)
        self.norm_spinBox_9.setObjectName(_fromUtf8("norm_spinBox_9"))
        self.horizontalLayout_2.addWidget(self.norm_spinBox_9)
        self.norm_spinBox = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox.setMaximum(1000)
        self.norm_spinBox.setObjectName(_fromUtf8("norm_spinBox"))
        self.horizontalLayout_2.addWidget(self.norm_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_26.addLayout(self.verticalLayout_2)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setMargin(11)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setMargin(11)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.norm_label_2 = QtGui.QLabel(self.Normalization)
        self.norm_label_2.setObjectName(_fromUtf8("norm_label_2"))
        self.horizontalLayout_18.addWidget(self.norm_label_2)
        self.norm_spinBox_10 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_10.setMaximum(1000)
        self.norm_spinBox_10.setObjectName(_fromUtf8("norm_spinBox_10"))
        self.horizontalLayout_18.addWidget(self.norm_spinBox_10)
        self.norm_spinBox_2 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_2.setMaximum(1000)
        self.norm_spinBox_2.setObjectName(_fromUtf8("norm_spinBox_2"))
        self.horizontalLayout_18.addWidget(self.norm_spinBox_2)
        self.verticalLayout_16.addLayout(self.horizontalLayout_18)
        self.verticalLayout_26.addLayout(self.verticalLayout_16)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setMargin(11)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setMargin(11)
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.norm_label_3 = QtGui.QLabel(self.Normalization)
        self.norm_label_3.setObjectName(_fromUtf8("norm_label_3"))
        self.horizontalLayout_20.addWidget(self.norm_label_3)
        self.norm_spinBox_11 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_11.setMaximum(1000)
        self.norm_spinBox_11.setObjectName(_fromUtf8("norm_spinBox_11"))
        self.horizontalLayout_20.addWidget(self.norm_spinBox_11)
        self.norm_spinBox_3 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_3.setMaximum(1000)
        self.norm_spinBox_3.setObjectName(_fromUtf8("norm_spinBox_3"))
        self.horizontalLayout_20.addWidget(self.norm_spinBox_3)
        self.verticalLayout_20.addLayout(self.horizontalLayout_20)
        self.verticalLayout_26.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.verticalLayout_21.setMargin(11)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setMargin(11)
        self.horizontalLayout_22.setSpacing(6)
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.norm_label_4 = QtGui.QLabel(self.Normalization)
        self.norm_label_4.setObjectName(_fromUtf8("norm_label_4"))
        self.horizontalLayout_22.addWidget(self.norm_label_4)
        self.norm_spinBox_12 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_12.setMaximum(1000)
        self.norm_spinBox_12.setObjectName(_fromUtf8("norm_spinBox_12"))
        self.horizontalLayout_22.addWidget(self.norm_spinBox_12)
        self.norm_spinBox_4 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_4.setMaximum(1000)
        self.norm_spinBox_4.setObjectName(_fromUtf8("norm_spinBox_4"))
        self.horizontalLayout_22.addWidget(self.norm_spinBox_4)
        self.verticalLayout_21.addLayout(self.horizontalLayout_22)
        self.verticalLayout_26.addLayout(self.verticalLayout_21)
        self.verticalLayout_23 = QtGui.QVBoxLayout()
        self.verticalLayout_23.setMargin(11)
        self.verticalLayout_23.setSpacing(6)
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setMargin(11)
        self.horizontalLayout_26.setSpacing(6)
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.norm_label_5 = QtGui.QLabel(self.Normalization)
        self.norm_label_5.setObjectName(_fromUtf8("norm_label_5"))
        self.horizontalLayout_26.addWidget(self.norm_label_5)
        self.norm_spinBox_13 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_13.setMaximum(1000)
        self.norm_spinBox_13.setObjectName(_fromUtf8("norm_spinBox_13"))
        self.horizontalLayout_26.addWidget(self.norm_spinBox_13)
        self.norm_spinBox_5 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_5.setMaximum(1000)
        self.norm_spinBox_5.setObjectName(_fromUtf8("norm_spinBox_5"))
        self.horizontalLayout_26.addWidget(self.norm_spinBox_5)
        self.verticalLayout_23.addLayout(self.horizontalLayout_26)
        self.verticalLayout_26.addLayout(self.verticalLayout_23)
        self.verticalLayout_25 = QtGui.QVBoxLayout()
        self.verticalLayout_25.setMargin(11)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setMargin(11)
        self.horizontalLayout_30.setSpacing(6)
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.norm_label_6 = QtGui.QLabel(self.Normalization)
        self.norm_label_6.setObjectName(_fromUtf8("norm_label_6"))
        self.horizontalLayout_30.addWidget(self.norm_label_6)
        self.norm_spinBox_14 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_14.setMaximum(1000)
        self.norm_spinBox_14.setObjectName(_fromUtf8("norm_spinBox_14"))
        self.horizontalLayout_30.addWidget(self.norm_spinBox_14)
        self.norm_spinBox_6 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_6.setMaximum(1000)
        self.norm_spinBox_6.setObjectName(_fromUtf8("norm_spinBox_6"))
        self.horizontalLayout_30.addWidget(self.norm_spinBox_6)
        self.verticalLayout_25.addLayout(self.horizontalLayout_30)
        self.verticalLayout_26.addLayout(self.verticalLayout_25)
        self.verticalLayout_24 = QtGui.QVBoxLayout()
        self.verticalLayout_24.setMargin(11)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(_fromUtf8("verticalLayout_24"))
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setMargin(11)
        self.horizontalLayout_28.setSpacing(6)
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.norm_label_7 = QtGui.QLabel(self.Normalization)
        self.norm_label_7.setObjectName(_fromUtf8("norm_label_7"))
        self.horizontalLayout_28.addWidget(self.norm_label_7)
        self.norm_spinBox_15 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_15.setMaximum(1000)
        self.norm_spinBox_15.setObjectName(_fromUtf8("norm_spinBox_15"))
        self.horizontalLayout_28.addWidget(self.norm_spinBox_15)
        self.norm_spinBox_7 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_7.setMaximum(1000)
        self.norm_spinBox_7.setObjectName(_fromUtf8("norm_spinBox_7"))
        self.horizontalLayout_28.addWidget(self.norm_spinBox_7)
        self.verticalLayout_24.addLayout(self.horizontalLayout_28)
        self.verticalLayout_26.addLayout(self.verticalLayout_24)
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setMargin(11)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setMargin(11)
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.norm_label_8 = QtGui.QLabel(self.Normalization)
        self.norm_label_8.setObjectName(_fromUtf8("norm_label_8"))
        self.horizontalLayout_24.addWidget(self.norm_label_8)
        self.norm_spinBox_16 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_16.setMaximum(1000)
        self.norm_spinBox_16.setObjectName(_fromUtf8("norm_spinBox_16"))
        self.horizontalLayout_24.addWidget(self.norm_spinBox_16)
        self.norm_spinBox_8 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_8.setMaximum(1000)
        self.norm_spinBox_8.setObjectName(_fromUtf8("norm_spinBox_8"))
        self.horizontalLayout_24.addWidget(self.norm_spinBox_8)
        self.verticalLayout_22.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setMargin(11)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem)
        self.NormValuebutton = QtGui.QPushButton(self.Normalization)
        self.NormValuebutton.setObjectName(_fromUtf8("NormValuebutton"))
        self.horizontalLayout_25.addWidget(self.NormValuebutton)
        self.verticalLayout_22.addLayout(self.horizontalLayout_25)
        self.verticalLayout_26.addLayout(self.verticalLayout_22)
        self.verticalLayout_27.addLayout(self.verticalLayout_26)
        self.verticalLayout_8.addWidget(self.Normalization)
        self.Normalization.setTitle(_translate("MainWindow", "Normalization", None))
        self.norm_label.setText(_translate("MainWindow", "Value 1", None))
        self.norm_label_2.setText(_translate("MainWindow", "Value 2", None))
        self.norm_label_3.setText(_translate("MainWindow", "Value 3", None))
        self.norm_label_4.setText(_translate("MainWindow", "Value 4", None))
        self.norm_label_5.setText(_translate("MainWindow", "Value 5", None))
        self.norm_label_6.setText(_translate("MainWindow", "Value 6", None))
        self.norm_label_7.setText(_translate("MainWindow", "Value 7", None))
        self.norm_label_8.setText(_translate("MainWindow", "Value 8", None))
        self.NormValuebutton.setText(_translate("MainWindow", "Add Value", None))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


