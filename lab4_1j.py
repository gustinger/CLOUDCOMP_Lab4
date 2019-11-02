import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
	response = ec2.delete_scurity_group(GroupId='****id')
	print('Success',response)
except ClientError as e:
	print(e)