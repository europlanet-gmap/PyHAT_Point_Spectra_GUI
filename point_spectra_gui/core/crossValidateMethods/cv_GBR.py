from PyQt5 import QtWidgets, QtCore
from sklearn.ensemble import GradientBoostingRegressor

from point_spectra_gui.ui.cv_GBR import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, GradientBoostingRegressor, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        pass

    def run(self):

        params = {'learning_rate': [float(i) for i in self.learninglineEdit.text().split(',')],
                    'n_estimators': [int(i) for i in self.numEstlineEdit.text().split(',')],
                    'max_depth': [int(i) for i in self.maxdepthlineEdit.text().split(',')],
                    'random_state': [0]}
        return params


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
