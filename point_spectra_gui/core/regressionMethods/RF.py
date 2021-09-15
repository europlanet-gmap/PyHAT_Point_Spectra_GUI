from PyQt5 import QtWidgets
from point_spectra_gui.ui.RandomForest import Ui_Form
from point_spectra_gui.util.Modules import Modules
from sklearn.ensemble import RandomForestRegressor


class Ui_Form(Ui_Form, RandomForestRegressor, Modules):
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

        params = {'n_estimators': self.numEstSpinBox.value(),
                  'max_depth': self.max_depthSpinBox.value(),
                  'random_state': 0
                  }
        return params, self.getChangedValues(params, RandomForestRegressor())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
