'''
Objectives

    Creation of abstract classes and abstract methods;
    multiple inheritance of abstract classes;
    overriding abstract methods;
    delivering multiple child classes.

Scenario

    You are about to create a multifunction device (MFD) that can scan and print documents;
    the system consists of a scanner and a printer;
    your task is to create blueprints for it and deliver the implementations;
    create an abstract class representing a scanner that enforces the following methods:
        scan_document – returns a string indicating that the document has been scanned;
        get_scanner_status – returns information about the scanner (max. resolution, serial number)
    Create an abstract class representing a printer that enforces the following methods:
        print_document – returns a string indicating that the document has been printed;
        get_printer_status – returns information about the printer (max. resolution, serial number)
    Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
        MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
        MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
        MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.
    Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.

'''
from abc import ABC, abstractclassmethod
from datetime import datetime as dt

class Scanner(ABC):
    @abstractclassmethod
    def scan_document(self):
        pass

    @abstractclassmethod
    def get_scanner_status(self):
        pass

class Printer(ABC):
    @abstractclassmethod
    def print_document(self):
        pass

    @abstractclassmethod
    def get_printer_status(self):
        pass

class MFD1(Printer, Scanner):
    def __init__(self, serial, maxres):
        self.__serialn = serial
        self.__resolution = maxres

    def scan_document(self, doc):
        print("Scanning document...")
        print(f"{doc} scanning completed!\n")

    def print_document(self, doc):
        print("Printing document...")
        print(f"{doc} printing completed!\n")

    def get_scanner_status(self):
        print(f"Multifunctional Device Py1 \'Home\' info:\nSerial Number: {self.__serialn}\nMax. Scanner Resolution: {self.__resolution} DPI\n")
    
    def get_printer_status(self):
        print(f"Multifunctional Device Py1 \'Home\' info:\nSerial Number: {self.__serialn}\nMax. Printer Resolution: {self.__resolution} DPI\n")

class MFD2(Printer, Scanner):
    def __init__(self, serial, maxres):
        self.__history = []
        self.__serialn = serial
        self.__resolution = maxres

    def scan_document(self, doc):
        print("Scanning document...")
        print(f"{doc} scanning completed!\n")

    def print_document(self, doc):
        print("Printing document...")
        time = dt.now().strftime('%d-%m-%Y %H:%M')
        self.__history.append(f"{doc} printed at {time}")
        print(f"{doc} printing completed!\n")

    def get_scanner_status(self):
        print(f"Multifunctional Device Py2 \'Office\' info:\nSerial Number: {self.__serialn}\nMax. Scanner Resolution: {self.__resolution} DPI\n")
    
    def get_printer_status(self):
        print(f"Multifunctional Device Py2 \'Office\' info:\nSerial Number: {self.__serialn}\nMax. Printer Resolution: {self.__resolution} DPI\n")

    def get_printer_history(self):
        if len(self.__history) > 0:
            for h in self.__history:
                print(f'{h}')
        else:
            print("Printer History Empty\n")

class MFD3(Printer, Scanner):
    def __init__(self, serial, maxres) -> None:
        self.__phistory = []
        self.__fhistory = []
        self.__serialn = serial
        self.__resolution = maxres

    def scan_document(self, doc, fax=False, faxNum=0):
        if fax:
            print("Scanning document...")
            time = dt.now().strftime('%d-%m-%Y %H:%M')
            self.__fhistory.append(f"{doc} scanned at {time} and send to fax number {faxNum}")
            print(f"{doc} scanning completed! Fax send successfully\n")
        else:
            print("Scanning document...")
            time = dt.now().strftime('%d-%m-%Y %H:%M')
            self.__fhistory.append(f"{doc} scanned at {time}")
            print(f"{doc} scanning completed!\n")

    def print_document(self, doc):
        time = dt.now().strftime('%d-%m-%Y %H:%M')
        self.__phistory.append(f"{doc} printed at {time}")
        print(f"Printing document...\n{doc} printing completed!\n")

    def get_scanner_status(self):
        print(f"Multifunctional Device Py3 \'Ultimate\' info:\nSerial Number: {self.__serialn}\nMax. Scanner Resolution: {self.__resolution} DPI\n")
    
    def get_printer_status(self):
        print(f"Multifunctional Device Py3 \'Ultimate\' info:\nSerial Number: {self.__serialn}\nMax. Printer Resolution: {self.__resolution} DPI\n")

    def get_printer_history(self):
        if len(self.__phistory) > 0:
            for h in self.__phistory:
                print(f'{h}')
        else:
            print("Printer History Empty\n")

    def get_fax_history(self):
        if len(self.__fhistory) > 0:
            for f in self.__fhistory:
                print(f'{f}')
        else:
            print("Fax History Empty\n")

mfd1 = MFD1("PY115XC", 90)
mfd2 = MFD2("PY351FG", 150)
mfd3 = MFD3("PY527BR", 300)

mfd1.print_document("python_readme.txt")
mfd1.scan_document("py_logo.jpg")
mfd1.get_printer_status()
mfd1.get_scanner_status()

mfd2.print_document("python_3.10_Docs.html")
mfd2.scan_document("linux_tux.png")
mfd2.get_printer_history()
print()
mfd2.get_printer_status()
mfd2.get_scanner_status()

mfd3.print_document("python_advanded_techniques.pdf")
mfd3.scan_document("course_certificate", fax=True, faxNum=5551234)
mfd3.get_printer_history()
print()
mfd3.get_fax_history()
print()
mfd3.get_printer_status()
mfd3.get_scanner_status()