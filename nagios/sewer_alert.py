#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import nagios

distance = float(rs485.command('SewerMonitor', 'getDistance'))
print 'Sewer level: %d' % (distance)

if distance > 55:
    exit(nagios.STATE_CRITICAL)
if distance > 40:
    exit(nagios.STATE_WARNING)

exit(nagios.STATE_OK)


