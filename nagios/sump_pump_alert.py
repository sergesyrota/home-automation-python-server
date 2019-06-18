#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import nagios

status = rs485.command('SumpPump', 'alertPresent')

if status == 'YES' or status == 'YES, Ack\'ed':
    reason = rs485.command('SumpPump', 'alertReason')
    if reason == 'Water level':
        print 'Water level: %s CM' % (rs485.command('SumpPump', 'getDistance'))
    elif reason == 'Battery voltage':
        print 'Battery voltage: %s' % (rs485.command('SumpPump', 'getBattVoltage'))
    else:
        print reason
    if status == 'YES':
        exit(nagios.STATE_CRITICAL)
    else:
        exit(nagios.STATE_WARNING)

print "OK"
exit(nagios.STATE_OK)


