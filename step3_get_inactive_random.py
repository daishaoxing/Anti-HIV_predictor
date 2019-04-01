import random
f1=open('./data/chembl_NCI_aids_inactive_final.smi','r')
f2=open('./data/chembl_NCI_aids_inactive_final_ok.smi','w')
aa=f1.readlines()
bb=random.sample(aa,9797) ###change it
for i in bb:
	f2.write(i)