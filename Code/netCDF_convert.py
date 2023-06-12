#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:49:16 2019

@author: jacobarnold

Purpose:
Convert ADCP data into netCDF file
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import netCDF4
from netCDF4 import Dataset

#%%

dataset = Dataset('Documents/Classes/THEMO/TABS225m09/Data/test2.nc', 'w', format='NETCDF4_CLASSIC')

#%%

# Create dimensions
dataset.createDimension('depth', 43)
dataset.createDimension('time', 32352)
#dataset.createDimension('direction', 1168381)

# Create variables
times = dataset.createVariable('time', np.float64, ('time'))
depths = dataset.createVariable('depth', np.float64, ('depth'))
direction = dataset.createVariable('direction', np.float64, ('time'))
speed = dataset.createVariable('speed', np.float64, ('time', 'depth'))
velocity_u = dataset.createVariable('velocity_u', np.float64, ('time, depth'))
velocity_v = dataset.createVariable('velocity_v', np.float64, ('time, depth'))


#%%
'''
Descriptive properties of the netCDF file
'''
dataset.description = 'ADCP data from THEMO HAIFA project. (Update description after conversion is complete)'
dataset.history = 'Created [insert time of completion] with data from [insert data start times]. Gaps have occurred at [insert gap periods]'

dataset.source = '[insert website address]'

depths.units = 'meters' 
times.units = 'minutes since 0001-01-01 00:00:00'
times.calendar = 'gregorian'
direction.units = 'degrees from north'
speed.units = 'm/s'
velocity_u.units = 'm/s'
velocity_v.units = 'm/s'

#%%
# Let's get some data

#dates_original = np.loadtxt(
#            'Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
#            usecols=(0,),
#            skiprows=1,
#            dtype = object,
#            converters={0: lambda x: datetime.strptime(x.decode("ascii"), "%Y-%m-%d")},
#            delimiter=',',
#            unpack=True)


date_index = pd.date_range(start='2017-07-25 14:07:00', end='2019-05-30 13:37:00', periods=32352)

ADCP_2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D_F.csv',
                   index_col=0)
ADCP_U2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcpU2D_F.csv',
                   index_col=0)
ADCP_V2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcpV2D_F.csv',
                   index_col=0)

date_index = pd.to_datetime(date_index)

#ADCPspeed = The_ADCP.speed.as_matrix()
#ADCPdepth = The_ADCP.depth.as_matrix()
#ADCPdepth = np.array(ADCPdepth, dtype='float64')
#ADCPdirection = The_ADCP.direction.as_matrix()
#dates = The_ADCP.date.as_matrix()

#%%

times[:] = netCDF4.date2num(date_index, units=times.units, calendar = times.calendar)
depths[:] = ADCPdepth
direction[:] = ADCPdirection
speed[:] = adcp2D_F
velocity_u[:] = adcpU2D_F
velocity_v[:] = adcpV2D_F







