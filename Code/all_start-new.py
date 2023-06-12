#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:21:14 2019

@author: Jacob
TABS 225 THEMO Haifa Data

Purpose:
    Create histograms of the raw data with range defined by minimum and maximum reported 
    values to help identify gaps and errors in the data

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

therm = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/s9.csv', 
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
'''clean salinity'''
salinity.Salinity[salinity.Salinity < 38] = np.nan
salinity.Conductivity[salinity.Conductivity < 4] = np.nan

#%%
'''clean waves domimant period'''
waves.dominant_period[waves.dominant_period > 13] = np.nan

#%%

'''Scatter plot of salinity'''
plt.figure(figsize = (15,3))
plt.scatter(x = salinity.index, y = 'Salinity', data = salinity, s=1.5)
plt.title('Salinity <20 Filtered')
#plt.title('Salinity Unfiltered')
plt.xlabel('Date')
plt.ylabel('Salinity (PSU)')
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/blue_white/scat_salinity_<20_filtered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of temp from salinity'''
plt.figure(figsize = (15,3))
plt.scatter(x = salinity.index, y = 'Temperature', data = salinity, s=1.5)
plt.title('TABS225 Unfiltered Surface Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (\u2103)')
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/blue_white/scat_temp_froms9_unfiltered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of waves height'''
plt.figure(figsize = (15,3))
plt.scatter(x = waves.index, y = 'significant_height', data = waves, s=1.5)
plt.title('TABS225 Unfiltered Waves Significant Height')
plt.xlabel('Date')
plt.ylabel('Wave Height (m)')
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/blue_white/scat_waves_sight_unfiltered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of waves mean period'''
plt.figure(figsize = (15,3))
plt.scatter(x = waves.index, y = 'mean_period', data = waves, s=1.5)
plt.title('TABS225 Unfiltered Waves Mean Period')
plt.xlabel('Date')
plt.ylabel('Wave Period (s)')
#fig.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/blue_white/scat_waves_mean_period_unfiltered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of waves dominant period'''
plt.figure(figsize = (15,3))
plt.scatter(x = waves.index, y = 'dominant_period', data = waves, s=1.5)
#plt.title('TABS225 Unfiltered Waves Dominant Period')
plt.title('TABS225 Waves Dominant Period >30 Filtered')
plt.xlabel('Date')
plt.ylabel('Wave Period (s)')
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/blue_white/scat_waves_dom_period_>30_filtered.png',bbox_inches='tight',dpi=400)

#%%
'''Scatter plot of fluorometer'''
plt.figure(figsize = (15,3))
plt.scatter(x = flour.index, y ='chlorophyll_concentration', data = flour, s=1.5)
plt.scatter(x = flour.index, y ='turbidity_units', data = flour, s=1.5)
plt.title('TABS225 Unfiltered Fluorometer')
plt.legend()
plt.xlabel('Date')

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/blue_white/fluorometer.png',bbox_inches='tight',dpi=400)


#%%
print(therm.temperature.mean())
print(therm.temperature.mode())
print(therm.temperature.std())
#%%
'''Trim therm'''
therm.temperature[therm.temperature > 31] = np.nan
therm.temperature[therm.temperature < 13] = np.nan

#%%
'''Scatter plot of therm string'''
fig, ax1 = plt.subplots(figsize = (15,3))
ax1.scatter(x = therm.index, y = 'temperature', data = therm, s=20)
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (\u2103)')

ax2 = ax1.twinx()
ax2.scatter(x = therm.index, y = 'depth', data = therm, s=1.5, c = 'green', alpha = .1)
ax2.set_ylabel('Depth (m)')

plt.tight_layout()
plt.show()



#%%

'''Scatter plot of therm'''

fig, ax1 = plt.subplots(figsize = (12,4))
#mappable = ax1.scatter(x = temp_prof.index, y = 'temperature', data = temp_prof,  s=10, c='depth', cmap='cmo.thermal')
mappable = ax1.scatter(x = therm.index, y = 'temperature', data = therm,  s=10, c='depth', cmap='cmo.thermal', edgecolor='white', linewidths=.05)
ax1.set_title('Water Temprature At Depths 5m to 85m')
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (\u2103)')
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Depth (m)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(5,90,5))
plt.tight_layout()

