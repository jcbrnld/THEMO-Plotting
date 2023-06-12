#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 04:56:22 2019

@author: jacobarnold

Purpose:
    Plot ADCP data in better ways. 
    Formerly just used scatter but will now attempt other methods to avoid horizontal overlapping.
    
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cmocean

The_ADCP = pd.read_csv('Documents/Classes/OCNG491/THEMO/Data_tabs225/ALL_17_07_26-new/adcp.csv',
                  parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
The_ADCP.rename(columns = {'depth[m]':'depth', 'direction[deg]':'direction','speed[m/s]':'speed'}, inplace=True)
#Acoustic Doppler Current Profiler Depth, Direction in degrees, Speed in m/s



plt.style.use('seaborn-deep')
#plt.style.use('ggplot')

#%%

'''Plotting the data of various sizes'''
# Trim outside values
The_ADCP[The_ADCP.speed > 3] = np.nan

# Create dataframe for before the gap
The_ADCP_Before_Gap = The_ADCP[:'2018-02-13 06:07:00'] 

# Create dataframe for after the gap
The_ADCP_After_Gap = The_ADCP['2018-09-02 00:07:00':]

The_ADCP_janfebmar_19 = The_ADCP['2019-01-01':'2019-03-31']

The_ADCP_after19gap = The_ADCP['2019-02-19':]


#%%
import datetime as dt
import matplotlib.dates as dates
import numpy.ma as ma


time = dates.date2num(The_ADCP.index)
deep = The_ADCP.depth
speed = The_ADCP.speed

dep = ma.masked_where(np.isnan(deep),deep)
Zm = ma.masked_where(np.isnan(speed),speed)
#%%

fig = plt.figure(figsize = (15,6))

ax1 = fig.add_subplot(111)
ax1.pcolormesh(time, dep, Zm, cmap='cmo.tempo')





#%%
fig = plt.figure(figsize=(15,6))
ax1 = fig.add_subplot(111)
ax1.contourf([time, The_ADCP.depth], The_ADCP.speed)