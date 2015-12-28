#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import nagios
import dht

data = dht.getDht('Sprinkler1', 'getDht')
if data['temperature'] < 5:
    print 'Freezing temperature: %dC' % data['temperature']
    exit(nagios.STATE_CRITICAL)
elif data['temperature'] < 10:
    print 'Low temperature: %dC' % data['temperature']
    exit(nagios.STATE_WARNING)

print "OK %dC" % data['temperature']
exit(nagios.STATE_OK)


