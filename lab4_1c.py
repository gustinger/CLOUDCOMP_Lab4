import sys
import boto3
from botocore.expceptions import Client Error

ec2 = boto3.client('ec2')
action = sys.argv[1].upper()
if action == 'ON':
	#do a dryrun first to verify permissions
	try:
		ec2.start_instances(InstanceIds=['instanceid'], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise
	#Dryrun succeeded, run start_instances again without dryrun
try:
		response = ec2.start_instances(InstanceIds=['instanceid'], DryRun=True)
		print(response)
	except ClientError as e:
		print(e)
else:
	#do a dryrun first to verify permissions
	try:
		ec2.start_instances(InstanceIds=['instanceid'], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise
	#Dryrun succeeded, run start_instances again without dryrun
try:
		response = ec2.start_instances(InstanceIds=['instanceid'], DryRun=True)
		print(response)
	except ClientError as e:
		print(e)