#!/usr/bin/env python3

# How to use the Azure Storage SDK with Python:
# https://docs.microsoft.com/en-us/azure/storage/storage-python-how-to-use-queue-storage

# DEPENDENCIES
# sudo apt-get install build-essential libssl-dev libffi-dev python-dev
# sudo pip install azure-storage blessings subprocess

import configparser
config = configparser.RawConfigParser()
config.read('storage.conf')
accName = config.get('storage_account', 'accName')
accKey = config.get('storage_account', 'accKey')
queueName = config.get('storage_account', 'queueName')

from azure.storage.queue import QueueService, QueueMessageFormat
from blessings import Terminal
import sys
import time
import subprocess

def get_stdout_from_cmd(command):
    try:
        p = subprocess.Popen(command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout = p.stdout.readlines()
    except:
        raise Exception('Unable to get_stdout_from_cmd(). Maybe fortune is not installed?')
    result = b''.join(stdout)
    return result

queue_service = QueueService(account_name=accName, account_key=accKey)
queue_service.encode_function = QueueMessageFormat.text_base64encode

t = Terminal()
print(t.red('Writing to Azure Storage Queue ' + queueName + '...'))

for i in range (1, 20):
        cmd = 'fortune'
        msg = get_stdout_from_cmd(cmd)
        queue_service.put_message(queueName, msg.decode("utf-8"))
        sys.stdout.write('!')
        sys.stdout.flush()

print('\nDone adding messages.')
