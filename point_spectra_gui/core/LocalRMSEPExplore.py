import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.util.spectral_data import spectral_data
from point_spectra_gui.ui.LocalRMSEPExplore import Ui_Form
from libpyhat.regression import local_rmsep
from point_spectra_gui.util.Modules import Modules
import numpy as np

class LocalRMSEPExplore(Ui_Form, Modules):


    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupLayout

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.refresh()
        self.chooseDataComboBox.currentIndexChanged.connect(self.refresh)
        self.hidefit()
        self.extrapolate_check.stateChanged.connect(self.hidefit)
        self.fitall.toggled.connect(self.set_radio_buttons)
        self.fit_local_min.toggled.connect(self.set_radio_buttons)

    def set_radio_buttons(self):
        if self.fitall.isChecked():
            self.fit_local_min.setChecked(False)
        if self.fit_local_min.isChecked():
            self.fitall.setChecked(False)

    def hidefit(self):
        if self.extrapolate_check.isChecked():
            hide = False
        else:
            hide = True

        self.fitall.setHidden(hide)
        self.fit_local_min.setHidden(hide)
        self.xmax.setHidden(hide)
        self.xmax_label.setHidden(hide)

    def refresh(self):
        self.changeComboListVars(self.choosecomp, self.get_choices('comp'))
        self.changeComboListVars(self.choosepredict, self.get_choices('predict'))

    def run(self):
        predictions = self.data[self.chooseDataComboBox.currentText()].df[('predict',self.choosepredict.currentText())]
        actuals = self.data[self.chooseDataComboBox.currentText()].df[('comp',self.choosecomp.currentText())]
        windowsize = [float(i) for i in self.window_size.text().split(',')]
        n_neighbors = np.array([int(i) for i in self.n_neighbors.text().split(',')])
        n_neighbors = n_neighbors[n_neighbors >= 1]
        sigma = [int(i) for i in self.sigma.text().split(',')]
        xmax = self.xmax.value()

        if self.plot_file.text() == '':
            plot_file = None
        else:
            plot_file = self.plot_file.text()

        fullfit = self.fitall.isChecked()
        local_rmsep.loacl_rmse_explore(predictions,actuals,windowsize=windowsize,min_rmsep_num=n_neighbors,sigma=sigma,
                                 plot_file=plot_file,xmax=xmax,outpath=self.outpath,element=self.choosecomp.currentText(),
                                 full_fit=fullfit)

    def get_choices(self, colname):
        try:
            choices = self.data[self.chooseDataComboBox.currentText()].df[colname].columns.values
            choices = [i for i in choices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            choices = ['No matching columns!']
        return choices


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = LocalRMSEPExplore()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
