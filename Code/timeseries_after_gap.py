#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:08:07 2019

@author: Jacob
TABS 225 THEMO Haifa Data

Purpose:
    Create time series of the raw data --trimmed to earthly values-- 
    to the primary data gap.
    
Each sensor's data will be plotted together.
Scatter AND line plots will be created 

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

def trim_late (dataframe, date):
    '''
    Takes in dataframe and date from which it should be trimmed 
    returns the dataframe trimmed FROM that date.
    '''
    dataframe = dataframe[date:]
    return dataframe


#%%
humid = trim_late(humid, '2018-09-02 09:20:31')


#%%
'''trim salinity'''
salinity.Salinity[salinity.Salinity < 20] = np.nan
salinity.Conductivity[salinity.Conductivity < 3] = np.nan

salinity = trim_late(salinity, '2018-09-02 00:01:13')

#%%
'''Scatter plot of salinity and temperature from microcat'''
fig, ax1 = plt.subplots(figsize = (15,3))

ax1.scatter(x = salinity.index, y = 'Salinity', data = salinity,  s=1.5, color='#4B8ECA')
#ax1.scatter(x = salinity.index, y = 'Temperature', data = salinity,  s=1.5)
ax1.set_title('Post Gap (2018-09-02 to 2019-01-29) Salinity, Water Temperature')
ax1.set_xlabel('Date')
ax1.set_ylabel('Salinity (PSU)')

ax2 = ax1.twinx()
ax2.scatter(x = salinity.index, y = 'Temperature', data = salinity,  s=1.5, color='#4BBC82')
ax2.set_ylabel('Water Temperature (\u2103)')
fig.legend(bbox_to_anchor = [0.95, 0.875])
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_salinity_temp_after.png',bbox_inches='tight',dpi=400)

#%%
'''trim waves'''
waves = trim_late(waves, '2018-09-02 00:13:01')
waves.dominant_period[waves.dominant_period > 13] = np.nan
#%%

'''Scatter plot of waves'''
fig, ax1 = plt.subplots(figsize = (15,3))

ax1.scatter(x = waves.index, y = 'dominant_period', data = waves,  s=1.5, color='#4B8ECA')
ax1.scatter(x = waves.index, y = 'mean_period', data = waves,  s=1.5, color='#BC3A3A')
ax1.set_title('Post Gap (2018-09-02 to 2019-01-29) Waves: Mean Period, Dominant Period, Significant Height')
ax1.set_xlabel('Date')
ax1.set_ylabel('Period (s)')

ax2 = ax1.twinx()
ax2.scatter(x = waves.index, y = 'significant_height', data = waves,  s=1.5, color='#4BBC82')
ax2.set_ylabel('Height (m)')
fig.legend(bbox_to_anchor = [0.197, 0.875])
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_waves_after.png',bbox_inches='tight',dpi=400)


#%%
'''trim temp_air'''
temp_air = trim_late(temp_air, '2018-09-02 09:20:26')

#%%
'''Scatter plot of temp_air'''
fig, ax1 = plt.subplots(figsize = (15,3))

ax1.scatter(x = temp_air.index, y = 'AvgLinearAdjVal', data = temp_air,  s=1.5, color='#4B8ECA')
ax1.set_title('Post Gap (2018-09-02 to 2019-01-29) Air Temperature (Average Linear Adjusted Value)')
ax1.set_xlabel('Date')
ax1.set_ylabel('Air Temperature (\u2103)')
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_air_temp_after.png',bbox_inches='tight',dpi=400)

#%%
'''trim barometer'''
baro = trim_late(baro, '2018-09-02 00:01:08')

#%%
'''Scatter plot of baro'''
fig, ax1 = plt.subplots(figsize = (15,3))

ax1.scatter(x = baro.index, y = 'BAROMETER', data = baro,  s=1.5, color='#4B8ECA')
ax1.set_title('Post Gap (2018-09-02 to 2019-01-29) Barometric Pressure')
ax1.set_xlabel('Date')
ax1.set_ylabel('Barometric Pressure (mbar)')
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_baro_after.png',bbox_inches='tight',dpi=400)

#%%
'''trim fluor'''
fluor = trim_late(fluor, '2018-09-02 00:10:08')
fluor.chlorophyll_concentration[fluor.chlorophyll_concentration < 0] = np.nan
#fluor.chlorophyll_concentration[fluor.chlorophyll_concentration > 7] = np.nan

