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
        self.instrument = rm.open_resource('GPIB0::7::INSTR')  # Instance the pyvisa connection
        self.instrument.read_termination = '\n'
        self.instrument.write_termination = '\n'
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
        self.timer_setting = 1000
        #self.gpib_address = 'GPIB0::22::INSTR'   #34401a mode
        self.gpib_address = 'GPIB0::7::INSTR'
        self.last_visa_error = None
        self.data_scroll_window = -10
        self.plot_mode = 'Data Squish'


    def update_mode_state(self, mode_string):
        self.mode_setting = mode_string

    def change_sample_count(self, slider_value):
        # This handler is called when the user changes the samples, updates the sample count & update UI
        self.samples_setting = slider_value

    def start_scan(self):
        self.current_sample += 1
        if self.mode_setting == "DCV":
            try:

                # 34401 mode:
                self.instrument.write("TARM SGL,1")
                #self.instrument.write(":SENS:VOLT:DC:DIG 8")
                #self.instrument.write(":SENS:VOLT:DC:AVER:TCON REP")
                #self.instrument.write(":SENS:VOLT:DC:AVER:COUN 10")
                time.sleep(3)
                self.response = self.instrument.read()

                print(self.response)
                #self.response = self.instrument.query(":MEAS:VOLT:DC? " + str(self.range_setting) + ",0" + str(
                    #self.resolution_setting))
            except pyvisa.VisaIOError as e:
                self.visa_error_handler(e.description)

        elif self.mode_setting == "ACV":

            self.response = self.instrument.query(":MEAS:VOLT:AC? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "TWO":
            self.response = self.instrument.query(":MEAS:RES? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "FWO":
            self.response = self.instrument.query(":MEAS:FRES? " + str(self.range_setting) + ",0" + str(
                self.resolution_setting))

        elif self.mode_setting == "DCI":
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

        # - commented out344401a mode

        #if self.impedance_setting == "ON":
        #    self.instrument.write(":INP:IMP:AUTO ON")
        #else:
         #   self.instrument.write(":INP:IMP:AUTO OFF")
            # AUTOZERO
        # if self.auto_zero_setting == "ON":
        #     self.instrument.write(":SENS:ZERO:AUTO ON")
        # elif self.auto_zero_setting == "OFF":
        #     self.instrument.write(":SENS:ZERO:AUTO OFF")
        # else:
        #     self.instrument.write(":SENS:ZERO:AUTO ONCE")
        #
        # self.instrument.write(":SENS:VOLT:DC:NPLC 10")
        # self.instrument.write(":SENS:VOLT:DC:DIG 8")
        #
        # self.instrument.write(":TRIG:DEL " + str(self.triggerDelay_setting))

        self.instrument.write("PRESET NORM")
        self.instrument.write("OFORMAT ASCII")
        self.instrument.write("DCV 10")
        self.instrument.write("TARM HOLD")
        self.instrument.write("TRIG AUTO")
        self.instrument.write("NPLC 200")
        self.instrument.write("NRDGS 1,AUTO")
        self.instrument.write("MEM OFF")
        self.instrument.write("END ALWAYS")
        self.instrument.write("NDIG 9")
        self.instrument.write("DISP MSG,\"Test\"")
        self.instrument.write("DISP ON")





        #self.instrument.write("AZERO ON")





    def close_instrument(self):
        self.instrument.write("*RST; *CLS")

    def IdQuery(self):
        #inst_id = self.instrument.query("*IDN?")
        self.instrument.write("TARM HOLD")
        inst_id = self.instrument.query("ID?")
        #inst_id = self.instrument.read()
        return inst_id

    def visa_error_handler(self, visa_error_code):
        # If a visa error occurs during an instrument query (timeout,etc) control is passed here
        # so we can recover gracefully
        self.last_visa_error = visa_error_code
        print(self.last_visa_error)



