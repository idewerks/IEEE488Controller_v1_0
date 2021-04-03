# This is the model file for the HP34401A
# This is part of a refactor to remove the data handling from the ui code.

# This should be instanced in the ui code
import pyvisa
import time

rm = pyvisa.ResourceManager()


class ModelBaseclass:
    def __init__(self):
        self.data_collected = []
        self.data_timestamp = []
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
        self.timer_setting = 20
        self.gpib_address = 'GPIB0::22::INSTR'
        self.last_visa_error = None

    def update_mode_state(self, mode_string):
        self.mode_setting = mode_string

    def sample_count_change(self, slider_value):
        # This handler is called when the user changes the samples, updates the sample count & update UI
        self.samples_setting = slider_value

    def start_scan(self):
        self.current_sample += 1
        if self.mode_setting == "DCV":
            try:
                self.response = self.instrument.query(":MEAS:VOLT:DC? " + str(self.range_setting) + ",0" + str(
                    self.resolution_setting))
            except pyvisa.VisaIOError as e:
                self.visa_error_handler(e.description)

        elif self.mode_setting == "ACV":
            query_string = ":MEAS:VOLT:AC? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting)

            self.response = self.instrument.query(":MEAS:VOLT:AC? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "TWO":
            self.response = self.instrument.query(":MEAS:RES? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "FWO":
            self.response = self.instrument.query(":MEAS:FRES? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "DCI":
            print(":MEAS:CURR:DC? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))
            self.response = self.instrument.query(":MEAS:CURR:DC? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "ACI":
            self.response = self.instrument.query(":MEAS:CURR:AC? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "FRE":
            self.response = self.instrument.query(":MEAS:FREQ? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "PER":
            self.response = self.instrument.query(":MEAS:PER? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "CON":
            self.response = self.instrument.query(":MEAS:CONT? ")

        elif self.mode_setting == "DIO":
            self.response = self.instrument.query(":MEAS:DIOD? ")

        if self.is_float(self.response):
            self.data_collected.append(float(self.response))  # cast the response tp type float, add to data list
            self.data_timestamp.append(time.time())  # Grab the current time & add to timestamp list
        else:   # We should do some cleanup here if the response was incorrect.
            print()

    def is_float(self, string_to_test):
        # This method tests a string parameter for float compatibility
        # Used for testing whether an instrument data response can be cast to float
        try:
            float(string_to_test)
            return True
        except ValueError:
            return False

    def setup_measurement(self):
        # IMPEDANCE
        if self.impedance_setting == "ON":
            self.instrument.write(":INP:IMP:AUTO ON")
        else:
            self.instrument.write(":INP:IMP:AUTO OFF")
            # AUTOZERO
        if self.auto_zero_setting == "ON":
            self.instrument.write(":SENS:ZERO:AUTO ON")
        elif self.auto_zero_setting == "OFF":
            self.instrument.write(":SENS:ZERO:AUTO OFF")
        else:
            self.instrument.write(":SENS:ZERO:AUTO ONCE")
        # RANGE & RESOLUTION
        # These will vary depending on mode selected. We cannot set these until we know which mode we are in,
        # so we will need to preload the range & resolution comboboxes with mode specific values

        # NPLC
        # self.instrument.write(":FUNC:NPLC " + self.NPLC_setting)        # this fails

        # TRIGGER DELAY
        self.instrument.write(":TRIG:DEL " + str(self.triggerDelay_setting))

    def close_instrument(self):
        self.instrument.write("*RST; *CLS")

    def IdQuery(self):
        inst_id = self.instrument.query("*IDN?")
        return inst_id

    def visa_error_handler(self, visa_error_code):
        # If a visa error occurs during an instrument query (timeout,etc) control is passed here
        # so we can recover gracefully
        self.last_visa_error = visa_error_code
        print(self.last_visa_error)



