#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import json
import dht
import subprocess
import urllib2

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Bedroom temperatures"
    print "graph_args --base 1000"
    print "graph_category sensors"
    print "graph_info Shows target and current temperatures in bedrooms"
    print "graph_vlabel deg F"
    print "master_current.label Master (current)"
    print "master_current.colour 2c7bf9"
    print "master_target.label Master (target)"
    print "master_target.colour 87b5ff"
    print "middle_current.label Middle (current)"
    print "middle_current.colour c67e01"
    print "middle_target.label Middle (target)"
    print "middle_target.colour efb04a"
    exit(0)

try:
    # Master bedroom
    data = dht.getJsonDht('EnvMaster', 'getDht')
    print('master_current.value {0:4.1f}'.format(data['fahrenheit']))
    p = subprocess.Popen('php /home/sergey/temps/hvac-zoning/server/cron-bedroom-controller.php getTarget', shell=True, stdout=subprocess.PIPE)
    data = p.stdout.read()
    print('master_target.value {0:4.1f}'.format(dht.ctof(float(data))))
    # Middle bedroom
    res = urllib2.urlopen('http://192.168.8.90/tstat/')
    data = json.loads(res.read())
    print('middle_current.value {0}'.format(data['temp']))
    if (data['tmode'] == 2):
        print('middle_target.value {0}'.format(data['t_cool']))
    else:
        print('middle_target.value {0}'.format(data['t_heat']))
except Exception as e:
    print >> sys.stderr, e
    exit(1)