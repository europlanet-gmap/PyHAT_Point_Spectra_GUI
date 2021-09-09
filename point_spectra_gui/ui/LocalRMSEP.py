# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupLayout = QtWidgets.QGroupBox(Form)
        self.groupLayout.setObjectName("groupLayout")
        self.gridLayout = QtWidgets.QGridLayout(self.groupLayout)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupLayout)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.n_neighbors = QtWidgets.QLineEdit(self.groupLayout)
        self.n_neighbors.setObjectName("n_neighbors")
        self.gridLayout.addWidget(self.n_neighbors, 4, 1, 1, 1)
        self.window_size = QtWidgets.QLineEdit(self.groupLayout)
        self.window_size.setObjectName("window_size")
        self.gridLayout.addWidget(self.window_size, 5, 1, 1, 1)
        self.sigma = QtWidgets.QLineEdit(self.groupLayout)
        self.sigma.setObjectName("sigma")
        self.gridLayout.addWidget(self.sigma, 6, 1, 1, 1)
        self.chooseAlgorithmLabel = QtWidgets.QLabel(self.groupLayout)
        self.chooseAlgorithmLabel.setObjectName("chooseAlgorithmLabel")
        self.gridLayout.addWidget(self.chooseAlgorithmLabel, 4, 0, 1, 1)
        self.choosepredict = QtWidgets.QComboBox(self.groupLayout)
        self.choosepredict.setObjectName("choosepredict")
        self.gridLayout.addWidget(self.choosepredict, 2, 1, 1, 1)
        self.prediction_label = QtWidgets.QLabel(self.groupLayout)
        self.prediction_label.setObjectName("prediction_label")
        self.gridLayout.addWidget(self.prediction_label, 2, 0, 1, 1)
        self.choosecomp = QtWidgets.QComboBox(self.groupLayout)
        self.choosecomp.setObjectName("choosecomp")
        self.gridLayout.addWidget(self.choosecomp, 1, 1, 1, 1)
        self.chooseDataLabel = QtWidgets.QLabel(self.groupLayout)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.extrapolate_check = QtWidgets.QCheckBox(self.groupLayout)
        self.extrapolate_check.setObjectName("extrapolate_check")
        self.gridLayout.addWidget(self.extrapolate_check, 7, 0, 1, 1)
        self.sigma_label = QtWidgets.QLabel(self.groupLayout)
        self.sigma_label.setObjectName("sigma_label")
        self.gridLayout.addWidget(self.sigma_label, 6, 0, 1, 1)
        self.plot_file_label = QtWidgets.QLabel(self.groupLayout)
        self.plot_file_label.setObjectName("plot_file_label")
        self.gridLayout.addWidget(self.plot_file_label, 10, 0, 1, 1)
        self.plot_file = QtWidgets.QLineEdit(self.groupLayout)
        self.plot_file.setObjectName("plot_file")
        self.gridLayout.addWidget(self.plot_file, 10, 1, 1, 1)
        self.fit_local_min = QtWidgets.QRadioButton(self.groupLayout)
        self.fit_local_min.setObjectName("fit_local_min")
        self.gridLayout.addWidget(self.fit_local_min, 8, 1, 1, 1)
        self.fitall = QtWidgets.QRadioButton(self.groupLayout)
        self.fitall.setChecked(True)
        self.fitall.setObjectName("fitall")
        self.gridLayout.addWidget(self.fitall, 8, 0, 1, 1)
        self.truecomp_label = QtWidgets.QLabel(self.groupLayout)
        self.truecomp_label.setObjectName("truecomp_label")
        self.gridLayout.addWidget(self.truecomp_label, 1, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupLayout)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.xmax = QtWidgets.QDoubleSpinBox(self.groupLayout)
        self.xmax.setMaximum(1000000.0)
        self.xmax.setObjectName("xmax")
        self.gridLayout.addWidget(self.xmax, 9, 1, 1, 1)
        self.xmax_label = QtWidgets.QLabel(self.groupLayout)
        self.xmax_label.setObjectName("xmax_label")
        self.gridLayout.addWidget(self.xmax_label, 9, 0, 1, 1)
        self.window_size_label = QtWidgets.QLabel(self.groupLayout)
        self.window_size_label.setObjectName("window_size_label")
        self.gridLayout.addWidget(self.window_size_label, 5, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupLayout.setTitle(("Local RMSEP"))
        self.label.setText(("Separate multiple values with commas:"))
        self.n_neighbors.setText(("40"))
        self.window_size.setText(("0"))
        self.sigma.setText(("10"))
        self.chooseAlgorithmLabel.setText(("Minimum # of neighbors"))
        self.prediction_label.setText(("Prediction"))
        self.chooseDataLabel.setText(("Choose test data set"))
        self.extrapolate_check.setText(("Extrapolate?"))
        self.sigma_label.setText(("Sigma (smoothing)"))
        self.plot_file_label.setText(("Plot file (optional)"))
        self.fit_local_min.setText(("Fit from last local minimum"))
        self.fitall.setText(("Fit all"))
        self.truecomp_label.setText(("True composition"))
        self.xmax_label.setText(("Extrapolate to"))
        self.window_size_label.setText(("Window size (same units as predictions)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

