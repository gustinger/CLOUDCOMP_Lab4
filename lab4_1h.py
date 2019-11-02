import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
	response = ec2.describe_scurity_groups(GroupIds='****id')
	print('Success',response)
except ClientError as e:
	print(e)