# This is the main dialog window for the HP34401A Instrument
# This is called by main.py

import csv
import sys
import time
import pyvisa

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QMainWindow, QFileDialog
from HP34401AdialogGridF import Ui_HP34401ADialog  # Get the Designer compiled dialog python class stub

rm = pyvisa.ResourceManager()


class HP34401Adialog(QDialog):
    def __init__(self):
        super(HP34401Adialog, self).__init__()
        self.HpDmm = rm.open_resource('GPIB0::22::INSTR')
        self.ui = Ui_HP34401ADialog()
        self.ui.setupUi(self)
        # access your UI elements through the `ui` attribute
        # Create a placeholder plot we can update later
        self.plot = self.ui.plotWidget.plot(x=[1.0, 2.0, 3.0, 4.0],
                                            y=[1.0, 2.0, 3.0, 4.0], pen="r", symbol="o", symbolBrush="g")

        self.ui.plotWidget.showGrid(x=True, y=True)
        # Set the time axis labels
        self.ui.plotWidget.setLabel('bottom', 'TIME', units='unix')
        # a = self.plot.getAxis('left')

        self.ui.plotWidget.getAxis('left').setTextPen('y')
        self.ui.plotWidget.getAxis('bottom').setTextPen('g')

        self.ui.progressBar.setValue(0)
        self.collectedData = []
        self.mytimestamp = []
        self.inst_mode = "DCV"
        self.sample = 0
        self.number_samples = 4
        self.ui.sampledisplayLabel.setText('TOTAL SAMPLES= ' + str(self.number_samples))

        self.scantimer = QTimer(self)
        self.sampletimerset = 100
        self.ui.savescanpushButton.hide()
        self.ui.samplestoppushButton.hide()

        # Setup Event Handlers
        # Sampling event handlers here
        self.ui.samplestartpushButton.clicked.connect(self.start_sample_timer)
        self.ui.samplestoppushButton.clicked.connect(self.stop_sample_timer)
        self.ui.samplesSlider.valueChanged.connect(self.sample_count_change)

        self.ui.TriggerDelaySlider.valueChanged.connect(self.trigger_delay_change)

        self.scantimer.timeout.connect(self.start_scan)

        # event handlers for mode button group
        self.ui.ACIpushButton.clicked.connect(self.set_aci_mode)
        self.ui.DCVpushButton.clicked.connect(self.set_dcv_mode)
        self.ui.CONpushButton.clicked.connect(self.set_con_mode)
        self.ui.ACVpushButton.clicked.connect(self.set_acv_mode)
        self.ui.DCIpushButton.clicked.connect(self.set_dci_mode)
        self.ui.DIOpushButton.clicked.connect(self.set_dio_mode)
        self.ui.FREpushButton.clicked.connect(self.set_fre_mode)
        self.ui.PERpushButton.clicked.connect(self.set_per_mode)
        self.ui.FWOpushButton.clicked.connect(self.set_fwo_mode)
        self.ui.TWOpushButton.clicked.connect(self.set_two_mode)
        self.ui.ExitpushButton.clicked.connect(self.exit_hp34401)
        self.ui.savescanpushButton.clicked.connect(self.savescan)

        self.ui.statustextBrowser.append('Reset and Clear Instrument')
        self.ui.statustextBrowser.append(self.HpDmm.query("*IDN?"))
        self.ui.statustextBrowser.append('Placing Instrument in remote mode')

        # Instrument Settings:
        # Populate the comboboxes

        self.ui.ImpedanceCombobox.addItem('Auto On')  # populate the combo box with available options
        # self.ui.ImpedanceCombobox.addItem('On')
        self.ui.ImpedanceCombobox.addItem('Auto Off')

        self.ui.AutozeroCombobox.addItem('On')
        self.ui.AutozeroCombobox.addItem('Off')
        self.ui.AutozeroCombobox.addItem('Once')

        self.ui.RangeCombobox.addItem('.01')
        self.ui.RangeCombobox.addItem('.1')
        self.ui.RangeCombobox.addItem('1.0')
        self.ui.RangeCombobox.addItem('10')
        self.ui.RangeCombobox.addItem('100')
        self.ui.RangeCombobox.addItem('Auto')

        self.ui.ResolutionCombobox.addItem('.01')
        self.ui.ResolutionCombobox.addItem('.001')
        self.ui.ResolutionCombobox.addItem('.0001')
        self.ui.ResolutionCombobox.addItem('.00001')
        self.ui.ResolutionCombobox.addItem('.000001')

        self.ui.NplcCombobox.addItem('.02')
        self.ui.NplcCombobox.addItem('.2')
        self.ui.NplcCombobox.addItem('1')
        self.ui.NplcCombobox.addItem('10')
        self.ui.NplcCombobox.addItem('100')

        self.ui.FreqapertureCombobox.addItem('.01')
        self.ui.FreqapertureCombobox.addItem('.1')
        self.ui.FreqapertureCombobox.addItem('1')

        self.ui.PeriodapertureCombobox.addItem('.01')
        self.ui.PeriodapertureCombobox.addItem('.1')
        self.ui.PeriodapertureCombobox.addItem('1')

        self.ui.ACbandwidthCombobox.addItem('3')
        self.ui.ACbandwidthCombobox.addItem('20')
        self.ui.ACbandwidthCombobox.addItem('200')

        self.ui.MathCombobox.addItem('Enabled')
        self.ui.MathCombobox.addItem('Disabled')

        self.ui.TrigsrcCombobox.addItem('Immediate')
        self.ui.TrigsrcCombobox.addItem('External')
        self.ui.TrigsrcCombobox.addItem('Bus')

        # self.ui.TrigdelayCombobox.addItem()

    def process_mode_buttons(self, button):
        # This is called whenever a mode button is pressed (DCV,ACV, etc). It basically changes the background color
        # each time a button is clicked. We also  need to remember the state of all the buttons, and make sure
        # one and and only one mode can be entered.We pass the button name as part of the method call.
        # Make sure the button is set as 'checkable' in Designer.
        # This sets the button behavior so it changes color states

        # Set all the buttons in the mode group to unchecked, then set the button selected to True (checked)
        # This sets the 'one and only one' button logic for the mode group
        self.ui.DCVpushButton.setChecked(False)
        self.ui.DIOpushButton.setChecked(False)
        self.ui.CONpushButton.setChecked(False)
        self.ui.DCIpushButton.setChecked(False)
        self.ui.ACVpushButton.setChecked(False)
        self.ui.FREpushButton.setChecked(False)
        self.ui.PERpushButton.setChecked(False)
        self.ui.ACIpushButton.setChecked(False)
        self.ui.FWOpushButton.setChecked(False)
        self.ui.TWOpushButton.setChecked(False)

        button.setChecked(True)
        # we need to manage the UI element states better. This will add functionality later
        # to allow various setup modes to be stored & recalled. Once we refactor to MV it should be much easier

    def set_aci_mode(self):
        self.process_mode_buttons(self.ui.ACIpushButton)
        self.inst_mode = "ACI"

    def set_acv_mode(self):
        self.process_mode_buttons(self.ui.ACVpushButton)
        self.inst_mode = "ACV"

    def set_dci_mode(self):
        self.process_mode_buttons(self.ui.DCIpushButton)
        self.inst_mode = "DCI"

    def set_dcv_mode(self):
        self.process_mode_buttons(self.ui.DCVpushButton)
        self.inst_mode = "DCV"

    # The following handlers are called when a mode button is clicked. The handlers pass the button that was
    # clicked to process_mode_buttons. This accomplishes the one and only one behavior of the mode group.

    def set_con_mode(self):
        self.process_mode_buttons(self.ui.CONpushButton)
        self.inst_mode = "CON"

    def set_dio_mode(self):
        self.process_mode_buttons(self.ui.DIOpushButton)
        self.inst_mode = "DIO"

    def set_per_mode(self):
        self.process_mode_buttons(self.ui.PERpushButton)
        self.inst_mode = "PER"

    def set_fre_mode(self):
        self.process_mode_buttons(self.ui.FREpushButton)
        self.inst_mode = "FRE"

    def set_two_mode(self):
        self.process_mode_buttons(self.ui.TWOpushButton)
        self.inst_mode = "TWO"

    def set_fwo_mode(self):
        self.process_mode_buttons(self.ui.FWOpushButton)
        self.inst_mode = "FWO"

    def sample_count_change(self):
        # This handler is called when the user changes the samples, updates the sample count & update UI
        self.number_samples = self.ui.samplesSlider.value()
        self.ui.sampledisplayLabel.setText('TOTAL SAMPLES= ' + str(self.number_samples))

    def trigger_delay_change(self):
        self.trigger_delay = self.ui.TriggerDelaySlider.value()
        self.ui.SelectedTriggerdelayLabel.setText(str(self.trigger_delay))

    def start_sample_timer(self):
        # This handler clears the data buffers & sample index, starts the timer with a duration time_msec
        # time_msec = 250
        self.collectedData.clear()
        self.mytimestamp.clear()
        self.sample = 0
        self.ui.progressBar.setMaximum(self.number_samples)
        self.scantimer.start(self.sampletimerset)

    def stop_sample_timer(self):
        # This handler stops the sample timer

        self.ui.samplestoppushButton.hide()
        self.ui.samplestartpushButton.show()
        self.scantimer.stop()

    def exit_hp34401(self):
        # This handler resets the HPIB instrument & closes the instrument window
        self.HpDmm.write("*RST; *CLS")
        self.close()

    def start_scan(self):

        # This executes every time a measurement is taken.
        # The user initiates with the scan start button
        # This starts the scan timer
        # This method is executed repeatedly at the timer rate
        # until the # of samples desired = actual samples taken
        # Once the sample conditions are met, the data is plotted to our embedded pyqtgraph
        # NOTE- Actual rates will also depend on the response time of the instrument. If the sampling rate
        # is faster than the instrument rate, the slowest prevails.

        # disable the save csv button
        self.ui.savescanpushButton.hide()
        self.ui.samplestoppushButton.show()
        self.ui.samplestartpushButton.hide()
        # update the scan progress bar
        self.ui.progressBar.setValue(self.sample)
        self.sample += 1
        # display the current and total samples to the UI
        self.ui.samplestakenLabel.setText('SAMPLE: ' + str(self.sample) + ' of ' + str(self.number_samples))
        # Set the time axis labels
        self.ui.plotWidget.setLabel('bottom', 'TIME', units='unix')
        # Configure the instrument query string based on what mode we are in.
        # Also sets the axis labels for the correct units
        if self.inst_mode == "DCV":
            atx = self.HpDmm.query(":MEAS:VOLT:DC? 10,0.0001")
            self.ui.plotWidget.setLabel('left', 'Value', units='Volts DC')
        elif self.inst_mode == "ACV":
            atx = self.HpDmm.query(":MEAS:VOLT:AC? 10,0.0001")
            self.ui.plotWidget.setLabel('left', 'Value', units='Volts AC')
        elif self.inst_mode == "TWO":
            atx = self.HpDmm.query(":MEAS:RES? 10,0.0001")
            self.ui.plotWidget.setLabel('left', 'Value', units='Ohms 2wire')
        elif self.inst_mode == "FWO":
            atx = self.HpDmm.query(":MEAS:FRES? 10,0.0001")
            self.ui.plotWidget.setLabel('left', 'Value', units='Ohms 4wire')
        elif self.inst_mode == "DCI":
            atx = self.HpDmm.query(":MEAS:CURR:DC?")
            self.ui.plotWidget.setLabel('left', 'Value', units='Amps DC')
        elif self.inst_mode == "ACI":
            atx = self.HpDmm.query(":MEAS:CURR:AC?")
            self.ui.plotWidget.setLabel('left', 'Value', units='Amps AC')
        elif self.inst_mode == "FRE":
            atx = self.HpDmm.query(":MEAS:FREQ?")
            self.ui.plotWidget.setLabel('left', 'Value', units='Hertz Frequency')
        elif self.inst_mode == "PER":
            atx = self.HpDmm.query(":MEAS:PER?")
            self.ui.plotWidget.setLabel('left', 'Value', units='Seconds Period')
        elif self.inst_mode == "CON":
            atx = self.HpDmm.query(":MEAS:CONT?")
            self.ui.plotWidget.setLabel('left', 'Value', units='Continuity')
        elif self.inst_mode == "DIO":
            atx = self.HpDmm.query(":MEAS:DIOD?")
            self.ui.plotWidget.setLabel('left', 'Value', units='Diode')
        self.collectedData.append(float(atx))  # cast the response tp type float, add to data list
        self.mytimestamp.append(time.time())  # Grab the current time & add to timestamp list
        self.ui.lcdNumber.display(atx)  # Update LCD
        self.plot.setData(self.mytimestamp, self.collectedData)
        if self.sample == self.number_samples:
            self.stop_sample_timer()
            self.plot.setData(self.mytimestamp, self.collectedData)
            self.ui.progressBar.setValue(self.sample)
            # Reset the sample counter
            self.sample = 0
            self.ui.savescanpushButton.show()
            self.ui.samplestoppushButton.hide()
            self.ui.samplestartpushButton.show()

    def savescan(self):
        # Save the timestamp and collected data lists to a user defined csv file
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        csv_file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                       "All Files (*);;CSV Files (*.csv)", options=options)
        if csv_file_name:
            # We now have a valid full path filename with default *.csv extension
            # We need to collect our data and timestamps in the right format,
            # Note- bugfix csv file had no newline between datarows- added newline parameter below
            with open(csv_file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(zip(self.mytimestamp, self.collectedData))
                print(zip(self.mytimestamp, self.collectedData))
            f.close()
            # Hide the save csv button
            self.ui.savescanpushButton.hide()

# Create a subclass of QMainWindow. This is the app entry window
