
"""
Just some scripts used in my web app, theres no singluar purpose 
for this file.
"""
import os
import sys
import time
import json
from typing import Union

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
