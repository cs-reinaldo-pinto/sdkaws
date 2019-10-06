import boto3

client = boto3.client('route53')

response = client.list_resource_record_sets(
    HostedZoneId='id',
)

for i in response['ResourceRecordSets']:
    if 'ResourceRecords' in i:
        if not 'TrafficPolicyInstanceId' in i:
            if 'CNAME' in i['Type']:
                print "Name: ",i['Name']
                print "Valor: ",i['ResourceRecords'][0]['Value']
