'Upload files to Azure Cloud Storage

import glob
import os
import time

logtime = time.strftime("%Y%m%d-%H%M%S")
logmessage = "uploadmp3.py started"
command = "sed -i '1s/^/" + logtime + " " + logmessage + "\\n/' /home/pi/selcuk/log.txt"
os.system(command)

from azure.storage import BlobService
blob_service = BlobService(account_name='account_name', account_key='account_key')
blob_service.create_container('record')
blob_service.create_container('record', x_ms_blob_public_access='container')
blob_service.set_container_acl('record', x_ms_blob_public_access='container')

directory = "/home/pi/selcuk/mp3"

os.chdir(directory)
for file in glob.glob("*.mp3"):
    full_path = directory + "/" + file
    blob_service.put_block_blob_from_path(
        'record',
        file,
        full_path,
        x_ms_blob_content_type='audio/mpeg3'
    )
    delete_command = "rm " + file
    os.system(delete_command)

    logtime = time.strftime("%Y%m%d-%H%M%S")
    logmessage = file + " uploaded to cloud and deleted from device"
    command = "sed -i '1s/^/" + logtime + " " + logmessage + "\\n/' /home/pi/selcuk/log.txt"
    os.system(command)
