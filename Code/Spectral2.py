#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:29:37 2019

@author: jacobarnold

Create function for spectral plot
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%%

salinity = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/microcat_F.csv',
                       infer_datetime_format=True, index_col=0)


#%%

def Spectral(data, variable, inter_start, inter_end, savename='skip', delT=2):
    '''
    Create subplots of:
        1. Time series of data
        2. Spectal plot of data
    
    Parameters
    ----------
    data: Pandas DataFrame with columns representing each variable in that DataFrame and rows 
        representing time/date (expecting 30 minute intervals)
    
    inter_start: date-time yyyy-mm-dd hh-mm-ss format
        The start of the interval that will be plotted 
        
    inter_end:  date-time yyyy-mm-dd hh-mm-ss format
        The end of the interval that will be plotted 
        
    savename: The name that the final plot will be saved to. 
        Default is skip. If no savename is given, the plot will not be saved. 
        File path == 'Documents/Classes/THEMO/TABS225m09/Plots/Spectral/'+savename
        
    delT = number of recordings per hour
        Default is 2 (ylabel for timeseies must be addressed if delT is not 2)
    '''
    
    variable=variable
    def cut():
        data2 = data[inter_start:inter_end][variable]
        return data2
    data2 = cut()
    
    data3 = np.array(data2.interpolate().values.ravel().tolist())
    
    spec = abs(np.fft.fft(data3-np.mean(data3)))**2
    nnn = len(data3)
    xf = ((np.arange(1,nnn/2+1))/(nnn*delT/24))
    if nnn % 2 == 0:
        ind = int(nnn/2+2)
    elif nnn % 2 ==1:
        ind = int(nnn/2+3)
    spec = spec[2:ind]
    
    def subplotter(axnum, inp1, title, ylabel, inp2='skip'):
        if inp2 == 'skip':
            ax[axnum].plot(inp1, linewidth=.8)
        else:
            ax[axnum].plot(inp1, inp2, linewidth=.8)
        ax[axnum].xaxis.set_major_locator(plt.MaxNLocator(18))
        ax[axnum].yaxis.set_major_locator(plt.MaxNLocator(8))
        ax[axnum].tick_params(axis='x', which='major', labelsize=8)
        ax[axnum].tick_params(axis='y', which='major', labelsize=8)
        if ax[axnum] == ax[0]:
            ax[axnum].set_xlabel('Hours*2 From '+inter_start, fontsize=9)
        elif ax[axnum] == ax[1]:
            ax[axnum].set_xlabel('Frequency [Hz]', fontsize=9)
        ax[axnum].set_title(title, fontweight='bold')
        ax[axnum].set_ylabel(ylabel)
        plt.tight_layout()
    
    fig,ax = plt.subplots(2,figsize=(8,6))
    subplotter(axnum=0, inp1=data3, title='Time Series', ylabel=variable)
    subplotter(axnum=1, inp1=xf, inp2=spec, title='Spectral Plot', ylabel='Fourier Transform Variance')
        

    if savename=='skip':
        pass
    else:
        plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/Spectral/'+savename,
                    bbox_inches='tight', dpi=500)
    

#%%
       
Spectral(data=salinity, variable='Temperature', 
         inter_start='2017-07-25 12:31:00', 
         inter_end='2018-02-13 06:01:00')






    
#%%

Spectral(data=salinity, variable='Temperature', 
         inter_start='2017-07-25 12:31:00', 
         inter_end='2017-08-25 12:31:00')





