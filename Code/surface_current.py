#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:26:17 2019

@author: jacobarnold
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import numpy as np


surf_cur = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/dcs.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Near surface current velocity (m/s)

salinity = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/microcat.csv',
                       parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#Salinity (PSU), conductivity(S/m), and temperature(degrees celcius) recorded at 1m 

#%%

fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(2,1,1)
ax1.scatter(x=surf_cur.index, y='East[cm/s]', data=surf_cur, s=1, c='#4B8ECA')
ax1.set_title('East Surface Current Component')
ax1.set_xlabel('Date')
ax1.set_ylabel('Speed[m/s]')

ax2 = fig.add_subplot(2,1,2)
ax2.scatter(x=surf_cur.index, y='North[cm/s]', data=surf_cur, s=1, c='#4BBC82')
ax2.set_title('North Surface Current Component')
ax2.set_xlabel('Date')
ax2.set_ylabel('Speed[m/s]')


plt.tight_layout()

#%%

surf_cur_before = surf_cur['2017-07':'2018-02']
salinity_before = salinity['2017-07':'2018-02']

#%%

surf_cur_t1 = surf_cur['2017-07-26 00:05:09':'2017-07-26 16:35:14']
salinity_t1 = salinity['2017-07-26 00:01:16':'2017-07-26 16:31:15']

#%%

fig = plt.figure(figsize=(20,8))
ax1 = fig.add_subplot(2,1,1)
ax1.scatter(x=surf_cur_before.index, y='East[cm/s]', data=surf_cur_before, s=1, c='#4B8ECA')
ax1.set_title('East Surface Current Component Before the Gap')
ax1.set_xlabel('Date')
ax1.set_ylabel('Speed[m/s]')

ax2 = fig.add_subplot(2,1,2)
ax2.scatter(x=salinity_before.index, y='Salinity', data=salinity_before, s=1, c='#4BBC82')
ax2.set_title('Salinity Before the Gap')
ax2.set_xlabel('Date')
ax2.set_ylabel('Salinity [PSU]')

plt.tight_layout()


#%%
#np.corrcoef(surf_cur['East[cm/s]'], salinity['Salinity'])

corr = np.corrcoef(surf_cur_t1['East[cm/s]'], salinity_t1['Salinity'])


#%%

# how='mean' is default but included for future reference
grouped_cur = surf_cur.resample('1h', how='mean')

grouped_cur_before = surf_cur_before.resample('1h', how='mean')

grouped_sal = salinity.resample('1h', how='mean')

grouped_sal_before = salinity_before.resample('1h', how='mean')
grouped_sal_before = grouped_sal_before[:-1]


#corr2 = np.corrcoef(grouped_cur_before['Abs_Speed[cm/s]'], grouped_sal_before['Salinity'])

grouped_cur_before['Abs_Speed[cm/s]'].corr(other=grouped_sal_before['Salinity']) # This is the 1 line way




#%%

together = grouped_cur_before[['Abs_Speed[cm/s]']].copy()
together['Salinity'] = grouped_sal_before['Salinity']
print(together.corr())
# -0.047994  Current speed and salinity corrolation before the gap

together_N = grouped_cur_before[['North[cm/s]']].copy()
together_N['Salinity'] = grouped_sal_before['Salinity']
print(together_N.corr())
# -0.088315  North current component and salinity corrolation before the gap

together_E = grouped_cur_before[['East[cm/s]']].copy()
together_E['Salinity'] = grouped_sal_before['Salinity']
print(together_E.corr())
# -0.108897  East current component and salinity corrolation before the gap


#%%

grouped_cur_after = grouped_cur['2018-09-02 00:01:13':]
grouped_sal_after = grouped_sal['2018-09-02 00:01:13':]

grouped_cur_after['Abs_Speed[cm/s]'].corr(other=grouped_sal_after['Salinity'])
# -0.038913371173101334  Current speed and salinity corrolation after the gap

grouped_cur_after['North[cm/s]'].corr(other=grouped_sal_after['Salinity'])
 # -0.02434320365873805 North current component and salinity corrolation after the gap
 
grouped_cur_after['East[cm/s]'].corr(other=grouped_sal_after['Salinity'])
# -0.044050409918175965 East current component and salinity corrolation after the gap


#%%
import seaborn as sns
salinity.corr()
sns.pairplot(salinity, vars=['Salinity','Conductivity','Temperature'])



#%%

sns.pairplot(data=surf_cur_before, vars=['Abs_Speed[cm/s]','North[cm/s]','East[cm/s]','Temperature[DegC]',
                                         'Heading[DegM]', 'Abs_Tilt[Deg]'])


#%%
'''
This all to verify that column Abs_Speed[cm/s] was the current speed component
'''

from math import sqrt
# This first line would have worked too but I went step by step for clarity
#grouped_cur_before['Magnitude'] = ((grouped_cur_before['East[cm/s]']**2)+(grouped_cur_before['North[cm/s]']**2))**(1/2)
grouped_cur_before['east_squared'] = grouped_cur_before['East[cm/s]']**2
grouped_cur_before['north_squared'] = grouped_cur_before['North[cm/s]']**2
grouped_cur_before['squ_added'] = grouped_cur_before['east_squared']+grouped_cur_before['north_squared']
grouped_cur_before['rooted'] = (grouped_cur_before['squ_added'])**(1/2)


together_my = grouped_cur_before[['rooted']].copy()
together_my['Salinity'] = grouped_sal_before['Salinity']
print(together_my.corr())

#%%

fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot(111)
ax.scatter(x=grouped_cur_before['Abs_Speed[cm/s]'], y=grouped_sal_before['Salinity'])

#%%

grouped_cur_before['Abs_Speed[cm/s]'].corr(other=grouped_sal_before['Temperature'])
# 0.11986387914658087  Current speed and surface temperature corrolation





































