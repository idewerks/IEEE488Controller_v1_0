# This is the main dialog window for the HP34401A Instrument
# This is called by main.py
import csv
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QMainWindow, QFileDialog
from HP34401AdialogGridF import Ui_HP34401ADialog  # Get the Designer compiled dialog python class stub
from Model import ModelBaseclass
from PyQt5.QtCore import Qt

# dialog.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
# dialog.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
# ----------------------------------------------------------------------------------------------------------------------
class HP34401Adialog(QDialog):
    def __init__(self):
        super(HP34401Adialog, self).__init__()
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.model = ModelBaseclass()
        self.ui = Ui_HP34401ADialog()
        self.ui.setupUi(self)
        # Create a placeholder plot we can update later
        self.plot = self.ui.plotWidget.plot(x=[1.0, 2.0, 3.0, 4.0],
                                            y=[1.0, 2.0, 3.0, 4.0], pen="r", symbol="o", symbolBrush="g")
        self.initialize_instrument_ui()
        # Setup Event Handlers
        # Sampling event handlers here <slots in the Qt parlance>------------------------------------------------------
        self.ui.samplestartpushButton.clicked.connect(self.start_sample_timer)
        self.ui.samplestoppushButton.clicked.connect(self.stop_sample_timer)
        self.ui.samplesSlider.valueChanged.connect(self.sample_count_change)
        self.ui.TriggerDelaySlider.valueChanged.connect(self.trigger_delay_change)

        # event handlers for mode button group----------------------------------------------
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
        self.ui.savescanpushButton.clicked.connect(self.save_scan_csv)

        self.ui_timer = QTimer(self)
        self.ui_timer.timeout.connect(self.start_scan)

    def initialize_instrument_ui(self):
        # This is called during the dialog init method. Initialize the ui elements to their default state.
        self.ui.plotWidget.showGrid(x=True, y=True)
        self.ui.plotWidget.setLabel('bottom', 'TIME', units='unix')
        self.ui.plotWidget.getAxis('left').setTextPen('y')
        self.ui.plotWidget.getAxis('bottom').setTextPen('g')
        self.ui.progressBar.setValue(0)
        self.ui.sampledisplayLabel.setText('TOTAL SAMPLES= ' + str(self.model.samples_setting))
        self.ui.savescanpushButton.hide()
        self.ui.samplestoppushButton.hide()
        self.ui.statustextBrowser.append('Reset and Clear Instrument')
        self.ui.statustextBrowser.append('Instrument Id:' + self.model.IdQuery())
        self.ui.statustextBrowser.append('Placing Instrument in remote mode')

        # Populate the comboboxes
        self.ui.ImpedanceCombobox.addItem('OFF')  # populate the combo box with available options
        self.ui.ImpedanceCombobox.addItem('ON')

        self.ui.AutozeroCombobox.addItem('ON')
        self.ui.AutozeroCombobox.addItem('OFF')
        self.ui.AutozeroCombobox.addItem('ONCE')

        self.ui.RangeCombobox.addItem('.01')
        self.ui.RangeCombobox.addItem('.1')
        self.ui.RangeCombobox.addItem('1.0')
        self.ui.RangeCombobox.addItem('10')
        self.ui.RangeCombobox.addItem('Auto')

        self.ui.ResolutionCombobox.addItem('.01')
        self.ui.ResolutionCombobox.addItem('.001')
        self.ui.ResolutionCombobox.addItem('.0001')
        self.ui.ResolutionCombobox.addItem('.00001')

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

        self.ui.MathCombobox.addItem('Disabled')
        self.ui.MathCombobox.addItem('Enabled')

        self.ui.TrigsrcCombobox.addItem('Immediate')
        self.ui.TrigsrcCombobox.addItem('External')
        self.ui.TrigsrcCombobox.addItem('Bus')

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

    # The following handlers are called when a mode button is clicked. The handlers pass the button that was
    # clicked to process_mode_buttons. This accomplishes the one and only one behavior of the mode group.
    def set_aci_mode(self):
        self.process_mode_buttons(self.ui.ACIpushButton)
        self.model.mode_setting = "DCV"
        self.ui.plotWidget.setLabel('left', 'Value', units='Amps AC')

    def set_acv_mode(self):
        self.process_mode_buttons(self.ui.ACVpushButton)
        self.model.mode_setting = "ACV"
        self.ui.plotWidget.setLabel('left', 'Value', units='Volts AC')

    def set_dci_mode(self):
        self.process_mode_buttons(self.ui.DCIpushButton)
        self.model.mode_setting = "DCI"
        self.ui.plotWidget.setLabel('left', 'Value', units='Amps DC')

    def set_dcv_mode(self):
        self.process_mode_buttons(self.ui.DCVpushButton)
        self.model.mode_setting = "DCV"
        self.ui.plotWidget.setLabel('left', 'Value', units='Volts DC')

    def set_con_mode(self):
        self.process_mode_buttons(self.ui.CONpushButton)
        self.model.mode_setting = "CON"
        self.ui.plotWidget.setLabel('left', 'Value', units='Continuity')

    def set_dio_mode(self):
        self.process_mode_buttons(self.ui.DIOpushButton)
        self.model.mode_setting = "DIO"
        self.ui.plotWidget.setLabel('left', 'Value', units='Diode')

    def set_per_mode(self):
        self.process_mode_buttons(self.ui.PERpushButton)
        self.model.mode_setting = "PER"
        self.ui.plotWidget.setLabel('left', 'Value', units='Seconds Period')

    def set_fre_mode(self):
        self.process_mode_buttons(self.ui.FREpushButton)
        self.model.mode_setting = "FRE"
        self.ui.plotWidget.setLabel('left', 'Value', units='Hertz Frequency')

    def set_two_mode(self):
        self.process_mode_buttons(self.ui.TWOpushButton)
        self.model.mode_setting = "TWO"
        self.ui.plotWidget.setLabel('left', 'Value', units='Ohms 2wire')

    def set_fwo_mode(self):
        self.process_mode_buttons(self.ui.FWOpushButton)
        self.model.mode_setting = "FWO"
        self.ui.plotWidget.setLabel('left', 'Value', units='Ohms 4wire')

    def sample_count_change(self):  # this uses a class method
        self.model.sample_count_change(self.ui.samplesSlider.value())
        self.ui.sampledisplayLabel.setText('TOTAL SAMPLES= ' + str(self.model.samples_setting))
        self.ui.progressBar.setMaximum(self.model.samples_setting)

    def trigger_delay_change(self):  # this modifies the class variable
        self.model.triggerDelay_setting = self.ui.TriggerDelaySlider.value()
        self.ui.SelectedTriggerdelayLabel.setText(str(self.model.triggerDelay_setting))

    def start_sample_timer(self):
        # self.model.start_sample_timer()
        self.model.data_timestamp.clear()
        self.model.data_collected.clear()
        self.model.current_sample = 0
        self.ui.progressBar.setMaximum(self.model.samples_setting)
        self.ui_timer.start(50)

    def stop_sample_timer(self):
        self.ui.samplestoppushButton.hide()
        self.ui.samplestartpushButton.show()
        # self.model.stop_sample_timer()
        self.ui_timer.stop()

    def exit_hp34401(self):
        # This handler resets the HPIB instrument & closes the instrument window
        self.model.close_instrument()
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
        self.update_model_from_ui()
        self.ui.savescanpushButton.hide()
        self.ui.samplestoppushButton.show()
        self.ui.samplestartpushButton.hide()
        self.ui.progressBar.setValue(self.model.current_sample)
        self.ui.samplestakenLabel.setText(
            'SAMPLE: ' + str(self.model.current_sample + 1) + ' of ' + str(self.model.samples_setting))
        self.ui.plotWidget.setLabel('bottom', 'TIME', units='unix')
        self.model.setup_measurement()
        # Parse the mode and set any ui elements, then call the start_scan method in the model.
        # We are trying to keep the UI and DATA concerns away from each other

        if self.model.mode_setting == "DCV":
            self.ui.plotWidget.setLabel('left', 'Value', units='Volts DC')
            self.model.start_scan()

        elif self.model.mode_setting == "ACV":
            self.ui.plotWidget.setLabel('left', 'Value', units='Volts AC')
            self.model.start_scan()

        elif self.model.mode_setting == "TWO":
            self.ui.plotWidget.setLabel('left', 'Value', units='Ohms 2wire')
            self.model.start_scan()

        elif self.model.mode_setting == "FWO":
            self.ui.plotWidget.setLabel('left', 'Value', units='Ohms 4wire')
            self.model.start_scan()

        elif self.model.mode_setting == "DCI":
            self.ui.plotWidget.setLabel('left', 'Value', units='Amps DC')
            self.model.start_scan()

        elif self.model.mode_setting == "ACI":
            self.ui.plotWidget.setLabel('left', 'Value', units='Amps AC')
            self.model.start_scan()

        elif self.model.mode_setting == "FRE":
            self.ui.plotWidget.setLabel('left', 'Value', units='Hertz Frequency')
            self.model.start_scan()

        elif self.model.mode_setting == "PER":
            self.ui.plotWidget.setLabel('left', 'Value', units='Seconds Period')
            self.model.start_scan()

        elif self.model.mode_setting == "CON":
            self.ui.plotWidget.setLabel('left', 'Value', units='Continuity')
            self.model.start_scan()

        elif self.model.mode_setting == "DIO":
            self.ui.plotWidget.setLabel('left', 'Value', units='Diode')
            self.model.start_scan()

        self.ui.lcdNumber.display(float(self.model.data_collected[-1]))  # Update LCD with most current reading
        self.plot.setData(self.model.data_timestamp, self.model.data_collected)

        if self.model.current_sample == self.model.samples_setting:
            self.plot.setData(self.model.data_timestamp, self.model.data_collected)
            self.ui.progressBar.setValue(self.model.current_sample)
            self.ui_timer.stop()
            self.ui.savescanpushButton.show()
            self.ui.samplestoppushButton.hide()
            self.ui.samplestartpushButton.show()

    def save_scan_csv(self):
        # Save the timestamp and collected data lists to a user defined csv file
        # todo Need to add csv headers to export file
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
                writer.writerows(zip(self.model.data_timestamp, self.model.data_collected))
                print(zip(self.model.data_timestamp, self.model.data_collected))
            f.close()
            # Hide the save csv button
            self.ui.savescanpushButton.hide()

    def update_model_from_ui(self):

        # This is a shortcut method, rather than updating via mouse events. We simply collect the settingd from the ui
        # and update the model
        self.model.impedance_setting = self.ui.ImpedanceCombobox.currentText()
        self.model.samples_setting = self.ui.samplesSlider.value()
        self.model.resolution_setting = self.ui.ResolutionCombobox.currentText()
        self.model.range_setting = self.ui.RangeCombobox.currentText()
        self.model.AcBw_setting = self.ui.ACbandwidthCombobox.currentText()
        self.model.auto_zero_setting = self.ui.AutozeroCombobox.currentText()
        self.model.frequencyGate_setting = self.ui.FreqapertureCombobox.currentText()
        self.model.periodGate_setting = self.ui.PeriodapertureCombobox.currentText()
        self.model.math_setting = self.ui.MathCombobox.currentText()
        self.model.NPLC_setting = self.ui.NplcCombobox.currentText()
        self.model.trigger_setting = self.ui.TrigsrcCombobox.currentText()
        self.model.triggerDelay_setting = self.ui.TriggerDelaySlider.value()
