"""
LAB 4 - 2a
"""

import boto3
import requests
bucket_name = 'gustingerlab24abucket'
key = 'README.md'
s3 = boto3.client('s3)
response = s3.generate_presigned_url(CLientMethod='get_object',Params={
    'Bucket': bucket_name,
    'Key': key})
print(response)