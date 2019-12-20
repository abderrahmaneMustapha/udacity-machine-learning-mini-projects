#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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

from sklearn import tree


#########################################################
### your code goes here ###
#lesson 03
def classify(features_train, labels_train):
    #quiz 37  use min_samples_split = 40 and calculate accuarcy
    clf  = tree.DecisionTreeClassifier(min_samples_split=40)
    clf  = clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    
    from sklearn.metrics import accuracy_score
    acc  =  accuracy_score(pred, labels_test)
    print("accuarcy : ",acc)

    #quiz 38 What's the number of features in your data

    #quiz 39 Change percentile from 10 to 1, and rerun dt_author_id.py. 
    # What’s the number of features now?
    # ../tools/email_preprocess.py
    # search for selector = SelectPercentile(f_classif, percentile=10)
    print("number of features : ",len(features_train[0]))

classify(features_train, labels_train)



#########################################################


