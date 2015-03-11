# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 09:12:34 2015

@author: craig.m.lennon
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Import goes sunspot data
sunspot = pd.read_csv('C:\Users\Craig\Documents\Python_DS\GA_DS\DAT4-students\craig\USAF_sunspot_1982_2014.csv', dtype = object)

clean_sunspot = sunspot[['data_code_date', 'UTC_obs', 'NOAA_USAF_spot_num', 'zurich', 'penumbra', 'compactness', 'number_of_spots', 'area']]

# only cases with complete sunspot class descriptions, ie zpc values

clean_sunspot = clean_sunspot[clean_sunspot.zurich.notnull()]
clean_sunspot = clean_sunspot[clean_sunspot.penumbra.notnull()]
clean_sunspot = clean_sunspot[clean_sunspot.compactness.notnull()]

# check NaN sum
# clean_sunspot.compactness.isnull().sum()


# clean up the trailing decimal point and zero
clean_sunspot.data_code_date = [item.replace('.0', '')  for item in clean_sunspot.data_code_date] 


clean_sunspot['year'] = [int('19' + date[2:4]) if int(date[2:4]) >=81 and int(date[2:4]) <=99 else int('20' + date[2:4]) for date in clean_sunspot.data_code_date]
clean_sunspot['month'] =  [int(date[4:6]) for date in clean_sunspot.data_code_date]
clean_sunspot['day'] =  [int(date[6:8]) for date in clean_sunspot.data_code_date]



UTC_time = [time[:-2] for time in clean_sunspot.UTC_obs]

clean_UTC_time = []

for time in UTC_time:
    if len(time) == 2:
        clean_UTC_time.append('00' + time)       
    elif len(time) == 3:
        clean_UTC_time.append('0' + time)       
    elif len(time) == 1:
        clean_UTC_time.append('000' + time)       
    else:
        clean_UTC_time.append(time)       
      
clean_sunspot['hour'] = [int(time[0:2]) for time in clean_UTC_time]
clean_sunspot['minute'] = [int(time[2:4]) for time in clean_UTC_time]

# Prepare a new series in the clean_sunspot dataframe that 
# contains datetime objects
#The day month is not correct


sunspot_date_time = []

# When the df was subset, the indices came with.  They weren't reindexed...
# hence the clunky solution.
clean_index = clean_sunspot.index

for i in clean_index:
    sunspot_date_time.append(datetime.datetime(clean_sunspot.year[i], clean_sunspot.month[i], clean_sunspot.day[i], clean_sunspot.hour[i], clean_sunspot.minute[i]))

clean_sunspot['date_time'] = sunspot_date_time


# correlated regions

# Clean up NOAA_USAF_spot_num so that it matches the same series in the x-ray (flare) data
clean_sunspot['cor_NOAA_USAF_spot_num'] = [str(item).replace('.0', '')  for item in clean_sunspot.NOAA_USAF_spot_num]

# Pass the list x_ray_event_regions created in the clean_xray script.
# this list contains unique values of NOAA numbers were flare events were observed
cor_sunspot = clean_sunspot[clean_sunspot.cor_NOAA_USAF_spot_num.isin(x_ray_event_regions)]

cor_regions = cor_sunspot.cor_NOAA_USAF_spot_num.unique()

# Now the hard part....

# Define an empty dataframe that will contain all sunspot observations that 
# are associated with an x-ray flare event.  The time difference between an sunspot
# measurement and a flare measurent has been set to 6 hours to be considered
# associated
associated_sun = pd.DataFrame()
flares_and_spots= pd.DataFrame()

for region in ['11909', '11928', '11936']:
    
    # Split cor_sunspot df and clean_x_ray df by unique sunspot number    
    temp_sun = cor_sunspot[cor_sunspot.cor_NOAA_USAF_spot_num == region]
    temp_x = clean_x_ray[clean_x_ray.cor_NOAA_USAF_spot_num == region]
    flares_and_spots_temp = pd.DataFrame()       
    
    for time in temp_x.date_time:

        dummy_sun = temp_sun[(time-temp_sun.date_time) < np.timedelta64(hours =6)]
        if dummy_sun.shape[0] != 0:         
            #flares_and_spots_temp = pd.DataFrame()        
            dummy_sun['time_diff'] = abs(time - dummy_sun.date_time)
            dummy_sun['x_ray_time'] = time
            #min_diff = (dummy_sun.time_diff.min())/datetime.timedelta(seconds = 1)
            dummy_sun['diff_sec'] = dummy_sun.time_diff/datetime.timedelta(seconds = 1 )
            #associated_sun = associated_sun.append(dummy_sun[dummy_sun.diff_sec.isin(min_diff)])
        
            dummy_sun =  dummy_sun[dummy_sun.diff_sec <= 21600 ]
            if len(dummy_sun.diff_sec) > 1:
                dummy_sun = dummy_sun[dummy_sun.diff_sec == min(dummy_sun.diff_sec)]
                
            associated_sun = associated_sun.append(dummy_sun)
        
            associated_sun = associated_sun.append(dummy_sun[dummy_sun.diff_sec <= 21600 ])
            
            # pull these out of the time loop too
            associated_sun.reset_index(drop = True) 
            temp_x.reset_index(drop = True)
            # temp_x[temp_x.date_time == time]  NOTE!!!!

           # associated_sun.reset_index(inplace = True) 
            #temp_x.reset_index(inplace = True)
   # <--- pull these out of the time loop, temp x is joined too many times         
            flares_and_spots_temp = temp_x.join(associated_sun, lsuffix = 'flare_event')
            flares_and_spots = flares_and_spots.append(flares_and_spots_temp)


