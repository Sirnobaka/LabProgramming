from ctypes import *

lib = cdll.msvcrt   # подключаем библиотеку msvcrt.dll
lib.printf(b"From dll with love!\n") # вывод строки через стандартную printf

var_a = 31
lib.printf(b"Print int_a = %d\n", var_a) # вывод переменной int
                                # printf("Print int_a = %d\n", var_a); // аналог в С

lib = cdll.LoadLibrary(r"C:\Windows\System32\msvcrt.dll")
lib.printf(b"From dll with love!\n")    # вывод строки через стандартную printf

lib_2 = CDLL(r"C:\Windows\System32\msvcrt.dll") # подключаем библиотеку msvcrt.dll

var_a = 31
lib_2.printf(b"Print int_a = %d\n", var_a)  # вывод переменной int