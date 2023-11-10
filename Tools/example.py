# -*- coding=utf-8 -*-
"""
© 2021 RIGOL TECHNOLOGIES CO., LTD. All Rights Reserved.

You have a royalty-free right to use, modify, reproduce and distribute
the Sample Application Files (and/or any modified version) in any way
you find useful, provided that you agree that RIGOL Technologies has no
warranty, obligations or liability for any Sample Application Files.

RIGOL Technologies provides programming examples for illustration only,
This sample program assumes that you are familiar with the programming
language being demonstrated and the tools used to create and debug
procedures. RIGOL Technologies support engineers can help explain the
functionality of RIGOL Technologies software components and associated
commands, but they will not modify these samples to provide added
functionality or construct procedures to meet your specific needs.

If you have any problem or requirement when using this program, please contact
RIGOL.
E-mail: service@rigol.com
Website: http://www.rigol.com
"""

#####################################################################
# This programming example is used to set DCV function parameters and
# get DCV measure of the RIGOL DM products.
# Support products: RIGOL DM3058, RIGOL DM3068
#####################################################################
import sys
import time
import pyvisa

# Change this variable to the address of your instrument
# DEVADDR = "GPIB0::XX::INSTR" # Device address for GPIB
# DEVADDR = "TCPIP0::1XX.2XX.X.XX::INSTR" # Device address for LAN
DEVADDR = "USB0::0xXXXX::0xXXXX::DMXXXXXXXXXXX::INSTR" # Device address for USB


# Create a connection (session) to the instrument
try:
    DevRscrManger = pyvisa.ResourceManager()
    session = DevRscrManger.open_resource(DEVADDR)
    session.timeout = 5000
except pyvisa.Error as ex:
    print("Couldn\'t connect to {}, exiting now...".format(DEVADDR))
    sys.exit()

# Query instrument *IDN? information
print(session.query("*IDN?").strip())

# Function
def measure_dcv():
    '''
        Function: Set DM product DCV function and range level.
    '''
    session.write("CMDS RIGOL") # Use Rigol command

    session.write(":FUNCtion:VOLTage:DC") # Set DM product DCV function.
    # Other function are ACV, ACI, DCI, DIO, 2WR, 4WR, FREQ.

    session.write(":MEASure:VOLTage:DC 2") # Set DCV function 20V range.
    # Other DCV range are 200mV, 2V, 200V, 1000V.

    time.sleep(3) # Function and range configuration delay time is 3 second.
    print(str(session.query(":MEASure:VOLTage:DC?"))) # Get DCV measure in Vpp.

# Run the function
measure_dcv()

# Close the connection to the instrument
session.close()
DevRscrManger.close()
print('Done.')
