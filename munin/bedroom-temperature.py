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
    print "master_current.draw LINE2"
    print "master_target.label Master (target)"
    print "master_target.colour 87b5ff"
    print "middle_current.label Middle (current)"
    print "middle_current.draw LINE2"
    print "middle_current.colour c67e01"
    print "middle_target.label Middle (target)"
    print "middle_target.colour efb04a"
    print "guest_current.label Guest (current)"
    print "guest_current.draw LINE2"
    print "guest_current.colour 0ba08a"
    print "guest_target.label Guest (target)"
    print "guest_target.colour 6de0cf"
    exit(0)

try:
    # Master bedroom
    data = json.load(open('/tmp/nest_cache_ffdbe1bde9d0791224a3995efcc2ef89'))
    print('master_current.value {0:4.1f}'.format(data['oKZteeWa7Y_ka_ivTHj8hMTRR5q0HWhn']['ambient_temperature_f']))
    print('master_target.value {0:4.1f}'.format(data['oKZteeWa7Y_ka_ivTHj8hMTRR5q0HWhn']['target_temperature_f']))
    
#    p = subprocess.Popen('env - $(cat /home/sergey/temps/hvac-zoning/cli-thermostat/.env.master) php /home/sergey/temps/hvac-zoning/cli-thermostat/thermostat.php', shell=True, stdout=subprocess.PIPE)
#    data = json.loads(p.stdout.read())
#    print('master_current.value {0:4.1f}'.format(data['current']))
#    print('master_target_heat.value {0:4.1f}'.format(data['target']['heat']))
#    print('master_target_cool.value {0:4.1f}'.format(data['target']['cool']))
    
    # Middle bedroom
    print('middle_current.value {0:4.1f}'.format(data['oKZteeWa7Y9yS7GWYJ8uecTRR5q0HWhn']['ambient_temperature_f']))
    print('middle_target.value {0:4.1f}'.format(data['oKZteeWa7Y9yS7GWYJ8uecTRR5q0HWhn']['target_temperature_f']))
    
    # Guest bedroom
    print('guest_current.value {0:4.1f}'.format(data['oKZteeWa7Y_GQ-upue_lG8TRR5q0HWhn']['ambient_temperature_f']))
    print('guest_target.value {0:4.1f}'.format(data['oKZteeWa7Y_GQ-upue_lG8TRR5q0HWhn']['target_temperature_f']))
#    p = subprocess.Popen('env - $(cat /home/sergey/temps/hvac-zoning/cli-thermostat/.env.south) php /home/sergey/temps/hvac-zoning/cli-thermostat/thermostat.php', shell=True, stdout=subprocess.PIPE)
#    data = json.loads(p.stdout.read())
#    print('guest_current.value {0:4.1f}'.format(data['current']))
#    print('guest_target_heat.value {0:4.1f}'.format(data['target']['heat']))
#    print('guest_target_cool.value {0:4.1f}'.format(data['target']['cool']))
    
    # Master bedroom
#    data = dht.getJsonDht('EnvMaster', 'getDht')
#    print('master_current.value {0:4.1f}'.format(data['fahrenheit']))
#    p = subprocess.Popen('php /home/sergey/temps/hvac-zoning/server/cron-bedroom-controller.php getTarget', shell=True, stdout=subprocess.PIPE)
#    data = p.stdout.read()
#    print('master_target.value {0:4.1f}'.format(dht.ctof(float(data))))
    # Middle bedroom
#    res = urllib2.urlopen('http://192.168.8.90/tstat/', timeout=60)
#    data = json.loads(res.read())
#    print('middle_current.value {0}'.format(data['temp']))
#    if (data['tmode'] == 2):
#        print('middle_target.value {0}'.format(data['t_cool']))
#    else:
#        print('middle_target.value {0}'.format(data['t_heat']))
    # Guest bedroom
#    res = urllib2.urlopen('http://guest-thermostat.iot.syrota.com:5000//')
#    data = json.loads(res.read())
#    print('guest_current.value {0:4.1f}'.format(dht.ctof(data['temperature'])))
#    p = subprocess.Popen('php /home/sergey/temps/hvac-zoning/server/cron-bedroom-controller.php getTargetGuest', shell=True, stdout=subprocess.PIPE)
#    data = p.stdout.read()
#    print('guest_target.value {0:4.1f}'.format(dht.ctof(float(data))))
except Exception as e:
    print >> sys.stderr, e
    exit(1)