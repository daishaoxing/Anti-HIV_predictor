import pybel
def get_bits(f1):
    mols = list(pybel.readfile("smi",f1));
    titles = [x.title for x in mols]
    bits = [set(x.calcfp().bits) for x in mols]
    return bits,titles
f1=open('./data/remove_inactive08.txt','w')
f2=open('./data/remove_inactive08a.txt','w')
remove_in=[]
activebits,activetitles=get_bits('./data/chembl_NCI_aids_active.smi')
inactivebits,inactivetitles=get_bits('./data/chembl_NCI_aids_inactive.smi')
for i in range(len(activetitles)):
	myactive=activebits[i]
	myactivet=activetitles[i]
	for j in range(len(inactivebits)):
		myinactive=inactivebits[j]
		myinactivet=inactivetitles[j]
		myinter=myactive & myinactive
		myunion=myactive | myinactive
		if float(len(myunion))!=0:
			sim=len(myinter)/float(len(myunion))
			if sim>0.8:
				stra=myinactivet+'\t'+myactivet+'\t'+str(sim)+'\n'
#				print stra
				f2.write(stra)
				remove_in.append(myinactivet)
				remove_in.append(myactivet)
remove_in=list(set(remove_in))
for i in remove_in:
	f1.write(i+'\n')