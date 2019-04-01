import pybel
f1=open('./data/chembl_NCI_aids_inactive.smi','r')
f2=open('./data/chembl_NCI_aids_active.smi','r')
f3=open('./data/remove_inactive08.txt','r')
f4=open('./data/chembl_NCI_aids_inactive_final.smi','w')
f5=open('./data/chembl_NCI_aids_active_final.smi','w')
list1=[]
for i in f3.readlines():
	bb=i.strip()
	list1.append(bb)
for i in f1.readlines():
	bb=i.strip().split('\t')
	if bb[1] not in list1:
		f4.write(i)
for i in f2.readlines():
	bb=i.strip().split('\t')
	if bb[1] not in list1:
		f5.write(i)