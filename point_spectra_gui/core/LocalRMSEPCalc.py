import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.util.spectral_data import spectral_data
from point_spectra_gui.ui.LocalRMSEPCalc import Ui_Form
from libpyhat.regression import local_rmsep
from point_spectra_gui.util.Modules import Modules
import numpy as np

class LocalRMSEPCalc(Ui_Form, Modules):


    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupLayout

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.chooseUnkData, self.datakeys)
        self.refresh()
        self.chooseDataComboBox.currentIndexChanged.connect(self.refresh)
        self.chooseUnkData.currentIndexChanged.connect(self.refresh)
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
        self.changeComboListVars(self.chooseUnkpredict, self.get_choices_unk('predict'))

    def run(self):
        predictions = self.data[self.chooseDataComboBox.currentText()].df[('predict',self.choosepredict.currentText())]
        actuals = self.data[self.chooseDataComboBox.currentText()].df[('comp',self.choosecomp.currentText())]
        unk_predicts = self.data[self.chooseUnkData.currentText()].df[('predict',self.chooseUnkpredict.currentText())]
        windowsize = self.win_size_spin.value()
        n_neighbors = self.n_neighbors_spin.value()
        sigma = self.sigma_spin.value()

        xmax = self.xmax.value()
        extrap = self.extrapolate_check.isChecked()
        fullfit = self.fitall.isChecked()
        local_rmseps = local_rmsep.local_rmse_calc(predictions,actuals,unk_predicts,windowsize=windowsize,min_rmsep_num=n_neighbors,
                                    sigma=sigma,extrapolate=extrap,full_fit=fullfit,xmax=xmax)
        self.data[self.chooseUnkData.currentText()].df[('predict','Local_RMSEP - '+self.chooseUnkpredict.currentText())]=local_rmseps


    def get_choices(self, colname):
        try:
            choices = self.data[self.chooseDataComboBox.currentText()].df[colname].columns.values
            choices = [i for i in choices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            choices = ['No matching columns!']
        return choices
    def get_choices_unk(self, colname):
        try:
            choices = self.data[self.chooseUnkData.currentText()].df[colname].columns.values
            choices = [i for i in choices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            choices = ['No matching columns!']
        return choices


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = LocalRMSEP()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
