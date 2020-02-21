#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()


#find outliers 
for key, value in data_dict.items():
    if value['bonus'] == data.max():
        #print (key)
        pass

data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

plt.scatter(data[:,0], data[:,1])
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()


#find more outliers
i=0
while(i < 3):
    deleted_key = "" 
    for key, value in data_dict.items():
      
        if value['bonus'] == data.max():
            print(i)
            print(key)
            deleted_key = key
            print("delete this ",deleted_key)
    data_dict.pop(deleted_key,0)
    data = featureFormat(data_dict, features)
    i+=1
   