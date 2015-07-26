#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import soil_sensors

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Soil probes battery voltage"
    print "graph_args --base 1000"
    print "graph_category sensors"
    print "graph_info Soil moisture sensors around the yard, battery voltage."
    print "graph_vlabel Voltage in V"
    print "rf1sen0.label Raised Flower Bed 0"
    print "rf1sen0.warning 2.9:"
    print "rf1sen0.critical 2.4:"
    print "rf1sen1.label Raised Flower Bed 1"
    print "rf1sen1.warning 2.9:"
    print "rf1sen1.critical 2.4:"
    exit(0)

problems = False
for i in range(0,2):
    try:
        data = soil_sensors.getData('RfReceiver1', i)
        print 'rf1sen%d.value %.3f' % (i, data['batteryVoltage'])
    except Exception as e:
        problems = True
