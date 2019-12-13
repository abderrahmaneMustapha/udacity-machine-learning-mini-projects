#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

def email_classify(features_train,  labels_train):
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()

    fit_time = time()
    clf.fit(features_train, labels_train)
    print("time to train the classifier : ",round(time() - fit_time,3))

    predict_time = time()
    predict = clf.predict([[393939]])
    print("time to make prediction : ",round(time() - predict_time,3))
    
    return clf.score(features_test, labels_test)


print(email_classify(features_train,  labels_train))


#########################################################
### your code goes here ###


#########################################################