fluor.chlorophyll_concentration[fluor.chlorophyll_concentration > 3] = np.nan
fluor.turbidity_units[fluor.turbidity_units > 2] = np.nan
#%%
'''Scatter plot of chlorophyll concentration and turbdity from fluor'''
fig, ax1 = plt.subplots(figsize = (15,3), sharex=True)

ax1.scatter(x = fluor.index, y = 'chlorophyll_concentration', data = fluor,  s=1.5, color='#4B8ECA')
#ax1.scatter(x = salinity.index, y = 'Temperature', data = salinity,  s=1.5)
ax1.set_title('Post Gap (2018-09-02 to 2018-12-27) Fluorometer: Chlorophyll Concentration (< 3), Turbidity (< 2)')
ax1.set_xlabel('Date')
ax1.set_ylabel('Chlorophyll Concentration (μg/L)')

ax2 = ax1.twinx()
ax2.scatter(x = fluor.index, y = 'turbidity_units', data = fluor,  s=1.5, color='#4BBC82')
ax2.set_ylabel('Turbidity (NTU)')
fig.legend(bbox_to_anchor = [0.253, 0.685])
#fig.legend(bbox_to_anchor = [0.253, 0.875])
fig.autofmt_xdate()
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_fluor_after_adj.png',bbox_inches='tight',dpi=400)
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_fluor_after_adj2.png',bbox_inches='tight',dpi=400)

#%%
'''trim temp_prof'''
temp_prof = trim_late(temp_prof, '2018-09-02 00:01:08')
#temp_prof.temperature[temp_prof.temperature > 45] = np.nan
temp_prof.temperature[temp_prof.temperature > 31] = np.nan
temp_prof.temperature[temp_prof.temperature < 17] = np.nan

#%%
'''Scatter plot of temp_prof'''

fig, ax1 = plt.subplots(figsize = (20,8))

mappable = ax1.scatter(x = temp_prof.index, y = 'temperature', data = temp_prof,  s=1.5, c='depth', cmap='cmo.thermal')
ax1.set_title('Post Gap (2018-09-02 to 2018-12-21) Water Temprature (trimmed) At Depths 5m to 85m')
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (\u2103)')
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Depth (m)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(5,90,5))
fig.autofmt_xdate()
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_temp_prof_after_trimmed.png',bbox_inches='tight',dpi=400)

#%%
'''trim humid'''
humid = trim_late(humid, '2018-09-02 09:20:31')
#%%
'''Scatter plot of humidity'''
fig, ax1 = plt.subplots(figsize = (15,3))

ax1.scatter(x = humid.index, y = 'AvgLinearAdjVal', data = humid,  s=1.5, color='#4B8ECA')
ax1.set_title('Post Gap (2018-09-02 to 2019-01-29) Humidity (Average Linear Adjusted Value)')
ax1.set_xlabel('Date')
ax1.set_ylabel('Relative Humidity (%)')
#fig.autofmt_xdate()
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_humidity_after.png',bbox_inches='tight',dpi=400)


#%%
'''Wind_vel'''
# No recordings since gap
#%%
'''trim The_ADCP'''
The_ADCP = trim_late(The_ADCP, '2018-09-02 00:07:00')
The_ADCP[The_ADCP.speed > 10] = np.nan
#The_ADCP = The_ADCP[The_ADCP['speed']<10]

#%%
'''Scatter plot of The_ADCP by speed'''

fig, ax1 = plt.subplots(figsize = (20,8))

mappable = ax1.scatter(x = The_ADCP.index, y = 'speed', data = The_ADCP,  s=1.5, c='depth', cmap='cmo.tempo')
ax1.set_title('Pre Gap (2017-07-26 to 2018-02-13) Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Current Speed (m/s)')
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Depth (m)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(5,135,10))

plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_ADCP1.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of The_ADCP by depth'''



fig, ax1 = plt.subplots(figsize = (20,8))

mappable = ax1.scatter(x = The_ADCP.index, y = 'depth', data = The_ADCP,  s=33, c='speed', cmap='cmo.tempo')
ax1.set_title('Pre Gap (2017-07-26 to 2018-02-13) Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/after_gap/scat_ADCP2.png',bbox_inches='tight',dpi=400)




