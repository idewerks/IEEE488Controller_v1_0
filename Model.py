# This is the model file for the HP34401A
# This is part of a refactor to remove the data handling from the ui code.
# from State import InstrumentStateBaseclass

import pyvisa
import time
rm = pyvisa.ResourceManager()


class ModelBaseclass:
    def __init__(self):
        self.data_collected = []  # List for holding data, ui needs access
        self.data_timestamp = []  # List for holding timestamps, ui needs access
        self.response = ''
        self.instrument = rm.open_resource('GPIB0::22::INSTR')  # Instance the pyvisa connection
        self.current_sample = 0
        self.impedance_setting = "On"
        self.auto_zero_setting = 'OFF'
        self.range_setting = 10
        self.resolution_setting = .00001
        self.NPLC_setting = 2
        self.frequencyGate_setting = 1
        self.periodGate_setting = 1
        self.AcBw_setting = 200
        self.math_setting = 0
        self.trigger_setting = 'Immediate'
        self.triggerDelay_setting = 0
        self.samples_setting = 16
        self.mode_setting = 'DCV'
        self.timer_setting = 100
        self.gpib_address = 'GPIB0::22::INSTR'

    def update_mode_state(self, mode_string):
        self.mode_setting = mode_string

    def sample_count_change(self, slider_value):
        # This handler is called when the user changes the samples, updates the sample count & update UI
        self.samples_setting = slider_value

    def start_scan(self):
        self.current_sample += 1
        if self.mode_setting == "DCV":
            self.response = self.instrument.query(":MEAS:VOLT:DC? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "ACV":
            self.response = self.instrument.query(":MEAS:VOLT:AC? " + str(self.range_setting) + "," + str(
                self.resolution_setting))

        elif self.mode_setting == "TWO":
            self.response = self.instrument.query(":MEAS:RES? " + str(self.range_setting) + "," + str(
                self.resolution_setting))

        elif self.mode_setting == "FWO":
            self.response = self.instrument.query(":MEAS:FRES? " + str(self.range_setting) + "," + str(
                self.resolution_setting))

        elif self.mode_setting == "DCI":
            self.response = self.instrument.query(":MEAS:CURR:DC? " + str(self.range_setting) + "," + str(
                self.resolution_setting))

        elif self.mode_setting == "ACI":
            self.response = self.instrument.query(":MEAS:CURR:AC? " + str(self.range_setting) + "," + str(
                self.resolution_setting))

        elif self.mode_setting == "FRE":
            self.response = self.instrument.query(":MEAS:FREQ? " + str(self.range_setting) + "," + str(
                self.resolution_setting))

        elif self.mode_setting == "PER":
            self.response = self.instrument.query(":MEAS:PER? " + str(self.range_setting) + "," + str(
                self.resolution_setting))

        elif self.mode_setting == "CON":
            self.response = self.instrument.query(":MEAS:CONT? ")

        elif self.mode_setting == "DIO":
            self.response = self.instrument.query(":MEAS:DIOD? ")

        self.data_collected.append(float(self.response))  # cast the response tp type float, add to data list
        self.data_timestamp.append(time.time())  # Grab the current time & add to timestamp list

    def setup_measurement(self):
        # called just before a scan, this method sets up the instrument based on UI settings
        # ------------------------------------------------------------------------------------------------------------
        # IMPEDANCE
        if self.impedance_setting == "ON":
            self.instrument.write(":INP:IMP:AUTO ON")  # On or Off
        else:
            self.instrument.write(":INP:IMP:AUTO OFF")  # On or Off
        # ------------------------------------------------------------------------------------------------------------
        # AUTOZERO
        if self.auto_zero_setting == "ON":
            self.instrument.write(":SENS:ZERO:AUTO ON")  # On or Off
        elif self.auto_zero_setting == "OFF":
            self.instrument.write(":SENS:ZERO:AUTO OFF")  # On or Off
        else:
            self.instrument.write(":SENS:ZERO:AUTO ONCE")
        # ------------------------------------------------------------------------------------------------------------
        # RANGE & RESOLUTION

        # These will vary depending on mode selected. We cannot set these until we know which mode we are in,
        # so we will need to preload the range & resolution comoboxes with mode specific values
        # ------------------------------------------------------------------------------------------------------------
        # NPLC
        #self.instrument.write(":FUNC:NPLC " + self.NPLC_setting)        # this fails


        # Set Trigger Delay

        self.instrument.write(":TRIG:DEL " + str(self.triggerDelay_setting))

    def close_instrument(self):
        self.instrument.write("*RST; *CLS")

    def IdQuery(self):

        inst_id = self.instrument.query("*IDN?")
        return inst_id
