from PyQt5 import QtWidgets
from libpyhat.Unmixing.unmix import FCLS
from point_spectra_gui.ui.unmix_FCLS import Ui_Form
from point_spectra_gui.util.Modules import Modules

class Ui_Form(Ui_Form, FCLS, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        # self.checkMinAndMax()
        # self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def run(self):
        normalize = self.checkBox.isChecked()
        return normalize

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())