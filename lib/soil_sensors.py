__author__ = 'sergey'

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485

import re
from struct import *

class soilException(Exception):
    pass

def getData(address, sensorId):
    text = rs485.command(address, "getSensor:%d" % sensorId)
    p = re.compile('(\d+)s ago: ([0-9a-fA-F]{14})')
    res = p.search(text).groups()
    if (int(res[0]) > 1800):
        raise soilException("Result too old (%d seconds); Discarding" % res[1])
    # byte sensor ID
    # 16-bit unsigned number: soil moisture
    # 16-bit unsigned number: internal leak sensor
    # 16-bit unsigned number: battery voltage
    data = unpack('<BHHH', res[1].decode('hex'))
    return {
        'soilMoisture': data[1],
        'internalLeak': data[2],
        'batteryVoltage': float(data[3])/1000
        }
