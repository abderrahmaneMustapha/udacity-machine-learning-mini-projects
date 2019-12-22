#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# quiz from 5 to 15 
count = 0
for  person_name in enron_data:   
       count+= enron_data[person_name]['poi']
print(count)

#How Many POIs Exist?
poi_txt = open("../final_project/poi_names.txt", "r")
poi_txt_lines = poi_txt.readlines()[2:]
print(len(poi_txt_lines))

#Query the Dataset 1
result  =  [enron for enron in enron_data.keys() if "PRENTICE" in enron]

print(enron_data[result[0]]['total_stock_value'])
#print(result)
#Query the Dataset 2
result  =  [enron for enron in enron_data.keys() if "COLWELL" in enron]
#print(result)
print(enron_data[result[0]]['from_this_person_to_poi'])

#Query the Dataset 3
result  =  [enron for enron in enron_data.keys() if "SKILLING" in enron]
#print(result)
print(enron_data[result[0]]['exercised_stock_options'])

#Follow the Money
result  =  [enron for enron in enron_data.keys() if ("LAY KEN" in enron or "SKILLING JEFFREY " in enron or"FASTOW ANDREW" in enron) ]
print(result)
most_money = [enron_data[name]['total_payments']for name in result]
print(most_money)

#Unfilled Features
result = enron_data['FASTOW ANDREW S']['deferral_payments']
print(result)

#Dealing with Unfilled Features
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1

print('emails', count_email)
print('salary', count_salary)


#Missing POIs 1 (optional)
count_payment = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_payment +=1
print(count_payment)
print( count_payment/len(enron_data))

#Missing POIs 2 (optional)
count_payment = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi']==True:
        count_payment +=1

print(count_payment/len(enron_data))

print(len(enron_data))

    
