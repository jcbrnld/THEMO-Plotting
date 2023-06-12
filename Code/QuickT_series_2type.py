#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:51:36 2019

@author: jacobarnold
TABS 225 THEMO Haifa Data

Purpose:
    Check for data continuity from November 1 2018 to March 18 2019
    


"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cmocean

#%%
The_ADCP = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
                   parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
The_ADCP.rename(columns = {'depth[m]':'depth', 'direction[deg]':'direction','speed[m/s]':'speed'}, inplace=True)
#Acoustic Doppler Current Profiler Depth, Direction in degrees, Speed in m/s

#%%

surf_cur = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/dcs.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Near surface current velocity (m/s)

fluor = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/flntu.csv',
                    parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Fluorescence recorded at 1m (Chlorophyll in μg/L) (Turbidity in NTU)

salinity = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/microcat.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Salinity (PSU), conductivity(S/m), and temperature(degrees celcius) recorded at 1m 

temp_prof = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/s9.csv', 
                        parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Temperature recorded at different depths beginning at 5m and ending at 85m (degrees celcius)

met_pak = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/metpak.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
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

plt.style.use('seaborn-deep')

#%%

def tseries1(data, col1, title, ylabel):
    '''
    Plots a simple 1 variable scatter time series 
    The function assumes that the dataframe uses a datetime index
    '''
    fig, ax = plt.subplots(figsize = (15,4))
    ax.scatter(x=data.index, y=col1, data=data, s = 1.5, color='#4B8ECA')
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel(ylabel)
    plt.tight_layout()

def tseries2(data, col1, col2, title, ylabel1, ylabel2):
    fig, ax1 = plt.subplots(figsize = (15,4))
    ax1.scatter(x=data.index, y=col1, data=data, s=1.5, color='#4B8ECA')
    ax1.set_title(title)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(ylabel1)
    ax2 = ax1.twinx()
    ax2.scatter(x=data.index, y=col2, data=data, s=1.5, color='#4BBC82')
    ax2.set_ylabel(ylabel2)
    fig.legend()
    plt.tight_layout()

#%%    

tseries2(salinity, 'Salinity', 'Temperature', 'Salinity And Temperature from Microcat', 'Salinity (PSU)', 'Water Temperature (\u2103)')   
tseries2(waves, 'significant_height', 'mean_period', 'Waves Significant Height and Mean Period', 'Height (m)', 'Mean Period (s)')
tseries1(temp_air, 'AvgLinearAdjVal', 'Air Temperature', 'Air Temperature (\u2103)')
tseries1(baro, 'BAROMETER', 'Barometer', 'Barometric Pressure (mbar)')
tseries2(fluor, 'chlorophyll_concentration', 'turbidity_units', 'Fluorometer', 'Chlorophyll Concentration (μg/L)', 'Turbidity (NTU)')
tseries2(temp_prof, 'temperature', 'depth', 'Temperature Profiles', 'Water Temperature (\u2103)', 'Depth (m)')
tseries1(humid, 'AvgLinearAdjVal', 'Humidity', 'Relative Humidity (%)')
tseries2(The_ADCP, 'speed', 'depth', 'Acoustic Dopler Current Profiler (ADCP)', 'Speed (m/s)', 'Depth (m)')









