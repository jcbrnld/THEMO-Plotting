#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:22:17 2019

@author: jacobarnold

Purpose:
    Attempt pcolormesh with ADCP data
    
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cmocean
import matplotlib.dates as mdates
from matplotlib import ticker

#%%

adcp2D = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D.csv',
                     infer_datetime_format=True,
                     index_col=0,
                     header=1,
                     skiprows=[2]
                     ).T

adcp2D_temp = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D.csv',
                     infer_datetime_format=True,
                     header=1,
                     skiprows=[2]
                     )
adcp2D_temp2 = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D.csv',
                     infer_datetime_format=True,
                     index_col=0
                     )


time = adcp2D_temp.depth
time = pd.to_datetime(time)
bin_depths = adcp2D_temp2.loc['depth',:]

#%%
adcpU2D = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp_u2D.csv',
                     infer_datetime_format=True,
                     index_col=0,
                     header=1,
                     skiprows=[2]
                     ).T


#%%
adcpV2D = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp_v2D.csv',
                     infer_datetime_format=True,
                     index_col=0,
                     header=1,
                     skiprows=[2]
                     ).T

#%%
date_index = pd.date_range(start='2017-07-25 14:07:00', end='2019-05-30 13:37:00', periods=32352)

adcp_BG = adcp2D.T[:'2018-02-13 06:07:00'].T
adcp_AG = adcp2D.T['2018-09-02 09:37:00':].T

#time_B = time[:9429]
#time_A = time[9543:]
date_index_B = date_index[:9728]
date_index_A = date_index[19383:]


adcpU_BG = adcpU2D.T[:'2018-02-13 06:07:00'].T
adcpU_AG = adcpU2D.T['2018-09-02 09:37:00':].T

adcpV_BG = adcpV2D.T[:'2018-02-13 06:07:00'].T
adcpV_AG = adcpV2D.T['2018-09-02 09:37:00':].T


#%%

# Create the new date index with no missing values



# Specify the index is in datetime format

def date_fmt(dataframe):
    '''
    Returns the input dataframe with index defined as datetime
    
    Parameters
    ----------
    dataframe: var
        The dataframe that will be processed
        dataframe should be two dimensional with column names as dates and 
        index as another trait
        dataframe should have an index of dates in it's transposed position
        dataframe will be transposed in the function to create index of dates 
        dataframe will be transposed when returned to revert to original index
    '''
    temp = dataframe.T
    temp.index = pd.to_datetime(temp.index)
    return temp.T

adcp2D = date_fmt(adcp2D)
adcpU2D = date_fmt(adcpU2D)
adcpV2D = date_fmt(adcpV2D)
adcp_BG = date_fmt(adcp_BG)
adcp_AG = date_fmt(adcp_AG)
adcpU_BG = date_fmt(adcpU_BG)
adcpU_AG = date_fmt(adcpU_AG)
adcpV_BG = date_fmt(adcpV_BG)
adcpV_AG = date_fmt(adcpV_AG)


# Create the filled dataframes
adcp2D_F = adcp2D.T.reindex(date_index).T
adcpU2D_F = adcpU2D.T.reindex(date_index).T
adcpV2D_F = adcpV2D.T.reindex(date_index).T
adcp_BG_F = adcp_BG.T.reindex(date_index_B).T
adcp_AG_F = adcp_AG.T.reindex(date_index_A).T
adcpU_BG_F = adcpU_BG.T.reindex(date_index_B).T
adcpU_AG_F = adcpU_AG.T.reindex(date_index_A).T
adcpV_BG_F = adcpV_BG.T.reindex(date_index_B).T
adcpV_AG_F = adcpV_AG.T.reindex(date_index_A).T




#%%
# Create function to plot the ADCP data
#lim_spd = float('%2.2f' % np.nanpercentile(adcp2D,99))

def plot_adcp(times, depths, data_2d, title, colormap, name):
    fig = plt.figure(figsize=(12,3))
    ax1 = fig.add_subplot(111)
    m1 = ax1.pcolormesh(times, depths, data_2d, cmap=colormap, vmin=0, vmax=1)
    ax1.invert_yaxis()
    ax1.set_title(title)
    ax1.set_ylabel('Depth (m)')
    ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.tick_params(axis='x', which='major', labelsize=7)
    ax1.tick_params(axis='y', which='major', labelsize=9)
    fig.autofmt_xdate()
    cbar=plt.colorbar(m1, ax=ax1)
    cbar.set_label('Speed (m/s)')
    cbar.ax.tick_params(labelsize=9)
    cbar.locator = ticker.MaxNLocator(nbins=11)
    cbar.update_ticks()
    plt.tight_layout()
#    plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/ADCP/'+name+'.png',
#                bb_inches='tight', dpi=1000)


#%%
    
plot_adcp(date_index, bin_depths, adcp2D_F, 'All ADCP Data', 'cmo.thermal', 'all')

plot_adcp(date_index_B, bin_depths, adcp_BG_F, 'Speed Before Data Gap', 'cmo.thermal', 'Before_gap')

plot_adcp(date_index_A, bin_depths, adcp_AG_F, 'Speed After Data Gap', 'cmo.thermal', 'After_gap')




#%%
# Now plot the U and V
#lim_U = float('%2.2f' % np.nanpercentile(adcpU2D,99))
#lim_V = float('%2.2f' % np.nanpercentile(adcpV2D,99))
#u_v = max([lim_U, lim_V])
def plot_adcp_2(times, depths, data_2d, title, colormap, name):
    fig = plt.figure(figsize=(12,3))
    ax1 = fig.add_subplot(111)
    m1 = ax1.pcolormesh(times, depths, data_2d, cmap=colormap, vmin=-1, vmax=1)
    ax1.invert_yaxis()
    ax1.set_title(title)
    ax1.set_ylabel('Depth (m)')
    ax1.yaxis.set_major_locator(plt.MaxNLocator(10))
    ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.tick_params(axis='x', which='major', labelsize=7)
    ax1.tick_params(axis='y', which='major', labelsize=9)
    fig.autofmt_xdate()
    cbar=plt.colorbar(m1, ax=ax1)
    cbar.set_label('Speed (m/s)')
    cbar.ax.tick_params(labelsize=9)
    cbar.locator = ticker.MaxNLocator(nbins=11)
    cbar.update_ticks()
    plt.tight_layout()
#    plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/ADCP/'+name+'.png',
#                bb_inches='tight', dpi=1000)

#%%

plot_adcp_2(date_index, bin_depths, adcpU2D_F, 'ADCP U Velocity', 'cmo.balance', 'all_U')
plot_adcp_2(date_index, bin_depths, adcpV2D_F, 'ADCP V Velocity', 'cmo.balance', 'all_V')

plot_adcp_2(date_index_B, bin_depths, adcpU_BG_F, 'U Velocity Before Data Gap', 'cmo.balance', 'Before_gap_U')
plot_adcp_2(date_index_B, bin_depths, adcpV_BG_F, 'V Velocity Before Data Gap', 'cmo.balance', 'Before_gap_V')

plot_adcp_2(date_index_A, bin_depths, adcpU_AG_F, 'U Velocity After Data Gap', 'cmo.balance', 'After_gap_U')
plot_adcp_2(date_index_A, bin_depths, adcpV_AG_F, 'V Velocity After Data Gap', 'cmo.balance', 'After_gap_V')






