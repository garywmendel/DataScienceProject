# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 13:26:49 2015

@author: garywmendel
"""

# K-means model for determining natural yopine categories
'''
CLUSTER ANALYSIS
How do we implement a k-means clustering algorithm?

scikit-learn KMeans documentation for reference:
http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
'''

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np



# Import Yopine data
data = pd.read_csv('poll3.csv')
d = data

np.random.seed(0)

# Run TF/ID vectorizer on data to get sentences out
# from BeautifulSoup import BeautifulSoup

r = pd.read_csv('poll3.csv')
type(r)
len(r)

r.columns

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# pollAnswer field is a JSON object
# read the Sony pollAnswer into an object called 'sony'
import json
sony = json.loads(data.pollAnswer[3881])
# Need to extract sentence(s) list from data
# check out the object
type(sony)              # it's a list
len(sony)               # length is 4
type(sony[0])           # each list element is a dictionary
sony[0]['answerText']   # that dictionary has the answerText
len(sony[0]['votes'])   # calculate the number of votes for that answer

data.head()
for i in range(0,len(data)):
    poll = json.loads(data.pollAnswer[i])
    print data.pollQuestion[i]
    poll_tally = {}
    for answer in poll:
         key = answer['answerText']
         if 'votes' in answer.keys():
             value = len(answer['votes'])
         poll_tally[key] = value
    print poll_tally
json.loads(data.pollAnswer[0])
questions = data.pollQuestion
answers = [' '.join([b['answerText'] for b in json.loads(a)]) for a in data.pollAnswer]
for q, a in zip(questions, answers):
    print q, a
# sentence_list=[data]  
# Need to dump this into a new df

# sentence_list=['hello how are you', "I am doing great", "my name is abc"]

vectorizer=TfidfVectorizer(min_df=1, max_df=0.9, stop_words='english', decode_error='ignore')
vectorized=vectorizer.fit_transform(answers)

km=KMeans(n_clusters=3, init='k-means++',n_init=10)
km.fit(vectorized)


km.labels_

km.predict(vectorizer.fit_transform(answers))
km.predict(vectorizer.fit_transform(questions))

# Run KMeans
est = KMeans(n_clusters=3, init='random')
est.fit(d)
y_kmeans = est.predict(d)

colors = np.array(['#FF0054','#FBD039','#23C2BC'])
plt.figure()
plt.scatter(d[:, 2], d[:, 0], c=colors[y_kmeans], s=50)
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[0])


# LDA portion of the project:
import lda
import numpy as np # not able to import LDA
sentences = ["my name is sinan", "Im gary", "This is gary and sinan"]
# Instantiate a count vectorizer with two additional parameters
vect = CountVectorizer(stop_words='english', ngram_range=[1,3]) 
sentences_train = vect.fit_transform(sentences)

# Instantiate an LDA model
model = lda.LDA(n_topics=10, n_iter=500)
model.fit(sentences_train) # Fit the model 
n_top_words = 10
topic_word = model.topic_word_
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vect.get_feature_names())[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ', '.join(topic_words)))
# ------------------------------------------
# EXERCISE: Find the centers and plot them 
#           on the same graph.
# ------------------------------------------

centers = est.cluster_centers_
plt.scatter(centers[:, 2], centers[:, 0], c='k', linewidths=3,
            marker='+', s=300)

'''
VISUALIZING THE CLUSTERS
What are some different options to visualize 
multi-dimensional data? Let's look at three ways you can do this.
- Scatter Plot Grid
- 3D Plot
- Parallel Coordinates
'''

#================================
# Option #1: Scatter Plot Grid
plt.figure(figsize=(8, 8))
plt.suptitle('Scatter Plot Grid',  fontsize=14)
# Upper Left
plt.subplot(221) # going to be making a 2x2 graph.  last 1 = position
plt.scatter(d[:,2], d[:,0], c = colors[y_kmeans])
plt.ylabel(iris.feature_names[0])

# Upper Right
plt.subplot(222)
plt.scatter(d[:,3], d[:,0], c = colors[y_kmeans])

# Lower Left
plt.subplot(223)
plt.scatter(d[:,2], d[:,1], c = colors[y_kmeans])
plt.ylabel(iris.feature_names[1])
plt.xlabel(iris.feature_names[2])

# Lower Right
plt.subplot(224)
plt.scatter(d[:,3], d[:,1], c = colors[y_kmeans])
plt.xlabel(iris.feature_names[3])

#================================
# Option #2: 3d plot
from mpl_toolkits.mplot3d import Axes3D
plt.suptitle('3d plot', fontsize=15)
ax = Axes3D(plt.figure(figsize=(10, 9)), rect=[.01, 0, 0.95, 1], elev=30, azim=134)
ax.scatter(d[:,0], d[:,1], d[:,2], c = colors[y_kmeans], s=120)
ax.set_xlabel('Sepal Width')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
# Modified from the example here: 
# http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_iris.html

# ---------------------------------------
# EXERCISE: Create a Parallel Coordinates 
#           visualization with the classes
# ---------------------------------------


#================================
# Option 3: Parallel Coordinates

from pandas.tools.plotting import parallel_coordinates
# I'm going to convert to a pandas dataframe
# Using a snippet of code we learned from one of Kevin's lectures!
features = [name[:-5].title().replace(' ', '') for name in iris.feature_names]
iris_df = pd.DataFrame(iris.data, columns = features)
iris_df['Name'] = iris.target_names[iris.target]
parallel_coordinates(data=iris_df, class_column='Name', 
                     colors=('#FF0054', '#FBD039', '#23C2BC'))
                     
'''
DETERMINING THE NUMBER OF CLUSTERS
How do you choose k? There isn't a bright line, but we can evaluate 
performance metrics such as the silhouette coefficient and within sum of 
squared errors across values of k.

scikit-learn Clustering metrics documentation:
http://scikit-learn.org/stable/modules/classes.html#clustering-metrics
'''

# Create a bunch of different models
k_rng = range(1,15)
est = [KMeans(n_clusters = k).fit(d) for k in k_rng]

#================================
# Option 1: Silhouette Coefficient
# Generally want SC to be closer to 1, while also minimizing k

from sklearn import metrics
silhouette_score = [metrics.silhouette_score(d, e.labels_, metric='euclidean') for e in est[1:]]

# Plot the results
plt.figure(figsize=(7, 8))
plt.subplot(211)
plt.title('Using the elbow method to inform k choice')
plt.plot(k_rng[1:], silhouette_score, 'b*-')
plt.xlim([1,15])
plt.grid(True)
plt.ylabel('Silhouette Coefficient')
plt.plot(3,silhouette_score[1], 'o', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='r')

# -----------------------------------------------------
# EXERCISE: Calculate the within sum of squared errors 
#           and plot over a range of k
# -----------------------------------------------------


#================================
# Option 2: Within Sum of Squares (a.k.a., inertia)
# Generally want to minimize WSS, while also minimizing k

within_sum_squares = [e.inertia_ for e in est]

# Plot the results
plt.subplot(212)
plt.plot(k_rng, within_sum_squares, 'b*-')
plt.xlim([1,15])
plt.grid(True)
plt.xlabel('k')
plt.ylabel('Within Sum of Squares')
plt.plot(3,within_sum_squares[2], 'ro', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='r')
