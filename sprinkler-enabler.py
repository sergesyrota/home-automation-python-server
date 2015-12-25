#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import soil_sensors

locations = {
    'fern': {'moisture-address': 0, 'sprinklerDevice': 'Sprinkler1', 'sprinkler-valve': 0, 'thresholds': {700: 3*3600, 800: 2*3600}},
    'raised-flower-bed':  {'moisture-address': 1, 'sprinklerDevice': 'Sprinkler2', 'sprinkler-valve': 0, 'thresholds': {850: 3*3600, 900: 2*3600, 950: 3600}}
}

for name, details in locations.iteritems():
    data = soil_sensors.getData('RfReceiver1', details['moisture-address'])
    for moisture, duration in details['thresholds'].iteritems():
        print 'Comparing sensor %d to threshold %d' % (data['soilMoisture'], moisture)
        if (data['soilMoisture'] < moisture and data['soilMoisture'] > 300):
            print 'Turning %s on for %d seconds, as moisture is under %d (%d)' % (name, duration, moisture, data['soilMoisture'])
            rs485.command(details['sprinklerDevice'], "openValve%d:%d" % (details['sprinkler-valve'], duration))
            break
