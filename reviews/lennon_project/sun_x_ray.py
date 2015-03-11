# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 08:58:12 2015

@author: craig.m.lennon
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Import goes x-ray data
x_ray = pd.read_csv('C:\Users\Craig\Documents\Python_DS\GA_DS\DAT4-students\craig\goes_1981_2013.csv')

# remove data code and station code leaving only the date as yymmdd
x_ray['measurement_date'] = [str(int(date))[5:12] for date in x_ray.data_code_date]

# make a smaller dataframe with dates, times, and x-ray class
clean_x_ray = x_ray[['measurement_date', 'start_time', 'end_time', 'max_time', 'sunspot_region_number', 'x_ray_class']]


# Split the measurment date in year month and day. Convert to integer
clean_x_ray['year'] = [int('19' + date[0:2]) if int(date[0:2]) >=81 and int(date[0:2]) <=99 else int('20' + date[0:2]) for date in clean_x_ray.measurement_date]
clean_x_ray['month'] =  [int(date[2:4]) for date in clean_x_ray.measurement_date]
clean_x_ray['day'] =  [int(date[4:]) for date in clean_x_ray.measurement_date]

# Split time into hours and minutes. Convert to integer
start_time = [str(int(time)) for time in clean_x_ray.start_time]

clean_start_time = []
for time in start_time:
    if len(time) == 2:
        clean_start_time.append('00' + time)       
        #print '00' + time
    elif len(time) == 3:
        clean_start_time.append('0' + time)       
        #print '0' + time
    elif len(time) == 1:
        clean_start_time.append('000' + time)       
        #print '000' + time
    else:
        clean_start_time.append(time)       
      
clean_x_ray['hour'] = [int(time[0:2]) for time in clean_start_time]
clean_x_ray['minute'] = [int(time[2:4]) for time in clean_start_time]

# Prepare a new series in the clean_x_ray dataframe that 
# contains datetime objects
date_time = []
for i in range(len(clean_x_ray.year)):
    date_time.append(datetime.datetime(clean_x_ray.year[i], clean_x_ray.month[i], clean_x_ray.day[i], clean_x_ray.hour[i], clean_x_ray.minute[i]))

clean_x_ray['date_time'] = date_time

# create a new series called NOAA_USAF_spot_num.  this will be used to correlete flares to sunspot groups
#
clean_x_ray['cor_NOAA_USAF_spot_num'] = [str(item).replace('.0', '') for item in clean_x_ray.sunspot_region_number] 

x_ray_event_regions = pd.Series(clean_x_ray.cor_NOAA_USAF_spot_num.unique())
#x_ray_event_regions.to_csv('C:\Users\Craig\Documents\Python_DS\GA_DS\DAT4-students\craig\event_regions.csv')


x_ray_event_regions = x_ray_event_regions.tolist()

# Sunspots


# Import raw NOAA/USAF sunspot data
sunspot = pd.read_csv('C:\Users\Craig\Documents\Python_DS\GA_DS\DAT4-students\craig\USAF_sunspot_1982_2014.csv', dtype = object)

# Create a new data frame containing 'important' columns.
# data_code_date:  observation code and date
# UTC_obs: time of sunspot observation in UTC
# NOAA_USAF_spot_num: unique identifier given to a sunspot or spot cluster
# zurich: Sunspot McIntosh Classifer 1
# penumbra: Sunspot McIntosh Classifer 2
# compactness: Sunspot McIntosh Classifer 3
# number_of_spots: number of sunspots at a NOAA_USAF number
# area: area of sunspot cluster (km^2 or a goofy astronomical unit of area?)

clean_sunspot = sunspot[['data_code_date', 'UTC_obs', 'NOAA_USAF_spot_num', 'zurich', 'penumbra', 'compactness', 'number_of_spots', 'area']]

# only cases with complete sunspot class descriptions, ie zpc values

clean_sunspot = clean_sunspot[clean_sunspot.zurich.notnull()]
clean_sunspot = clean_sunspot[clean_sunspot.penumbra.notnull()]
clean_sunspot = clean_sunspot[clean_sunspot.compactness.notnull()]

# check NaN sum
# clean_sunspot.compactness.isnull().sum()


# clean up the trailing decimal point and zero
clean_sunspot.data_code_date = [item.replace('.0', '')  for item in clean_sunspot.data_code_date] 

# Create new columns for year, month, and day for each sunspot observation
clean_sunspot['year'] = [int('19' + date[2:4]) if int(date[2:4]) >=81 and int(date[2:4]) <=99 else int('20' + date[2:4]) for date in clean_sunspot.data_code_date]
clean_sunspot['month'] =  [int(date[4:6]) for date in clean_sunspot.data_code_date]
clean_sunspot['day'] =  [int(date[6:8]) for date in clean_sunspot.data_code_date]


