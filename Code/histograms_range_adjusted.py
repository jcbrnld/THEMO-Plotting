#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 20:47:56 2019

@author: jacobarnold
TABS225 THEMO Haifa data
Purpose:
    Create histograms of the data with an accpetable range.

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
plt.style.use('ggplot')
#%%
'''salinity and temperature recorder'''
fig0,axes = plt.subplots(nrows=3, ncols=1, figsize=(6,15))
fig0.suptitle('Temperature and Salinity', fontsize=20)
#fig0.subplots_adjust(top=.2)
axes[0].hist(x = 'Salinity', data = salinity, range = (38.5,40), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[0].set_ylabel('Number of Recordings')
axes[0].set_xlabel('Salinity (PSU)')
axes[1].hist(x='Conductivity', data = salinity, range = (4.5,7), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1].set_ylabel('Number of Recordings')
axes[1].set_xlabel('Conductivity (S/m)')
axes[2].hist(x = 'Temperature', data = salinity, range = (17,31), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[2].set_ylabel('Number of Recordings')
axes[2].set_xlabel('Temperature (\u00b0C)')

#plt.tight_layout()
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/s9_sal_tempV2.png',bbox_inches='tight',dpi=400)

#%%
'''Air pressure from barometer'''
plt.hist(x = 'BAROMETER', data = baro, range = (1000,1032), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
plt.title('Air Pressure Data')
plt.ylabel('Number of Recordings')
plt.xlabel('Pressure (mbar)')
plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/air_presV2.png',bbox_inches='tight',dpi=400)
#%%
'''Fluorometer'''
fig1,axes = plt.subplots(nrows=1, ncols=2, figsize=(15,8))
#plt.subplots_adjust(top=.2)
fig1.suptitle('Fluorometer Data', fontsize=20)
axes[0].hist(x='chlorophyll_concentration', data = fluor, range = (0,7), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[0].set_ylabel('Number of Recordings')
axes[0].set_xlabel('Chlorophyll Concentration (μg/L)')
axes[1].hist(x = 'turbidity_units', data = fluor, range = (0,25), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1].set_ylabel('Number of Recordings')
axes[1].set_xlabel('Turbidity (NTU)')

#plt.tight_layout()
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/fluorometerV2.png',bbox_inches='tight',dpi=400)

#%%
'''Waves'''
fig2,axes = plt.subplots(nrows=3, ncols=1, figsize=(6,15))
fig2.suptitle('Waves Data', fontsize=20)
#plt.subplots_adjust(hspace=0, top=.3)
axes[0].hist(x='significant_height', data = waves, range = (0,5.5), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[0].set_ylabel('Number of Recordings')
axes[0].set_xlabel('Waves Significant Height (m)')
axes[1].hist(x='mean_period', data = waves, range = (2,8), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1].set_ylabel('Number of Recordings')
axes[1].set_xlabel('Waves Mean Period (s)')
axes[2].hist(x='dominant_period', data = waves, range = (0,20), bins = 40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[2].set_ylabel('Number of Recordings')
axes[2].set_xlabel('Waves Dominant Period (s)')

#plt.tight_layout()
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/wavesV2.png',bbox_inches='tight',dpi=400)

#%%
'''Humidity'''
fig3,axes = plt.subplots(nrows=3, ncols=1, figsize=(6,15))
fig3.suptitle('Humidity Data', fontsize=20)
#plt.subplots_adjust(hspace=0, top=.3)
axes[0].hist(x='AvgLinearAdjVal', data = humid, range = (19,94), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[0].set_ylabel('Number of Recordings')
axes[0].set_xlabel('Humidity Average Linear Adjusted Value')
axes[1].hist(x='external_humidity_AvgVal', data = humid, range = (2128,2431), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1].set_ylabel('Number of Recordings')
axes[1].set_xlabel('Humidity Average Value')
axes[2].hist(x='AvgVolt', data = humid, range = (0,1), bins = 40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[2].set_ylabel('Number of Recordings')
axes[2].set_xlabel('Average Voltage Recording')

#plt.tight_layout()
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/humidityV2.png',bbox_inches='tight',dpi=400)

#%%
'''Air Temperature'''
fig4,axes = plt.subplots(nrows=3, ncols=1, figsize=(6,15))
fig4.suptitle('Air Temperature Data', fontsize=20)
#plt.subplots_adjust(hspace=0, top=.3)
axes[0].hist(x='AvgLinearAdjVal', data = temp_air, range = (9.5,32), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[0].set_ylabel('Number of Recordings')
axes[0].set_xlabel('Temperature Average Linear Adjusted Value (\u00b0C)')
axes[1].hist(x='external_temperature_AvgVal', data = temp_air, range = (2211,2302), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1].set_ylabel('Number of Recordings')
axes[1].set_xlabel('Temperature Average Value')
axes[2].hist(x='AvgVolt', data = temp_air, range = (0.35,0.65), bins = 40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[2].set_ylabel('Number of Recordings')
axes[2].set_xlabel('Average Voltage Recording')

#plt.tight_layout()
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/air_tempV2.png',bbox_inches='tight',dpi=400)


#%%
'''Wind Velocity'''
fig5,axes = plt.subplots(nrows=3, ncols=2, figsize=(15,20))
#plt.subplots_adjust(hspace=0, top=.12)
fig5.suptitle('Anemometer Data', fontsize=21)
axes[0,0].hist(x='magnitude_1', data=wind_vel, range = (0.037649,18.1542), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
#axes[0,0].grid(axis='y', alpha=0.7)
axes[0,0].set_ylabel('Number of Recordings')
axes[0,0].set_xlabel('Wind Velocity (m/s)')
axes[1,0].hist(x='winddirection', data=wind_vel, range = (0.030832,359.981), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1,0].set_ylabel('Number of Recordings')
axes[1,0].set_xlabel('Wind Direction (\u00b0)')
axes[0,1].hist(x='magnitude_2', data=wind_vel, range = (0.387507,21.89), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[0,1].set_ylabel('Number of Recordings')
axes[0,1].set_xlabel('Gust Velocity (m/s)')
axes[1,1].hist(x='gustdirection', data=wind_vel, range = (0.011214,359.972), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1,1].set_ylabel('Number of Recordings')
axes[1,1].set_xlabel('Wind Gust Direction (\u00b0)')
axes[2,0].hist(x='north', data=wind_vel, range = (-15.1779,11.1592), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[2,0].set_ylabel('Number of Recordings')
axes[2,0].set_xlabel('Wind North Component (m/s)')
axes[2,1].hist(x='east', data=wind_vel, range = (-17.8562,12.3392), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[2,1].set_ylabel('Number of Recordings')
axes[2,1].set_xlabel('Wind East Component (m/s)')


#plt.tight_layout()
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/wind_velocityV2.png',bbox_inches='tight',dpi=400)

#%%
'''Temperature Profiles'''
fig6,axes = plt.subplots(nrows=1, ncols=2, figsize=(15,8))
#plt.subplots_adjust(top=.2)
fig6.suptitle('Temperature Profile Data', fontsize=20)
axes[0].hist(x='temperature', data = temp_prof, range = (5,40), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[0].set_ylabel('Number of Recordings')
axes[0].set_xlabel('Temperature Profiles (5m to 85m) (\u00b0C)')
axes[1].hist(x = 'depth', data = temp_prof, range = (5,86), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1].set_ylabel('Number of Recordings')
axes[1].set_xlabel('Depth (m)')

#plt.tight_layout()
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/temp_profV2.png',bbox_inches='tight',dpi=400)

#%%
'''ADCP'''
fig7,axes = plt.subplots(nrows=3, ncols=1, figsize=(6,15))
fig7.suptitle('ADCP Data', fontsize=20)
#plt.subplots_adjust(hspace=0, top=.3)
axes[0].hist(x='speed[m/s]', data = The_ADCP, range = (0,47), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[0].set_ylabel('Number of Recordings')
axes[0].set_xlabel('Current Speed (m/s)')
axes[1].hist(x='direction[deg]', data = The_ADCP, range = (0,360), bins=40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[1].set_ylabel('Number of Recordings')
axes[1].set_xlabel('Curremt Direction (\u00b0)')
axes[2].hist(x='depth[m]', data = The_ADCP, range = (3,131), bins = 40, color='#607c8e', edgecolor='black', linewidth='1.2')
axes[2].set_ylabel('Number of Recordings')
axes[2].set_xlabel('Current Depth (m)')

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/ADCPV2.png',bbox_inches='tight',dpi=400)

#%%
'''Wind Velocity Polar Histogram'''
#ax8 = plt.subplot(111, polar=True)
#bars = ax8.bar(wind_vel.winddirection, wind_vel.magnitude_1, color='#607c8e', width=.05, edgecolor='black', linewidth='.1')
#ax8.set_theta_zero_location('N')
'''Better way'''
from matplotlib.pyplot import figure

fig8 = figure(figsize=(15,15))
ax8 = fig8.add_axes([0.1,0.1,0.8,0.8], polar=True)
ax8.bar(wind_vel.winddirection, wind_vel.magnitude_1, color='#607c8e', width=0.05, edgecolor='black', linewidth='.1')
ax8.set_theta_zero_location('N')
ax8.set_title('Wind Velocity (m/s)')
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/wind_velocity1_polarV1.png',bbox_inches='tight',dpi=400)

#%%
fig8 = figure(figsize=(15,15))
ax8 = fig8.add_axes([0.1,0.1,0.8,0.8], polar=True)
ax8.bar(wind_vel.gustdirection, wind_vel.magnitude_2, color='#607c8e', width=0.05, edgecolor='black', linewidth='.1')
ax8.set_theta_zero_location('N')
ax8.set_title('Wind Gust Velocity (m/s)')
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Histograms/wind_velocity2_polarV1.png',bbox_inches='tight',dpi=400)


#%%

#%%

fig8 = figure(figsize=(15,15))
ax8 = fig8.add_axes([0.1,0.1,0.8,0.8], polar=True)
ax8.bar(wind_vel.winddirection, wind_vel.magnitude_1, color='#607c8e', width=0.05, edgecolor='black', linewidth='.1')
ax8.set_theta_zero_location('N')



















