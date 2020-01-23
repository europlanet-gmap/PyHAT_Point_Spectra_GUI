# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.yminlabel = QtWidgets.QLabel(self.groupBox)
        self.yminlabel.setObjectName("yminlabel")
        self.horizontalLayout_2.addWidget(self.yminlabel)
        self.yminSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.yminSpinBox.setMinimum(-1e+28)
        self.yminSpinBox.setMaximum(1e+47)
        self.yminSpinBox.setObjectName("yminSpinBox")
        self.horizontalLayout_2.addWidget(self.yminSpinBox)
        self.ymaxlabel = QtWidgets.QLabel(self.groupBox)
        self.ymaxlabel.setObjectName("ymaxlabel")
        self.horizontalLayout_2.addWidget(self.ymaxlabel)
        self.ymaxSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.ymaxSpinBox.setMinimum(-1e+45)
        self.ymaxSpinBox.setMaximum(1e+47)
        self.ymaxSpinBox.setObjectName("ymaxSpinBox")
        self.horizontalLayout_2.addWidget(self.ymaxSpinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 10, 1, 1, 1)
        self.xtitle_label = QtWidgets.QLabel(self.groupBox)
        self.xtitle_label.setObjectName("xtitle_label")
        self.gridLayout_2.addWidget(self.xtitle_label, 7, 0, 1, 1)
        self.xtitle_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.xtitle_lineEdit.setObjectName("xtitle_lineEdit")
        self.gridLayout_2.addWidget(self.xtitle_lineEdit, 7, 1, 1, 1)
        self.ytitle_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ytitle_lineEdit.setObjectName("ytitle_lineEdit")
        self.gridLayout_2.addWidget(self.ytitle_lineEdit, 11, 1, 1, 1)
        self.ytitle_label = QtWidgets.QLabel(self.groupBox)
        self.ytitle_label.setObjectName("ytitle_label")
        self.gridLayout_2.addWidget(self.ytitle_label, 11, 0, 1, 1)
        self.newfig_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.newfig_lineEdit.setObjectName("newfig_lineEdit")
        self.gridLayout_2.addWidget(self.newfig_lineEdit, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xminLabel = QtWidgets.QLabel(self.groupBox)
        self.xminLabel.setObjectName("xminLabel")
        self.horizontalLayout.addWidget(self.xminLabel)
        self.xminDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.xminDoubleSpinBox.setMaximum(1e+42)
        self.xminDoubleSpinBox.setObjectName("xminDoubleSpinBox")
        self.horizontalLayout.addWidget(self.xminDoubleSpinBox)
        self.xmaxLabel = QtWidgets.QLabel(self.groupBox)
        self.xmaxLabel.setObjectName("xmaxLabel")
        self.horizontalLayout.addWidget(self.xmaxLabel)
        self.xmaxDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.xmaxDoubleSpinBox.setMaximum(1e+53)
        self.xmaxDoubleSpinBox.setObjectName("xmaxDoubleSpinBox")
        self.horizontalLayout.addWidget(self.xmaxDoubleSpinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 1, 1, 1)
        self.figname_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.figname_comboBox.setObjectName("figname_comboBox")
        self.gridLayout_2.addWidget(self.figname_comboBox, 1, 1, 1, 1)
        self.newfig_label = QtWidgets.QLabel(self.groupBox)
        self.newfig_label.setObjectName("newfig_label")
        self.gridLayout_2.addWidget(self.newfig_label, 2, 0, 1, 1)
        self.figureNameLabel = QtWidgets.QLabel(self.groupBox)
        self.figureNameLabel.setObjectName("figureNameLabel")
        self.gridLayout_2.addWidget(self.figureNameLabel, 1, 0, 1, 1)
        self.chooseRowsLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseRowsLabel.setObjectName("chooseRowsLabel")
        self.gridLayout_2.addWidget(self.chooseRowsLabel, 9, 0, 1, 1)
        self.colorLabel = QtWidgets.QLabel(self.groupBox)
        self.colorLabel.setObjectName("colorLabel")
        self.gridLayout_2.addWidget(self.colorLabel, 12, 0, 1, 1)
        self.lineLabel = QtWidgets.QLabel(self.groupBox)
        self.lineLabel.setObjectName("lineLabel")
        self.gridLayout_2.addWidget(self.lineLabel, 13, 0, 1, 1)
        self.plotTitleLabel = QtWidgets.QLabel(self.groupBox)
        self.plotTitleLabel.setObjectName("plotTitleLabel")
        self.gridLayout_2.addWidget(self.plotTitleLabel, 4, 0, 1, 1)
        self.alphaLabel = QtWidgets.QLabel(self.groupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.gridLayout_2.addWidget(self.alphaLabel, 14, 0, 1, 1)
        self.xVariableLabel = QtWidgets.QLabel(self.groupBox)
        self.xVariableLabel.setObjectName("xVariableLabel")
        self.gridLayout_2.addWidget(self.xVariableLabel, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 16, 2, 1, 1)
        self.chooseColumnLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseColumnLabel.setObjectName("chooseColumnLabel")
        self.gridLayout_2.addWidget(self.chooseColumnLabel, 8, 0, 1, 1)
        self.plotFilenameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.plotFilenameLineEdit.setReadOnly(True)
        self.plotFilenameLineEdit.setObjectName("plotFilenameLineEdit")
        self.gridLayout_2.addWidget(self.plotFilenameLineEdit, 16, 1, 1, 1)
        self.plotTitleLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.plotTitleLineEdit.setObjectName("plotTitleLineEdit")
        self.gridLayout_2.addWidget(self.plotTitleLineEdit, 4, 1, 1, 2)
        self.chooseColumnComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseColumnComboBox.setObjectName("chooseColumnComboBox")
        self.gridLayout_2.addWidget(self.chooseColumnComboBox, 8, 1, 1, 2)
        self.lineWidthLabel = QtWidgets.QLabel(self.groupBox)
        self.lineWidthLabel.setObjectName("lineWidthLabel")
        self.gridLayout_2.addWidget(self.lineWidthLabel, 15, 0, 1, 1)
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout_2.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.plotFilenameLabel = QtWidgets.QLabel(self.groupBox)
        self.plotFilenameLabel.setObjectName("plotFilenameLabel")
        self.gridLayout_2.addWidget(self.plotFilenameLabel, 16, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout_2.addWidget(self.chooseDataComboBox, 0, 1, 1, 2)
        self.colorComboBox = QtWidgets.QComboBox(self.groupBox)
        self.colorComboBox.setObjectName("colorComboBox")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.gridLayout_2.addWidget(self.colorComboBox, 12, 1, 1, 2)
        self.xVariableListWidget = QtWidgets.QListWidget(self.groupBox)
        self.xVariableListWidget.setObjectName("xVariableListWidget")
        self.gridLayout_2.addWidget(self.xVariableListWidget, 5, 1, 1, 2)
        self.lineWidthDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.lineWidthDoubleSpinBox.setMaximum(10.0)
        self.lineWidthDoubleSpinBox.setSingleStep(0.05)
        self.lineWidthDoubleSpinBox.setProperty("value", 0.5)
        self.lineWidthDoubleSpinBox.setObjectName("lineWidthDoubleSpinBox")
        self.gridLayout_2.addWidget(self.lineWidthDoubleSpinBox, 15, 1, 1, 2)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.alphaDoubleSpinBox.setDecimals(0)
        self.alphaDoubleSpinBox.setMaximum(100.0)
        self.alphaDoubleSpinBox.setProperty("value", 100.0)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.gridLayout_2.addWidget(self.alphaDoubleSpinBox, 14, 1, 1, 2)
        self.lineComboBox = QtWidgets.QComboBox(self.groupBox)
        self.lineComboBox.setObjectName("lineComboBox")
        self.lineComboBox.addItem("")
        self.lineComboBox.addItem("")
        self.lineComboBox.addItem("")
        self.lineComboBox.addItem("")
        self.gridLayout_2.addWidget(self.lineComboBox, 13, 1, 1, 2)
        self.chooseRowsListWidget = QtWidgets.QListWidget(self.groupBox)
        self.chooseRowsListWidget.setObjectName("chooseRowsListWidget")
        self.gridLayout_2.addWidget(self.chooseRowsListWidget, 9, 1, 1, 2)
        self.newfig_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.newfig_checkBox.setChecked(True)
        self.newfig_checkBox.setObjectName("newfig_checkBox")
        self.gridLayout_2.addWidget(self.newfig_checkBox, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.chooseDataComboBox, self.plotTitleLineEdit)
        Form.setTabOrder(self.plotTitleLineEdit, self.xVariableListWidget)
        Form.setTabOrder(self.xVariableListWidget, self.chooseColumnComboBox)
        Form.setTabOrder(self.chooseColumnComboBox, self.chooseRowsListWidget)
        Form.setTabOrder(self.chooseRowsListWidget, self.xminDoubleSpinBox)
        Form.setTabOrder(self.xminDoubleSpinBox, self.xmaxDoubleSpinBox)
        Form.setTabOrder(self.xmaxDoubleSpinBox, self.colorComboBox)
        Form.setTabOrder(self.colorComboBox, self.lineComboBox)
        Form.setTabOrder(self.lineComboBox, self.alphaDoubleSpinBox)
        Form.setTabOrder(self.alphaDoubleSpinBox, self.lineWidthDoubleSpinBox)
        Form.setTabOrder(self.lineWidthDoubleSpinBox, self.plotFilenameLineEdit)
        Form.setTabOrder(self.plotFilenameLineEdit, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Plot Spectra"))
        self.yminlabel.setText(("Y Min"))
        self.ymaxlabel.setText(("Y Max"))
        self.xtitle_label.setText(("X Title"))
        self.ytitle_label.setText(("Y Title"))
        self.newfig_lineEdit.setText(("Fig 1"))
        self.xminLabel.setText(("X Min"))
        self.xmaxLabel.setText(("X Max"))
        self.newfig_label.setText(("New figure name"))
        self.figureNameLabel.setText(("Figure Name"))
        self.chooseRowsLabel.setText(("Choose Rows:"))
        self.colorLabel.setText(("Color"))
        self.lineLabel.setText(("Line style"))
        self.plotTitleLabel.setText(("Plot Title"))
        self.alphaLabel.setText(("Opacity (%)"))
        self.xVariableLabel.setText(("X Variable:"))
        self.pushButton.setText(("..."))
        self.chooseColumnLabel.setText(("Choose Column"))
        self.lineWidthLabel.setText(("Line width"))
        self.chooseDataLabel.setText(("Choose Data"))
        self.plotFilenameLabel.setText(("Plot Filename"))
        self.colorComboBox.setItemText(0, ("Red"))
        self.colorComboBox.setItemText(1, ("Green"))
        self.colorComboBox.setItemText(2, ("Blue"))
        self.colorComboBox.setItemText(3, ("Cyan"))
        self.colorComboBox.setItemText(4, ("Yellow"))
        self.colorComboBox.setItemText(5, ("Magenta"))
        self.colorComboBox.setItemText(6, ("Black"))
        self.lineComboBox.setItemText(0, ("Line"))
        self.lineComboBox.setItemText(1, ("Dashed Line"))
        self.lineComboBox.setItemText(2, ("Dotted Line"))
        self.lineComboBox.setItemText(3, ("Points (No Line)"))
        self.newfig_checkBox.setText(("New Figure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())