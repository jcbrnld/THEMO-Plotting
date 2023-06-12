#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:46:47 2019

@author: jacobarnold

Purpose:
    Fill data gaps for 1D variables (everything but adcp)
    
"""
import pandas as pd

#%%
# Import dataframes here
fluor = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/flntu.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
# smooth out the second discrepencies
fluor.index = fluor.index.map(lambda x: x.replace(second=0))
fluor.drop('threshold', axis=1, inplace=True)
fluor.drop('const_err', axis=1, inplace=True)

surf_cur = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/dcs.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
surf_cur.index = surf_cur.index.map(lambda x: x.replace(second=0))
#Near surface current velocity (m/s)

salinity = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/microcat.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
salinity.index = salinity.index.map(lambda x: x.replace(second=0))
#Salinity (PSU), conductivity(S/m), and temperature(degrees celcius) recorded at 1m 

temp_prof = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/s9.csv', 
                        parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Temperature recorded at different depths beginning at 5m and ending at 85m (degrees celcius)

met_pak = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/metpak.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
met_pak.drop('threshold', axis=1, inplace=True)
met_pak.drop('const_err', axis=1, inplace=True)
met_pak.index = met_pak.index.map(lambda x: x.replace(second=0))
#Meteorology package - Air temp (degrees Celcius), Relative humidity (%), Wind Velocity (m/s) and pressure (millibars).

wind_vel = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/windsonic.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Wind velocity recorded at -3m (meters/second)

humid = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/mp101a_humidity.csv',
                    parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Humidity in the air recorded at -3m (RH%)

temp_air = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/mp101a_temprature.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Temperature of the air recorded at -3m (degrees celcius)

baro = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/barometer.csv',
                   parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Barometric pressure recorded at -3m (millibar)

waves = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/waves.csv',
                    parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Height of waves (meters) period of waves (seconds)


#%%

# Create the new date index with no missing values
date_index_fluor = pd.date_range(start='2017-07-26 00:10:00', end='2018-12-27 17:10:00', periods=24947)
date_index_surf_cur = pd.date_range(start='2017-07-26 00:05:00', end='2019-05-30 13:05:00', periods=32331)
date_index_sal = pd.date_range(start='2017-07-24 05:31:00', end='2019-05-30 13:01:00', periods=32416)
date_index_met = pd.date_range(start='2017-07-26 00:05:00', end='2019-05-30 13:05:00', periods=32331)

# Define the index as date time
def date_fmt_1D(dataframe):
    temp = dataframe
    temp.index = pd.to_datetime(temp.index)
    return temp



#%%
# Fluor

fluor = date_fmt_1D(fluor)

fluor = fluor[~fluor.index.duplicated()]
fluor_F = fluor.reindex(date_index_fluor)
fluor_F.to_csv('Documents/Classes/THEMO/TABS225m09/Data/flntu_F.csv')

#%%
# surf_cur
test = surf_cur.groupby(surf_cur.index)

surf_cur = surf_cur[~surf_cur.index.duplicated()]
surf_cur = date_fmt_1D(surf_cur)
surf_cur_F = surf_cur.reindex(date_index_surf_cur)
surf_cur_F.to_csv('Documents/Classes/THEMO/TABS225m09/Data/dcs_F.csv')



#%%
# salinity
salinity = date_fmt_1D(salinity)
salinity = salinity[~salinity.index.duplicated()]
salinity_F = salinity.reindex(date_index_sal)
salinity_F.to_csv('Documents/Classes/THEMO/TABS225m09/Data/microcat_F.csv')

#%%
#met_pak
met_pak = date_fmt_1D(met_pak)
met_pak = met_pak[~met_pak.index.duplicated()]
met_pak_F = met_pak.reindex(date_index_met)
met_pak_F.to_csv('Documents/Classes/THEMO/TABS225m09/Data/metpak_F.csv')

