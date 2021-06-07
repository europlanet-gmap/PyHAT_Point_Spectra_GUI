from PyQt5 import QtWidgets

from point_spectra_gui.ui.RenameColumn import Ui_Form
from point_spectra_gui.util.Modules import Modules
import numpy as np

class RenameColumn(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.choosedata_comboBox.currentIndexChanged.connect(lambda: self.update_lvl0())
        self.choosecol_lvl0.currentIndexChanged.connect(lambda: self.update_lvl1())
        self.setComboBox(self.choosedata_comboBox, self.datakeys)

    def update_lvl0(self):
        self.vars_level0 = np.unique(self.data[self.choosedata_comboBox.currentText()].df.columns.get_level_values(0))
        self.setComboBox(self.choosecol_lvl0, self.vars_level0)

    def update_lvl1(self):
        self.vars_level1 = np.array(self.data[self.choosedata_comboBox.currentText()].df[self.choosecol_lvl0.currentText()].columns.values)
        self.setComboBox(self.choosecol_lvl1, self.vars_level1)

    def run(self):
        old_lvl0 = self.choosecol_lvl0.currentText()
        old_lvl1 = self.choosecol_lvl1.currentText()
        new_lvl0 = self.new_lvl0_lineEdit.text()
        new_lvl1 = self.new_lvl1_lineEdit.text()
        #convert to float if possible
        try:
            new_lvl0 = float(new_lvl0)
        except:
            pass
        try:
            new_lvl1 = float(new_lvl1)
        except:
            pass
        dataname = self.choosedata_comboBox.currentText()
        data = self.data[dataname].df
        data[(new_lvl0,new_lvl1)] = data[(old_lvl0,old_lvl1)] #create the new column
        self.data[dataname].df = data.drop((old_lvl0,old_lvl1),axis=1) #drop the old column


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = RenameColumn()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
