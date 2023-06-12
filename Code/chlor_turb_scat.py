#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 18:04:02 2019

@author: jacobarnold
Scatter plot of Chlorinity vs Turbidity
From THEMO Haifa TABS225 data

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fluor = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/flntu.csv',
                    parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Fluorescence recorded at 1m (Chlorophyll in μg/L) (Turbidity in NTU)


#%%
fig, ax1 = plt.subplots(figsize = (10,8))

ax1.scatter(x = 'chlorophyll_concentration', y = 'turbidity_units', data = fluor, s=2, color = '#4BBC82')
ax1.set_title('Chlorophyll Plotted against Turbidity')
ax1.set_xlabel('Chlorophyll Concentration (μg/L)')
ax1.set_ylabel('Turbidity (NTU)')
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/scat_fluor_turbid1.png',bbox_inches='tight',dpi=400)

#%%
fig, ax1 = plt.subplots(figsize = (10,8))

ax1.scatter(x = 'chlorophyll_concentration', y = 'turbidity_units', data = fluor, s=2, color = '#4BBC82')
ax1.set_title('Chlorophyll Plotted against Turbidity')
ax1.set_xlabel('Chlorophyll Concentration (μg/L)')
ax1.set_ylabel('Turbidity (NTU)')
plt.xlim(0,0.9)
plt.ylim(0,0.9)
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/scat_fluor_turbid2.png',bbox_inches='tight',dpi=400)



#%%
'''trim fluor'''
#fluor = fluor[:'2018-02-13 05:40:11']
fluor = fluor['2018-09-02 00:10:08':]

#%%
fig, ax1 = plt.subplots(figsize = (10,8))

ax1.scatter(x = 'chlorophyll_concentration', y = 'turbidity_units', data = fluor, s=2, color = '#4BBC82')
ax1.set_title('Chlorophyll Plotted against Turbidity')
ax1.set_xlabel('Chlorophyll Concentration (μg/L)')
ax1.set_ylabel('Turbidity (NTU)')
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/scat_fluor_turbid_before1.png',bbox_inches='tight',dpi=400)
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/scat_fluor_turbid_after1.png',bbox_inches='tight',dpi=400)


#%%

fig, ax1 = plt.subplots(figsize = (10,8))

ax1.scatter(x = 'chlorophyll_concentration', y = 'turbidity_units', data = fluor, s=2, color = '#4BBC82')
ax1.set_title('Chlorophyll Plotted against Turbidity')
ax1.set_xlabel('Chlorophyll Concentration (μg/L)')
ax1.set_ylabel('Turbidity (NTU)')
plt.xlim(0,0.7)
plt.ylim(0,0.7)

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/scat_fluor_turbid_before2.png',bbox_inches='tight',dpi=400)

#%%
fig, ax1 = plt.subplots(figsize = (10,8))

ax1.scatter(x = 'chlorophyll_concentration', y = 'turbidity_units', data = fluor, s=2, color = '#4BBC82')
ax1.set_title('Chlorophyll Plotted against Turbidity')
ax1.set_xlabel('Chlorophyll Concentration (μg/L)')
ax1.set_ylabel('Turbidity (NTU)')
plt.xlim(0,0.5)
plt.ylim(0,2.5)

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/scat_fluor_turbid_after2.png',bbox_inches='tight',dpi=400)




