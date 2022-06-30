import time
import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import sys
from keithley2600 import Keithley2600
sys.path.append(r'C:\Users\Andy\Python\keithley-2636')
#from k2636 import *
from Instrument_Sounds import PlayGamma
import os

# check included paths
#for path in sys.path:
#    print(path)

#print(os.environ.get('PYTHONPATH'))

rm = pyvisa.ResourceManager()
print('List of resources:')
print(rm.list_resources())

kei = rm.open_resource('USB0::0x05E6::0x2636::4439682::INSTR')
print('Keithley SMU ID:')
print(kei.query("*IDN?"))
print(kei.query("print(localnode.model)"))
print(kei.query("print(localnode.serialno)"))

kei.write('beeper.beep(0.3, 600)')

kei.write('delay(1)')
print('Commands')
print(kei.query("print('Hello, World!')"))
#kei.write("smub.source.levelv = 0")
kei.write("V_min = 2.6")
kei.write("smua.source.output = smua.OUTPUT_ON")
# it's equal to
kei.write("smua.source.output = 1")
#
print(kei.query("print('V_min =', V_min)"))
kei.write("smua.source.levelv = V_min")
#print(kei.write("smua.measure.i()"))
#kei.write("smua.measure.v()")
# To show current on display
kei.write("smua.measure.i()")
print('Current =', kei.query("print(smua.measure.i())"))
print('Voltage =', kei.query("print(smua.measure.v())"))
kei.write("smua.source.output = smua.OUTPUT_OFF")
#kei.write("smua.source.levelv = 0")
#print(kei.query("smua.measure.v"))
#kei.write("smua.source.output = smua.OUTPUT_OFF")


#print(kei.read("smua.source.leveli"))
#kei.write("*RST")

#kei.write("smua.source.limiti = 1e-3")
#kei.write("print(smua.source.compliance)")

#####

#PlayGamma(kei)
