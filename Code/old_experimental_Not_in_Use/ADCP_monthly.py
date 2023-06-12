#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:38:53 2019

@author: Jacob

Purpose:
    Create montly time series of the ADCP data from the beginning 
    of recording (2017-07-26 00:07:00) to present.
"""
import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import cmocean
#%%
The_ADCP = pd.read_csv('~/Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
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
    Direction is expected to be in degrees as this function converts 
    direction to radians. 
    '''
    dataframe['dir_rad'] = dataframe[dir_col]/180 * pi
    dataframe['V_Component'] = dataframe[spd_col] * (np.sin(dataframe['dir_rad']))
    dataframe['U_Component'] = dataframe[spd_col] * (np.cos(dataframe['dir_rad']))
   
#%%
Give_UV(The_ADCP, 'direction', 'speed')

#%%

def ADCP_month_U(inter_start, inter_end, yr_mnth):
    '''
    To plot each month the The_ADCP data U velocity component magnitude
    inter_start is the first day of the month
    inter_end is the last day of the month
    yr-month is to set the appropriate month in the title and save in the correct folder
    '''
    fig = plt.figure(figsize=(20,3.5))

    ax1 = fig.add_subplot(111)
    mappable = ax1.scatter(x = The_ADCP[inter_start:inter_end].index,
                           y = The_ADCP[inter_start:inter_end].depth, 
                           data = The_ADCP[inter_start:inter_end],s=3.5, 
                       c='U_Component', cmap='cmo.balance', marker='s')
    ax1.set_title('U Current Velocity at Depths ' + '('+yr_mnth+')')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Depth (m)')
    ax1.invert_yaxis()
    cbar = plt.colorbar(mappable=mappable, ax=ax1)
    cbar.set_label('Speed (m/s)')

    fig.autofmt_xdate()
    plt.tight_layout()    
    
    plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/Monthly_Timeseries/'+yr_mnth+'/ADCP_U.png',
                bbox_inches='tight', dpi=400)

#%%
    
def ADCP_month_V(inter_start, inter_end, yr_mnth):
    '''
    To plot each month the The_ADCP data V velocity component magnitude
    inter_start is the first day of the month
    inter_end is the last day of the month
    yr-month is to set the appropriate month in the title and save in the correct folder
    '''
    fig = plt.figure(figsize=(20,3.5))

    ax1 = fig.add_subplot(111)
    mappable = ax1.scatter(x = The_ADCP[inter_start:inter_end].index,
                           y = The_ADCP[inter_start:inter_end].depth, 
                           data = The_ADCP[inter_start:inter_end],s=3.5, 
                       c='V_Component', cmap='cmo.balance', marker='s')
    ax1.set_title('V Current Velocity at Depths ' + '('+yr_mnth+')')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Depth (m)')
    ax1.invert_yaxis()
    cbar = plt.colorbar(mappable=mappable, ax=ax1)
    cbar.set_label('Speed (m/s)')

    fig.autofmt_xdate()
    plt.tight_layout()    
    
    plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/Monthly_Timeseries/'+yr_mnth+'/ADCP_V.png',
                bbox_inches='tight', dpi=400)


#%%
    
def ADCP_mag_month(inter_start, inter_end, yr_mnth):
    '''
    To plot each month the The_ADCP data speed
    inter_start is the first day of the month
    inter_end is the last day of the month
    yr-month is to set the appropriate month in the title and save in the correct folder 
    '''
    fig = plt.figure(figsize=(20,3.5))

    ax1 = fig.add_subplot(111)
    mappable = ax1.scatter(x = The_ADCP[inter_start:inter_end].index,
                           y = The_ADCP[inter_start:inter_end].depth, 
                           data = The_ADCP[inter_start:inter_end],s=4, 
                       c='speed', cmap='cmo.tempo', marker='s')
    ax1.set_title('Current speed at Depths ' + '('+yr_mnth+')')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Depth (m)')
    ax1.invert_yaxis()
    cbar = plt.colorbar(mappable=mappable, ax=ax1)
    cbar.set_label('Speed (m/s)')
   # cbar.ax.invert_yaxis()
  #  cbar.set_ticks(np.arange(0,1.62,0.2))
    fig.autofmt_xdate()
    plt.tight_layout()    
    
    plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/Monthly_Timeseries/'+yr_mnth+'/ADCP_spd.png',
                bbox_inches='tight', dpi=400)
    

    
#%% 
'''
2017
'''

ADCP_month_U('2017-07-24','2017-07-31', '2017-07')    
ADCP_month_V('2017-07-24','2017-07-31', '2017-07')
ADCP_mag_month('2017-07-24','2017-07-31', '2017-07')

ADCP_month_U('2017-08-01','2017-08-31', '2017-08')
ADCP_month_V('2017-08-01','2017-08-31', '2017-08')
ADCP_mag_month('2017-08-01','2017-08-31', '2017-08')
    
ADCP_month_U('2017-09-01','2017-09-30', '2017-09')  
ADCP_month_V('2017-09-01','2017-09-30', '2017-09') 
ADCP_mag_month('2017-09-01','2017-09-30', '2017-09') 

ADCP_month_U('2017-10-01','2017-10-31', '2017-10')
ADCP_month_V('2017-10-01','2017-10-31', '2017-10')
ADCP_mag_month('2017-10-01','2017-10-31', '2017-10')

ADCP_month_U('2017-11-01','2017-11-30', '2017-11')
ADCP_month_V('2017-11-01','2017-11-30', '2017-11')
ADCP_mag_month('2017-11-01','2017-11-30', '2017-11')

ADCP_month_U('2017-12-01','2017-12-31', '2017-12')
ADCP_month_V('2017-12-01','2017-12-31', '2017-12')
ADCP_mag_month('2017-12-01','2017-12-31', '2017-12')

#%%
'''
2018
'''
ADCP_month_U('2018-01-01','2018-01-31', '2018-01')
ADCP_month_V('2018-01-01','2018-01-31', '2018-01')
ADCP_mag_month('2018-01-01','2018-01-31', '2018-01')

ADCP_month_U('2018-02-01','2018-02-28', '2018-02')
ADCP_month_V('2018-02-01','2018-02-28', '2018-02')
ADCP_mag_month('2018-02-01','2018-02-28', '2018-02')

ADCP_month_U('2018-03-01','2018-03-31', '2018-03')
ADCP_month_V('2018-03-01','2018-03-31', '2018-03')
ADCP_mag_month('2018-03-01','2018-03-31', '2018-03')

ADCP_month_U('2018-05-01','2018-05-31', '2018-05')
ADCP_month_V('2018-05-01','2018-05-31', '2018-05')
ADCP_mag_month('2018-05-01','2018-05-31', '2018-05')

ADCP_month_U('2018-06-01','2018-06-30', '2018-06')
ADCP_month_V('2018-06-01','2018-06-30', '2018-06')
ADCP_mag_month('2018-06-01','2018-06-30', '2018-06')

ADCP_month_U('2018-09-01','2018-09-30', '2018-09')
ADCP_month_V('2018-09-01','2018-09-30', '2018-09')
ADCP_mag_month('2018-09-01','2018-09-30', '2018-09')

ADCP_month_U('2018-10-01','2018-10-31', '2018-10')
ADCP_month_V('2018-10-01','2018-10-31', '2018-10')
ADCP_mag_month('2018-10-01','2018-10-31', '2018-10')

ADCP_month_U('2018-11-01','2018-11-30', '2018-11')
ADCP_month_V('2018-11-01','2018-11-30', '2018-11')
ADCP_mag_month('2018-11-01','2018-11-30', '2018-11')

ADCP_month_U('2018-12-01','2018-12-31', '2018-12')
ADCP_month_V('2018-12-01','2018-12-31', '2018-12')
ADCP_mag_month('2018-12-01','2018-12-31', '2018-12')

#%%
'''
2019
'''
ADCP_month_U('2019-01-01','2019-01-31','2019-01')
ADCP_month_V('2019-01-01','2019-01-31','2019-01')
ADCP_mag_month('2019-01-01','2019-01-31','2019-01')

ADCP_month_U('2019-02-01','2019-02-28','2019-02')
ADCP_month_V('2019-02-01','2019-02-28','2019-02')
ADCP_mag_month('2019-02-01','2019-02-28','2019-02')

ADCP_month_U('2019-03-01','2019-03-31','2019-03')
ADCP_month_V('2019-03-01','2019-03-31','2019-03')
ADCP_mag_month('2019-03-01','2019-03-31','2019-03')

ADCP_month_U('2019-04-01','2019-04-30','2019-04')
ADCP_month_V('2019-04-01','2019-04-30','2019-04')
ADCP_mag_month('2019-04-01','2019-04-30','2019-04')

ADCP_month_U('2019-05-01','2019-05-31','2019-05')
ADCP_month_V('2019-05-01','2019-05-31','2019-05')
ADCP_mag_month('2019-05-01','2019-05-31','2019-05')



    