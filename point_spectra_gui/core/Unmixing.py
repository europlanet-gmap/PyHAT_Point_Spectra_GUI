from PyQt5 import QtWidgets

from point_spectra_gui.util import Qtickle
from point_spectra_gui.core.unmixingMethods import *
from point_spectra_gui.ui.Unmixing import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.util.spectral_data import spectral_data
#import mesma
from libpyhat.Unmixing.unmix import unmix

class Unmixing(Ui_Form, Modules):
    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Modules.setupUi(self, Form)
        self.unmixingMethods()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.algorithm_list = ['Choose an algorithm',
                               'NNLS',
                               'FCLS',
                               'UCLS']#,
                               #'MESMA']

        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.endmemberscomboBox, self.datakeys)
        self.setComboBox(self.chooseMethodComboBox, self.algorithm_list)
        self.chooseMethodComboBox.currentIndexChanged.connect(
            lambda: self.make_unmix_widget(self.chooseMethodComboBox.currentText()))

    def getGuiParams(self):
        """
        Overriding Modules' getGuiParams, because I'll need to do a list of lists
        in order to obtain the regressionMethods' parameters
        """
        self.qt = Qtickle.Qtickle(self)
        s = []
        s.append(self.qt.guiSave())
        for items in self.alg:
            s.append(items.getGuiParams())
        return s

    def setGuiParams(self, dict):
        """
        Overriding Modules' setGuiParams, because we are accessing a list of lists
        And each submodule contains it's own `setGuiParams`
        """
        self.qt = Qtickle.Qtickle(self)
        self.qt.guiRestore(dict[0])
        for i in range(len(dict)):
            self.alg[i - 1].setGuiParams(dict[i])

    def selectiveSetGuiParams(self, dict):
        """
        Override Modules' selective Restore function

        Setup Qtickle
        selectively restore the UI, the data to do that will be in the 0th element of the dictionary
        We will then iterate through the rest of the dictionary
        Will now restore the parameters for the algorithms in the list, Each of the algs have their own selectiveSetGuiParams

        :param dict:
        :return:
        """

        self.qt = Qtickle.Qtickle(self)
        self.qt.selectiveGuiRestore(dict[0])
        for i in range(len(dict)):
            self.alg[i - 1].selectiveSetGuiParams(dict[i])


    def run(self):
        col = 'wvl'
        method = self.chooseMethodComboBox.currentText()
        datakey = self.chooseDataComboBox.currentText()
        endmembers = self.endmemberscomboBox.currentText()

        normalize = self.getMethodParams(self.chooseMethodComboBox.currentIndex())
        mask = None
        self.data[datakey].df = unmix(self.data[datakey].df, self.data[endmembers].df,normalize,mask,col=col,unmix_method=method)

    def make_unmix_widget(self, alg, params=None):
        self.hideAll()
        #print(alg)
        for i in range(len(self.algorithm_list)):
            if alg == self.algorithm_list[i]:
                self.alg[i - 1].setHidden(False)

    def hideAll(self):
        for a in self.alg:
            a.setHidden(True)

    def unmixingMethods(self):
        self.alg = []
        list_forms = [unmix_NNLS,
                      unmix_FCLS,
                      unmix_UCLS]#,
                      #unmix_MESMA]
        for items in list_forms:
            self.alg.append(items.Ui_Form())
            self.alg[-1].setupUi(self.Form)
            self.dim_reduction_vlayout.addWidget(self.alg[-1].get_widget())
            self.alg[-1].setHidden(True)

    def getMethodParams(self, index):
        return self.alg[index - 1].run()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()

    ui = Unmixing()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



