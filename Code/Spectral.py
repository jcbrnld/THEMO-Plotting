#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:19:07 2019

@author: jacobarnold

Purpose:
    Spectral analysis of timeseries data
    
"""

import numpy as np
import pandas as pd

#from scipy import signal
import matplotlib.pyplot as plt
import cmocean
#import matplotlib.dates as mdates

#%%
salinity = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/microcat_F.csv',
                       infer_datetime_format=True, index_col=0)

tempall = salinity.Temperature
temp_nanfilled = np.array(tempall.fillna(tempall.mean()))
temp1 = salinity['2017-11-27 10:01:00':'2018-01-16 09:31:00'].Temperature
sal1 = salinity['2017-11-27 10:01:00':'2018-01-16 09:31:00'].Salinity
sal1_1 = np.array(sal1)
temp1_1 = np.array(temp1)
temp2 = salinity['2019-01-01':'2019-01-09 13:01:00'].Temperature

before_temp = salinity['2017-07-25 12:31:00':'2018-02-13 06:01:00'].Temperature
before_nanfill = np.array(before.fillna(before.mean()))
after_temp = salinity['2018-09-02 05:31:00':].Temperature
after_nanfill = np.array(after.fillna(after.mean()))

#%%

surf_cur = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/dcs_F.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Near surface current velocity (m/s)
east_cur = np.array(surf_cur['East[cm/s]'])

nans = np.argwhere(np.isnan(east_cur))
#%%

met_pak = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/metpak_F.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)



#%%

# Find largest gap  
# between two elements in an array. 
import sys 
  
# function to solve the given problem 
def solve(a, n): 
    max1 = -sys.maxsize - 1
    for i in range(0, n, 1): 
        for j in range(0, n, 1): 
            if (abs(a[i] - a[j]) > max1): 
                max1 = abs(a[i] - a[j]) 
  
    return max1 
  
# Driver Code 
#if __name__ == '__main__': 
size = len(nans) 
#    print("Largest gap is :", solve(nans, size)) 

solve(nans, size)

#%%
# Interpolate

before_tempI = np.array(before_temp.interpolate().values.ravel().tolist())
after_tempI = np.array(after_temp.interpolate().values.ravel().tolist())



#%%

def spectral(data, name='skip', delT=2, start_time='First Recording', variable='Variable'):
    spec = abs(np.fft.fft(data-np.mean(data)))**2
    nnn = len(data)
    xf = ((np.arange(1,nnn/2+1))/(nnn*delT/24))
    if nnn % 2 == 0:
        ind = int(nnn/2+2)
    elif nnn % 2 ==1:
        ind = int(nnn/2+3)
    spec = spec[2:ind]
    
    fig = plt.figure(figsize=(8,6))
    ax1 = fig.add_subplot(2,1,1)
    ax1.plot(data,linewidth=.8)
    ax1.xaxis.set_major_locator(plt.MaxNLocator(18))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax1.tick_params(axis='x', which='major', labelsize=8)
    ax1.tick_params(axis='y', which='major', labelsize=8)
    ax1.set_xlabel('Hours*2 From '+ start_time, fontsize=9)
    ax1.set_title('Time Series', fontweight='bold')
    ax1.set_ylabel(variable)
    
    ax2 = fig.add_subplot(2,1,2)
    ax2.plot(xf, spec, linewidth=.8)
    ax2.set_title('Spectral Plot', fontweight='bold')
    ax2.set_xlabel('Frequency [Hz]', fontsize=9)
    ax2.set_ylabel('Fourier Transform Variance')
    ax2.xaxis.set_major_locator(plt.MaxNLocator(18))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(8))
    ax2.tick_params(axis='x', which='major', labelsize=8)
    ax2.tick_params(axis='y', which='major', labelsize=8)
    plt.tight_layout()
    
    if name == 'skip':
        pass
    else:
        plt.savefig('Documents/Classes/THEMO/TABS225m09/Plots/Spectral/'+name,
                    bbox_inches='tight', dpi=500)

#%%
spectral(temp1_1, 2, '2017-11-27 10:01:00', 'Temperature [\u2103]')    

spectral(sal1_1)

spectral(temp_nanfilled, 2, '2017-07-24 05:31:00', 'Temperature [\u2103]')

spectral(before_nanfill,2,'2017-07-24 05:31:00', 'Temperature [\u2103]')

spectral(after_nanfill,2,'2018-09-02 00:31:00', 'Temperature [\u2103]')

spectral(data=before_tempI, delT=2,start_time='2017-07-24 05:31:00', variable='Temperature [\u2103]')

spectral(after_tempI, 'after_tempI.png',2,'2018-09-02 05:31:00', 'Temperature [\u2103]')



























#%%
 

spec = abs(np.fft.fft(temp1_1 - np.mean(temp1_1)))**2

delT = 2
nnn = len(temp1_1)

fir = np.arange(1,nnn/2+1)
sec = nnn*delT/24
xf = fir/sec
fourth = int(nnn/2+2)
thir = spec[2:fourth]
#%%
fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(xf,thir, linewidth=.8)
ax1.set_xlabel('Frequency [Hz]')
ax1.set_ylabel('Fourier Transform Variance')




#%%
plt.plot(XF,spec)

#plt.plot(XF,spec[np.arange(2,nnn/2+1)])



#%%
'''
Use lower one
'''
#f,t,Sxx = signal.spectrogram(temp1_1)

#plt.pcolormesh(t, f, Sxx)
#plt.ylabel('Frequency [Hz]')
#plt.xlabel('Time [sec]')
#plt.show()


#%%
'''
Use this one
'''
f, t, Sxx = signal.spectrogram(temp1_1,  fs=1)
#f, t, Sxx = signal.spectrogram(temp1_1, return_onesided=False,  fs=1)
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(111)
m1 = ax1.pcolormesh(t, np.fft.fftshift(f), np.fft.fftshift(Sxx, axes=0), cmap = 'cmo.tempo')
#m1 = ax1.pcolormesh(np.fft.fftshift(f),t,  np.fft.fftshift(Sxx, axes=0).T, cmap = 'cmo.tempo')
ax1.set_ylabel('Frequency [Hz]')
#ax1.set_xlabel('Time [hr/2] from 2017-11-27 10:01:00')
ax1.set_title('Temperature Spectral Analysis [2017-11-27 to 2018-01-16]')
#ax1.set_ylim(-.2,.2)
cbar=plt.colorbar(m1, ax=ax1)
#cbar.set_label('Segment Times [t]')
plt.tight_layout()

#%%

f2, t2, Sxx2 = signal.spectrogram(temp1_1, fs=1)
fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(111)
ax1.plot(f2,Sxx2)
#ax1.plot(np.fft.fftshift(f2),np.fft.fftshift(Sxx2))
ax1.set_title('Temperature Spectral Analysis [2017-11-27 to 2018-01-16]')
ax1.set_xlabel('Sample Frequency')
plt.tight_layout()

#%%
# Comparison
f, t, Sxx = signal.spectrogram(temp1_1,  fs=1, nperseg=256)
#f, t, Sxx = signal.spectrogram(temp1_1, return_onesided=False,  fs=1)
fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(2,1,1)
m1 = ax1.pcolormesh(t, np.fft.fftshift(f), np.fft.fftshift(Sxx, axes=0), cmap = 'cmo.thermal')
#m1 = ax1.pcolormesh(np.fft.fftshift(f),t,  np.fft.fftshift(Sxx, axes=0).T, cmap = 'cmo.tempo')
ax1.set_ylabel('Frequency [Hz]')
#ax1.set_xlabel('Time [hr/2] from 2017-11-27 10:01:00')
ax1.set_title('Surface Temperature Spectrogram [2017-11-27 to 2018-01-16]')
#ax1.set_ylim(-.2,.2)
ax1.set_ylim(0,.2)
#cbar=plt.colorbar(m1, ax=ax1)
#cbar.set_label('Segment Times [t]')

ax2 = fig.add_subplot(2,1,2)
ax2.plot(temp1_1)
ax2.set_title('Surface Temperature [2017-11-27 to 2018-01-16]')
ax2.set_xlabel('Time [hr/2] from 2017-11-27 10:01:00')
ax2.set_xlim(0,2400)


plt.tight_layout()



#%%

plt.plot(f,Sxx.T[0])
plt.plot(f,Sxx.T[1])
plt.plot(f,Sxx.T[2])
plt.plot(f,Sxx.T[3])
plt.plot(f,Sxx.T[9])
