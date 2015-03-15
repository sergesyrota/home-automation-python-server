#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import re

def getMotion(device, command, value):
    text = rs485.command(device, command)
    text = re.sub(r'(\d+)s', r'\1', text)
    if (int(text) < 300):
        return value
    else:
        return "0"

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Motion sensors connected to home network"
    print "graph_args --base 1000"
    print "graph_args --upper-limit 5"
    print "graph_args --lower-limit 0"
    print "graph_category sensors"
    print "graph_info Each line represents one motion sensor. 0 = no motion in the last 5 minutes; >0 motion detected (value only to diferentiate between sensors on graph)"
    print "graph_vlabel Sensors triggered"
    print "dining.label Dining room"
    exit(0)

try:
    print 'dining.value ' + getMotion('DiningBlinds', 'timeSinceMotion', "1")
except Exception as e:
    print >> sys.stderr, e
    exit(1)