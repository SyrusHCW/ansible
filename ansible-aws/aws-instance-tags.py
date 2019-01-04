from boto3 import resource, client
import boto3
import boto.ec2

ec2 = boto3.resource('ec2')
instances = ec2.instances.filter()
conn = boto.ec2.connect_to_region('us-east-1')

ec2_ids = []
dsdc_sg = []
dsdc_id = []
test = []   #Contains EC2 ID's
sg = []     #Contains tags
akamai_sg = []

akamai_id = []
final_sg = []

dic1_value = {
    'Value': 'True',
    'Key': 'security:group:AKAMAI',
 } 

dic2_value = {
    'Value': 'True',
    'Key': 'security:group:DSDC',
 } 

test_test = []
test_test1 = []
test_test2 = []

for instance in instances:
     ec2_ids.append(instance.id)
#print(ec2_ids)

for ec2_id in ec2_ids:
    instance = ec2.Instance(ec2_id)
    ec2_id_space = '{0}{1}'.format(ec2_id, ' ')
    test_test.append(ec2_id_space)                         #This will add the id to test var
#print(test_test[1])
    tags = instance.tags or [] 
    for tag in tags:
	#print(tag)

	if tag == dic1_value:                    #This will configure Akamai 
            #print(tag)
	    #print(ec2_id)
	    woot = [ec2_id,[tag]]
	    test_test1.append(woot)
	    #test_test1.append(tag)
	#print(test_test1)
	if tag == dic2_value:                    #This will configure Akamai 
            #print(tag)
            #print(ec2_id)
	    butt = [ec2_id,[tag]]
	    #print(butt)
            test_test2.append(butt)
            #test_test2.append(tag)
#print(test_test2)
#print(test_test1)

#print(test_test2)

new_new =[]

#print(test_test1)[1]

blah = len(test_test1)

#print(test_test1)

#print(blah)

boop = len(test_test2)

#print(test_test2)


nano = []



vi = []

for y in range(0,blah):
	brian = test_test1[y][0]
	for w in range(0,boop):
		bob = test_test2[w][0]
		if brian == bob:
			bro = brian, test_test2[w][1], test_test1[y][1]
			vi.append(bro)

print(vi)







#for name1 in test_test1:
#	for name2 in test_test2:
		#if name1 == name2:
		#print(name1, name2)



#for name in test_test1:
#	if name == "i-002422f77d6d980f5":
		#print(name)

#print(new_new)


"""
new_instance = {}


for name in test_test1:
	if name == "i-0387b1f27bb1bf216":
		new_instance[name]="hmmm"

print(new_instance)
"""
