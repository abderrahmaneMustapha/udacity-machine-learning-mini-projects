#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn import svm
from sklearn.metrics import accuracy_score
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]

svc = svm.SVC(C=10000, kernel='rbf')


fit_time = time()
fit = svc.fit(features_train, labels_train)
print("time to train the classifier : ",round(time() - fit_time,3))

predict_time = time()
pred = svc.predict(features_test)
print(accuracy_score(pred,labels_test))


print("tests in chris class ",sum(pred))

#print('for 10 : ',pred[10])
#print('for 26 : ',pred[26])
#print('for 50 : ',pred[50])

print("time to make prediction : ",round(time() - predict_time,3))

print("accuary : ",accuracy_score(pred, labels_test))
