from PyQt5 import QtWidgets, QtCore
from sklearn.linear_model import BayesianRidge

from point_spectra_gui.ui.cv_BayesianRidge import Ui_Form
from point_spectra_gui.util.Modules import Modules


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
        alphawidgets = [self.alpha_label, self.alpha_lineEdit, self.alpha1Label, self.alpha1LineEdit, self.alpha2Label, self.alpha2LineEdit]
        self.toggle_params(alphawidgets,self.alpha_checkbox.isChecked())
        self.lambda_checkbox.setChecked(True)
        lambdawidgets = [self.lambda_label,self.lambda_lineEdit, self.lambda1Label, self.lambda1LineEdit, self.lambda2_label, self.lambda2LineEdit]
        self.toggle_params(lambdawidgets, self.lambda_checkbox.isChecked())
        self.alpha_checkbox.stateChanged.connect(
            lambda: self.toggle_params(alphawidgets, self.alpha_checkbox.isChecked()))
        self.lambda_checkbox.stateChanged.connect(
            lambda: self.toggle_params(lambdawidgets, self.lambda_checkbox.isChecked()))


    def run(self):
        fit_intercept_items = [i.text() == 'True' for i in self.fitIntercept_List.selectedItems()]
        normalize_items = [i.text() == 'True' for i in self.normalize_List.selectedItems()]
        if self.alpha_checkbox.isChecked() == True:
            alpha_init = [None]
        else:
            alpha_init = [float(i) for i in self.alpha_lineEdit.text().split(',')]

        if self.lambda_checkbox.isChecked() == True:
            lambda_init = [None]
        else:
            lambda_init = [float(i) for i in self.lambda_lineEdit.text().split(',')]

        params = {
            'n_iter': [int(i) for i in self.numOfIterationsLineEdit.text().split(',')],
            'tol': [float(i) for i in self.toleranceLineEdit.text().split(',')],
            'alpha_init':alpha_init,
            'alpha_1': [float(i) for i in self.alpha1LineEdit.text().split(',')],
            'alpha_2': [float(i) for i in self.alpha2LineEdit.text().split(',')],
            'lambda_init': lambda_init,
            'lambda_1': [float(i) for i in self.lambda1LineEdit.text().split(',')],
            'lambda_2': [float(i) for i in self.lambda2LineEdit.text().split(',')],
            'compute_score': [False],
            'fit_intercept': fit_intercept_items,
            'normalize': normalize_items,
            'copy_X': [True],
            'verbose': [True]}

        return params


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
