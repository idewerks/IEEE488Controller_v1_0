# Main code for the HPIB Instrument Manager
# IDEwerks Inc. 3/2021

# UI is generated within Qt Designer and saved as a .ui xml file
# pyuic is used to convert the ui to python code. I have a script in PyCharm that handles all that

import sys
import pyvisa
import processInstrument
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from IEEE488mainwindow import Ui_IEEE488InstrumentManager
from HP34401AdialogMain import HP34401Adialog
rm = pyvisa.ResourceManager()


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
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
        self.ui.loadInstrumentButton.clicked.connect(self.loadinstrclicked)

    def dialog_box(self):
        self.myDialog.show()

    def scanbtn_clicked(self):
        # Scan for instruments & update the label showing the currently used shared visa library
        self.ui.shared_visa_lib_label.setText(str(rm))
        self.ui.instrumentcomboBox.clear()
        valid_resources = rm.list_resources()
        for x in valid_resources:
            self.ui.instrumentcomboBox.addItem(x)  # populate the combo box with available instruments

    def inst_combobox_selected(self, instrument):
        # An instrument has been selected here in the combo box
        # The value of instrument holds the currently selected visa address
        current_selected_instrument = instrument
        a = processInstrument.getInstrumentInfo(rm, current_selected_instrument)

    def loadinstrclicked(self):
        # todo pass gpib address parameters when we call dialogbox()
        self.dialog_box()

    def exitbtnclicked(self):
        app.quit()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec_())
