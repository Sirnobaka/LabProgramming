import time
import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import sys
#from keithley2600 import Keithley2600
sys.path.append(r'C:\Users\Andy\Python\keithley-2636')
#from k2636 import *
#from Instrument_Sounds import PlayGamma
import os
import csv

# check included paths
#for path in sys.path:
#    print(path)

#print(os.environ.get('PYTHONPATH'))
#########
rm = pyvisa.ResourceManager()
print('List of resources:')
print(rm.list_resources())

kei = rm.open_resource('USB0::0x05E6::0x2636::4439682::INSTR')
#########
def SetChAVoltage(volt):
    kei.write("smua.source.levelv = "+str(volt))

def ReadChAVoltage():
    return kei.query("print(smua.measure.v())")

def ReadChACurrent():
    return kei.query("print(smua.measure.i())")

def ChA_Off():
    kei.write("smua.source.output = smua.OUTPUT_OFF")

def ChA_On():
    kei.write("smua.source.output = smua.OUTPUT_ON")

def Diod_Steps(Vmin, Vmax, step, nTiles, FileName, newFile):
    kei.write("smua.measure.autozero = smua.AUTOZERO_AUTO") #[[auto recalibration]]
    kei.write("smua.source.func = smua.OUTPUT_DCVOLTS")
    kei.write("smua.measure.nplc = 1")
    kei.write("smua.measure.delay = 0.1")
    values = np.arange(Vmin,Vmax,step)
    file = open('output/'+FileName, 'a', encoding='UTF8', newline='')
    header = ['voltage_in', 'voltage_out', 'current', 'current2', 'nTiles']
    writer = csv.writer(file, delimiter =' ')
    # Write your notes here
    file.write('My note \n')
    if newFile:
        writer.writerow(header)
    for i in values:
        if i > 3.5:
            break
        SetChAVoltage(i)
        # To show current on display
        kei.write("smua.measure.i()")
        kei.write('delay(0.1)')
        writer.writerow([round(i, 3), float(ReadChAVoltage()), float(ReadChACurrent()), float(ReadChACurrent()), nTiles])
    file.close()


kei.write('beeper.beep(0.3, 600)')
kei.write('delay(1)')
#
#kei.write("smua.source.levelv = V_min")
#SetChAVoltage(2)
#kei.write("smua.measure.i()")
#print()
#print('Current =', ReadChACurrent())
#print('Voltage =', ReadChAVoltage())
ChA_On()
Diod_Steps(2.5, 3.6, 0.1, 3, 'Test_file2.txt', newFile=True)
ChA_Off()
kei.write('beeper.beep(0.3, 700)')
