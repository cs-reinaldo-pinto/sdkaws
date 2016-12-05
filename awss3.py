#/usr/bin/python

import boto3

#s3=boto3.resource('s3')

name='tes1'

session = boto3.Session(profile_name='dev')

s3 = session.client('s3')
s3.create_bucket(Bucket=name)

print (s3.list_objects(Bucket=name))

print (s3.get_bucket_logging(Bucket=name))
