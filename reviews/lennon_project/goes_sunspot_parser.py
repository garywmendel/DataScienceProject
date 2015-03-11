<<<<<<< HEAD
<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 13:36:23 2014

@author: craig.m.lennon
"""

import pandas as pd


# Year range for GOES x-ray data
years = range(1975, 2015) #text file naming convention changes as 2012

# ftp address for GOES data
goes_URL_1 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/'

# column specifications and header names for GOES data
goes_cols = [(0 , 12), (13 , 17), (18 , 22), (23 , 27), (28 , 37), (59 , 60), (61 , 62), (67 , 71), (72 , 79), (80 , 85), (86 , 94), (95 , 102), (103 , 111) ]
goes_header = ['data_code_date', 'start_time', 'end_time', 'max_time', 'lat_long', 'x_ray_class', 'x_ray_intensity', 'station_name', 'int_flux', 'sunspot_region_number', 'CMP_date', 'region_area', 'total_SXI_int']

# Ininitialize an empy dataframe
goes_MX = pd.DataFrame()
temp_df = pd.DataFrame()

for year in years:
    if year <=  2011:    
        # Generates a URL for each year of data   maybe add an if statement for years to 2014 
        goes_URL_2 = goes_URL_1 + str(year) + '/' + 'goes-xray_' + str(year) + '.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))
    
    elif year == 2012:
        goes_URL_2 = goes_URL_1 + '2012/goes-xray-report_2012-processed.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))

    elif year == 2013:
        goes_URL_2 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/2013/goes-xray_report_2013-processed.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))
        
    
    else:
        goes_URL_2 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/2014/goes-xray-report_2014.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))        
        
    

# Write GOES x-ray data to a csv for future analysis

goes_MX.to_csv('/Users/garywmendel/Dropbox/gary stuff/python/DataScience/datascienceproject/reviews/lennon_project/GaryOutput/goes_1975_2014.csv')


###############################################################################



# Obtain sunspot data

# Year range for sunspot data
sunspot_years = range(1981, 2014)

# FTP address for sunspot data
sunspot_URL_1 = 'ftp://ftp.ngdc.noaa.gov/STP/SOLAR_DATA/SUNSPOT_REGIONS/USAF_MWL/'

# column specification for sunspot data

# ftp://ftp.ngdc.noaa.gov/STP/SOLAR_DATA/SUNSPOT_REGIONS/USAF_MWL/docs/usaf_mwl.fmt
# the tuple (x,y) ends on the column i want and does not include the first col num x
sunspot_cols = [(0 , 8), (9 , 13), (14 , 20) , (21 , 23), (25 , 26) , (27, 32), (32 , 33), (33 , 38), (38 , 39), (39 ,40), (40 , 41), (41 , 42), (43 , 45), (46 , 48), (48 , 52) , (53 , 55), (55 , 57), (57, 61), (62 , 64), (64 , 66), (66 , 70), (71 , 74), (75 , 76), (76 , 80)]
sunspot_header = ['data_code_date', 'UTC_obs', 'lat_long', 'mt_wil_mag_class', 'max_B_field', 'MWIL_spot_num', 'MWIL_subscript', 'NOAA_USAF_spot_num', 'NOAA_USAF_subscript', 'zurich', 'penumbra', 'compactness', 'number_of_spots', 'long_extent', 'area', 'ind_cent_merid_pass_year', 'ind_cent_merid_pass_month', 'ind_cent_merid_pass_day', 'reg_cent_merid_pass_year', 'reg_cent_merid_pass_month', 'reg_cent_merid_pass_day', 'station_serial_number', 'quality', 'station_abbv']

# Initialize an empty dataframe

temp_df = pd.DataFrame()
sunspot_regions = pd.DataFrame()

for year in sunspot_years:
    
    if year <= 1994:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'usaf_mwl.' + str(year)[2:]
        
        # For each year a temporary dataframe is created and then appended to sunspot_regions
        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    
    
    elif year == 1995:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'usaf_mwl.95.rev'

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))
        
    elif year > 1995 and year <= 2005:
        
        # For each year a temporary dataframe is created and then appended to sunspot_regions
        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    
    

    elif year > 2005 and year <= 2009:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'USAF.' + str(year)[2:]

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))          
    
    else:
    
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'solar_regions_reports_' + str(year) + '-processed.txt' 

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    


# Write sunspot data to a csv for future analysis

sunspot_regions.to_csv('/Users/garywmendel/Dropbox/gary stuff/python/DataScience/datascienceproject/reviews/lennon_project/GaryOutput/USAF_sunspot_1981_2013.csv')

        
# NOTE: UTC is not reading leading zeros
       
for time in sunspot_regions.UTC_obs:
    if len(str(time)) == 2:
        print '00' + str(time)
    elif len(str(time)) == 3:
        print '0' + str(time)
    elif len(str(time)) == 1:
        print '000' + str(time)    
    else:
        print str(time)
      
=======
>>>>>>> 8c891d63e8222c983340a06e49a2cdda05075e4a
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 13:36:23 2014

@author: craig.m.lennon
"""

