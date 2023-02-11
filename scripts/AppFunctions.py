
"""
Just some scripts used in my web app, theres no singluar purpose 
for this file.
"""
import os
import sys
import time
import json
import pytz
from typing import Union
from datetime import datetime


def read_key(keydir: str, name: str) -> Union[str,None]:
    """
    Reads a secure string from a file.
    """
    value = None
    keyfile = os.path.join(keydir, '{}.key'.format(name))
    try:
        with open(keyfile, 'r') as kf:
            value = kf.read().strip().replace('\n','')
    except Exception as e:
        print('Failed to read key {} from {}: {}'.format(name, keyfile, str(e)))
    return value

def make_datetime(timezone: str) -> tuple:
    rn =  datetime.utcnow().replace(tzinfo=pytz.utc)
    time = ''
    date = ''
    rn_zoned = rn.astimezone(pytz.timezone(timezone))
    date = rn_zoned.strftime('%A, %-d, %Y')
    time = rn_zoned.strftime('%-I:%M %p')
    return date, time
