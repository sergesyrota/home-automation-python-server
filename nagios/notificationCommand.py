#!/usr/bin/python

import sys
import urllib
import urllib2
import hashlib

if len(sys.argv) != 3:
    print "USAGE: notificationCommand.py <to> <message>"
    exit(1)

message = sys.argv[2].replace('\\n', "\n");
data = {'to': sys.argv[1],
        'message': message,
        'token': hashlib.md5(message).hexdigest()}

response = urllib2.urlopen('http://www.syrota.com/houseAlert.php', urllib.urlencode(data))
#print(response.read())