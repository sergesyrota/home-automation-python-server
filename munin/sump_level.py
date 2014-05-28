#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485


if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Sump Pit Water Level"
    print "graph_args --base 1000"
    print "graph_args --upper-limit 0"
    print "graph_args --lower-limit -700"
    print "graph_category sensors"
    print "graph_info This shows water level in the sump pit of the basement, relative to the top cover"
    print "graph_vlabel Distance in cm"
    print "level.label level"
    print "level.warning -40"
    print "level.critical -30"
    exit(0)

try:
    print 'level.value ' + rs485.command('SumpPump', 'getDistance')
except Exception as e:
    print >> sys.stderr, e
    exit(1)