#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:52:38 2019

@author: Jacob
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



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


def quickplot(dataframe, variable, title, y_label):
    fig, ax1 = plt.subplots(figsize = (15,3))

    ax1.scatter(x = dataframe.index, y = variable, data=dataframe, s=1.5, color='#4B8ECA')
    ax1.set_title(title)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(y_label)
    fig.autofmt_xdate()
    plt.tight_layout()

#%%

quickplot(The_ADCP, 'speed', 'ADCP Speed', 'Speed (m/s)')
quickplot(The_ADCP, 'depth', 'ADCP Depth', 'Depth (m)')
quickplot(The_ADCP, 'direction', 'ADCP Direction', 'Direction (Degrees from North)')

quickplot(surf_cur, 'Abs_Speed[cm/s]','Surface Current Absolute Speed', 'Speed (cm/s)')
quickplot(surf_cur, 'Direction[DegM]','Surface Current Direction', 'Direction (Degrees)')
quickplot(surf_cur, 'East[cm/s]','Surface Current East Speed Component', 'Speed (cm/s)')
quickplot(surf_cur, 'Temperature[DegC]','Temperature from Surface Current Meter', 'Temperature (\u2103)')
quickplot(surf_cur, 'Heading[DegM]','Surface Current Heading', 'Direction (Degrees)')
quickplot(surf_cur, 'North[cm/s]','Surface Current North Speed Component', 'Speed (m/s)')
quickplot(surf_cur, 'Abs_Tilt[Deg]','Surface Current Absolute Tilt Recoding', 'Tilt (Degrees)')
quickplot(surf_cur, 'Strength[db]','Surface Current Recording Strength', 'Strength (db)')
quickplot(surf_cur, 'Abs_Speed[cm/s]','Surface Current Absolute Speed', 'Speed (m/s)')
quickplot(surf_cur, 'Max_Tilt[Deg]','Surface Current Max Tilt Recoding', 'Tilt (Degrees)')
quickplot(surf_cur, 'Std_Tilt[Deg]','Surface Current Std Tilt Recoding', 'Tilt (Degrees)')
quickplot(surf_cur, 'Tilt_Y[Deg]','Surface Current Y Tilt Recoding', 'Tilt (Degrees)')
quickplot(surf_cur, 'Tilt_X[Deg]','Surface Current X Tilt Recoding', 'Tilt (Degrees)')
quickplot(surf_cur, 'SP_Std[cm/s]','Surface Current SP_Std', 'Speed (m/s)')

quickplot(fluor, 'chlorophyll_concentration', 'Chlorophyll Concentration', 'Chlorophyll Concentration (μg/L)')
quickplot(fluor, 'turbidity_units', 'Turbidity', 'Turbidity (NTU)')

quickplot(salinity, 'Salinity', 'Salinity Timeseries', 'Salinity (PSU)')
quickplot(salinity, 'Temperature', 'Temperature from Salinity Recorder', 'Temperature (\u2103)')

#temp_prof.temperature[temp_prof.temperature > 31] = np.nan 
quickplot(temp_prof, 'temperature', 's9 Thermistor String Temperature', 'Water temperature (\u2103)')
quickplot(temp_prof, 'depth', 's9 Thermistor String Depth', 'Recording Depth (m)')

quickplot(met_pak, 'temperature', 'Air Temperature from MetPak', 'Temperature (\u2103)')
quickplot(met_pak, 'humidity', 'Humidity from MetPak', 'Humidity (%)')
quickplot(met_pak, 'dewpoint', 'Dewpoint from MetPak', 'Dewpoint Temperature (\u2103)')
quickplot(met_pak, 'wind_direction', 'Wind Direction from MetPak', 'Direction (Degrees)')
quickplot(met_pak, 'wind_speed', 'Wind Speed from MetPak', 'Wind Speed (m/s)')
quickplot(met_pak, 'pressure', 'Air Pressure from MetPak', 'Pressure (millibars)')

quickplot(wind_vel, 'north', 'Wind Velocity North Component', 'Wind Velocity(m/s)')
quickplot(wind_vel, 'east', 'Wind Velocity East Component', 'Wind Velocity(m/s)')
quickplot(wind_vel, 'magnitude_1', 'Wind Velocity Magnitude 1', 'Wind Velocity(m/s)')
quickplot(wind_vel, 'magnitude_2', 'Wind Velocity Magnitude 2', 'Wind Velocity(m/s)')
quickplot(wind_vel, 'gustdirection', 'Gust Direction', 'Direction(Degrees)')
quickplot(wind_vel, 'winddirection', 'Wind Direction', 'Direction(Degrees)')

quickplot(humid, 'external_humidity_AvgVal', 'Humidity Average Original Value', 'Recorded Value')
quickplot(humid, 'AvgVolt', 'Average Voltage from Humidity Recorder', 'Volatage')
quickplot(humid, 'AvgLinearAdjVal', 'Humidity Average linear Adjusted Value', 'Relative Humidity (%)')

quickplot(temp_air, 'external_temperature_AvgVal', 'Temperature Average Original Value', 'Recorded Value')
quickplot(temp_air, 'AvgVolt', 'Average Voltage from Humidity Recorder', 'Volatage')
quickplot(temp_air, 'AvgLinearAdjVal', 'Temperature Average linear Adjusted Value', 'Temperature (\u2103)')

quickplot(baro, 'BAROMETER', 'Air Pressure', 'Air Pressure (Millibars)')

quickplot(waves, 'dominant_period', 'Waves Dominant Period', 'Period (s)')
quickplot(waves, 'significant_height', 'Waves Significant Height', 'Height (m)')
quickplot(waves, 'mean_period', 'Waves Mean Period', 'Period (s)')










