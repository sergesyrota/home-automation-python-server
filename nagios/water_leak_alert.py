#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import nagios
import subprocess

timeRange = '6h'
filePath = '/var/lib/munin/local/srv1.local-water_meter-gph-d.rrd'
gphMultiplier = 19.02;
maxZeroFlowGph = 0.15;

# Take last {timeRange} of 5 minute readings (removing anything that does not start with timestamp),
# multiply by 19.02 (to bring to gallons per hour), then count how many complete 0 readings we got
numberZeros = subprocess.Popen("rrdtool fetch %s MIN -s end-%s | grep '^[0-9]'  | awk '{if ($2*%.03f<%.03f) {print 0} else {print $2*%.03f}}' | grep 0$ | wc -l" % (filePath, timeRange, gphMultiplier, maxZeroFlowGph, gphMultiplier), stdout=subprocess.PIPE, shell=True).stdout.read()

if (int(numberZeros) > 0):
    print '5 minute sections with 0 reading during %s: %d' % (timeRange, int(numberZeros))
    exit(nagios.STATE_OK)
else:
    print 'No 5 minute sections with 0 readings in the last %s! Possible water leak!' % timeRange
    exit(nagios.STATE_CRITICAL)
