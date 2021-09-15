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
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.nc_label = QtWidgets.QLabel(self.groupBox)
        self.nc_label.setObjectName("nc_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nc_label)
        self.nc_spin = QtWidgets.QSpinBox(self.groupBox)
        self.nc_spin.setMinimum(1)
        self.nc_spin.setMaximum(1000)
        self.nc_spin.setProperty("value", 4)
        self.nc_spin.setObjectName("nc_spin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nc_spin)
        self.metric_label = QtWidgets.QLabel(self.groupBox)
        self.metric_label.setObjectName("metric_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.metric_label)
        self.metric = QtWidgets.QComboBox(self.groupBox)
        self.metric.setObjectName("metric")
        self.metric.addItem("")
        self.metric.addItem("")
        self.metric.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.metric)
        self.n_neighbors_label = QtWidgets.QLabel(self.groupBox)
        self.n_neighbors_label.setObjectName("n_neighbors_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.n_neighbors_label)
        self.n_neighbors = QtWidgets.QSpinBox(self.groupBox)
        self.n_neighbors.setMinimum(1)
        self.n_neighbors.setMaximum(10000)
        self.n_neighbors.setProperty("value", 5)
        self.n_neighbors.setObjectName("n_neighbors")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.n_neighbors)
        self.class_col_label = QtWidgets.QLabel(self.groupBox)
        self.class_col_label.setObjectName("class_col_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.class_col_label)
        self.class_col = QtWidgets.QComboBox(self.groupBox)
        self.class_col.setObjectName("class_col")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.class_col)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.nc_label.setText(("# of dimensions"))
        self.metric_label.setText(("Metric"))
        self.metric.setItemText(0, ("Plain"))
        self.metric.setItemText(1, ("Orthonormalized"))
        self.metric.setItemText(2, ("Weighted"))
        self.n_neighbors_label.setText(("# of neighbors"))
        self.class_col_label.setText(("Class column"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

