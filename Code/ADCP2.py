#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:27:29 2019

@author: jacobarnold

Purpose
plot ADCP U and V 
"""
import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import cmocean
#%%
The_ADCP = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
                   parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
The_ADCP.rename(columns = {'depth[m]':'depth', 'direction[deg]':'direction','speed[m/s]':'speed'}, inplace=True)
#Acoustic Doppler Current Profiler Depth, Direction in degrees, Speed in m/s

The_ADCP.drop('threshold', axis=1, inplace=True)
The_ADCP.drop('const_err', axis=1, inplace=True)
The_ADCP[The_ADCP.speed > 3] = np.nan
The_ADCP.dropna(axis=0, inplace=True)
#%%

def Give_UV (dataframe, dir_col, spd_col):
    '''
    Calculate U (east) and V (north) velocity components from a dataframe containing 
    direction and speed measurements.
    
    Parameters
    ----------
    dataframe: var
        The dataframe that will be processed
        dataframe must contain the dir_col and spd_col parameters
    dir_col: str
        The column in dataframe that contains directional data
        Directional data are expected to be in degrees from north growing
        in the clockwise direction: 
               0/360
                -N-
         270-W-      -E- 90
                -S-
                180
    spd_col: str
        The column in dataframe that contains speed data
    '''
    dataframe['dir_rad'] = dataframe[dir_col]/180 * pi
    dataframe['U_Component'] = dataframe[spd_col] * (np.sin(dataframe['dir_rad']))
    dataframe['V_Component'] = dataframe[spd_col] * (np.cos(dataframe['dir_rad']))
   
#%%
Give_UV(The_ADCP, 'direction', 'speed')

#%%

fig = plt.figure(figsize=(15,4))

ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x=The_ADCP.index, y=The_ADCP.depth, c=The_ADCP.U_Component, data=The_ADCP,
                      cmap='cmo.balance', s=.7, marker='s')
ax1.set_title('ADCP U Velocity')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Date')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
fig.autofmt_xdate()
plt.tight_layout()

#%%
fig = plt.figure(figsize=(15,4))

ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x=The_ADCP.index, y=The_ADCP.depth, c=The_ADCP.V_Component, data=The_ADCP,
                      cmap='cmo.balance', s=.7, marker='s')
ax1.set_title('ADCP V Velocity')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Date')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
fig.autofmt_xdate()
plt.tight_layout()







