#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import nagios

alarmStatus = rs485.command('Sprinkler1', 'getLeakAlarm');
if alarmStatus == 'YES':
    print 'WATER LEAK: %s' % (rs485.command('Sprinkler1', 'getLeak'))
    exit(nagios.STATE_CRITICAL)

if alarmStatus == 'NO':
    print "OK %s" % (rs485.command('Sprinkler1', 'getLeak'))
    exit(nagios.STATE_OK)

print 'Not sure: %s' % alarmStatus
exit(nagios.STATE_UNKNOWN)