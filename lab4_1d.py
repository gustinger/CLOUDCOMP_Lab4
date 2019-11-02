import sys
import boto3
from botocore.expceptions import ClientError
ec2 = boto3.client('ec2')
action = sys.argv[1].upper()

#do a dryrun first to verify permissions
try:
	ec2.reboot_instances(InstanceIds=['instanceid'], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
		print("You don't have permission to reboot instances.")
		raise
	#Dryrun succeeded, run start_instances again without dryrun

try:
		response = ec2.reboot_instances(InstanceIds=['instanceid'], DryRun=False)
		print('Success',response)
	except ClientError as e:
		print(e)