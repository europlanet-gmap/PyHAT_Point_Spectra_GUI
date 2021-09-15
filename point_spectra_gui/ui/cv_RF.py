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
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.numEstLabel = QtWidgets.QLabel(self.formGroupBox)
        self.numEstLabel.setObjectName("numEstLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numEstLabel)
        self.numEstlineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.numEstlineEdit.setObjectName("numEstlineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numEstlineEdit)
        self.max_depthLabel = QtWidgets.QLabel(self.formGroupBox)
        self.max_depthLabel.setObjectName("max_depthLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.max_depthLabel)
        self.maxdepthlineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.maxdepthlineEdit.setObjectName("maxdepthlineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.maxdepthlineEdit)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setTitle(("Random Forest Regression"))
        self.numEstLabel.setText(("# of estimators"))
        self.numEstlineEdit.setText(("100"))
        self.max_depthLabel.setText(("Max Depth"))
        self.maxdepthlineEdit.setText(("3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

