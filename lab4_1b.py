import sys
import boto3

ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
	response = ec2.monitor_instances('InstanceID')
else:
	response = ec2.unmonitor_instances('instanceid')
print(response)