import os
from datetime import datetime, timedelta, timezone

from azure.storage.blob import (BlobServiceClient, BlobSasPermissions,
                                ContainerClient, generate_blob_sas)
from dotenv import load_dotenv
from authy.models import Profile

load_dotenv()
env = os.environ


def container_files(container):
    storage_name = env.get('STORAGE_NAME')
    storage_key = env.get('STORAGE_KEY')
    connect_str = ('DefaultEndpointsProtocol=https;AccountName='
                   + storage_name + ';AccountKey=' + storage_key
                   + ';EndpointSuffix=core.windows.net')

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container)
    blob_list = []
    for blob_i in container_client.list_blobs():
        blob_list.append(blob_i.name)

    return blob_list


def file_urls(filename, container):
    storage_name = env.get('STORAGE_NAME')
    storage_key = env.get('STORAGE_KEY')

    expiry = datetime.now(timezone.utc) + timedelta(hours=1)
    sas_i = generate_blob_sas(account_name=storage_name,
                              container_name=container,
                              blob_name=filename,
                              account_key=storage_key,
                              permission=BlobSasPermissions(read=True),
                              expiry=expiry)

    sas_url = (f'https://{storage_name}.blob.core.windows.net/{container}'
               f'/{filename}?{sas_i}')

    return sas_url


def get_files(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startswith('.'):
                yield entry


def upload(container, files, blob_files):
    cnxn = env.get('STORAGE_CONN_STRING')
    container_client = ContainerClient.from_connection_string(cnxn, container)

    sent = False
    for file in files:
        if file.name not in blob_files:
            blob_client = container_client.get_blob_client(file.name)
            with open(file.path, "rb") as data:
                blob_client.upload_blob(data)
                sent = True

    return sent
