# program to represent the alarm system in a teams network
# @author: Doshmajhan, bharmat

from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer
from twisted.internet.task import LoopingCall
from threading import Thread
from time import sleep
import RPi.GPIO as GPIO
import os
import argparse

class Alarm(Thread):
    def __init__(self, fileName=''):
        Thread.__init__(self)
        self.fileName = fileName
        self.currentStat = 1
        self.enabled = True

    def run(self):
        while True:
            stat = self.get_stat()
            self.currentStat = stat
            print "Current: " + str(self.currentStat) + " " + str(self.fileName)
            sleep(5)

    def get_stat(self):
        return 1

    def setEnabled(self, enabled):
        self.enabled = enabled

    def isEnabled(self):
        return self.enabled

def updating_writer(a):
    context  = a[0]
    function = 3
    slave_id = 0x00
    address  = 0x00
    values = [int(pi.get_stat())]
    context[slave_id].setValues(function,address,values)

    #print context[slave_id].getValues(function, address)  # prints our holding register
    result = context[slave_id].getValues(function, 0x01)
    #print result # prints the register the server writes to
    #set_alarm(result)

def set_alarm(result):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    if result == 1:
        GPIO.setup(23, GPIO.OUT)
        print "GREEN on"
        GPIO.output(23, GPIO.HIGH)
        time.sleep(3)
        print "GREEN off"
        GPIO.output(23, GPIO.LOW)

    else:
        GPIO.setup(18, GPIO.OUT)
        print "RED on"
        GPIO.output(18, GPIO.HIGH)
        time.sleep(3)
        print "RED off"
        GPIO.output(18, GPIO.LOW)

def main():
    # initialize the four register types
    store = ModbusSlaveContext(
        di = ModbusSequentialDataBlock(0, [0]*100),
        co = ModbusSequentialDataBlock(0, [0]*100),
        hr = ModbusSequentialDataBlock(0, [0]*100),
        ir = ModbusSequentialDataBlock(0, [0]*100))
    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName  = 'SPARSA'
    identity.ProductCode = 'SP'
    identity.VendorUrl   = 'http://doshmajhan.com/magicschoolbus'
    identity.ProductName = 'SPARSA Alarm Sensor'
    identity.ModelName   = 'SP_1337'
    identity.MajorMinorRevision = '1.0'
    pi.start()
    time = 5 # 5 seconds delaytime = 5 # 5 seconds delay
    loop = LoopingCall(f=updating_writer, a=(context,))
    loop.start(time, now=False) # initially delay by time
    StartTcpServer(context, identity=identity, address=('0.0.0.0', 502))

if __name__ == '__main__':

    pi = Alarm()
    main()
