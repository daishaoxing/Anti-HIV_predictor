import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.externals import joblib
#####loaddata
alldataMat=joblib.load("./data/alldata.pkl.z")
alldataClasses=joblib.load("./data/alldatalabel.pkl.z")
#assigning predictor and target variables
x = numpy.array(alldataMat)
y = numpy.array(alldataClasses)

###########SVM
clf = svm.SVC(C=500,kernel='rbf',probability=True) ###change parameters C
svm_model=clf.fit(x, y)
joblib.dump(svm_model,'./data/HIV_SVM_model_500_rbf_win.pkl.z')
#############RF
clf = RandomForestClassifier(max_depth=None,n_estimators=1000,
                             max_leaf_nodes=None,min_samples_split=2,
                             min_samples_leaf=1) ###change parameters n_estimators
RFmodel=clf.fit(x, y)
joblib.dump(RFmodel,'./data/HIV_RF_model_1000_win.pkl.z')
