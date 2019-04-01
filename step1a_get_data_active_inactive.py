f1=open('./data/aids_ec50_may04.txt','r')
f2=open('./data/aids_ec50_may04_active.txt','w')
f3=open('./data/aids_ec50_may04_inactive.txt','w')
dict1={}
for i in f1.readlines()[1:]:
	aa=i.strip().split(',')
	if aa[2]=='M' and int(aa[5])>=2:
		dict1.setdefault(aa[0], []).append(float(aa[4]))

for j in dict1.keys():
	mean=(sum(dict1[j])+0.0)/len(dict1[j])
	if mean < -5:
		f2.write(j+'\t'+str(mean)+'\n')
	if mean > -4:
		f3.write(j+'\t'+str(mean)+'\n')