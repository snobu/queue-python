
fortune &rarr; Azure Storage Queue &rarr; Python Consumer Demo
--------------------------------------------------------------

#### Create a flat file, name it `storage.conf` and make it look like this:
    [storage_account]
    accName = STORAGE_ACCOUNT_NAME
    accKey = STORAGE_ACCOUNT_KEY
    queueName = QUEUE_NAME

**NOTE:** Azure Storage Queue names are always **all lowercase**.

#### Run `./qput.py` to post and `./qread.py` to read from queue:
    $ ./qput.py
    Writing to Azure Storage Queue queue1...
    !!!!!!!!!!!!!!!!!!!
    Done adding messages.


    $ ./qread.py
    Connected to Azure Storage Queue queue1...
    Approximate number of messages in queue:  64
    ---------------------------------------

    "Virtual" means never knowing where your next byte is coming from.

    ----------------------------------------

    Lie, n.:
    A very poor substitute for the truth, but the only one
    discovered to date.

    ----------------------------------------

#### Dependencies:
    $ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
    $ pip install azure-storage blessings subprocess
    
#### How to use the Azure Storage SDK with Python:
https://docs.microsoft.com/en-us/azure/storage/storage-python-how-to-use-queue-storage
