#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import urlparse

def getTemperature(device, command):
    res = rs485.command(device, command)
    if (res.startswith("ERROR")):
        raise Exception('Error polling ' + device + ':' + command + ' ' + res)
    return "%d" % (32+(float(res)*9/5))

def getTemperatureFromBench(command):
    res = rs485.command('Bench', command)
    if (res.startswith("ERROR")):
        raise Exception('Error polling Bench:' + command + ' ' + res)
    resVars = urlparse.parse_qs(res);
    if (int(resVars['age'][0]) > 300 or int(resVars['temp'][0]) > 700):
        return "U"
    # Result is in tenth of degrees celsius, so need to divide by 10 to get proper number
    return "%.1f" % (32+(float(resVars['temp'][0])*9/50))

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Indoor temperatures"
    print "graph_args --base 1000"
    print "graph_category sensors"
    print "graph_info Shows temperature trends across the house"
    print "graph_vlabel deg F"
    print "watermain.label Crawlspace"
    print "watermain.warning 45:"
    print "watermain.critical 40:"
    print "leah.label Leah Room"
    print "parents.label Guest Bedroom"
    exit(0)

try:
    print 'watermain.value ' + getTemperature('WtrMn', 'getTemp')
    print 'leah.value ' + getTemperatureFromBench('getSens1')
    print 'parents.value ' + getTemperatureFromBench('getSens2')
except Exception as e:
    print >> sys.stderr, e
    exit(1)