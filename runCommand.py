#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485

__author__ = 'sergey'

if len(sys.argv) != 3:
    print "USAGE: runCommand.py <Device Address> <Command>"
    exit(1)

print rs485.command(sys.argv[1], sys.argv[2])
