# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 12:58:34 2015

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
x_ray_event_regions.to_csv('C:\Users\Craig\Documents\Python_DS\GA_DS\DAT4-students\craig\event_regions.csv')


x_ray_event_regions = x_ray_event_regions.tolist()

