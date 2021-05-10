def getInstrumentInfo(rm, instrument):
    # Lets try and identify the instrument we just selected in the combobox instrument selector
    this_instrument = rm.open_resource(instrument)

    # Note the ID command varies depending on age of instrument. In particular, IEE488.1 vs IEEE488.2
    # For newer instruments, *IDN? is the correct query, ID? is for older instruments
    # It looks like the easiest is to send the 488.2 command *IDN? and look at result.
    # If it contains a colon, its just returning the same address e.g. GPIBx::address::INSTR
    # if not containing a colon, the ID is valid, otherwise try again with ID? sequence

    # Problem here, the 8596E responds with /r/n to the 488.2 query.
    # responds with HP8596E\r\n to the 488.1 command
    # Lets try a 488-2 command first:
    # Nope, bad idea, some older instruments lock on a syntax error when trying 488.2 first.
    # Lets try issuing a 488.1 first, then fallback to 488.2
    hpib_response = this_instrument.query('*IDN?')

    delimiter = ':'
    # if the response is < 6 chars OR it contains a colon, the 488.2 command failed, try a 488.1 command
    if len(hpib_response) < 6 or delimiter in hpib_response:
        hpib_response = this_instrument.query('ID?')