import pandas as pd


# Year range for GOES x-ray data
years = range(1982, 2014) #text file naming convention changes as 2012

# ftp address for GOES data
goes_URL_1 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/'

# column specifications and header names for GOES data
goes_cols = [(0 , 12), (13 , 17), (18 , 22), (23 , 27), (28 , 37), (59 , 60), (61 , 62), (67 , 71), (72 , 79), (80 , 85), (86 , 94), (95 , 102), (103 , 111) ]
goes_header = ['data_code_date', 'start_time', 'end_time', 'max_time', 'lat_long', 'x_ray_class', 'x_ray_intensity', 'station_name', 'int_flux', 'sunspot_region_number', 'CMP_date', 'region_area', 'total_SXI_int']

# Ininitialize an empy dataframe
goes_MX = pd.DataFrame()
temp_df = pd.DataFrame()

for year in years:
    if year <=  2011:    
        # Generates a URL for each year of data   maybe add an if statement for years to 2014 
        goes_URL_2 = goes_URL_1 + str(year) + '/' + 'goes-xray_' + str(year) + '.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))
    
    elif year == 2012:
        goes_URL_2 = goes_URL_1 + '2012/goes-xray-report_2012-processed.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))

    elif year == 2013:
        goes_URL_2 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/2013/goes-xray_report_2013-processed.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))
        
    
    else:
        goes_URL_2 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/2014/goes-xray-report_2014.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))        
        
    

# Write GOES x-ray data to a csv for future analysis

goes_MX.to_csv('/Users/garywmendel/Dropbox/gary stuff/python/DataScience/datascienceproject/reviews/lennon_project/GaryOutput/goes_1982_2014.csv')


###############################################################################



# Obtain sunspot data

# Year range for sunspot data
sunspot_years = range(1982, 2014)

# FTP address for sunspot data
sunspot_URL_1 = 'ftp://ftp.ngdc.noaa.gov/STP/SOLAR_DATA/SUNSPOT_REGIONS/USAF_MWL/'

# column specification for sunspot data

# ftp://ftp.ngdc.noaa.gov/STP/SOLAR_DATA/SUNSPOT_REGIONS/USAF_MWL/docs/usaf_mwl.fmt
# the tuple (x,y) ends on the column i want and does not include the first col num x
sunspot_cols = [(0 , 8), (9 , 13), (14 , 20) , (21 , 23), (25 , 26) , (27, 32), (32 , 33), (33 , 38), (38 , 39), (39 ,40), (40 , 41), (41 , 42), (43 , 45), (46 , 48), (48 , 52) , (53 , 55), (55 , 57), (57, 61), (62 , 64), (64 , 66), (66 , 70), (71 , 74), (75 , 76), (76 , 80)]
sunspot_header = ['data_code_date', 'UTC_obs', 'lat_long', 'mt_wil_mag_class', 'max_B_field', 'MWIL_spot_num', 'MWIL_subscript', 'NOAA_USAF_spot_num', 'NOAA_USAF_subscript', 'zurich', 'penumbra', 'compactness', 'number_of_spots', 'long_extent', 'area', 'ind_cent_merid_pass_year', 'ind_cent_merid_pass_month', 'ind_cent_merid_pass_day', 'reg_cent_merid_pass_year', 'reg_cent_merid_pass_month', 'reg_cent_merid_pass_day', 'station_serial_number', 'quality', 'station_abbv']

