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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################

from sklearn import svm


#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]


#print len(features_train)
#print len(labels_train)

#arr = features_train[0]
#arr2 = arr[:len(arr)/5]
#print arr2
#print type(arr2)


# C=10.0, accuracy_score  = 0.616040955631
# C=100.0, accuracy_score  = 0.616040955631
# C=1000.0, accuracy_score  = 0.821387940842
# C=10000.0, accuracy_score  = 0.892491467577

t0 = time()

clf = svm.SVC(C=10000.0, kernel="rbf")
clf.fit(features_train, labels_train)

print "training time:", round(time()-t0, 3), "s"


pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score

acc = accuracy_score(pred, labels_test)


print acc
print pred[50]

chris = 0
for y in pred:
	if y == 1:
		chris += 1

print chris