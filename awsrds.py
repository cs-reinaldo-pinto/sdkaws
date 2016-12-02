#/usr/bin/python

import boto3
import time


#rds = boto3.client(profile_name='dev')

#rds = boto3.setup_default_session(region_name='us-east-1a')
rds = boto3.client('rds')
time = time.strftime("%d%m%Y")

name_db='db-12-02-01-07'#'testore'



#describeSnapshot
snapshot = rds.describe_db_snapshot_attributes(
    DBSnapshotIdentifier='db-2016-12-02-01-07'
)

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
