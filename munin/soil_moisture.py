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
    print "rf1sen0.label Fern"
    print "rf1sen1.label Raised Flower Bed"
    exit(0)

problems = False
for i in range(0,2):
    try:
        data = soil_sensors.getData('RfReceiver1', i)
        print 'rf1sen%d.value %d' % (i, data['soilMoisture'])
    except Exception as e:
        problems = True
