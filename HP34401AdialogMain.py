# This is the main dialog window for the HP34401A Instrument
# This is called by main.py
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication
from HP34401AdialogGridG import Ui_HP34401ADialog  # Get the Designer compiled dialog python class stub
from Model import ModelBaseclass
from PyQt5.QtCore import Qt
import csv
import pyqtgraph as pg
import pyqtgraph.exporters


class HP34401Adialog(QDialog):
    def __init__(self):
        super(HP34401Adialog, self).__init__()
        # Enable windows minimize/maximize buttons
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        # Instance the instrument model
        self.model = ModelBaseclass()

        # Instance the UI
        self.ui = Ui_HP34401ADialog()
        self.ui.setupUi(self)

        pg.setConfigOptions(antialias=True)
        # Define the color, width,style of the min max lines plot
        self.max_value_linetype = pg.mkPen(color='y', width=2, style=QtCore.Qt.DashDotDotLine, cosmetic=True)
        self.min_value_linetype = pg.mkPen(color='y', width=2, style=QtCore.Qt.DashDotDotLine, cosmetic=True)

        # Instance the plotwidget
        self.this_plot_widget = self.ui.plotWidget
        self.max_value_plot = []
        self.min_value_plot = []
        self.plot = []

        self.initialize_instrument_ui()
        # Setup Event Handlers
        # Sampling event handlers here <slots in the Qt parlance>------------------------------------------------------
        self.ui.samplestartpushButton.clicked.connect(self.start_sample_timer)
        self.ui.samplestoppushButton.clicked.connect(self.stop_sample_timer)
        self.ui.samplesSlider.valueChanged.connect(self.sample_count_change)
        self.ui.TriggerDelaySpinbox.valueChanged.connect(self.trigger_delay_change)
        self.ui.showdatapointscheckBox.clicked.connect(self.show_datapoints)
        self.ui.showminmaxcheckBox.clicked.connect(self.show_minmax)

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
        # Save event handlers
        self.ui.savescanpushButton.clicked.connect(self.save_scan_csv)
        self.ui.saveplotButton.clicked.connect(self.save_plot)
        self.ui.scrollwindowcomboBox.currentTextChanged.connect(self.scroll_window_update)
        self.ui.PlotmodeCombobox.currentTextChanged.connect(self.update_plot_mode)
        # Set up scan timer
        self.ui_timer = QTimer(self)
        self.ui_timer.timeout.connect(self.start_scan)

    def initialize_instrument_ui(self):
        # This is called during the dialog init method. Initialize the ui elements.
        self.this_plot_widget.setAntialiasing(True)
        self.this_plot_widget.addLegend(pen="m")  # pen here is the legend border color
        # Note there is no remove item method for the legend
        self.plot = self.this_plot_widget.plot(x=[1.0, 2.0, 3.0, 4.0],
                                               y=[1.0, 2.0, 3.0, 4.0],
                                               pen='r', symbol='o', symbolBrush='g', name='CHANNEL 1')

        self.max_value_plot = []
        self.min_value_plot = []
        self.this_plot_widget.getAxis('bottom').setTextPen('g')
        self.this_plot_widget.setBackground('#2B2B2B')
        self.this_plot_widget.showGrid(x=True, y=True)
        # tweak the axiis
        self.this_plot_widget.getAxis('left').setTextPen('y')
        self.this_plot_widget.getAxis('bottom').setTextPen('g')
        # This changes the grid color, text, axis title
        # self.this_plot_widget.getAxis('bottom').setPen('g')
        self.this_plot_widget.getAxis('bottom').setStyle(tickTextOffset=10)
        self.this_plot_widget.getAxis('left').setStyle(tickTextOffset=10)
        self.this_plot_widget.getAxis('bottom').setStyle(tickLength=80)
        self.this_plot_widget.getAxis('left').setStyle(tickLength=-40)
        self.this_plot_widget.setLabel('bottom', 'TIME', units='unix')
        # Set a bunch of default initial values
        self.ui.progressBar.setValue(0)
        self.ui.sampledisplayLabel.setText('TOTAL SAMPLES= ' + str(self.model.samples_setting))
        self.ui.savescanpushButton.hide()
        self.ui.samplestoppushButton.hide()
        # Update the status window
        self.ui.statustextBrowser.append('Reset and Clear Instrument')
        self.ui.statustextBrowser.append('Instrument Id:' + self.model.IdQuery())
        self.ui.statustextBrowser.append('Placing Instrument in remote mode')
        # Populate the comboboxes
        self.ui.ImpedanceCombobox.addItems(["OFF", "ON"])
        self.ui.AutozeroCombobox.addItems(["ON", "OFF", "ONCE"])
        self.ui.RangeCombobox.addItems(["10", "1", ".1", ".01", "AUTO"])
        self.ui.ResolutionCombobox.addItems([".00001", ".0001", ".001", ".01"])
        self.ui.NplcCombobox.addItems([".02", ".2", "1", "10", "100"])
        self.ui.FreqapertureCombobox.addItems(["1", ".1", ".01"])
        self.ui.PeriodapertureCombobox.addItems(["1", ".1", ".01"])
        self.ui.ACbandwidthCombobox.addItems(["3", "20", "200"])
        self.ui.MathCombobox.addItems(["Disabled", "Enabled"])
        self.ui.TrigsrcCombobox.addItems(["Immediate", "External", "Bus"])
        self.ui.PlotmodeCombobox.addItems(["Data Squish", "Data Scroll", "Snapshot"])
        self.ui.scrollwindowcomboBox.addItems(["10", "100", "1000", "10000"])

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
        self.model.mode_setting = "ACI"
        self.this_plot_widget.setLabel('left', 'Value', units='Amps AC')

    def set_acv_mode(self):
        self.process_mode_buttons(self.ui.ACVpushButton)
        self.model.mode_setting = "ACV"
        self.this_plot_widget.setLabel('left', 'Value', units='Volts AC')

    def set_dci_mode(self):
        self.process_mode_buttons(self.ui.DCIpushButton)
        self.model.mode_setting = "DCI"
        self.this_plot_widget('left', 'Value', units='Amps DC')

    def set_dcv_mode(self):
        self.process_mode_buttons(self.ui.DCVpushButton)
        self.model.mode_setting = "DCV"
        self.this_plot_widget.setLabel('left', 'Value', units='Volts DC')

    def set_con_mode(self):
        self.process_mode_buttons(self.ui.CONpushButton)
        self.model.mode_setting = "CON"
        self.this_plot_widget.setLabel('left', 'Value', units='Continuity')

    def set_dio_mode(self):
        self.process_mode_buttons(self.ui.DIOpushButton)
        self.model.mode_setting = "DIO"
        self.this_plot_widget.setLabel('left', 'Value', units='Diode')

    def set_per_mode(self):
        self.process_mode_buttons(self.ui.PERpushButton)
        self.model.mode_setting = "PER"
        self.this_plot_widget.setLabel('left', 'Value', units='Seconds Period')

    def set_fre_mode(self):
        self.process_mode_buttons(self.ui.FREpushButton)
        self.model.mode_setting = "FRE"
        self.this_plot_widget.setLabel('left', 'Value', units='Hertz Frequency')

    def set_two_mode(self):
        self.process_mode_buttons(self.ui.TWOpushButton)
        self.model.mode_setting = "TWO"
        self.this_plot_widget.setLabel('left', 'Value', units='Ohms 2wire')

    def set_fwo_mode(self):
        self.process_mode_buttons(self.ui.FWOpushButton)
        self.model.mode_setting = "FWO"
        self.this_plot_widget.setLabel('left', 'Value', units='Ohms 4wire')

    def sample_count_change(self):
        self.model.sample_count_change(self.ui.samplesSlider.value())
        self.ui.sampledisplayLabel.setText('TOTAL SAMPLES= ' + str(self.model.samples_setting))
        # self.ui.progressBar.setMaximum(self.model.samples_setting)

    def trigger_delay_change(self):
        self.model.triggerDelay_setting = self.ui.TriggerDelaySpinbox.value()

    def start_sample_timer(self):
        # This enables the scan timer which starts the scan loop
        # Initialize and clear elements here as part of the start scan process
        self.model.data_timestamp.clear()
        self.model.data_collected.clear()
        self.model.current_sample = 0
        self.model.setup_measurement()
        self.ui.progressBar.setMaximum(self.model.samples_setting)
        self.ui_timer.start(self.model.timer_setting)
        # Note the timer setting is located in the model. Using too fast of a setting can starve the ui loop
        self.ui.statustextBrowser.append('Starting Sample Timer')
        self.update_model_from_ui()
        self.model.last_visa_error = ''

    def stop_sample_timer(self):
        self.ui.samplestoppushButton.hide()
        self.ui.samplestartpushButton.show()
        self.ui_timer.stop()
        self.ui.statustextBrowser.append('Stopping Sample Timer')

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
        # The data is plotted to our embedded pyqtgraph on a point-point basis
        # NOTE- Actual rates will also depend on the response time of the instrument. If the sampling rate
        # is faster than the instrument rate, the slowest prevails.

        self.ui.savescanpushButton.hide()
        self.ui.saveplotButton.hide()
        self.ui.samplestartpushButton.hide()
        self.ui.samplestoppushButton.show()
        self.ui.progressBar.setValue(self.model.current_sample)
        self.ui.samplestakenLabel.setText(
            'SAMPLE: ' + str(self.model.current_sample + 1) + ' of ' + str(self.model.samples_setting))
        self.this_plot_widget.setLabel('bottom', 'TIME', units='unix')
        # Parse the mode and set any ui elements, then call the start_scan method in the model.
        # We are trying to keep the UI and DATA concerns away from each other
        if self.model.mode_setting == "DCV":
            self.this_plot_widget.setLabel('left', 'Value', units='Volts DC')
            self.model.start_scan()
        elif self.model.mode_setting == "ACV":
            self.this_plot_widget.setLabel('left', 'Value', units='Volts AC')
            self.model.start_scan()
        elif self.model.mode_setting == "TWO":
            self.this_plot_widget.setLabel('left', 'Value', units='Ohms 2wire')
            self.model.start_scan()
        elif self.model.mode_setting == "FWO":
            self.this_plot_widget.setLabel('left', 'Value', units='Ohms 4wire')
            self.model.start_scan()
        elif self.model.mode_setting == "DCI":
            self.this_plot_widget.setLabel('left', 'Value', units='Amps DC')
            self.model.start_scan()
        elif self.model.mode_setting == "ACI":
            self.this_plot_widget.setLabel('left', 'Value', units='Amps AC')
            self.model.start_scan()
        elif self.model.mode_setting == "FRE":
            self.this_plot_widget.setLabel('left', 'Value', units='Hertz Frequency')
            self.model.start_scan()
        elif self.model.mode_setting == "PER":
            self.this_plot_widget.setLabel('left', 'Value', units='Seconds Period')
            self.model.start_scan()
        elif self.model.mode_setting == "CON":
            self.this_plot_widget.setLabel('left', 'Value', units='Continuity')
            self.model.start_scan()
        elif self.model.mode_setting == "DIO":
            self.this_plot_widget.setLabel('left', 'Value', units='Diode')
            self.model.start_scan()

        # check for visa errors
        if self.model.last_visa_error:
            self.ui.statustextBrowser.append(self.model.last_visa_error)
            self.ui.statustextBrowser.append("Datapoint Ignored- Visa Fault")
        else:
            self.ui.lcdNumber.display(str(float(
                self.model.data_collected[-1])) + " " + self.model.mode_setting)  # Update LCD with most current reading

            if self.model.plot_mode == 'Data Scroll':
                plot_range = -self.model.data_scroll_window
                scroll_plot_data = self.model.data_collected[plot_range:]
                scroll_time_data = self.model.data_timestamp[plot_range:]
                self.plot.setData(scroll_time_data, scroll_plot_data)
            else:
                self.plot.setData(self.model.data_timestamp, self.model.data_collected)

            if self.ui.showminmaxcheckBox.isChecked():
                self.show_minmax()

        if self.model.current_sample == self.model.samples_setting:
            # END OF COMPLETE SCAN
            self.ui.statustextBrowser.append('Scan completed with ' + str(self.model.current_sample) + ' DataPoints')
            #self.plot.setData(self.model.data_timestamp, self.model.data_collected)
            self.ui.progressBar.setValue(self.model.current_sample)
            self.ui_timer.stop()
            self.ui.statustextBrowser.append('Scan timer stopped')
            self.ui.savescanpushButton.show()
            self.ui.saveplotButton.show()
            self.ui.samplestartpushButton.show()
            self.ui.samplestoppushButton.hide()

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
            self.ui.statustextBrowser.append('Scan saved as : ' + csv_file_name)

    def update_model_from_ui(self):
        # This is a shortcut method, rather than updating via ui events. We simply collect the settings from the ui
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
        self.model.triggerDelay_setting = self.ui.TriggerDelaySpinbox.value()
        self.model.data_scroll_window = int(self.ui.scrollwindowcomboBox.currentText())
        self.ui.statustextBrowser.append('Updated model from UI')

    def show_datapoints(self):
        # This method sets the symbol size to either 0 (no points), or size 10 to plot.
        # Probably not the best way to do this ? pyqtgraph makes it easy to create things, not so easy to remove
        if self.ui.showdatapointscheckBox.isChecked():
            self.plot.setSymbolSize(10)
        else:
            self.plot.setSymbolSize(0)

    def show_minmax(self):
        # Handle the maximum value line
        if self.ui.showminmaxcheckBox.isChecked():
            if self.max_value_plot:
                # If the plot exists, we just want to change the data
                self.max_value_plot.setPen(self.max_value_linetype)
                if self.model.current_sample > 0:
                    # Test for an empty list, max() will throw an error otherwise
                    # Update the plot data
                    self.max_value_plot.setValue(max(self.model.data_collected))
            else:
                if self.model.current_sample > 0:
                    self.max_value_plot = self.this_plot_widget.addLine(x=None, y=max(self.model.data_collected))
                    self.max_value_plot.setPen(self.max_value_linetype)
        else:
            self.this_plot_widget.removeItem(self.max_value_plot)
            self.max_value_plot = []

        # Handle the minimum value line
        if self.ui.showminmaxcheckBox.isChecked():
            if self.min_value_plot:
                # If the plot exists, we just want to change the data
                self.min_value_plot.setPen(self.min_value_linetype)
                if self.model.current_sample > 0:
                    # Test for an empty list, max() will throw an error otherwise
                    # Update the plot data
                    self.min_value_plot.setValue(min(self.model.data_collected))
            else:
                if self.model.current_sample > 0:
                    self.min_value_plot = self.this_plot_widget.addLine(x=None, y=min(self.model.data_collected))
                    self.min_value_plot.setPen(self.min_value_linetype)
        else:
            self.this_plot_widget.removeItem(self.min_value_plot)
            self.min_value_plot = []

    def save_plot(self):
        # Save current plot as graphic type
        # exporter = pg.exporters.ImageExporter(self.this_plot_widget)
        exporter = pg.exporters.ImageExporter(self.plot)

        # exporter.parameters()['height'] = 1024
        exporter.params['width'] = 1024
        # exporter.export('export.png')
        # This fails with a width error if we specify it, if we dont it throws a 0x0 size error
        print()

        # Reported fix in v0.12 of pyqtgraph. I installed but I have a sip error
        # reverted back to v0.11 for now so have not figured this out yet

        # fix: in ImageExporter.py, line 70:
        # bg = np.empty((int(self.params['width']), int(self.params['height']), 4), dtype=np.ubyte)

    def scroll_window_update(self):
        # Scroll window width has changed
        w_width = -int(self.ui.scrollwindowcomboBox.currentText())
        self.model.data_scroll_window = w_width

    def update_plot_mode(self):
        self.model.plot_mode = self.ui.PlotmodeCombobox.currentText()


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()
