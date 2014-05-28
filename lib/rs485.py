__author__ = 'sergey'

import gearman
import re

class rs485Exception(Exception):
    pass

gm_client = gearman.GearmanClient(['localhost:4730'])

def command(address, command):
    job = gm_client.submit_job("rs485", chr(2) + address + '>' + command + "\n")

    if job.timed_out:
        raise rs485Exception('Gearman request timed out!')
    elif job.state == gearman.constants.JOB_UNKNOWN:
        raise rs485Exception('Gearman connection failed!')
    elif not(job.complete):
        raise rs485Exception('Unknown Gearman error!')
    else:
        match = re.search(r'\x02>(.*)\n', job.result)
        if match is None:
            raise rs485Exception('RS485 response does not match pattern: ' + job.result)
        else:
            return match.group(1)
