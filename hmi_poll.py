# Server to handle status updates from the alarm clients
# @author: Doshmajhan, bharmat

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging
import argparse
import time
import sys
import random
import time

class sensor():
    def __init__(self, team, addr, stat):
        self.team = team
        self.filename = str(team) + "-stat.txt"
        self.addr = addr
        self.stat = self.get_stat(self.addr)
        self.sleeping = False
        self.timeout = 0

    def get_stat(self, addr):
        # connect to modbus slave
        try:
            client = ModbusClient(addr, port=502)
            client.connect()
            rr = client.read_holding_registers(0x00,1,unit=0)
            stat = rr.registers[0]
            print "Stat " + str(stat)
            client.close()
            return stat

        except:
            # if unable to connect, return None
            log_stuff("Unable to connect to " + self.addr)
            return None


def log_stuff(message):
    with open('scada.log','a+') as f:
        now = time.strftime("%c")
        f.write(now + " - " + message + "\n")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Poll the alarm sensor of a given team.')
    parser.add_argument('-t', help='The URL to start scraping from', dest="team",  required="True")
    parser.add_argument('-a', help='Address of the alarm sensor to poll', dest="address", required="True")
    args = parser.parse_args()
    f = open('status.txt', 'w')
    while True:
        sensor_obj = sensor(args.team, args.address, 0)

        if(sensor_obj.stat != None and sensor_obj.stat == 1):
            log_stuff("Alarm sensor is ON")

        elif (sensor_obj.stat != None and sensor_obj.stat != 0):
            log_stuff("Alarm sensor is OFF")
        
        f.write(sensor_obj.stat)

        time.sleep(10)

    print "Exiting"
