#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import dht
import rs485

def getHumidity(device, command):
    res = rs485.command(device, command)
    if (res.startswith("ERROR")):
        raise Exception('Error polling ' + device + ':' + command + ' ' + res)
    return res

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Indoor humidity"
    print "graph_args --base 1000"
    print "graph_category sensors"
    print "graph_info Shows humidity trends across the house"
    print "graph_vlabel %RH"
    print "watermain.label Crawlspace"
    print "basement.label Basement LIV2-B2 (in ceiling)"
    print "utility.label Utility Room (by window)"
    exit(0)

try:
    print 'watermain.value ' + getHumidity('WtrMn', 'getHumidity')
    data = dht.getDht('Sprinkler1', 'getDht')
    print 'basement.value ' + data['humidity']
    data = dht.getDht('Sprinkler2', 'getDht')
    print 'utility.value ' + data['humidity']
except Exception as e:
    print >> sys.stderr, e
    exit(1)