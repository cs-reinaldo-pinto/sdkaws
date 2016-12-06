#/usr/bin/python

import boto3
import time
import sys
import botocore
#rds = boto3.client(profile_name='dev')

#rds = boto3.setup_default_session(region_name='us-east-1a')
client = boto3.client('rds')
#time = time.strftime("%d%m%Y")

#name_db='db-12-02-01-07'#'testore'

response =  client.describe_db_instances(DBInstanceIdentifier="dbdevconciliador")
response = response['DBInstances']

db = response[0]
print (db)

db_do_amor = db['DBInstanceIdentifier']
print '\n'+(db_do_amor)

db_do_amor = db_do_amor

status = db['DBInstanceStatus']
print '\n'+(status)

if status == "available":
    print 'Entrou'
    dbname = db['DBInstanceIdentifier']
    snapshot = client.create_db_snapshot(DBSnapshotIdentifier='snapshotdoamor2',DBInstanceIdentifier=db_do_amor)
else:
    print 'Nao entrou'

#describeSnapshot
#snapshot = rds.describe_db_snapshot_attributes(
#    DBSnapshotIdentifier=''
#)

#create Snapshot
#create = cliente.create_db_client_snapshot(
#    DBSnapshotIdentifier='testesnapshot'+time
#    ,DBInstanceIdentifier='tesstore'
#    ,Tags=[
#        {
#            'Key':'Ambiente'
#            'Value':'DEV'
#        },
#    ]
#)


#DBInstanceIdentifier='testereinaldo'
#,DBSnapshotIdentifier='testereinaldo'
