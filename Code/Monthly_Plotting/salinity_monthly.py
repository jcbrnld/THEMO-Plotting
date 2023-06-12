#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:40:32 2019

@author: jacobarnold

purpose: create monthly time series of salinity data
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates


salinity_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/microcat_F.csv',
                    index_col=0, infer_datetime_format=True)

#%%

# Define the index as date time
def date_fmt_1D(dataframe):
    temp = dataframe
    temp.index = pd.to_datetime(temp.index)
    return temp

salinity_F = date_fmt_1D(salinity_F)

salinity_F.Salinity[salinity_F.Salinity<38]=np.nan
salinity_F.Temperature[salinity_F.Temperature>31]=np.nan

#%%

def plot_month(inter_start, inter_end, yr_mnth):
    
    
    fig = plt.figure(figsize=(12,4))

    ax1 = fig.add_subplot(111)
    ax1.scatter(x = salinity_F[inter_start:inter_end].index,
                y = salinity_F[inter_start:inter_end]['Salinity'],
                 s=5.5, color='#4BBC82')
    ax1.set_title('Surface Salinity'+'('+yr_mnth+')')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Salinity (PSU)')
    ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax1.tick_params(axis='x', which='major', labelsize=7)
    ax1.tick_params(axis='y', which='major', labelsize=9)
    ax1.tick_params(axis='y', colors = '#4BBC82')

    ax2 = ax1.twinx()
    ax2.scatter(x = salinity_F[inter_start:inter_end].index,
                y = salinity_F[inter_start:inter_end]['Temperature'],
                 s=5.5, color='#4B8ECA')
    ax2.set_ylabel('Temperature (\u2103)')
    ax2.tick_params(axis='y', which='major', labelsize=9)
    ax2.tick_params(axis='y', colors = '#4B8ECA')
    ax2.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax2.set_xlim(pd.Timestamp(inter_start), pd.Timestamp(inter_end))
    fig.autofmt_xdate()
    fig.tight_layout()

#    plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/Monthly_Timeseries/'+yr_mnth+'/Salinity.png',
#                bbox_inches='tight', dpi=400)




#%% 
'''
2017
'''

plot_month('2017-07-26 00:10:00','2017-07-31 23:40:00', '2017-07')    

plot_month('2017-08-01','2017-08-31', '2017-08')
    
plot_month('2017-09-01','2017-09-30', '2017-09')  

plot_month('2017-10-01','2017-10-31', '2017-10')

plot_month('2017-11-01','2017-11-30', '2017-11')

plot_month('2017-12-01','2017-12-31', '2017-12')

#%%
'''
2018
'''
plot_month('2018-01-01','2018-01-31', '2018-01') 

plot_month('2018-02-01','2018-02-28', '2018-02') 

plot_month('2018-03-01','2018-03-31', '2018-03')

plot_month('2018-05-01','2018-05-31', '2018-05')

plot_month('2018-06-01','2018-06-30', '2018-06')

plot_month('2018-07-01','2018-07-31', '2018-07')

plot_month('2018-08-01','2018-08-31', '2018-08')

plot_month('2018-09-01','2018-09-30', '2018-09')

plot_month('2018-10-01','2018-10-31', '2018-10')

plot_month('2018-11-01','2018-11-30', '2018-11')

plot_month('2018-12-01','2018-12-31', '2018-12')

#%%
'''
2019
'''
plot_month('2019-01-01','2019-01-31','2019-01') 

plot_month('2019-02-01','2019-02-28','2019-02')

plot_month('2019-03-01','2019-03-31','2019-03')

plot_month('2019-04-01','2019-04-30','2019-04')

plot_month('2019-05-01','2019-05-30','2019-05')

