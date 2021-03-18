import pyvisa as pg
import sys

rm = pg.ResourceManager()

class Instrument:
    def __init__(self, instrument_settings):
        # The constructor expects a dictionary where keys are instrument parameters. This is built outside the class
        # and passed to the class init here. Passing all this crap around is easier with a dict.
        # Convenience attributes are localized & extracted
        # When instancing this class, include an dictionary argument with keys below
        self.inst_address = instrument_settings.get('inst_address')
        self.instrument_mode = instrument_settings.get('instrument_mode')
        self.trigger_source = instrument_settings.get('trigger_source')
        self.trigger_delay = instrument_settings.get('trigger_delay')
        self.resolution = instrument_settings.get('resolution')
        self.measurement_range = instrument_settings.get('measurement_range')
        self.scan_rate = instrument_settings.get('scan_rate')
        self.number_samples = instrument_settings.get('number_samples')
        self.auto_zero = instrument_settings.get('auto_zero')
        self.integration_time_nplc = instrument_settings.get('integration_time_nplc')
        self.math_enabled = instrument_settings.get('math_enabled')

    # Note these following methods dont update the instrument, they simply update the class variables for later use.

    def set_instrument_addr(self, new_instrument_address):
        # Set the instrument address-
        # This is a string in the form 'GPIB::INSTR::22', etc...
        self.inst_address = new_instrument_address

    def set_trigger_source(self, new_trigger_source):
        # Set the instrument trigger mode
        # parameter is string = 'IMM', 'SOUR', 'EXT' are valid
        self.trigger_source = new_trigger_source

    def set_trigger_delay(self, new_trigger_delay):
        # Set the instrument trigger delay
        # parameter is float msec ?
        self.trigger_delay = new_trigger_delay

    def set_resolution(self, new_resolution):
        # Set the instrument resolution
        # parameter is float in native units eg 0.0001
        self.resolution = new_resolution

    def set_measurement_range(self, new_measurement_range):
        # Set the instrument range
        # parameter is float in native units eg 10
        self.measurement_range = new_measurement_range

    def set_scan_rate(self, new_scan_rate):
        # Set the instrument scan rate.
        # parameter is int in msec eg 250
        self.scan_rate = new_scan_rate

    def set_number_samples(self, new_number_samples):
        # Set the instrument number of samples to be taken
        # parameter is int eg 8
        self.number_samples = new_number_samples

    def set_instrument_mode(self, new_instrument_mode):
        # Set the instrument mode
        # parameter is string = 'DCV', 'ACI', 'PER' are valid
        self.instrument_mode = new_instrument_mode

    def set_auto_zero_mode(self, new_auto_zero_mode):
        # Set the instrument auto-zero mode
        # parameter is a boolean, true=az, false= no az
        self.auto_zero = new_auto_zero_mode

    def set_integration_time(self, new_integration_time):
        # Parameter is stated in terms of power line cycles (PLC's)
        self.integration_time = new_integration_time

    def set_math_enabled(self, new_math_enabled):
        # Parameter is stated in terms of power line cycles (PLC's)
        self.math_enabled = new_math_enabled

     ## Getters__________________________________________________________________


    def get_instrument_id(self):

        gpib_command_string = '*IDN?'
        InstrumentConnection.current_instrument.query(gpib_command_string)




class InstrumentConnection:

    #current_instrument = None

    def __init__(self, visa_resource_manager, instrument_address):

        self.current_instrument = None
        self.instrument_address = instrument_address
        self.visa_resource_manager = visa_resource_manager
        try:
            # Attempt to open the resource
            self.current_instrument = self.visa_resource_manager.open_resource(self.instrument_address)
        except pg.VisaIOError as e:
            # Execution here when a visa open resource error occurs during init of this class.
            # Get the error tuple
            self.visa_error = e.args
            # I'm not sure now what to do with a class init error ????
            # print(self.current_instrument.last_status)
            # print(self.current_instrument.visalib.last_status)
            print(self.visa_error)
            # return self this wont work

    def set_instrument_connection(self, visa_resource_manager):
        self.visa_resource_manager = visa_resource_manager
        self.current_instrument = self.visa_resource_manager.open_resource(self.instrument_address)
        # Need to add error handling here

    def write_string_to_current_instrument(self, gpib_command_string):
        # Write a command string to the current instrument

        self.current_instrument.write(gpib_command_string)






class InstrumentData:

    def __init__(self):
        self.collectedData = []
        self.timestampData = []

    def get_inst_id(self):
        print()


class SCPITranslator:

    # This class takes the current instrument settings as an argument, and translates that to suitable SCPI code
    def __init__(self, current_command_state):
        self.current_command_state = current_command_state
        print()







current_instrument_settings = {
    "inst_address": "GPIB0::22::INSTR",
    "instrument_mode": "DCV",
    "trigger_source": "IMM",
    "trigger_delay": 0,
    "resolution": 0.0001,
    "measurement_range": 10,
    "scan_rate": 250,
    "number_samples": 8,
    "auto_zero": 0,
    "integration_time_nplc": 1,
    "math_enabled": 0}




# __________________________________________________________________________________________________________________
# Here's some test code for the class:
# Instance the Instrument class with the current settings
my_instrument = Instrument(current_instrument_settings)
# test some class methods
# my_instrument.set_instrument_addr("gobbly gook")

my_translator = SCPITranslator(current_instrument_settings)

# instance the connection class with the current address
myConnection = InstrumentConnection(rm, my_instrument.inst_address)

# Note if gpib adapter isnt present it will throw an error:
# ('VI_ERROR_INTF_NUM_NCONFIG (-1073807195): The interface type is valid but the specified interface number
# is not configured.',)

# Check if myConnection has a visa_error attribute. If not, it was a success. If so, then it encountered a visa error
if hasattr(myConnection, 'visa_error'):
    print(myConnection.visa_error)


else:
    print("success")
print()

# instance the measurement class
# myMeasurement = Instrument()

# If this fails, myConnection.visa_error holds the error description
