from PyQt5 import QtWidgets
from point_spectra_gui.ui.GBR import Ui_Form
from point_spectra_gui.util.Modules import Modules
from sklearn.ensemble import GradientBoostingRegressor


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

        params = {'learning_rate': self.learningDoubleSpinBox.value(),
                  'n_estimators': self.numEstSpinBox.value(),
                  'max_depth': self.max_depthSpinBox.value(),
                  'random_state': 0
                  }
        return params, self.getChangedValues(params, GradientBoostingRegressor())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
