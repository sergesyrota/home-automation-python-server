#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485


if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title AC sump pump duty"
    print "graph_args --base 1000"
    print "graph_category sensors"
    print "graph_info This shows how much time AC pump spends working"
    print "graph_vlabel seconds"
    print "seconds.label ON seconds per minute"
    print "seconds.type DERIVE"
    print "seconds.min 0"
    print "seconds.cdef seconds,60,*"
    print "seconds.warning 30"
    print "seconds.critical 45"
    exit(0)

try:
    print 'seconds.value ' + rs485.command('SumpPump', 'getAcPumpOnTime')
except Exception as e:
    print >> sys.stderr, e
    exit(1)