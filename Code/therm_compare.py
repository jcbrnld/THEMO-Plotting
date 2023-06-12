#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:31:33 2019

@author: jacobarnold

Purpose:
    Compare temperature data from TABS225m09
    
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cmocean

#%%

therm =  pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/s9.csv', 
                        parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Temperature recorded at different depths beginning at 5m and ending at 85m (degrees celcius)

salinity = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/microcat.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Salinity (PSU), conductivity(S/m), and temperature(degrees celcius) recorded at 1m 

#%%
prof_wint_17 = therm['2017-11':'2018-01']
prof_wint_18 = therm['2018-11':'2019-01']


surf_wint_17 = salinity['2017-11':'2018-01']
surf_wint_18 = salinity['2018-11':'2019-01']



#%%
'''Trim therm'''
therm.temperature[therm.temperature > 31] = np.nan
therm.temperature[therm.temperature < 17] = np.nan

prof_wint_17.temperature[prof_wint_17.temperature > 26] = np.nan
prof_wint_17.temperature[prof_wint_17.temperature < 17] = np.nan
prof_wint_18.temperature[prof_wint_18.temperature > 26] = np.nan
prof_wint_18.temperature[prof_wint_18.temperature < 17] = np.nan

salinity.Temperature[salinity.Temperature > 31] = np.nan
surf_wint_17.Temperature[surf_wint_17.Temperature > 31] = np.nan
surf_wint_18.Temperature[surf_wint_18.Temperature > 31] = np.nan


#%%
'''compare surface temperature from salinity to therm for winter(ish) months'''

fig = plt.figure(figsize =  (20,14))

ax1 = fig.add_subplot(3,2,1)
mappable = ax1.scatter(x = therm.index, y = 'temperature',
                       data = therm,  s=10, c='depth',
                       cmap='cmo.thermal', edgecolor='white', linewidths=.05)
ax1.set_title('Water Temprature At Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (\u2103)')
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Depth (m)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(5,90,5))
cbar.ax.tick_params(labelsize=6)
ax1.tick_params(axis='both', which='major', labelsize=6)
plt.xticks(rotation=35, ha='right');
ax7 = ax1.twinx()
ax7.scatter(x=therm.index, y='depth', data=therm, s=.1, c='#4BBC82', alpha=.02)
ax7.set_ylabel('Recording Depth')
ax7.tick_params(axis='both', which='major', labelsize=6)
ax7.invert_yaxis()

ax2 = fig.add_subplot(3,2,2)
ax2.scatter(x = salinity.index, y = 'Temperature', data = salinity, s=3, c='#4B8ECA')
ax2.set_title('Surface Temperature')
ax2.set_xlabel('Date')
ax2.set_ylabel('Temperature (\u2103)')
ax2.tick_params(axis='both', which='major', labelsize=6)
plt.xticks(rotation=35, ha='right');

ax3 = fig.add_subplot(3,2,3)
mappable = ax3.scatter(x = prof_wint_17.index, y = 'temperature',
                       data = prof_wint_17,  s=10, c='depth',
                       cmap='cmo.thermal', edgecolor='white', linewidths=.05)
ax3.set_title('Water Temprature At Depths Fall-Winter 2017')
ax3.set_xlabel('Date')
ax3.set_ylabel('Temperature (\u2103)')
cbar = plt.colorbar(mappable=mappable, ax=ax3)
cbar.set_label('Depth (m)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(5,90,5))
cbar.ax.tick_params(labelsize=6)
ax3.tick_params(axis='both', which='major', labelsize=6)
plt.xticks(rotation=35, ha='right');
ax8 = ax3.twinx()
ax8.scatter(x=prof_wint_17.index, y='depth', data=prof_wint_17, s=.1, c='#4BBC82', alpha=.1)
ax8.set_ylabel('Recording Depth')
ax8.tick_params(axis='both', which='major', labelsize=6)
ax8.invert_yaxis()

ax4 = fig.add_subplot(3,2,4)
ax4.scatter(x = surf_wint_17.index, y = 'Temperature', data = surf_wint_17, s=3, c='#4B8ECA')
ax4.set_title('Surface Temperature Fall-Winter 2017')
ax4.set_xlabel('Date')
ax4.set_ylabel('Temperature (\u2103)')
ax4.tick_params(axis='both', which='major', labelsize=6)
plt.xticks(rotation=35, ha='right');

ax5 = fig.add_subplot(3,2,5)
mappable = ax5.scatter(x = prof_wint_18.index, y = 'temperature',
                       data = prof_wint_18,  s=10, c='depth',
                       cmap='cmo.thermal', edgecolor='white', linewidths=.05)
ax5.set_title('Water Temprature At Depths Fall-Winter 2018')
ax5.set_xlabel('Date')
ax5.set_ylabel('Temperature (\u2103)')
cbar = plt.colorbar(mappable=mappable, ax=ax5)
cbar.set_label('Depth (m)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(5,90,5))
cbar.ax.tick_params(labelsize=6)
ax5.tick_params(axis='both', which='major', labelsize=6)
plt.xticks(rotation=35, ha='right');
ax9 = ax5.twinx()
ax9.scatter(x=prof_wint_18.index, y='depth', data=prof_wint_18, s=.1, c='#4BBC82', alpha=.2)
ax9.set_ylabel('Recording Depth')
ax9.tick_params(axis='both', which='major', labelsize=6)
ax9.invert_yaxis()

ax6 = fig.add_subplot(3,2,6)
ax6.scatter(x = surf_wint_18.index, y = 'Temperature', data = surf_wint_18, s=3, c='#4B8ECA')
ax6.set_title('Surface Temperature Fall-Winter 2018')
ax6.set_xlabel('Date')
ax6.set_ylabel('Temperature (\u2103)')
ax6.tick_params(axis='both', which='major', labelsize=6)

plt.xticks(rotation=35, ha='right');

#fig.autofmt_xdate()
plt.tight_layout()
