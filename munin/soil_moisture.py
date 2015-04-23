#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import soil_sensors

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Soil moisture levels"
    print "graph_args --base 1000"
    print "graph_category sensors"
    print "graph_info Soil moisture sensors around the yard, showing relative soil moisture levels."
    print "graph_vlabel Soil moisture"
    print "rf1sen0.label Raised Flower Bed 1"
    exit(0)

try:
    data = soil_sensors.getData('RfReceiver1', 0)
    print 'rf1sen0.value %d' % data['soilMoisture']
except Exception as e:
    print >> sys.stderr, e
    exit(1)
