"""
FILE: blob_storage_service.py
 
DESCRIPTION:
    This example shows how to get the blob container from Azure cloud 
    also how to upload and download file to blob container.
        
    This service expects that the Azure storage connection string and  blob container name
 
USAGE: python blob_storage_service.py
   
 
EXAMPLE OUTPUT:
  Getting blob container client
  Blob Access Type: container
  Upload content to block blob
  Download content from block blob
  
"""


import os
import sys
from datetime import datetime, timedelta
 
from azure.storage.blob import AccessPolicy, BlobServiceClient, ContainerSasPermissions, PublicAccess
 
SOURCE_FILE = 'Source.txt'
DEST_FILE = 'Destination.txt'
class BlobStorageService(object):
 
    def getsetBlobData(self):
        blob_service_client = BlobServiceClient.from_connection_string(
            "DefaultEndpointsProtocol=https;AccountName=xxxx;AccountKey=yyyy;EndpointSuffix=core.windows.net")
        print(blob_service_client)
 
        container_client = blob_service_client.get_container_client("blobcontainer")
        
         print(container_client)
 
        try:
             
            # Instantiate a new BlobClient
            blob_client = container_client.get_blob_client(SOURCE_FILE)
 
            
            # Upload content to block blob
            with open(SOURCE_FILE, "rb") as data:
                blob_client.upload_blob(data, blob_type="BlockBlob")
           
 
            # Download block blob content
            with open(DEST_FILE, "wb") as my_blob:
                download_stream = blob_client.download_blob()
                my_blob.write(download_stream.readall())
 
        finally:
            print("Completed Execution")           
 
 
 
if __name__ == '__main__':
    sample = BlobStorageService()
    sample.getsetBlobData()