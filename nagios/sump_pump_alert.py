#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import nagios

if rs485.command('SumpPump', 'alertPresent') == 'YES':
    reason = rs485.command('SumpPump', 'alertReason')
    if reason == 'Water level':
        print 'Water level: %s CM' % (rs485.command('SumpPump', 'getDistance'))
    elif reason == 'Battery voltage':
        print 'Battery voltage: %s' % (rs485.command('SumpPump', 'getBattVoltage'))
    else:
        print reason
    exit(nagios.STATE_CRITICAL)

print "OK"
exit(nagios.STATE_OK)


