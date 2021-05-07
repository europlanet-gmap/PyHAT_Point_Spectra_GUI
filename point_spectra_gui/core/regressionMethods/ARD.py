from PyQt5 import QtWidgets
from sklearn.linear_model import ARDRegression

from point_spectra_gui.ui.ARD import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, ARDRegression, Modules):
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
        alphawidgets = [self.alpha1Label, self.alpha1DoubleSpinBox, self.alpha2Label, self.alpha2DoubleSpinBox]
        lambdawidgets = [self.lambdaLabel, self.lambdaDoubleSpinBox, self.lambdaLabel_2, self.lambdaDoubleSpinBox_2]
        self.alpha_checkbox.stateChanged.connect(
            lambda: self.toggle_params(alphawidgets, self.alpha_checkbox.isChecked()))
        self.lambda_checkbox.stateChanged.connect(
            lambda: self.toggle_params(lambdawidgets, self.lambda_checkbox.isChecked()))
        self.alpha_checkbox.setChecked(True)
        self.lambda_checkbox.setChecked(True)


    def run(self):
        params = {
            'n_iter': self.numOfIterationsSpinBox.value(),
            'tol': self.toleranceDoubleSpinBox.value(),
            'alpha_1': self.alpha1DoubleSpinBox.value(),
            'alpha_2': self.alpha2DoubleSpinBox.value(),
            'lambda_1': self.lambdaDoubleSpinBox.value(),
            'lambda_2': self.lambdaDoubleSpinBox_2.value(),
            'threshold_lambda': self.thresholdLambdaSpinBox.value(),
            'fit_intercept': self.fitInterceptCheckBox.isChecked(),
            'normalize': self.normalizeCheckBox.isChecked(),
        }
        return params, self.getChangedValues(params, ARDRegression())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
