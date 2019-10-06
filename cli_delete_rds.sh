#!/bin/bash


name="dbdoamor"
vpc="default-vpc-5f1f8f3b"

#create snapshot
aws rds create-db-snapshot --db-instance-identifier $name --db-snapshot-identifier $name

db_status=$(aws rds describe-db-instances --db-instance-identifier dbdoamor --query 'DBInstances[*].[DBInstanceStatus]' --output text)

until [ $db_status != "available" ]; do
	db_status=$(aws rds describe-db-instances --db-instance-identifier dbdoamor --query 'DBInstances[*].[DBInstanceStatus]' --output text)
	sleep 5
done

#delete db instance
aws rds delete-db-instance --db-instance-identifier $name

snapshot=$(aws rds describe-db-snapshots --db-instance-identifier '$name'  --output text | tail -1 | awk '{print $6}')
group_name=$(aws rds describe-db-subnet-groups |grep '$vpc' |tail -1 |awk -F":" '{print $(NF)}')

aws rds restore-db-instance-from-db-snapshot --db-instance-identifier $name --db-snapshot-identifier $snapshot --db-subnet-group-name $group_name

