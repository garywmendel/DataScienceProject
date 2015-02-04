# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 17:20:19 2015

@author: garywmendel
"""

# read in data
import pandas as pd
data = pd.read_csv('poll.csv')

# pollAnswer field is a JSON object
# read the Sony pollAnswer into an object called 'sony'
import json
sony = json.loads(data.pollAnswer[3881])

# check out the object
type(sony)              # it's a list
len(sony)               # length is 4
type(sony[0])           # each list element is a dictionary
sony[0]['answerText']   # that dictionary has the answerText
len(sony[0]['votes'])   # you can easy calculate the number of votes for that answer

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



# build a dictionary where the key is the answer, and the value is the number of votes
sony_tally = {}
for answer in sony:
    key = answer['answerText']
    value = len(answer['votes'])
    sony_tally[key] = value

print sony_tally