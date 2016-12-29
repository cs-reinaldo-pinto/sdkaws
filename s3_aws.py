#/usr/bin/python

from boto3 import client

#s3=boto3.resource('s3')

s3= client('s3')

#name='testereleng'
#s3=s3.Bucket(name=name)

#session = boto3.Session(profile_name='ola')

#s3 = session.client('s3')
#s3=s3.Bucket(name)

for key in s3.list_objects(Bucket='testereleng')['Contents']:
    print (key['Key']),(key['LastModified']) 
    time=key['LastModified']

print (time[])
#conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
#for key in conn.list_objects(Bucket='testereleng')['Contents']:
#    print(key['Key'])

#for objects in s3.objects.all():
#    print(objects)

#print (s3.list_objects(Bucket=name))

#stModifiedprint (s3.get_bucket_logging(Bucket=name))
