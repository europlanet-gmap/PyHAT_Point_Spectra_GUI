# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.new_lvl1_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.new_lvl1_lineEdit.setObjectName("new_lvl1_lineEdit")
        self.gridLayout.addWidget(self.new_lvl1_lineEdit, 3, 1, 1, 1)
        self.new_lvl1_label = QtWidgets.QLabel(self.groupBox)
        self.new_lvl1_label.setObjectName("new_lvl1_label")
        self.gridLayout.addWidget(self.new_lvl1_label, 3, 0, 1, 1)
        self.choosecol_label = QtWidgets.QLabel(self.groupBox)
        self.choosecol_label.setObjectName("choosecol_label")
        self.gridLayout.addWidget(self.choosecol_label, 1, 0, 1, 1)
        self.choosecol_lvl0 = QtWidgets.QComboBox(self.groupBox)
        self.choosecol_lvl0.setObjectName("choosecol_lvl0")
        self.gridLayout.addWidget(self.choosecol_lvl0, 1, 1, 1, 1)
        self.choosedata_label = QtWidgets.QLabel(self.groupBox)
        self.choosedata_label.setObjectName("choosedata_label")
        self.gridLayout.addWidget(self.choosedata_label, 0, 0, 1, 1)
        self.choosedata_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.choosedata_comboBox.setObjectName("choosedata_comboBox")
        self.gridLayout.addWidget(self.choosedata_comboBox, 0, 1, 1, 1)
        self.new_lvl0_label = QtWidgets.QLabel(self.groupBox)
        self.new_lvl0_label.setObjectName("new_lvl0_label")
        self.gridLayout.addWidget(self.new_lvl0_label, 2, 0, 1, 1)
        self.new_lvl0_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.new_lvl0_lineEdit.setObjectName("new_lvl0_lineEdit")
        self.gridLayout.addWidget(self.new_lvl0_lineEdit, 2, 1, 1, 1)
        self.choosecol_lvl1 = QtWidgets.QComboBox(self.groupBox)
        self.choosecol_lvl1.setObjectName("choosecol_lvl1")
        self.gridLayout.addWidget(self.choosecol_lvl1, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Rename Column"))
        self.new_lvl1_label.setText(("New second-level name:"))
        self.choosecol_label.setText(("Choose column to rename:"))
        self.choosedata_label.setText(("Choose Data:"))
        self.new_lvl0_label.setText(("New top-level name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

