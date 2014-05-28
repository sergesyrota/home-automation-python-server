#!/usr/bin/python
import rs485

__author__ = 'sergey'

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import datetime


print '%s - Distance: %s; AC Cycles: %s; Debug info: %s; Test: %s' % (datetime.datetime.now(), rs485.command('SumpPump', 'getDistance'), rs485.command('SumpPump', 'getAcPumpCycles'), rs485.command('SumpPump', 'debug'), rs485.command('SumpPump', 'getLastSelfTest'))
