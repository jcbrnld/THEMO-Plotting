#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:22:32 2019

@author: jacobarnold

Purpose:
    view adcp data on small (daily to weekly) scales
    
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cmocean
import matplotlib.dates as mdates
from matplotlib import ticker

#%%

adcp2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D_F.csv', 
                       index_col=0)
adcpU2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcpU2D_F.csv', 
                       index_col=0)
adcpV2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcpV2D_F.csv', 
                       index_col=0)

# Create the new date index with no missing values
date_index = pd.date_range(start='2017-07-25 14:07:00', end='2019-05-30 13:37:00', periods=32352)

adcp2D_temp2 = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D.csv',
                     infer_datetime_format=True,
                     index_col=0
                     )
bin_depths = adcp2D_temp2.loc['depth',:]


#%%

#lim_spd = float('%2.2f' % np.nanpercentile(adcp2D,99))

def adcp_short_spd(inter_start, inter_end, interval):
    '''
    Create plot of ADCP speed data
    This is intended for speed magnitude data only, not for velocity components
    
    Parameters
    ----------
    inter_start: date-time yyyy-mm-dd hh-mm-ss format
        The start of the interval that will be plotted 
        
    inter_end:  date-time yyyy-mm-dd hh-mm-ss format
        The end of the interval that will be plotted 
        
    yr_mnth: int or str
        Specifies which month and year are being plotted. 
        This will appear in the title and defines the directory in which 
        the plot will be saved 
    '''
    start_T = np.flatnonzero(date_index==inter_start)[0] 
    end_T = np.flatnonzero(date_index==inter_end)[0] + 1
    time_loc = date_index[start_T:end_T]
    data_loc = adcp2D_F.T[inter_start:inter_end].T
    fig = plt.figure(figsize=(10,4))
    ax1 = fig.add_subplot(111)
# For contourf
    m1 = ax1.contourf(time_loc, bin_depths, data_loc, levels=30, cmap='cmo.thermal', vmin=-0, vmax=1)
# For pcolormesh
#    m1 = ax1.pcolormesh(time_loc, bin_depths, data_loc, cmap='cmo.thermal', vmin=-0, vmax=1)
    ax1.invert_yaxis()
    ax1.set_title('Current Speed ' + '('+interval+')')
    ax1.set_ylabel('Depth (m)')
    ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(10))
    ax1.tick_params(axis='x', which='major', labelsize=7)
    ax1.tick_params(axis='y', which='major', labelsize=9)
    fig.autofmt_xdate()
    cbar=plt.colorbar(m1, ax=ax1)
    cbar.set_label('Speed (m/s)')
    cbar.ax.tick_params(labelsize=9)
    cbar.locator = ticker.MaxNLocator(nbins=11)
    cbar.update_ticks()
    plt.tight_layout()



#%%

#lim_U = float('%2.2f' % np.nanpercentile(adcpU2D,99))
#lim_V = float('%2.2f' % np.nanpercentile(adcpV2D,99))
#u_v = max([lim_U, lim_V])
    
def adcp_short_uv(inter_start, inter_end, interval):
    '''
    Create subplots of U and V velocity components of ADCP data 
    
    Parameters
    ----------
    inter_start: date-time yyyy-mm-dd hh-mm-ss format
        The start of the interval that will be plotted
        
    inter_end:  date-time yyyy-mm-dd hh-mm-ss format
        The end of the interval that will be plotted
        
    yr_mnth: int or str
        Specifies which month and year are being plotted
        This will appear in the title and defines the directory in which 
        the plot will be saved
    '''
    start_T = np.flatnonzero(date_index==inter_start)[0] 
    end_T = np.flatnonzero(date_index==inter_end)[0] + 1
    time_loc = date_index[start_T:end_T]
    dataU_loc = adcpU2D_F.T[inter_start:inter_end].T
    fig, axes = plt.subplots(2, sharex=True)
    fig.set_size_inches(12,6)

# For contourf
    m1 = axes[0].contourf(time_loc, bin_depths, dataU_loc, levels=30, cmap='cmo.balance', vmin=-1, vmax=1)
# For pcolormesh
#    m1 = axes[0].pcolormesh(time_loc, bin_depths, dataU_loc, cmap='cmo.balance', vmin=-1, vmax=1)
    axes[0].invert_yaxis()
    axes[0].set_title('U Current Velocity ' + '('+interval+')')
    axes[0].set_ylabel('Depth (m)')
    axes[0].yaxis.set_major_locator(plt.MaxNLocator(10))
 #   axes[0].xaxis.set_major_locator(plt.MaxNLocator(24))
    plt.xticks(time_loc.tolist(),time_loc.tolist())
    axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    axes[0].tick_params(axis='x', which='major', labelsize=7)
    axes[0].tick_params(axis='y', which='major', labelsize=9)
    fig.autofmt_xdate()
    
    dataV_loc = adcpV2D_F.T[inter_start:inter_end].T
# For contourf
    m2 = axes[1].contourf(time_loc, bin_depths, dataV_loc, levels=30, cmap='cmo.balance', vmin=-1, vmax=1)
# For pcolormesh
 #   m2 = axes[1].pcolormesh(time_loc, bin_depths, dataV_loc, cmap='cmo.balance', vmin=-1, vmax=1)
    axes[1].invert_yaxis()
    axes[1].set_title('V Current Velocity ' + '('+interval+')')
    axes[1].set_ylabel('Depth (m)')
    axes[1].yaxis.set_major_locator(plt.MaxNLocator(10))
    axes[1].xaxis.set_major_locator(plt.MaxNLocator(24))
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    axes[1].tick_params(axis='x', which='major', labelsize=7)
    axes[1].tick_params(axis='y', which='major', labelsize=9)
    fig.autofmt_xdate()
    plt.tight_layout()
    cbar = fig.colorbar(m1, ax=axes.ravel().tolist(), label='Speed m/s')  
    cbar.ax.tick_params(labelsize=9)
    cbar.locator = ticker.MaxNLocator(nbins=20)
    cbar.update_ticks()


#%%

adcp_short_spd('2018-01-01 00:07:00', '2018-01-01 23:37:00', '2018-01-01')
adcp_short_uv('2018-01-01 00:07:00', '2018-01-01 23:37:00', '2018-01-01')

adcp_short_spd('2018-01-02 00:07:00', '2018-01-02 23:37:00', '2018-01-01')
adcp_short_uv('2018-01-02 00:07:00', '2018-01-02 23:37:00', '2018-01-01')

adcp_short_spd('2018-01-01 00:07:00', '2018-01-01 23:37:00', '2018-01-01')
adcp_short_uv('2018-01-01 00:07:00', '2018-01-01 23:37:00', '2018-01-01')





