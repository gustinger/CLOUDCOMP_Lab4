"""
LAB 4 - 2a
"""

import boto3
import botocore
s3 = boto3.resource('s3)
filename = 'REAME.md'
bucket_name = 'gustingerlab24abucket'
key = 'myREADME.md'
s3.Bucket(bucket_name).download_file(key,filename)
