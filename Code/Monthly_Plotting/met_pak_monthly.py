#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:35:52 2019

@author: jacobarnold

purpose:
    Create monthly time series of metpak data
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

met_pak_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/metpak_F.csv',
                        infer_datetime_format = True, index_col=0)

#Meteorology package - Air temp (degrees Celcius), Relative humidity (%), Wind Velocity (m/s) and pressure (millibars).

#%%

# Define the index as date time
def date_fmt_1D(dataframe):
    temp = dataframe
    temp.index = pd.to_datetime(temp.index)
    return temp

met_pak_F = date_fmt_1D(met_pak_F)

#%%

def plot_month(inter_start, inter_end, yr_mnth):
    
    fig = plt.figure(figsize=(10,10))
    
    ax1 = fig.add_subplot(3,1,1)
    ax1.scatter(x=met_pak_F[inter_start:inter_end].index, 
             y=met_pak_F[inter_start:inter_end].temperature, s=5.5, color='#4BBC82')
    ax1.set_title('Air Temperature and Pressure '+'('+yr_mnth+')')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Temperature (\u2103)')
    ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax1.tick_params(axis='x', which='major', labelsize=7)
    ax1.tick_params(axis='y', which='major', labelsize=9)
    ax1.tick_params(axis='y', colors = '#4BBC82')         
                    
    ax2 = ax1.twinx()
    ax2.scatter(x = met_pak_F[inter_start:inter_end].index,
                y = met_pak_F[inter_start:inter_end]['pressure'],
                 s=5.5, color='#4B8ECA')
    ax2.set_ylabel('Barometric Pressure (mbar)')
    ax2.tick_params(axis='y', which='major', labelsize=9)
    ax2.tick_params(axis='y', colors = '#4B8ECA')
    ax2.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax2.set_xlim(pd.Timestamp(inter_start), pd.Timestamp(inter_end))
    fig.autofmt_xdate()
    fig.tight_layout()
    
    ax3 = fig.add_subplot(3,1,2)
    ax3.scatter(x=met_pak_F[inter_start:inter_end].index, 
             y=met_pak_F[inter_start:inter_end].humidity, s=5.5, color='#4BBC82')
    ax3.set_title('Humidity and Dewpoint '+'('+yr_mnth+')')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Humidity (%)')
    ax3.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax3.tick_params(axis='x', which='major', labelsize=7)
    ax3.tick_params(axis='y', which='major', labelsize=9)
    ax3.tick_params(axis='y', colors = '#4BBC82')         
                    
    ax4 = ax3.twinx()
    ax4.scatter(x = met_pak_F[inter_start:inter_end].index,
                y = met_pak_F[inter_start:inter_end]['dewpoint'],
                 s=5.5, color='#4B8ECA')
    ax4.set_ylabel('Dewpoint (\u2103)')
    ax4.tick_params(axis='y', which='major', labelsize=9)
    ax4.tick_params(axis='y', colors = '#4B8ECA')
    ax4.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax4.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax4.set_xlim(pd.Timestamp(inter_start), pd.Timestamp(inter_end))
    fig.autofmt_xdate()
    fig.tight_layout()

    ax5 = fig.add_subplot(3,1,3)
    ax5.scatter(x=met_pak_F[inter_start:inter_end].index, 
             y=met_pak_F[inter_start:inter_end].wind_speed, s=5.5, color='#4BBC82')
    ax5.set_title('Wind Speed and Direction '+'('+yr_mnth+')')
    ax5.set_xlabel('Date')
    ax5.set_ylabel('Wind Speed (m/s)')
    ax5.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax5.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax5.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax5.tick_params(axis='x', which='major', labelsize=7)
    ax5.tick_params(axis='y', which='major', labelsize=9)
    ax5.tick_params(axis='y', colors = '#4BBC82')         
                    
    ax6 = ax5.twinx()
    ax6.scatter(x = met_pak_F[inter_start:inter_end].index,
                y = met_pak_F[inter_start:inter_end]['wind_direction'],
                 s=5.5, color='#4B8ECA')
    ax6.set_ylabel('Wind Direction (Deg. from North)')
    ax6.tick_params(axis='y', which='major', labelsize=9)
    ax6.tick_params(axis='y', colors = '#4B8ECA')
    ax6.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax6.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax6.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax6.set_xlim(pd.Timestamp(inter_start), pd.Timestamp(inter_end))
    fig.autofmt_xdate()
    fig.tight_layout()    
    
    plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/Monthly_Timeseries/'+yr_mnth+'/met_pak.png',
                bbox_inches='tight', dpi=400)


#%%
    
'''
2017
'''

plot_month('2017-07-26 00:05:00','2017-07-31 23:35:00', '2017-07')    

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

    

