#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485


if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Sewage basin laser reading success persent"
    print "graph_args --base 1000"
    print "graph_args --upper-limit 100"
    print "graph_args --lower-limit 0"
    print "graph_category sensors"
    print "graph_info This shows how often reading collected by the laser sensor is within expected range"
    print "graph_vlabel % success"
    print "level.label success"
    print "level.warning 40:"
    print "level.critical 5:"
    exit(0)

try:
    print 'level.value %d' % (int(rs485.command('SewerMonitor', 'getPercentValid')))
except Exception as e:
    print >> sys.stderr, e
    exit(1)