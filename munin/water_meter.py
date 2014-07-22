#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485


if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Water meter"
    print "graph_args --base 1000"
    print "graph_category sensors"
    print "graph_info Shows number of half-rotations of water meter disc"
    print "graph_vlabel units"
    print "units.label Rotations per second"
    print "units.type DERIVE"
    print "units.min 0"
    exit(0)

try:
    print 'units.value ' + rs485.command('WtrMn', 'getCount')
except Exception as e:
    print >> sys.stderr, e
    exit(1)