#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import urllib2
from datetime import datetime, timedelta
import time
import json

baseUrl = 'https://api.forecast.io/forecast/%s/42.1160296,-87.9019692' % sys.argv[1]

# check only every other day
if (int(time.time())/(3600*24)%2 == 0):
    print "Odd/Even check: skip today"
    exit(0)

# not enabling if it has rained in the past 2 days (not sure about the data, but just assuming over 50% = it has rained)
for i in range(1,3):
    target_date = datetime.now() - timedelta(days=i);
    url = baseUrl + ',%d' % (int(time.time()) - (3600*24*i))
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    if data['daily']['data'][0]['precipProbability'] > 0.5:
        print "It rained in the past 2 days"
        exit(0)

# Not enabling if it'll rain today or tomorrow (50%+)
response = urllib2.urlopen(baseUrl)
data = json.loads(response.read())
if data['daily']['data'][0]['precipProbability'] > 0.5 or data['daily']['data'][1]['precipProbability'] > 0.5:
    print "It will rain soon"
    exit(0)

print "No rain, enabling sprinkler"
rs485.command('Sprinkler2', "openValve0:7200")