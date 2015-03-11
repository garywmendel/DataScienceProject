# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 18:18:40 2015

@author: Craig
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk import ConfusionMatrix


associated_df = pd.read_csv('/Users/garywmendel/Dropbox/gary stuff/python/DataScience/datascienceproject/reviews/lennon_project/associated.csv')
not_associated_df = pd.read_csv('/Users/garywmendel/Dropbox/gary stuff/python/DataScience/datascienceproject/reviews/lennon_project/unassociated.csv')

# Someone entered 0 instead of O for one row...remove the row.
not_associated_df = not_associated_df[not_associated_df.compactness != '0']

# Convert penumbra and compactness to lowercase, this is standard notation in the solar physics field
associated_df.penumbra = [item.lower() for item in associated_df.penumbra]
not_associated_df.penumbra = [item.lower() for item in not_associated_df.penumbra]


# Change x to y, penumbra and compactness both have x as a vaiable.  The x's are different.
associated_df.compactness = [item.lower() for item in associated_df.compactness]
associated_df.compactness = ['y' if item == 'x' else item for item in associated_df.compactness]
not_associated_df.compactness = [item.lower() for item in not_associated_df.compactness]
not_associated_df.compactness = ['y' if item == 'x' else item for item in not_associated_df.compactness]


# Data exploration/visualization
associated_df.zurich.value_counts().plot(kind = 'bar')
plt.xlabel('Zurich Classification')
plt.ylabel('Count')

associated_df.penumbra.value_counts().plot(kind = 'bar')
plt.xlabel('Penumbra Classification')
plt.ylabel('Count')

associated_df.compactness.value_counts().plot(kind = 'bar')
plt.xlabel('Compactness Classification')
plt.ylabel('Count')

associated_df.x_ray_class.value_counts().plot(kind = 'bar')
plt.xlabel('X-ray Class')
plt.ylabel('Count')

# Prepare data for sklearn

# map binary values for x ray types
associated_df['x_ray_class'] = associated_df.x_ray_class.map({'M':0, 'X':1})


# Objective 1:  Will the sunspot group produce a flare?


cols = ['zurich', 'penumbra', 'compactness', 'association']
all_groups = associated_df[cols].append(not_associated_df[cols])
all_groups['association'] = all_groups.association.map({'unassociated':0, 'associated':1})

# Convert penumbra and compactness to lowercase, this is standard notation in 
# the solar physics field
#all_groups.penumbra = [item.lower() for item in all_groups.penumbra]

# Change x to y, penumbra and compactness both have x as a vaiable.  The x's are different.
##all_groups.compactness = ['y' if item == 'x' else item for item in all_groups.compactness]

# Create a new series by concatenating zurich, penumbra, and compactness series 
all_groups['sunspot_class'] = all_groups.zurich + all_groups.penumbra + all_groups.compactness

# Create a list of allowed sunspot classes.
allowed = ['Axy', 'Bxo', 'Bxi', 'Cro', 'Cri', 'Cso', 'Csi', 'Cao', 'Cai', 'Cho', 'Chi', 'Cko', 'Cki', 'Dro', 'Dri', 'Ero', 'Eri', 'Fro', 'Fri', 'Dso', 'Dsi', 'Dsc', 'Dao', 'Dai', 'Dac', 'Dho', 'Dhi', 'Dhc', 'Dko', 'Dki', 'Dkc', 'Eso', 'Esi', 'Esc', 'Eao', 'Eai', 'Eac', 'Eho', 'Ehi', 'Ehc', 'Eko', 'Eki', 'Ekc', 'Fso', 'Fsi', 'Fsc', 'Fao', 'Fai', 'Fac', 'Fho', 'Fhi', 'Fhc', 'Fko', 'Fki', 'Fkc', 'Hry', 'Hsy', 'Hay', 'Hhy', 'Hky']

# Filter all_groups df with allowed class list.  Sunspot classifications are manually determined
# and classes that are not physically possible can be entered into the database.
all_groups = all_groups[all_groups.sunspot_class.isin(allowed)]

