"""
LAB 4 - 2a
"""

import boto3
bucket_name = '***'
s3 = boto3.client('s3')
response = s3.get_bucket_acl(Bucket=bucket_name)
print(response)