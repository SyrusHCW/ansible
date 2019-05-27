import boto3
from botocore.exceptions import ClientError

###vars
sg_id = ''
vpc_id = ''


###########################################################################
####### Uncomment if you are creating a new security-group ################
###########################################################################

ec2 = boto3.resource('ec2')
vpc = ec2.Vpc(vpc_id)


security_group = vpc.create_security_group(
            Description='Akamai Prod Site Sheild',
            GroupName='AK-PR-SS',
            DryRun=False,
)

sg = str(security_group)
sg_id = sg[22:42]

##########################################################################
##########################################################################
##########################################################################

security_group = ec2.SecurityGroup(sg_id)

##########################################################################
################# comment out if creating new security-group #############
##########################################################################

# First, we remove all existing rules in the group:
security_group.revoke_ingress(IpPermissions=security_group.ip_permissions)


##########################################################################
########################### Security group rules #########################
##########################################################################

#Second, we re-apply the rules
data = security_group.authorize_ingress(
        IpPermissions=[
            {'IpProtocol': 'tcp',
            'FromPort': 443,
             'ToPort': 443,
             'IpRanges': [{
             'CidrIp': '192.168.1.4/32', 
             'Description': 'Akamai-SS1'}]},
            {'IpProtocol': 'tcp',
            'FromPort': 443,
             'ToPort': 443,
             'IpRanges': [{
             'CidrIp': '192.168.1.5/32', 
             'Description': 'Akamai-SS1'}]},
            {'IpProtocol': 'tcp',
            'FromPort': 443,
             'ToPort': 443,
             'IpRanges': [{
             'CidrIp': '192.168.1.6/32', 
             'Description': 'Akamai-SS1'}]},
            {'IpProtocol': 'tcp',
            'FromPort': 443,
             'ToPort': 443,
             'IpRanges': [{
             'CidrIp': '192.168.1.7/32', 
             'Description': 'Akamai-SS1'}]},
            {'IpProtocol': 'tcp',
            'FromPort': 443,
             'ToPort': 443,
             'IpRanges': [{
             'CidrIp': '192.168.1.8/32', 
             'Description': 'Akamai-SS1'}]},
            {'IpProtocol': 'tcp',
            'FromPort': 443,
             'ToPort': 443,
             'IpRanges': [{
             'CidrIp': '192.168.1.9/32', 
             'Description': 'Akamai-SS1'}]},
            {'IpProtocol': 'tcp',
            'FromPort': 443,
             'ToPort': 443,
             'UserIdGroupPairs': [{
             'GroupId': sg_id}]}                              #This will permit hosts, in this security group to talk to themselves
            ])

tag = security_group.create_tags(
        DryRun=False,
        Tags=[
        {
            'Key': 'Name',
            'Value': 'Akamai-SS-IP'
        },
    ]
)

