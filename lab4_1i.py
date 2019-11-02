import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
	response = ec2.create_scurity_group(GroupName='lab41i', Description='lab41i created 10/29/19')
	print('Success',response)
except ClientError as e:
	print(e)