# Data exploration/visualization
all_groups.zurich.value_counts().plot(kind = 'bar')
plt.xlabel('Zurich Classification')
plt.ylabel('Count')

all_groups.penumbra.value_counts().plot(kind = 'bar')
plt.xlabel('Penumbra Classification')
plt.ylabel('Count')

all_groups.compactness.value_counts().plot(kind = 'bar')
plt.xlabel('Compactness Classification')
plt.ylabel('Count')

all_groups.sunspot_class.value_counts().plot(kind = 'bar')
plt.xlabel('Compactness Classification')
plt.ylabel('Count')
plt.yscale('log')

# Sunspot classification counts
all_groups.sunspot_class.value_counts()


# Split data into test and train sets for preliminary Naive Bayes test.
X_train, X_test, y_train, y_test = train_test_split(all_groups.sunspot_class, all_groups.association)

# Instantantiate the vectorizer.
vect = CountVectorizer(analyzer = 'char', lowercase = False) 
# Create document term matrices
train_dtm = vect.fit_transform(X_train)
test_dtm = vect.transform(X_test)

train_features = vect.get_feature_names()

len(train_features)
train_arr = train_dtm.toarray()

for i in range(len(train_features)):
    print train_features[i], sum(train_arr[:, i]) 

nb = MultinomialNB()
nb.fit(train_dtm, y_train)

preds= nb.predict(test_dtm)

print metrics.accuracy_score(y_test, preds)
print metrics.confusion_matrix(y_test, preds)
cross_val_score(nb, vect.fit_transform(all_groups.sunspot_class), all_groups.association, cv=10, scoring='roc_auc').mean()

# Assign numeric values
all_groups['zurich'] = all_groups.zurich.map({'A':0.1, 'H':0.15, 'B':0.3, 'C':0.45, 'D':0.6, 'E':0.75, 'F':0.9})
all_groups['penumbra'] = all_groups.penumbra.map({'x':0, 'r':0.1, 's':0.3, 'a':0.5, 'h':0.7, 'k':0.9})
all_groups['compactness'] = all_groups.compactness.map({'y':0, 'o':0.1, 'i':0.5, 'c':0.9})
all_groups['association'] = all_groups.association.map({0:0.1, 1:0.9})


# Objective 2:  What type of flare class, X or M?

# Create dummy variables for Zpc sunspot classification
associated_dummy_zurich = pd.get_dummies(associated_df.zurich)
associated_dummy_penumbra = pd.get_dummies(associated_df.penumbra)
associated_dummy_compactness = pd.get_dummies(associated_df.compactness)

dummy_associated = pd.concat([associated_dummy_zurich ,associated_dummy_penumbra, associated_dummy_compactness, associated_df.x_ray_class], axis=1)


# Split data into predictor (X) and outcome (y) dataframes. 
X = dummy_associated.iloc[:,:17]
y = dummy_associated.x_ray_class

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Try logistic regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
preds = logreg.predict(X_test)
logreg.score(X_test, y_test) # > 0.9, but something is wrong. See confusion matrix

print ConfusionMatrix(list(y_test), list(preds))

# AOC is 0.606.
logreg = LogisticRegression()
cross_val_score(logreg, X, y, cv = 10, scoring = 'roc_auc').mean()

# Naive Bayes


associated_df['sunspot_class'] = associated_df.zurich + '' + associated_df.penumbra + '' + associated_df.compactness

X_train, X_test, y_train, y_test = train_test_split(associated_df.sunspot_class, associated_df.x_ray_class)


vect = CountVectorizer(analyzer = 'char', lowercase = False) # Instantantiate the vectorizer
train_dtm = vect.fit_transform(X_train)
test_dtm = vect.transform(X_test)

train_features = vect.get_feature_names()

len(train_features)
train_arr = train_dtm.toarray()

for i in range(len(train_features)):
    print train_features[i], sum(train_arr[:, i]) 

nb = MultinomialNB()
nb.fit(train_dtm, y_train)

preds= nb.predict(test_dtm)

print metrics.accuracy_score(y_test, preds)
print metrics.confusion_matrix(y_test, preds) # Still not predicting type of flare type well

