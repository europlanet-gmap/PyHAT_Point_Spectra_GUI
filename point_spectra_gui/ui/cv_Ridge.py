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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Ridge = QtWidgets.QGroupBox(Form)
        self.Ridge.setEnabled(True)
        self.Ridge.setTitle("")
        self.Ridge.setObjectName("Ridge")
        self.formLayout_2 = QtWidgets.QFormLayout(self.Ridge)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.min_alphaLabel = QtWidgets.QLabel(self.Ridge)
        self.min_alphaLabel.setObjectName("min_alphaLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.min_alphaLabel)
        self.min_alpha_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.Ridge)
        self.min_alpha_doubleSpinBox.setDecimals(20)
        self.min_alpha_doubleSpinBox.setObjectName("min_alpha_doubleSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.min_alpha_doubleSpinBox)
        self.max_alphaLabel = QtWidgets.QLabel(self.Ridge)
        self.max_alphaLabel.setObjectName("max_alphaLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.max_alphaLabel)
        self.max_alpha_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.Ridge)
        self.max_alpha_doubleSpinBox.setDecimals(20)
        self.max_alpha_doubleSpinBox.setObjectName("max_alpha_doubleSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.max_alpha_doubleSpinBox)
        self.n_alpha_label = QtWidgets.QLabel(self.Ridge)
        self.n_alpha_label.setObjectName("n_alpha_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.n_alpha_label)
        self.n_alpha_spinBox = QtWidgets.QSpinBox(self.Ridge)
        self.n_alpha_spinBox.setMinimum(1)
        self.n_alpha_spinBox.setMaximum(999999999)
        self.n_alpha_spinBox.setObjectName("n_alpha_spinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.n_alpha_spinBox)
        self.fitInterceptLabel = QtWidgets.QLabel(self.Ridge)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fit_intercept_list = QtWidgets.QListWidget(self.Ridge)
        self.fit_intercept_list.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fit_intercept_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.fit_intercept_list.setObjectName("fit_intercept_list")
        item = QtWidgets.QListWidgetItem()
        self.fit_intercept_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.fit_intercept_list.addItem(item)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fit_intercept_list)
        self.normalizeLabel = QtWidgets.QLabel(self.Ridge)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalize_list = QtWidgets.QListWidget(self.Ridge)
        self.normalize_list.setMaximumSize(QtCore.QSize(16777215, 50))
        self.normalize_list.setObjectName("normalize_list")
        item = QtWidgets.QListWidgetItem()
        self.normalize_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.normalize_list.addItem(item)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.normalize_list)
        self.verticalLayout_2.addWidget(self.Ridge)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.min_alphaLabel.setText(("Min Alpha"))
        self.max_alphaLabel.setText(("Max Alpha"))
        self.n_alpha_label.setText(("# of Alphas"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        __sortingEnabled = self.fit_intercept_list.isSortingEnabled()
        self.fit_intercept_list.setSortingEnabled(False)
        item = self.fit_intercept_list.item(0)
        item.setText(("True"))
        item = self.fit_intercept_list.item(1)
        item.setText(("False"))
        self.fit_intercept_list.setSortingEnabled(__sortingEnabled)
        self.normalizeLabel.setText(("Normalize"))
        __sortingEnabled = self.normalize_list.isSortingEnabled()
        self.normalize_list.setSortingEnabled(False)
        item = self.normalize_list.item(0)
        item.setText(("True"))
        item = self.normalize_list.item(1)
        item.setText(("False"))
        self.normalize_list.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

