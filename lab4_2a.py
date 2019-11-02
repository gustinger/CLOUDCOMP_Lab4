"""
LAB 4 - 2a
"""

import boto3
import logging
import botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket = bucket_name)
        else:
            s3_client = boto3.client('s3',region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketContiguation=location)
    except ClientError as e:
        logging.error(e)
        return False
     return True
     
     create_bucket('gustingerlab42abucket','us-east-2')
