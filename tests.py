import pyvisa

def TestKeiTley():
    rm = pyvisa.ResourceManager()
    print('List of resources:')
    print(rm.list_resources())

    kei = rm.open_resource('USB0::0x05E6::0x2636::4439682::INSTR')

    print('Keithley SMU ID:')
    print(kei.query("*IDN?"))
    print(kei.query("print(localnode.model)"))
    print(kei.query("print(localnode.serialno)"))