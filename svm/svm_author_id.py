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
svc = svm.SVC(kernel='linear')

fit_time = time()
fit = svc.fit(features_train, labels_train)
print("time to train the classifier : ",round(time() - fit_time,3))

predict_time = time()
pred = svc.predict(features_test)
print("time to make prediction : ",round(time() - predict_time,3))

print("accuary : ",accuracy_score(pred, labels_test))



#########################################################
### your code goes here ###

#########################################################


