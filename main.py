### Main code for the HPIB Instrument Manager

### IDEwerks Inc. 3/2021

# UI is generated within Qt Designer and saved as a .ui xml file
# pyuic is used to convert the ui to python code.
# Nothing Fancy, but added a bunch of code to allow embedding a pyqtgraph plot
#
# Needs some optimization, but basically works with some functionality not yet implemented

import sys

import pyvisa
import processInstrument
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QDialog, QMainWindow, QFileDialog

from IEEE488mainwindow import Ui_IEEE488InstrumentManager
from HP34401AdialogMain import HP34401Adialog
rm = pyvisa.ResourceManager()

class MyWindow(QMainWindow):

    def __init__(self, parent=None):
        # super(MyWindow, self).__init__(parent)
        super().__init__(parent)
        self.myDialog = HP34401Adialog()
        self.ui = Ui_IEEE488InstrumentManager()
        self.ui.setupUi(self)
        # define method when scan button is clicked
        self.ui.ScanButton.clicked.connect(self.scanbtn_clicked)
        # define method when instr selected
        self.ui.instrumentcomboBox.activated[str].connect(
            self.inst_combobox_selected)
        self.ui.exitButton.clicked.connect(self.exitbtnclicked)
        # Open a new window for the HP34401a Instrument when clicked
        self.ui.loadInstrumentButton.clicked.connect(self.loadinstrclicked)

    def dialogbox(self):
        # self.hide
        self.myDialog.show()
        print("just hit show")

    def scanbtn_clicked(self):
        # Scan for instruments & update the label showing the currently used shared visa library
        self.ui.shared_visa_lib_label.setText(str(rm))
        self.ui.instrumentcomboBox.clear()
        # enumerate the rm resource tuple to extract the currently active instrument addresses
        # and add it to gui element
        valid_resources = rm.list_resources()
        # Populate a combo box with the resources
        for x in valid_resources:
            # print(x)
            self.ui.instrumentcomboBox.addItem(x)  # populate the combo box with available instruments

    def inst_combobox_selected(self, instrument):
        # An instrument has been selected here in the combo box
        # The value of instrument holds the currently selected visa address
        current_selected_instrument = instrument
        processInstrument.getInstrumentInfo(rm, current_selected_instrument)

    def loadinstrclicked(self):
        # self.close()
        # todo pass gpib address parameters when we call dialogbox()

        self.dialogbox()

    def exitbtnclicked(self):
        app.quit()


# Use this for apps that pass in command line parameters
# app = QApplication(sys.argv)
# Use this for apps with no command line parameters
app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec_())
