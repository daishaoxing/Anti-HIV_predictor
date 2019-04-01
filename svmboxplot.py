import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
f1=open('svm_performance_final.txt','r')
f2=open('svm_performance_final_roc_auc.txt','w')
dict1={}
for i in f1.readlines():
	a,b,c,d,e,f,g=i.strip().split('\t')
	auc=float(g)
	mykey=float(a)
	dict1.setdefault(mykey, []).append(auc)
labels=[]
data=[]
dict2= sorted(dict1.iteritems(), key=lambda d:d[0])
for i in dict2:
	mylabel,mydata=i
	labels.append(mylabel)
	mean=np.mean(mydata)##mean=sum(mydata)/(len(mydata)+0.0)
	stra=str(mylabel)+'\t'+str(mean)+'\n'
	f2.write(stra)
	data.append(mydata)
labels=[0.5, 1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
plt.figure()
plt.boxplot(data,labels=labels,showmeans=True)
plt.grid(axis='y',          # set y-axis grid lines
        linestyle='--',     # use dashed lines
        which='major',      # only major ticks
        color='lightgrey',  # line colour
        alpha=0.7           # make lines semi-translucent
        ) 
#plt.ylim(ymax = 1, ymin = 0.82)
plt.ylabel('AUC')                  # y-axis label
plt.xlabel('Penalty parameter C')  # x-axis label
#plt.savefig('SVM_auc_boxplot.pdf',format='pdf')
plt.show()