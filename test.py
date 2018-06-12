from SVM import *
from data import *
#如果为gauss核的话  ['Gauss',标准差]
svm=SVM(data,'Line',1000,0.02,0.001)
svm.train()
print("*******************************")
print(svm.predict([4,0]))
print(svm.a)
print(svm.w)
print(svm.b)