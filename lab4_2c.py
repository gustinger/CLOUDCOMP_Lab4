"""
LAB 4 - 2a
"""

import boto3
s3_client = boto3.client('s3')
filename = 'REAME.md'
bucket_name = 'gustingerlab24abucket'
s3_client.upload_file(filename,bucket_name,filename)