#%%
prof_dec_17 = therm['2017-12']
prof_dec_18 = therm['2018-12']
#%%
'''Scatter plot of temp_prof for december months'''

def compare_two_therms(data1, data2, cmap):

    fig = plt.figure(figsize = (12,10))

    ax1 = fig.add_subplot(2,1,1)
    mappable = ax1.scatter(x = data1.index, y = 'temperature', data = data1,  s=10, c='depth', cmap=cmap, edgecolor='white', linewidths=.05)
    ax1.set_title('Water Temprature At Depths 5m to 85m')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Temperature (\u2103)')
    cbar = plt.colorbar(mappable=mappable, ax=ax1)
    cbar.set_label('Depth (m)')
    cbar.ax.invert_yaxis()
    cbar.set_ticks(np.arange(5,90,5))

    ax2 = fig.add_subplot(2,1,2)
    mappable = ax2.scatter(x = data2.index, y = 'temperature', data = data2,  s=10, c='depth', cmap=cmap, edgecolor='white', linewidths=.05)
    ax2.set_title('Water Temprature At Depths 5m to 85m')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Temperature (\u2103)')
    cbar = plt.colorbar(mappable=mappable, ax=ax2)
    cbar.set_label('Depth (m)')
    cbar.ax.invert_yaxis()
    cbar.set_ticks(np.arange(5,90,5))
    fig.autofmt_xdate()
    plt.tight_layout()


#%%
    
compare_two_therms(prof_dec_17, prof_dec_18, 'cmo.thermal')

#%%
prof_wint_17 = temp_prof['2017-11':'2018-02']
prof_wint_18 = temp_prof['2018-11':'2019-02']
#%%

compare_two_therms(prof_wint_17, prof_wint_18, 'cmo.thermal')

#%%
prof_short_17 = therm['2017-12-05':'2017-12-20']
prof_short_18 = therm['2018-12-05':'2018-12-20']

#%%
prof_short_17.temperature[prof_short_17.temperature > 23] = np.nan
prof_short_17.temperature[prof_short_17.temperature < 20] = np.nan
prof_short_18.temperature[prof_short_18.temperature > 23] = np.nan
prof_short_18.temperature[prof_short_18.temperature < 20] = np.nan
#%%

compare_two_therms(prof_short_17, prof_short_18, 'cmo.thermal')


#%%
surf_wint_17 = salinity['2017-11':'2018-02']
surf_wint_18 = salinity['2018-11':'2019-02']

#%%
'''compare surface temperature from salinity to therm for winter(ish) months'''

fig = plt.figure(figsize =  (20,14))

ax1 = fig.add_subplot(3,2,1)
mappable = ax1.scatter(x = therm.index, y = 'temperature',
                       data = therm,  s=10, c='depth',
                       cmap='cmo.thermal', edgecolor='white', linewidths=.05)
ax1.set_title('Water Temprature At Depths 5m to 85m')
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
mappable = ax3.scatter(x = prof_wint_17.index, y = 'temperature', data = prof_wint_17,  s=10, c='depth', cmap='cmo.thermal', edgecolor='white', linewidths=.05)
ax3.set_title('Water Temprature At Depths 5m to 85m Fall-Winter 2017')
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
mappable = ax5.scatter(x = prof_wint_18.index, y = 'temperature', data = prof_wint_18,  s=10, c='depth', cmap='cmo.thermal', edgecolor='white', linewidths=.05)
ax5.set_title('Water Temprature At Depths 5m to 85m Fall-Winter 2018')
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

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/comparing_temps_depth.png', bbox_inches='tight', dpi=400)

#%%
# Need to find a way to make The_ADCP the same size as salinity in order to corrolate
#The_ADCP.groupby(The_ADCP['hour'])



np.corrcoef(The_ADCP.speed, salinity.Salinity)




