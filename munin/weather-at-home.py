#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import urllib2
import json
import dht

if len(sys.argv) > 1 and sys.argv[1] == "autoconf":
    print "yes"
    exit(0)


if len(sys.argv) > 1 and sys.argv[1] == "config":
    print "graph_title Outdoor home temperature"
    print "graph_args --base 1000"
    print "graph_category sensors"
    print "graph_info Shows outdoor temperature over time"
    print "graph_vlabel deg F"
    print "temp.label Outside temperature"
    print "feels.label Outside Feels like"
    print "garage.label Garage temperature"
    exit(0)


try:
    # Weather data
    baseUrl = 'https://api.darksky.net/forecast/4d495cee5b2fe58a3e12c1a453cd3afe/42.1160296,-87.9019692'
    response = urllib2.urlopen(baseUrl)
    data = json.loads(response.read())
    print "temp.value %.01f" % data['currently']['temperature']
    print "feels.value %.01f" % data['currently']['apparentTemperature']

    # Garage
    data = dht.getJsonDht('GarageSens', 'getDht')
    print('garage.value {0:4.1f}'.format(data['fahrenheit']))
except Exception as e:
    print >> sys.stderr, e
    exit(1)