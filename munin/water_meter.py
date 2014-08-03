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
    print "graph_info Shows water usage rate"
    print "graph_vlabel gph"
    print "gph.label Gallons per hour"
    print "gph.type DERIVE"
    # Original value is per second. One half-rotation is 20mL. 20ml/second * 3600 = 20ml/hour; 1 gal = 3785.41ml;
    # to get gallons perhour, multiply by 3600 * 20/3785.41 = 19.020396733775205327824462871921
    print "gph.cdef gph,19.02,*"
    print "gph.min 0"
    exit(0)

try:
    print 'gph.value ' + rs485.command('WtrMn', 'getCount')
except Exception as e:
    print >> sys.stderr, e
    exit(1)