# Initialize an empty dataframe

temp_df = pd.DataFrame()
sunspot_regions = pd.DataFrame()

for year in sunspot_years:
    
    if year <= 1994:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'usaf_mwl.' + str(year)[2:]
        
        # For each year a temporary dataframe is created and then appended to sunspot_regions
        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    
    
    elif year == 1995:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'usaf_mwl.95.rev'

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))
        
    elif year > 1995 and year <= 2005:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'usaf_mwl.' + str(year)[2:]

        # For each year a temporary dataframe is created and then appended to sunspot_regions
        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    
    

    elif year > 2005 and year <= 2009:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'USAF.' + str(year)[2:]

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))          
    
    else:
    
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'solar_regions_reports_' + str(year) + '-processed.txt' 

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    


# Write sunspot data to a csv for future analysis

sunspot_regions.to_csv('/Users/garywmendel/Dropbox/gary stuff/python/DataScience/datascienceproject/reviews/lennon_project/GaryOutput/USAF_sunspot_1982_2013.csv')

        
# NOTE: UTC is not reading leading zeros
       
for time in sunspot_regions.UTC_obs:
    if len(str(time)) == 2:
        print '00' + str(time)
    elif len(str(time)) == 3:
        print '0' + str(time)
    elif len(str(time)) == 1:
        print '000' + str(time)    
    else:
        print str(time)
      
<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 13:36:23 2014

