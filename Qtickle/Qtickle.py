import inspect
import os
from PyQt5 import QtCore
from distutils.util import strtobool
import sys
from PyQt5.QtWidgets import *


class Qtickle(object):
    def __init__(self, ui):
        self.ui = ui

    def guisave(self):
        dict = {}
        # Save geometry
        # self.settings.setValue('size', self.ui.size())
        # self.settings.setValue('pos', self.ui.pos())
        try:
            for name, obj in inspect.getmembers(self.ui):
                if isinstance(obj, QLineEdit):
                    name = obj.objectName()
                    value = obj.text()
                    dict[name] = value

                if isinstance(obj, QCheckBox):
                    name = obj.objectName()
                    state = obj.isChecked()
                    dict[name] = state

                if isinstance(obj, QRadioButton):
                    name = obj.objectName()
                    value = obj.isChecked()  # get stored value from registry
                    dict[name] = value

                if isinstance(obj, QSpinBox):
                    name = obj.objectName()
                    value = obj.value()  # get stored value from registry
                    dict[name] = value

                if isinstance(obj, QDoubleSpinBox):
                    name = obj.objectName()
                    value = obj.value()
                    dict[name] = value

                if isinstance(obj, QSlider):
                    name = obj.objectName()
                    value = obj.value()  # get stored value from registry
                    dict[name] = value

                if isinstance(obj, QLabel):
                    name = obj.objectName()
                    value = obj.text()
                    dict[name] = value

                if isinstance(obj, QComboBox):
                    values = []  # the list that will hold all values from QCombobox
                    name = obj.objectName()  # get the QCombobox object's name
                    for i in range(obj.count()):  # QCombobox contains a number of items
                        itemData = obj.itemText(i)
                        values.append(itemData)  # put those items into a list for saving
                    index = obj.findText(obj.currentText())  # return the index of the item, assign to selected
                    dict[name + "_values"] = values  # save all the values in settings
                    dict[name + "_index"] = index  # save the indexed value in settings

                if isinstance(obj, QListWidget):
                    values = []
                    name = obj.objectName()
                    for i in range(obj.count()):
                        itemData = str(obj.item(i).text())  # Get all the string data
                        values.append(itemData)  # add it to a list
                    dict[name + "_values"] = values
                    # since there is a possibility of multiple items,
                    # we'll just save the string representation of those items to be restored
                    dict[name + "_index"] = [str(x.text()) for x in obj.selectedItems()]

            print(dict)  # Debug purposes
            return dict
        except Exception as e:
            print(e)

    def guirestore(self, dict):
        # Restore geometry
        # self.ui.resize(self.settings.value('size', QtCore.QSize(500, 500)))
        # self.ui.move(self.settings.value('pos', QtCore.QPoint(60, 60)))
        for name, obj in inspect.getmembers(self.ui):
            try:
                if isinstance(obj, QLineEdit):
                    name = obj.objectName()
                    value = dict[name]
                    obj.setText(value)  # restore lineEditFile

                if isinstance(obj, QCheckBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        try:
                            obj.setChecked(strtobool(value))  # restore checkbox
                        except:
                            obj.setChecked(value)

                if isinstance(obj, QRadioButton):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setChecked(strtobool(value))

                if isinstance(obj, QSlider):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(int(value))  # restore value from registry

                if isinstance(obj, QSpinBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(int(value))  # restore value from registry

                if isinstance(obj, QDoubleSpinBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(int(value))

                if isinstance(obj, QLabel):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setText(value)

                if isinstance(obj, QComboBox):
                    name = obj.objectName()
                    values = dict[name + "_values"]
                    # clear all the objects
                    # so that we don't run into issues
                    # with restoring the list of values
                    obj.clear()
                    if values is not None:
                        for value in values:
                            if not (value == '' or value == "") and len(value) > 0:
                                # if there are some values in the list, we should add them to the Combobox
                                obj.addItem(value)

                    index = dict[name + "_index"]  # next we want to select the item in question by getting it's index
                    obj.setCurrentIndex(int(index))

                if isinstance(obj, QListWidget):
                    name = obj.objectName()
                    values = dict[name + "_values"]
                    obj.clear()
                    if values is not None:
                        for value in values:
                            list_item = QListWidgetItem(value)
                            obj.addItem(list_item)
                    index = dict[name + "_index"]
                    try:
                        obj.setCurrentItem(obj.findItems(index, QtCore.Qt.MatchExactly)[0])
                    except:
                        pass

            except Exception as e:
                print(e)

