#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import json
import re

def getData():
    for i in range(3):
        #print "trying %d" % i
        try:
            return rs485.command('SolarMon', 'getmWh')
        except Exception as e:
            if i>=2:
                raise e

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Solar Test Monitor"
    print "graph_args --base 1000 --lower-limit 0"
    print "graph_period hour"
    print "graph_category sensors"
    print "graph_info Displays power generation of solar panels oriented in different directions"
    print "graph_vlabel Power in mW"
    print "a4.type DERIVE"
    print "a4.label A4"
    print "a5.type DERIVE"
    print "a5.label A5"
    exit(0)

try:
    raw = getData()
    # :facepalm: invalid json
    raw = re.sub(r"(\d):", '"\\1":', raw)
    #print raw
    data = json.loads(raw)
    #print data
    print 'a4.value %d' % (data["4"])
    print 'a5.value %d' % (data["5"])
except Exception as e:
    print >> sys.stderr, e
    exit(1)