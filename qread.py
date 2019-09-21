#!/usr/bin/env python3

# How to use the Azure Storage SDK with Python:
# https://docs.microsoft.com/en-us/azure/storage/storage-python-how-to-use-queue-storage

import configparser
config = configparser.RawConfigParser()
config.read('storage.conf')
accName = config.get('storage_account', 'accName')
accKey = config.get('storage_account', 'accKey')
queueName = config.get('storage_account', 'queueName')

# sudo pip install blessings
from azure.storage.queue import QueueService, QueueMessageFormat
from blessings import Terminal
import sys
import time

queue_service = QueueService(account_name=accName, account_key=accKey)
queue_service.decode_function = QueueMessageFormat.text_base64decode

t = Terminal()
print(t.green('Connected to Azure Storage Queue ' + queueName + '...'))
# Get approximate number of messages in queue
queue_metadata = queue_service.get_queue_metadata(queueName)
count = queue_metadata.approximate_message_count
print('Approximate number of messages in queue: ', count, '\n')

while True:
    messages = queue_service.get_messages(queueName)
    if messages:
        # Get the next message
        for message in messages:
            print(t.bold_yellow(message.content))
            queue_service.delete_message(queueName, message.id, message.pop_receipt)
            print(t.blue('-' * 40 + '\n'))
        time.sleep(4)
