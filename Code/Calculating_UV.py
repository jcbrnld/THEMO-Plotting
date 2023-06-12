#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:08:58 2019

@author: jacobarnold

Purpose:
Calculate U and V componenets velocity components of data

"""
import numpy as np
import pandas as pd
from math import pi
#%%
The_ADCP = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
                   parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
The_ADCP.rename(columns = {'depth[m]':'depth', 'direction[deg]':'direction','speed[m/s]':'speed'}, inplace=True)
#Acoustic Doppler Current Profiler Depth, Direction in degrees, Speed in m/s

The_ADCP.drop('threshold', axis=1, inplace=True)
The_ADCP.drop('const_err', axis=1, inplace=True)

#%%

def Give_UV (dataframe, dir_col, spd_col):
    '''
    Calculate U (east) and V (north) velocity components from a dataframe containing 
    direction and speed measurements.
    Direction is expected to be in degrees as this function converts 
    direction to radians. 
    '''
    dataframe['dir_rad'] = dataframe[dir_col]/180 * pi
    dataframe['U_Component'] = dataframe[spd_col] * (np.sin(dataframe['dir_rad']))
    dataframe['V_Component'] = dataframe[spd_col] * (np.cos(dataframe['dir_rad']))
   
#%%
Give_UV(The_ADCP, 'direction', 'speed')

#%%
The_ADCP.to_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp_uv.csv')

