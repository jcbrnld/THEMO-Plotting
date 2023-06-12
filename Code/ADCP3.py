#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:17:38 2019

@author: jacobarnold

Purpose:
Plot ADCP data using pcolormesh

"""

import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import cmocean
#%%
The_ADCP = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
                   parse_dates=[[0,1]], infer_datetime_format = True)
The_ADCP.rename(columns = {'d_stamp_t_stamp':'date','depth[m]':'depth', 'direction[deg]':'direction','speed[m/s]':'speed'}, inplace=True)
#Acoustic Doppler Current Profiler Depth, Direction in degrees, Speed in m/s

The_ADCP.drop('threshold', axis=1, inplace=True)
The_ADCP.drop('const_err', axis=1, inplace=True)
The_ADCP[The_ADCP.speed > 3] = np.nan
The_ADCP.dropna(axis=0, inplace=True)



#%%
fig = plt.figure(figsize=(10,4))
ax1 = fig.add_subplot(111)
m1 = ax1.pcolormesh(The_ADCP.index, The_ADCP.depth, The_ADCP.U_Component, cmap='cmo.balance')
cbar=plt.colorbar(m1, ax=ax1)

#%%
from datetime import datetime
The_ADCP = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
                   parse_dates=[[0,1]], infer_datetime_format = True)

ADCP = np.loadtxt('Documents/Classes/THEMO/TABS225m09/Data/adcp.csv', delimiter=',',usecols=(2,3,4), skiprows=1)
dates = np.loadtxt(
            'Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
            usecols=(0,),
            skiprows=1,
            dtype = object,
            converters={0: lambda x: datetime.strptime(x.decode("ascii"), "%Y-%m-%d")},
            delimiter=',',
            unpack=True)

#.decode("utf-8") ASCII
#%%
'''
isolate variables as float64 types
'''
# this works but .values may have to be used in the future instead of .asmatrix
ADCPspeed = The_ADCP.speed
adcpspeed = ADCPspeed.as_matrix()

ADCPdepth = The_ADCP.depth
adcpdepth = ADCPdepth.as_matrix()


ds = np.vstack((adcpspeed, adcpdepth)).T
