#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485

import re

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Backup pump voltage"
    print "graph_args --base 1000"
    print "graph_args --upper-limit 13"
    print "graph_args --lower-limit 10"
    print "graph_category sensors"
    print "graph_info This shows battery voltage for backup sump pump"
    print "graph_vlabel voltage"
    print "voltage.label Voltage in V"
    print "voltage.warning 12.6:"
    print "voltage.critical 12.2:"
    exit(0)

try:
    text = rs485.command('SumpPump', 'getBattVoltage')
    text = re.sub(r'(\d+)mV', r'\1', text)
    voltage = int(text)/1000.0
    print 'voltage.value ' + str(voltage)
except Exception as e:
    print >> sys.stderr, e
    exit(1)