# Clean up UTC_time column and create hour and minute columns
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

sunspot_date_time = []

# There's a better way to do this, but I just learned that today and this already works...
clean_index = clean_sunspot.index

for i in clean_index:
    sunspot_date_time.append(datetime.datetime(clean_sunspot.year[i], clean_sunspot.month[i], clean_sunspot.day[i], clean_sunspot.hour[i], clean_sunspot.minute[i]))

clean_sunspot['date_time'] = sunspot_date_time


# correlated regions

# Clean up NOAA_USAF_spot_num so that it matches the same series in the x-ray (flare) data
clean_sunspot['cor_NOAA_USAF_spot_num'] = [str(item).replace('.0', '')  for item in clean_sunspot.NOAA_USAF_spot_num]

# Pass the list x_ray_event_regions created in the clean_xray script.
# this list contains unique values of NOAA numbers where flare events were observed
cor_sunspot = clean_sunspot[clean_sunspot.cor_NOAA_USAF_spot_num.isin(x_ray_event_regions)]

cor_regions = cor_sunspot.cor_NOAA_USAF_spot_num.unique()

# Define an empty dataframe that will contain all sunspot observations that 
# are associated with an x-ray flare event.  The time difference between a sunspot
# measurement and a flare measurent has been set to 6 hours to be considered
# associated


associated_sun = pd.DataFrame()

for region in cor_regions:
    
    # Split cor_sunspot df and clean_x_ray df by unique sunspot number    
    temp_sun = cor_sunspot[cor_sunspot.cor_NOAA_USAF_spot_num == region]
    temp_x = clean_x_ray[clean_x_ray.cor_NOAA_USAF_spot_num == region]
    
    for time in temp_x.date_time:
        # only select sunspot rows where the x-ray observation time and sunspot observation time
        # occur within six hours
        dummy_sun = temp_sun[(time-temp_sun.date_time) < np.timedelta64(hours =6)]
        

        if dummy_sun.shape[0] != 0:         
            # Create a new column that contains the time difference between flare
            # and sunspot observations in seconds and deal with negative timedeltas.
        
            dummy_sun['time_diff'] = abs(time - dummy_sun.date_time) 
            dummy_sun['diff_sec'] = dummy_sun.time_diff/datetime.timedelta(seconds = 1 )
            dummy_sun = dummy_sun[dummy_sun.diff_sec <= 21600] # 21600 seconds
            
            # Add a column containing the x-ray flare observation time, this will be used
            # as an index value later.
            dummy_sun['x_ray_time'] = time

            # If multiple sunspot observations occur within 6 hours of a flare
            # only take the smallest timedelta.
            
            if len(dummy_sun.diff_sec) > 0:            
                dummy_sun = dummy_sun[dummy_sun.diff_sec == min(dummy_sun.diff_sec)]
                
                # dataframe of sunspot obersavtions associated with a solar flare
                associated_sun = associated_sun.append(dummy_sun)
                
# Set the index values of x-ray data and associated sunspot data in order to 
# facilitate merging 
                
clean_x_ray_time_index = clean_x_ray.set_index('date_time')
associated_sun_time_index = associated_sun.set_index('x_ray_time')

# Create a final data frame that contains features (ZPC) and outcomes (associated, flare type)
flares_and_spots = pd.merge(associated_sun_time_index, clean_x_ray_time_index, left_index = True, right_index = True) 

flares_and_spots = flares_and_spots[['zurich', 'penumbra', 'compactness','x_ray_class']]             

associated_len =  len(flares_and_spots.zurich)
flares_and_spots['association'] =  ['associated' for i in range(1, associated_len + 1)]         
flares_and_spots.to_csv('C:\\Users\\Craig\Documents\\Python_DS\\GA_DS\\DAT4-students\\craig\\associated.csv')
    
    

#clean_x_ray[~clean_x_ray.cor_NOAA_USAF_spot_num.isin(cor_regions)]
unassociated_spots = clean_sunspot[~clean_sunspot.cor_NOAA_USAF_spot_num.isin(x_ray_event_regions)]
unassociated_spots = unassociated_spots[unassociated_spots.year >= 1982]
unassociated_spots_time_index = unassociated_spots.set_index('date_time')
unassociated_spots_time_index = unassociated_spots_time_index[['zurich', 'penumbra', 'compactness']]
unassociated_len = len(unassociated_spots.zurich)
unassociated_spots_time_index['association'] = ['unassociated' for i in range(1, 1 + unassociated_len )]

unassociated_spots_time_index.to_csv('C:\\Users\\Craig\Documents\\Python_DS\\GA_DS\\DAT4-students\\craig\\unassociated.csv')
