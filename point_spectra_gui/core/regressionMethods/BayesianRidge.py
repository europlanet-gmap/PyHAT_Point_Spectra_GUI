from PyQt5 import QtWidgets
from point_spectra_gui.ui.BayesianRidge import Ui_Form
from point_spectra_gui.util.Modules import Modules
from sklearn.linear_model import BayesianRidge


class Ui_Form(Ui_Form, BayesianRidge, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def toggle_params(self, widgets, state):
        for w in widgets:
            if state:
                w.setHidden(True)
            else:
                w.setHidden(False)

    def connectWidgets(self):
        self.alpha_checkbox.setChecked(True)
        alphawidgets = [self.alphalabel, self.alphadoubleSpinBox, self.alpha1Label, self.alpha1DoubleSpinBox, self.alpha2Label,
                        self.alpha2DoubleSpinBox]
        self.toggle_params(alphawidgets, self.alpha_checkbox.isChecked())
        self.lambda_checkbox.setChecked(True)
        lambdawidgets = [self.lambdaLabel, self.lambdaDoubleSpinBox, self.L1label, self.L1doubleSpinBox,
                         self.L2label, self.L2doubleSpinBox]
        self.toggle_params(lambdawidgets, self.lambda_checkbox.isChecked())
        self.alpha_checkbox.stateChanged.connect(
            lambda: self.toggle_params(alphawidgets, self.alpha_checkbox.isChecked()))
        self.lambda_checkbox.stateChanged.connect(
            lambda: self.toggle_params(lambdawidgets, self.lambda_checkbox.isChecked()))

    def run(self):
        if self.alpha_checkbox.isChecked() == True:
            alpha_init = None
        else:
            alpha_init = self.alphadoubleSpinBox.value()

        if self.lambda_checkbox.isChecked() == True:
            lambda_init = None
        else:
            lambda_init = self.lambdaDoubleSpinBox.value()

        params = {'n_iter': self.numOfIterationsSpinBox.value(),
                  'tol': self.toleranceDoubleSpinBox.value(),
                  'alpha_init':alpha_init,
                  'alpha_1': self.alpha1DoubleSpinBox.value(),
                  'alpha_2': self.alpha2DoubleSpinBox.value(),
                  'lambda_init':lambda_init,
                  'lambda_1': self.lambdaDoubleSpinBox.value(),
                  'lambda_2': self.lambdaDoubleSpinBox.value(),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'normalize': self.normalizeCheckBox.isChecked(),
                  }
        return params, self.getChangedValues(params, BayesianRidge())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
