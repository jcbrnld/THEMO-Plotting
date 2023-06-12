#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:21:14 2019

@author: Jacob
TABS 225 THEMO Haifa Data

Purpose:
    Identify gaps and errors in the data

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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


#%%

#%%
'''clean salinity'''
salinity.Salinity[salinity.Salinity < 20] = np.nan
salinity.Conductivity[salinity.Conductivity < 3] = np.nan

#%%
'''clean waves domimant period'''
waves.dominant_period[waves.dominant_period > 30]

#%%

'''Scatter plot of salinity'''
plt.figure(figsize = (15,3))
plt.scatter(x = salinity.index, y = 'Salinity', data = salinity, s=1.5)
plt.title('Salinity <20 Filtered')
plt.xlabel('Date')
plt.ylabel('Salinity')
#fig.savefig('Documents/Classes/OCNG491/THEMO/ABC_17_07_26-19_01_21/Time_series/blue_white/scat_salinity_less20_filtered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of temp from s9'''
plt.figure(figsize = (15,3))
plt.scatter(x = salinity.index, y = 'Temperature', data = salinity, s=1.5)
plt.title('TABS225 Unfiltered s9 Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature ($\circ$C)')
#fig.savefig('Documents/Classes/OCNG491/THEMO/ABC_17_07_26-19_01_21/Time_series/blue_white/scat_temp_froms9_unfiltered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of waves height'''
plt.figure(figsize = (15,3))
plt.scatter(x = waves.index, y = 'significant_height', data = waves, s=1.5)
plt.title('TABS225 Unfiltered Waves Significant Height')
plt.xlabel('Date')
plt.ylabel('Wave Height (m)')
#fig.savefig('Documents/Classes/OCNG491/THEMO/ABC_17_07_26-19_01_21/Time_series/blue_white/scat_waves_sight_unfiltered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of waves mean period'''
plt.figure(figsize = (15,3))
plt.scatter(x = waves.index, y = 'mean_period', data = waves, s=1.5)
plt.title('TABS225 Unfiltered Waves Mean Period')
plt.xlabel('Date')
plt.ylabel('Wave Period (s)')
#fig.savefig('Documents/Classes/OCNG491/THEMO/ABC_17_07_26-19_01_21/Time_series/blue_white/scat_waves_mean_period_unfiltered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of waves dominant period'''
plt.figure(figsize = (15,3))
plt.scatter(x = waves.index, y = 'dominant_period', data = waves, s=1.5)
plt.title('TABS225 Unfiltered Waves Dominant Period')
plt.xlabel('Date')
plt.ylabel('Wave Period (s)')
#fig.savefig('Documents/Classes/OCNG491/THEMO/ABC_17_07_26-19_01_21/Time_series/blue_white/scat_waves_dom_period_unfiltered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of flourometer'''
plt.figure(figsize = (15,3))
plt.scatter(x = flour.index, y ='chlorophyll_concentration', data = flour, s=1.5)
plt.scatter(x = flour.index, y ='turbidity_units', data = flour, s=1.5)
plt.title('TABS225 Unfiltered Flourometer')
plt.legend()
plt.xlabel('Date')

#fig.savefig('Documents/Classes/OCNG491/THEMO/ABC_17_07_26-19_01_21/Time_series/blue_white/scat_waves_mean_period_unfiltered.png',bbox_inches='tight',dpi=400)


#%%
'''Scatter plot of temperature profiler'''
fig, ax1 = plt.subplots(figsize = (15,3))
ax1.scatter(x = temp_prof.index, y = 'temperature', data = temp_prof, s=5)
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature ($\circ$C)')

ax2 = ax1.twinx()
ax2.scatter(x = temp_prof.index, y = 'depth', data = temp_prof, s=1.5, c = 'green', alpha = .1)
ax2.set_ylabel('Depth (m)')

plt.tight_layout()
plt.show()

#%%
'''Scatter plot of wind velocity'''
fig, ax1 = plt.subplots(figsize = (15,3))
ax1.scatter(x = wind_vel.index, y = 'magnitude_1', data = wind_vel, s=5)
ax1.set_xlabel('Date')
ax1.set_ylabel('Velocity (m/s)')

ax2 = ax1.twinx()
ax2.scatter(x = wind_vel.index, y = 'winddirection', data = wind_vel, s=1.5, c = 'green')
ax2.set_ylabel('Wind Direction ($\circ$)')

plt.tight_layout()
plt.show()

#%%

'''Scatter plot of air temperature'''
plt.figure(figsize = (15,3))
plt.scatter(x = temp_air.index, y = 'AvgLinearAdjVal', data = temp_air, s=1.5)
plt.title('TABS225 Unfiltered Air Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature ($\circ$C)')

#%%

'''Scatter plot of humidity'''
plt.figure(figsize = (15,3))
plt.scatter(x = humid.index, y ='AvgLinearAdjVal', data = humid, s=1.5)
plt.title('TABS225 Unfiltered Humidity')
plt.xlabel('Date')
plt.ylabel('Relative Humidity (%)')







