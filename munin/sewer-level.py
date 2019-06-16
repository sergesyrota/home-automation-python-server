#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485


if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Sewage Basin Level"
    print "graph_args --base 1000"
    print "graph_args --upper-limit 100"
    print "graph_args --lower-limit 0"
    print "graph_category sensors"
    print "graph_info This shows the level in sewage basin of the basement"
    print "graph_vlabel Distance in cm"
    print "level.label level"
    print "level.warning 50"
    print "level.critical 80"
    exit(0)

try:
    print 'level.value %d' % (float(rs485.command('SewerMonitor', 'getDistance')))
except Exception as e:
    print >> sys.stderr, e
    exit(1)