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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print type(enron_data)
for data in enron_data:
	print data
	item = enron_data[data]
	print item
	print len(item)
	break

# person of interest	
count = 0 
for person_name in enron_data:
	if enron_data[person_name]["poi"]:
		count += 1
print count

# How many POIs are there in total?
poi_reader = open('../final_project/poi_names.txt', 'r')
poi_reader.readline() # skip url
poi_reader.readline() # skip blank line
poi_count = 0

for poi in poi_reader:
	poi_count += 1
print poi_count

#What is the total value of the stock belonging to James Prentice? 
print enron_data['PRENTICE JAMES']['total_stock_value']

#How many email messages do we have from Wesley Colwell to persons of interest
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#Whats the value of stock options exercised by Jeffrey K Skilling?
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']		
	
#Of these three individuals (Lay, Skilling and Fastow), who took home the most money
most_paid = ''
highest_payment = 0

for key in ('LAY KENNETH L', 'FASTOW ANDREW S', 'SKILLING JEFFREY K'):
	if enron_data[key]['total_payments'] > highest_payment:
		highest_payment = enron_data[key]['total_payments']
		most_paid = key

print most_paid, highest_payment

#How many folks in this dataset have a quantified salary? 
salary_count = 0 
for person_name in enron_data:
	if enron_data[person_name]['salary'] != 'NaN':
		salary_count += 1
print salary_count

#What about a known email address? 
email_count = 0 
for person_name in enron_data:
	if enron_data[person_name]['email_address'] != 'NaN':
		email_count += 1
print email_count

# How many people have NaN for total_payments? What is the percentage of total?
no_payments_count = 0 
for person_name in enron_data:
	if enron_data[person_name]['total_payments'] == 'NaN':
		no_payments_count += 1
print float(no_payments_count)/len(enron_data) * 100


# What percentage of POIs in the data have "NaN" for their total payments?
POIs = dict((key,value) for key, value in enron_data.items() if value['poi'] == True)
number_POIs = len(POIs)
print number_POIs

no_total_payments = 0 
for person_name in POIs:
	if POIs[person_name]['total_payments'] != 'NaN':
		no_total_payments += 1
print float(no_total_payments)/number_POIs * 100

# What is the new number of people with NaN total_payments?
print len(enron_data) + 10
print 10 + len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))

# What is the new number of POIs?
print 10 + len(POIs)

# What percentage have NaN for their total_payments?
print float(10)/(10 + len(POIs))*100


