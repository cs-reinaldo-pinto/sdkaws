#/usr/bin/python

from boto3 import client
import re

s3 = client('s3')

ola = s3.list_objects(Bucket='test-devops-sandbox')
print (type(ola))

list_buckets=[]
for key in s3.list_objects(Bucket='test-devops-sandbox')['Contents']:
    buckets = (key['Key']),(key['LastModified'])
    objt = re.sub(r'/',r'',buckets[0])
    print objt
    list_buckets.append(objt)

for objeto in list_buckets:
    if "devops" == objeto:
        print "Entrou"
        s3.copy_object(Bucket='test-devops-sandbox',Key='Nossa')
