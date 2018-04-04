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
print("The length of enron:",len(enron_data))
print("The features of each person",len(enron_data[enron_data.keys()[0]]))
# a=0
# for list in enron_data.keys():
#     if enron_data[list]['poi']==1:
#         a=a+1
# print("The NO. of POI",a)
# print("James Prentice's stocks is:",enron_data['PRENTICE JAMES']['total_stock_value'])
# print("'COLWELL WESLEY's sending mails is:",enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data['SKILLING JEFFREY K'].keys())
total_payments=0
poi_number=0
for list in enron_data.keys():
    # if enron_data[list]['poi']==True:
    #     poi_number+=1
        if enron_data[list]['total_payments']=='NaN':
            total_payments+=1
print(poi_number)
print(total_payments)





