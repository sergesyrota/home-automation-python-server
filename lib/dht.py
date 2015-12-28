__author__ = 'sergey'

import rs485
import re

class dhtException(Exception):
    pass

def getDht(device, command):
    text = rs485.command(device, command)
    p = re.compile('(\d+)C; (\d+)%RH; (\d+)s ago')
    res = p.search(text).groups()
    if (int(res[2]) > 1800):
        raise dhtException("Result too old (%d seconds); Discarding" % int(res[0]))
    return {
        'temperature': float(res[0]),
        'fahrenheit': (32+(float(res[0])*9/5)),
        'humidity': res[1],
        'age': res[2]
        }
