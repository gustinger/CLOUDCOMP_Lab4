import boto3

ec2 = boto3.client('ec2')
response = ec2.delete_key_pair(KeyName='gustingerLab41fKey')
print('Success', response)