f1=open('./data/aids_ec50_may04_active.txt','r')
f2=open('./data/aids_ec50_may04_inactive.txt','r')
f3=open('./data/chembl_HIV_active.smi','r')
f4=open('./data/Open_2D_Oct2014.smi','r')
f5=open('./data/chembl_NCI_aids_active.smi','w')
f6=open('./data/chembl_NCI_aids_inactive.smi','w')

dict1={}
for i in f4.readlines():
	aa=i.strip().split('\t')
	if len(aa)==2:
		dict1[aa[1]]=aa[0]

for i in f1.readlines():
	aa=i.strip().split('\t')
	if aa[0] in dict1.keys():
		f5.write(dict1[aa[0]]+'\t'+aa[0]+'\n')

for i in f2.readlines():
	aa=i.strip().split('\t')
	if aa[0] in dict1.keys():
		f6.write(dict1[aa[0]]+'\t'+aa[0]+'\n')

chembl=''.join(f3.readlines())
f5.write(chembl)
