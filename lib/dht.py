__author__ = 'sergey'

import rs485
import re
import json

class dhtException(Exception):
    pass

def ctof(deg):
    return (32+(float(deg)*9/5))

def ftoc(deg):
    return ((float(deg) - 32)*5/9)

def getJsonDht(device, command, ageLimit=300):
    res = rs485.command(device, command)
    if (res.startswith("ERROR")):
        raise dhtException('Error polling ' + device + ':' + command + ' ' + res)
    data = json.loads(res)
    if (data['age'] > ageLimit):
        raise dhtException("DHT data is too old: {0        } seconds".format(data['age']))
    # Normalize unit of measure to Celsius
    temp = float(data['t'])
    if (data['unit'] == 'C*100'):
        temp = temp/100.0
    elif (data['unit'] == 'F'):
        temp = ftoc(temp)
    return {
        'temperature': temp,
        'fahrenheit': ctof(temp),
        'humidity': data['rh'],
        'age': data['age']
        }

def getDht(device, command):
    text = rs485.command(device, command)
    p = re.compile('(\d+)C; (\d+)%RH; (\d+)s ago')
    res = p.search(text).groups()
    if (int(res[2]) > 1800):
        raise dhtException("Result too old (%d seconds); Discarding" % int(res[0]))
    return {
        'temperature': float(res[0]),
        'fahrenheit': ctof(float(res[0])),
        'humidity': res[1],
        'age': res[2]
        }
