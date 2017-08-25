import multiprocessing as mp
import os.path
import sys
import time

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from point_spectra_gui.future_.functions import *
from point_spectra_gui.future_.util import delete
from point_spectra_gui.future_.util.excepthook import my_exception_hook


def new():
    p = mp.Process(target=main, args=())
    p.start()


def connectWidgets(ui):
    """
    Connect all the widgets associated with the MainWindow UI
    :param ui:
    :return:
    """
    # TODO figure out how to get this code into `MainWindow.py`
    ui.actionRead_ChemCam_Data.triggered.connect(lambda: ui.addWidget(ReadChemCamData.Ui_Form))
    ui.actionRemove_Baseline.triggered.connect(lambda: ui.addWidget(BaselineRemoval.Ui_Form))
    ui.actionCross_Validation.triggered.connect(lambda: ui.addWidget(CrossValidation.Ui_Form))
    ui.actionDimensionality_Reduction.triggered.connect(lambda: ui.addWidget(DimensionalityReduction.Ui_Form))
    ui.actionInterpolate.triggered.connect(lambda: ui.addWidget(Interpolation.Ui_Form))
    ui.actionLoad_Data.triggered.connect(lambda: ui.addWidget(LoadData.Ui_Form))
    ui.actionApply_Mask.triggered.connect(lambda: ui.addWidget(MaskData.Ui_Form))
    ui.actionMultiply_by_Vector.triggered.connect(lambda: ui.addWidget(MultiplyByVector.Ui_Form))
    ui.actionNormalization.triggered.connect(lambda: ui.addWidget(Normalization.Ui_Form))
    ui.actionSet_Output_Path.triggered.connect(lambda: ui.addWidget(OutputFolder.Ui_Form))
    ui.actionPeak_Areas.triggered.connect(lambda: ui.addWidget(PeakAreas.Ui_Form))
    ui.actionPlot.triggered.connect(lambda: ui.addWidget(Plot.Ui_Form))
    ui.actionPlot_ICA_PCA.triggered.connect(lambda: ui.addWidget(Plot_ICA_PCA.Ui_Form))
    ui.actionPlot_Spectra.triggered.connect(lambda: ui.addWidget(PlotSpectra.Ui_Form))
    ui.actionTrain.triggered.connect(lambda: ui.addWidget(RegressionTrain.Ui_Form))
    ui.actionRemove_Rows.triggered.connect(lambda: ui.addWidget(RemoveRows.Ui_Form))
    ui.actionSplit_Data.triggered.connect(lambda: ui.addWidget(SplitDataset.Ui_Form))
    ui.actionStratified_Folds.triggered.connect(lambda: ui.addWidget(StratifiedFolds.Ui_Form))
    ui.actionSubmodel_Predict.triggered.connect(lambda: ui.addWidget(SubmodelPredict.Ui_Form))
    ui.deleteModulePushButton.clicked.connect(lambda: delete.del_layout(ui.verticalLayout_3))
    ui.actionCreate_New_Workflow.triggered.connect(lambda: new())
    ui.actionExit.triggered.connect(lambda: sys.exit())
    ui.actionSave_Current_Workflow.triggered.connect(lambda: ui.on_save_clicked())


def get_splash(app):
    """
    Get the splash screen for the application
    But check to see if the image even exists
    :param app:
    :return:
    """
    dir = '../../images/'
    if os.path.exists(dir + 'splash.png'):
        splash_pix = QPixmap(dir + 'splash.png')  # default
        app_icon = QtGui.QIcon(dir + 'icon.png')
        app.setWindowIcon(app_icon)
        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setMask(splash_pix.mask())
        splash.show()
        time.sleep(0.5)
        app.processEvents()


def main():
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    app = QtWidgets.QApplication(sys.argv)
    get_splash(app)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindow.Ui_MainWindow()
    ui.setupUi(mainWindow)
    connectWidgets(ui)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
