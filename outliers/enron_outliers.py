#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )


#Whats the dictionary key of the biggest Enron outliers?
name_key = None
max_salary = 0

for key in data_dict:
    if data_dict[key]["salary"] != 'NaN' and data_dict[key]["salary"] > max_salary:
	    name_key = key
	    max_salary = data_dict[key]["salary"]
		
print name_key, max_salary

#removing the outliers because its spreed sheet quirk		
data_dict.pop(name_key, 0 )

#Identify the outliers whos bonus is more than 5 million dollars, and a salary of over 1 million dollars
for key in data_dict:
    if data_dict[key]["salary"] > 1000000 and data_dict[key]["bonus"] > 5000000 
	and data_dict[key]["salary"]  != 'NaN' and data_dict[key]["bonus"]  != 'NaN':
	    print key


		
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)



for point in data:
    salary = point[0]
    bonus = point[1]	
    matplotlib.pyplot.scatter( salary, bonus )
   


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



