#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import urlparse
import dht

def getTemperature(device, command):
    res = rs485.command(device, command)
    if (res.startswith("ERROR")):
        raise Exception('Error polling ' + device + ':' + command + ' ' + res)
    return "%d" % (32+(float(res)*9/5))

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
    print "main_sink.label Under main kitchen sink"
    print "utility.label Utility Room (by window)"
    exit(0)

try:
    print 'watermain.value ' + getTemperature('WtrMn', 'getTemp')
    #data = dht.getDht('Sprinkler1', 'getDht')
    #print 'main_sink.value %d' % data['fahrenheit']
    data = dht.getDht('Sprinkler2', 'getDht')
    print 'utility.value %d' % data['fahrenheit']
except Exception as e:
    print >> sys.stderr, e
    exit(1)