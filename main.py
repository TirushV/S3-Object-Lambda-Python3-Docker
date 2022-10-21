import boto3

s3 = boto3.client('s3')

print('Original Object: ')
original = s3.get_object(
  Bucket='<s3-bucket-name>',
  Key='title.txt')
print(original['Body'].read().decode('utf-8'))

print('Processed Object: ')
transformed = s3.get_object(
  Bucket='arn:aws:s3-object-lambda:ap-south-1:<AWS-Account>:accesspoint/title-transform',
  Key='title.txt')
print(transformed['Body'].read().decode('utf-8'))