@author: craig.m.lennon
"""

import pandas as pd


# Year range for GOES x-ray data
years = range(1975, 2015) #text file naming convention changes as 2012

# ftp address for GOES data
goes_URL_1 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/'

# column specifications and header names for GOES data
goes_cols = [(0 , 12), (13 , 17), (18 , 22), (23 , 27), (28 , 37), (59 , 60), (61 , 62), (67 , 71), (72 , 79), (80 , 85), (86 , 94), (95 , 102), (103 , 111) ]
goes_header = ['data_code_date', 'start_time', 'end_time', 'max_time', 'lat_long', 'x_ray_class', 'x_ray_intensity', 'station_name', 'int_flux', 'sunspot_region_number', 'CMP_date', 'region_area', 'total_SXI_int']

# Ininitialize an empy dataframe
goes_MX = pd.DataFrame()
temp_df = pd.DataFrame()

for year in years:
    if year <=  2011:    
        # Generates a URL for each year of data   maybe add an if statement for years to 2014 
        goes_URL_2 = goes_URL_1 + str(year) + '/' + 'goes-xray_' + str(year) + '.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))
    
    elif year == 2012:
        goes_URL_2 = goes_URL_1 + '2012/goes-xray-report_2012-processed.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))

    elif year == 2013:
        goes_URL_2 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/2013/goes-xray_report_2013-processed.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))
        
    
    else:
        goes_URL_2 = 'ftp://ftp.ngdc.noaa.gov/STP/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/2014/goes-xray-report_2014.txt'
    
        # For each year a temporary dataframe is created
        temp_df = pd.read_fwf(goes_URL_2, header = None, colspecs = goes_cols)
        temp_df.columns = goes_header

        temp_df = temp_df[temp_df['sunspot_region_number'] > 0]
        temp_df = temp_df[temp_df.x_ray_class.isin(['M', 'X'])]
    
        goes_MX = goes_MX.append(pd.DataFrame(data = temp_df))        
        
    

# Write GOES x-ray data to a csv for future analysis

goes_MX.to_csv('/Users/garywmendel/Dropbox/gary stuff/python/DataScience/datascienceproject/reviews/lennon_project/GaryOutput/goes_1975_2014.csv')


###############################################################################



# Obtain sunspot data

# Year range for sunspot data
sunspot_years = range(1981, 2014)

# FTP address for sunspot data
sunspot_URL_1 = 'ftp://ftp.ngdc.noaa.gov/STP/SOLAR_DATA/SUNSPOT_REGIONS/USAF_MWL/'

# column specification for sunspot data

# ftp://ftp.ngdc.noaa.gov/STP/SOLAR_DATA/SUNSPOT_REGIONS/USAF_MWL/docs/usaf_mwl.fmt
# the tuple (x,y) ends on the column i want and does not include the first col num x
sunspot_cols = [(0 , 8), (9 , 13), (14 , 20) , (21 , 23), (25 , 26) , (27, 32), (32 , 33), (33 , 38), (38 , 39), (39 ,40), (40 , 41), (41 , 42), (43 , 45), (46 , 48), (48 , 52) , (53 , 55), (55 , 57), (57, 61), (62 , 64), (64 , 66), (66 , 70), (71 , 74), (75 , 76), (76 , 80)]
sunspot_header = ['data_code_date', 'UTC_obs', 'lat_long', 'mt_wil_mag_class', 'max_B_field', 'MWIL_spot_num', 'MWIL_subscript', 'NOAA_USAF_spot_num', 'NOAA_USAF_subscript', 'zurich', 'penumbra', 'compactness', 'number_of_spots', 'long_extent', 'area', 'ind_cent_merid_pass_year', 'ind_cent_merid_pass_month', 'ind_cent_merid_pass_day', 'reg_cent_merid_pass_year', 'reg_cent_merid_pass_month', 'reg_cent_merid_pass_day', 'station_serial_number', 'quality', 'station_abbv']

# Initialize an empty dataframe

temp_df = pd.DataFrame()
sunspot_regions = pd.DataFrame()

for year in sunspot_years:
    
    if year <= 1994:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'usaf_mwl.' + str(year)[2:]
        
        # For each year a temporary dataframe is created and then appended to sunspot_regions
        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    
    
    elif year == 1995:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'usaf_mwl.95.rev'

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))
        
    elif year > 1995 and year <= 2005:
        
        # For each year a temporary dataframe is created and then appended to sunspot_regions
        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    
    

    elif year > 2005 and year <= 2009:
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'USAF.' + str(year)[2:]

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))          
    
    else:
    
        sunspot_URL_2 = sunspot_URL_1 + str(year) + '/' + 'solar_regions_reports_' + str(year) + '-processed.txt' 

        temp_df = pd.read_fwf(sunspot_URL_2, header = None, colspecs = sunspot_cols)
        temp_df.columns = sunspot_header
        sunspot_regions = sunspot_regions.append(pd.DataFrame(data = temp_df))    


# Write sunspot data to a csv for future analysis

sunspot_regions.to_csv('/Users/garywmendel/Dropbox/gary stuff/python/DataScience/datascienceproject/reviews/lennon_project/GaryOutput/USAF_sunspot_1981_2013.csv')

        
# NOTE: UTC is not reading leading zeros
       
for time in sunspot_regions.UTC_obs:
    if len(str(time)) == 2:
        print '00' + str(time)
    elif len(str(time)) == 3:
        print '0' + str(time)
    elif len(str(time)) == 1:
        print '000' + str(time)    
    else:
        print str(time)
      
>>>>>>> 89d32b10f9165af332947786045b6c7ad027294c
=======
>>>>>>> pr/36
>>>>>>> 8c891d63e8222c983340a06e49a2cdda05075e4a
