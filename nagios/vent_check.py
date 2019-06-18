#!/usr/bin/python

import sys
sys.path.insert(0, '/var/www/home/py/lib')
import rs485
import nagios
import argparse

parser = argparse.ArgumentParser(description='Vent argument')
parser.add_argument('--name', required=True,
                    help='Devie name on RS485 network')

args = parser.parse_args()

errorMsg = rs485.command(args.name, 'errorPresent')

if errorMsg == 'NO':
    print "OK"
    exit(nagios.STATE_OK)
else:
    print errorMsg
    exit(nagios.STATE_WARNING)


