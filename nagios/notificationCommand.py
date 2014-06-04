#!/usr/bin/python

import sys
import urllib
import urllib2

if len(sys.argv) != 3:
    print "USAGE: notificationCommand.py <to> <message>"
    exit(1)

with open('/etc/nagios/alert.secret', 'r') as content_file:
    token = content_file.read()

message = sys.argv[2].replace('\\n', "\n");
data = {'to': sys.argv[1],
        'message': message,
        'token': token}

response = urllib2.urlopen('http://www.syrota.com/houseAlert.php', urllib.urlencode(data))
#print(response.read())