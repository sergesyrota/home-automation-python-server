#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import json
import subprocess
import urllib2

def cToF(degrees):
    return (32+(degrees*9/5))

def getTemperature(device, command):
    res = rs485.command(device, command)
    if (res.startswith("ERROR")):
        raise Exception('Error polling ' + device + ':' + command + ' ' + res)
    data = json.loads(res)
    if (data['age'] < 300):
        return data['t']/100.0  # Unit is C*100
    else:
        raise Exception("DHT data is too old: {0        } seconds".format(data['age']))

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
    print "master_target.colour cee1ff"
    print "middle_current.label Middle (current)"
    print "middle_current.colour f99d2c"
    print "middle_target.label Middle (target)"
    print "middle_target.colour f7d1a3"
    exit(0)

try:
    # Master bedroom
    print('master_curret.value {0:4.1f}'.format(cToF(getTemperature('EnvMaster', 'getDht'))))
    p = subprocess.Popen('php /home/sergey/temps/hvac-zoning/server/cron-bedroom-controller.php getTarget', shell=True, stdout=subprocess.PIPE)
    data = p.stdout.read()
    print('master_target.data {0:4.1f}'.format(cToF(float(data))))
    # Middle bedroom
    res = urllib2.urlopen('http://192.168.8.90/tstat/')
    data = json.loads(res.read())
    print('middle_current.data {0}'.format(data['temp']))
    if (data['tmode'] == 2):
        print('middle_target.data {0}'.format(data['t_cool']))
    else:
        print('middle_target.data {0}'.format(data['t_heat']))
except Exception as e:
    print >> sys.stderr, e
    exit(1)