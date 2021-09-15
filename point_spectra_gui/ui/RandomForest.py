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
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numEstLabel)
        self.numEstSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.numEstSpinBox.setMaximum(999999999)
        self.numEstSpinBox.setProperty("value", 100)
        self.numEstSpinBox.setObjectName("numEstSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numEstSpinBox)
        self.max_depthLabel = QtWidgets.QLabel(self.formGroupBox)
        self.max_depthLabel.setObjectName("max_depthLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.max_depthLabel)
        self.max_depthSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.max_depthSpinBox.setMinimum(1)
        self.max_depthSpinBox.setProperty("value", 3)
        self.max_depthSpinBox.setObjectName("max_depthSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.max_depthSpinBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setTitle(("Random Forest Regression"))
        self.numEstLabel.setText(("# of estimators"))
        self.numEstSpinBox.setToolTip(("Maximum number of iterations. Default is 300."))
        self.numEstSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.max_depthLabel.setText(("Max Depth"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

