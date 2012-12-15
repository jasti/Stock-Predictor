'''
Created on Nov 24, 2012

@author: zudec
'''
import csv
import sys
import numpy
from numpy import  array
import decimal
import string
from sklearn import linear_model
from operator import itemgetter
from sklearn import tree
import random
from sklearn import cross_validation 



rawList= []
positiveRawList = []
negativeRawList = []
element = []
positiveResponses=0
negativeResponses=0

f = open("alchemy.txt", 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        element = []
        element.append(float(row[0]))
        element.append(float(row[1]))
        element.append(float(row[2]))
        element.append(float(row[3]))
        element.append(float(row[4]))
    


    
        rawList.append(element)   
        
finally:
    f.close()
    
    


a = array( rawList)



X = a[:, 0:2]
Y= a[:,4]

print X
print Y

lr = linear_model.LogisticRegression()

lr.fit(X,Y)
proba1 = lr.predict(X)

proba = lr.predict_proba(X)

print("lr output scores %s",proba1)

#lr_scores = cross_validation.cross_val_score(lr, X, Y, cv=10)
#print "lr accuracy: %0.2f (+/- %0.2f)" % (lr_scores.mean(), lr_scores.std() / 2)

dt = tree.DecisionTreeClassifier()

dt.fit(X,Y)
proba2 = lr.predict(X)
proba = dt.predict_proba(X) 

print("dt output scores %s",proba2)

#dt_scores = cross_validation.cross_val_score(dt, X, Y, cv=10)
#print "dt accuracy: %0.2f (+/- %0.2f)" % (dt_scores.mean(), dt_scores.std() / 2)

'''
from sklearn.linear_model import SGDClassifier

clf =SGDClassifier(loss="modified_huber", penalty="l2")
clf.fit(X,Y)
proba = clf.predict_proba(X)
clf_scores = cross_validation.cross_val_score(clf, X, Y, cv=10)
print "SGDClassifier accuracy: %0.2f (+/- %0.2f)" % (clf_scores.mean(), clf_scores.std() / 2)

'''


    





