import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
f1=open('RF_performance_final.txt','r')
f2=open('RF_performance_final_roc_auc.txt','w')
dict1={}
for i in f1.readlines():
	a,b,c,d,e,f,g=i.strip().split('\t')
	auc=float(g)
	mykey=int(a)
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

plt.figure()
plt.boxplot(data,labels=labels,showmeans=True)
plt.grid(axis='y',          # set y-axis grid lines
        linestyle='--',     # use dashed lines
        which='major',      # only major ticks
        color='lightgrey',  # line colour
        alpha=0.7           # make lines semi-translucent
        ) 
#plt.ylim(ymax = 0.930, ymin = 0.90)
plt.ylabel('AUC')                  # y-axis label
plt.xlabel('The number of trees in the forest (n_estimators)')  # x-axis label
#plt.savefig('RF_AUC_boxplot.pdf',format='pdf')
plt.show()
