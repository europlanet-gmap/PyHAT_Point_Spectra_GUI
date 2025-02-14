from PyQt5 import QtWidgets
from libpyhat.transform.dim_reductions.lfda import LFDA
from point_spectra_gui.ui.dimred_LFDA import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, LFDA, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.nc_spin.setValue(8)

    def update(self,new_y_choices):
        self.changeComboListVars(self.class_col, new_y_choices)

    def run(self):
        ycol = self.class_col.currentText()
        metric = self.metric.currentText()
        knn = self.n_neighbors.value()
        params = {
            'r': self.nc_spin.value(),
            'metric':metric,
            'knn':knn}
        params_key = str(params)
        return params, params_key, ycol

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())