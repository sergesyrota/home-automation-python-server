#!/usr/bin/python
__author__ = 'sergey'

# implements text based communication with home's RS-485 bus.
# Only one of these worked should be started to avoid collisions on the bus

import gearman
import serial
import daemon

# sends a string to the bus, and returns the reply
def task_listener_rs485(gearman_worker, gearman_job):
    rs485 = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
    rs485.write(gearman_job.data)
    res = rs485.readline()
    rs485.close()
    return res


gm_worker = gearman.GearmanWorker(['localhost:4730'])
# gm_worker.set_client_id is optional
gm_worker.set_client_id('rs485-worker')
gm_worker.register_task('rs485', task_listener_rs485)

#Enter our work loop and call gm_worker.after_poll() after each time we timeout/see socket activity
with daemon.DaemonContext():
    gm_worker.work()