# This works,  finally. It is giving a data frame of associated sunspots that is
# 3978 x 17

# the clean_x_ray dataframe is 4571 x 13

# I need to get rid of 593 riows before i merge.  I can do this by removing
# the spot numbers not included in cor_regions.  This is stupid clunky...


# MERGE


'''
associated_sun = pd.DataFrame()

temp_sun = cor_sunspot[cor_sunspot.cor_NOAA_USAF_spot_num == '11928']
temp_x = clean_x_ray[clean_x_ray.cor_NOAA_USAF_spot_num == '11928']


for time in temp_x.date_time:
    associated_sun_temp = pd.DataFrame()
   # print time-temp_sun.date_time < np.timedelta64(hours =6)
    #temp_sun['time_diff'] = time - time-temp_sun.date_time    
#     print temp_sun[time-temp_sun.date_time < np.timedelta64(hours =6)]
    associated_sun_temp = associated_sun_temp.append(temp_sun[(time-temp_sun.date_time) < np.timedelta64(hours =6)])
     
    if len(associated_sun_temp.date_time) > 1:
         associated_sun_temp = associated_sun_temp[abs(time - associated_sun_temp.date_time).min()]
         associated_sun = associated_sun.append(associated_sun_temp)
    else:
         associated_sun = associated_sun.append(associated_sun_temp)

associated_sun.shape   
   
'''   #associated_sun.append(temp_sun[time-temp_sun.date_time < np.timedelta64(hours =6)])


### THIS WORKS
associated_sun = pd.DataFrame()

temp_sun = cor_sunspot[cor_sunspot.cor_NOAA_USAF_spot_num.isin(['11909'])]
temp_x = clean_x_ray[clean_x_ray.cor_NOAA_USAF_spot_num.isin(['11909'])]


for time in temp_x.date_time:
   # print time-temp_sun.date_time < np.timedelta64(hours =6)
    #temp_sun['time_diff'] = time - time-temp_sun.date_time    
#     print temp_sun[time-temp_sun.date_time < np.timedelta64(hours =6)]     
        test = temp_sun[(time-temp_sun.date_time) < np.timedelta64(hours =6)]
        test['time_diff'] = abs(time - test.date_time) 
        if test.shape[0] != 0:  
            min_diff = (test.time_diff.min())/datetime.timedelta(seconds = 1)
            test['diff_sec'] = test.time_diff/datetime.timedelta(seconds = 1 )
            associated_sun = associated_sun.append(test[test.diff_sec.isin(min_diff)])
 
associated_sun.reset_index(inplace = True) 
temp_x.reset_index(inplace = True)
flares_and_spots = temp_x.join(associated_sun, lsuffix = 'flare_event')
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    associated_sun = associated_sun.append(temp_sun[(time-temp_sun.date_time) < np.timedelta64(hours =6)])
    print abs(time-temp_sun.date_time).min()

for time in temp_x.date_time:
    print associated_sun[abs(time - associated_sun.date_time).min()]
    

combin    
temp_x[temp_x.cor_NOAA_USAF_spot_num =='11928']



merge(temp_x, associated_sun, on = 'cor_NOAA_USAF_spot_num')
#### END WHAT WORKS





# and now i'm confused.  split on sunspot group, find time delta, write df
x_ray_event_regions.tail()

if abs(clean_x_ray.date_time[425]-cor_sunspot.date_time[4]/np.timedelta64(1, 'h')) <= 6:
    print "yay"

abs(datetime.timedelta(-1, 51000).min)<datetime.timedelta(360

#if abs(clean_x_ray.date_time[425]-cor_sunspot.date_time.head(3)/np.timedelta64(1, 'h') <= 6:
    #print cor_sunspot[clean_x_ray.date_time[425]-cor_sunspot.date_time/np.timedelta64(1, 'h') <= 6]