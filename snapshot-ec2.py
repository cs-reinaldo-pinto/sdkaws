import boto3
from datetime import datetime,timedelta


def lambda_handler(event, context):

    client = boto3.client('ec2')
    
    days = -1
    id_owner='account'
    volume_id='vol-id'
    snapshots = client.describe_snapshots(OwnerIds=[id_owner])
    time_now = datetime.now()
    
    def delete_snapshot(snapshot_time,delete_snap_id,vol_id):
        print "==========================================="
        print "Delete Snapshot ID: '%s' " % (delete_snap_id)
        print "Datetime:",snapshot_time
        print "Backup Volume ID: '%s'" % (vol_id)
        snapshot_resource = boto3.resource('ec2')
        snapshot = snapshot_resource.Snapshot(delete_snap_id)
        snapshot.delete()
        
    for snapshot in snapshots['Snapshots']:
        snapshot_time = snapshot['StartTime'].replace(tzinfo=None)
        if (volume_id == snapshot['VolumeId'] and (time_now - snapshot_time) > timedelta(days)):
            delete_snap_id = snapshot['SnapshotId']
            delete_snapshot(snapshot_time,delete_snap_id,snapshot['VolumeId']) 
        else: 
            snapshot_id = snapshot['SnapshotId']
            print "==========================================="
            print "Snapshot id '%s' recent, within of configured limit or different volume ID '%s' than specified." % (snapshot['SnapshotId'],snapshot['VolumeId'])
            print "Datetime:",snapshot_time
    return
