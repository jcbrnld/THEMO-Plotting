#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:32:55 2019

@author: jacobarnold

TABS225 THEMO Haifa Data

Purpose:
    To plot data from the Acoustic Doppler Current Profiler (ADCP) in useful 
    and attractive ways.
    
Line plots will be attemped and scatter plots will be included with an overall 
focus on including a colorbar to ensure plots' utility. 

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cmocean

The_ADCP = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp.csv',
                  parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
The_ADCP.rename(columns = {'depth[m]':'depth', 'direction[deg]':'direction','speed[m/s]':'speed'}, inplace=True)
#Acoustic Doppler Current Profiler Depth, Direction in degrees, Speed in m/s



plt.style.use('seaborn-deep')
#plt.style.use('ggplot')




#%%
'''Plotting the data of various sizes'''
# Trim outside values
The_ADCP[The_ADCP.speed > 3] = np.nan

# Create dataframe for before the gap
The_ADCP_Before_Gap = The_ADCP[:'2018-02-13 06:07:00'] 

# Create dataframe for after the gap
The_ADCP_After_Gap = The_ADCP['2018-09-02 00:07:00':]

The_ADCP_17 = The_ADCP['2017-07-26':'2017-12-31']

The_ADCP_18 = The_ADCP['2018-01-01':'2018-12-31']

The_ADCP_19 = The_ADCP['2019-01-01':]

#%%  

'''Scatter plot of The_ADCP by speed'''
#cmap = cmocean.cm.deep

#A = np.random.randint(3, 131, (10,10))
#mappable = ax1.pcolormesh(A, vmin=3, vmax=131, cmap=cmap)
fig, ax1 = plt.subplots(figsize = (20,8))

mappable = ax1.scatter(x = The_ADCP.index, y = The_ADCP.speed, s=1.5, c='depth', cmap='cmo.deep')
ax1.set_title('Pre Gap (2017-07-26 to 2018-02-13) Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Current Speed (m/s)')
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Depth (m)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(5,135,10))
plt.tight_layout()


#%%
def plot_ADCP(data, title, axes):
    
    mappable = axes.scatter(x = data.index, y = data.depth, s=1.3, c=data.speed,
                       cmap='cmo.tempo', marker='s')
    axes.set_title('Title', fontsize=10)
    axes.set_xlabel('Date')
    axes.set_ylabel('Depth (m)')
    axes.invert_yaxis()
    cbar = plt.colorbar(mappable=mappable, ax=axes)
    cbar.set_label('Speed (m/s)')
    axes.tick_params(axis='both', which='major', labelsize=8)
    cbar.set_ticks(np.arange(0,1.62,0.2))
    plt.tight_layout()




#%%
'''Choosing a colormap'''


fig = plt.figure(figsize=(15,10))

ax1 = fig.add_subplot(3,2,1)
mappable = ax1.scatter(x = The_ADCP_Before_Gap.index, y = 'depth', data = The_ADCP_Before_Gap,  s=4, c='speed', cmap='cmo.deep')
ax1.set_title('Deep')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
#plt.tight_layout()

ax2 = fig.add_subplot(3,2,2)
mappable = ax2.scatter(x = The_ADCP_Before_Gap.index, y = 'depth', data = The_ADCP_Before_Gap,  s=4, c='speed', cmap='cmo.rain')
ax2.set_title('Rain')
ax2.set_xlabel('Date')
ax2.set_ylabel('Depth (m)')
ax2.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax2)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
#plt.tight_layout()


ax3 = fig.add_subplot(3,2,3)
mappable = ax3.scatter(x = The_ADCP_Before_Gap.index, y = 'depth', data = The_ADCP_Before_Gap,  s=4, c='speed', cmap='cmo.thermal')
ax3.set_title('Thermal')
ax3.set_xlabel('Date')
ax3.set_ylabel('Depth (m)')
ax3.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax3)
cbar.set_label('Speed (m/s)')
cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
#plt.tight_layout()


ax4 = fig.add_subplot(3,2,4)
mappable = ax4.scatter(x = The_ADCP_Before_Gap.index, y = 'depth', data = The_ADCP_Before_Gap,  s=4, c='speed', cmap='cmo.haline')
ax4.set_title('Haline')
ax4.set_xlabel('Date')
ax4.set_ylabel('Depth (m)')
ax4.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax4)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
#plt.tight_layout()


ax5 = fig.add_subplot(3,2,5)
mappable = ax5.scatter(x = The_ADCP_Before_Gap.index, y = 'depth', data = The_ADCP_Before_Gap,  s=4, c='speed', cmap='cmo.matter')
ax5.set_title('Matter')
ax5.set_xlabel('Date')
ax5.set_ylabel('Depth (m)')
ax5.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax5)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
#plt.tight_layout()


ax6 = fig.add_subplot(3,2,6)
mappable = ax6.scatter(x = The_ADCP_Before_Gap.index, y = 'depth', data = The_ADCP_Before_Gap,  s=4, c='speed', cmap='cmo.tempo')
ax6.set_title('Tempo')
ax6.set_xlabel('Date')
ax6.set_ylabel('Depth (m)')
ax6.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax6)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))

plt.tight_layout()


#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/Choosing_cmap.png',bbox_inches='tight',dpi=400)




#%%
fig = plt.figure(figsize=(15,12))
ax1 = fig.add_subplot(3,1,1)
plot_ADCP(The_ADCP, 'Test1', ax1)

ax2 = fig.add_subplot(3,1,2)
plot_ADCP(The_ADCP_Before_Gap, 'Test2', ax2)

ax3 = fig.add_subplot(3,1,3)
plot_ADCP(The_ADCP_Before_Gap, 'Test3', ax3)

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/all_before_after.png',bbox_inches='tight',dpi=400)
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/all_before_after_thermal.png',bbox_inches='tight',dpi=400)


#%%
fig = plt.figure(figsize = (10,3))

# Plot all 2017 ADCP data
ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP_17.index, y = The_ADCP_17.depth, s=1.5,
                       c=The_ADCP_17.speed, cmap='cmo.tempo', marker='s')
ax1.set_title('2017 ADCP Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
fig.autofmt_xdate()
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/all_2017.png',bbox_inches='tight',dpi=400)


#%%
fig = plt.figure(figsize = (10,3))

# Plot all 2018 ADCP data
ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP_18.index, y = The_ADCP_18.depth, s=1.5,
                       c=The_ADCP_18.speed, cmap='cmo.tempo', marker='s')
ax1.set_title('2018 ADCP Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
fig.autofmt_xdate()
plt.tight_layout()

plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/all_2018.png',bbox_inches='tight',dpi=400)


#%%
fig = plt.figure(figsize = (10,3))

# Plot all 2019 ADCP data
ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP_19.index, y = The_ADCP_19.depth, s=1.5,
                       c=The_ADCP_19.speed, cmap='cmo.tempo', marker='s')
ax1.set_title('2019 ADCP Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
fig.autofmt_xdate()
plt.tight_layout()

plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/all_2019.png',
            bbox_inches='tight',dpi=400)












#%%
fig = plt.figure(figsize = (15,6))

# Plot all
ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP.index, y = 'depth', data = The_ADCP,  marker='s', s=14, c='speed', cmap='cmo.tempo')
ax1.set_title('All ADCP Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
fig.autofmt_xdate()
plt.tight_layout()
#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/all.png',bbox_inches='tight',dpi=400)

#%%
fig = plt.figure(figsize = (15,4))

ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP_Before_Gap.index, y = 'depth', data = The_ADCP_Before_Gap,  s=15, c='speed', cmap='cmo.tempo', marker='s')
ax1.set_title('Pre Gap ADCP Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
fig.autofmt_xdate()
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/Before.png',bbox_inches='tight',dpi=400)

#%%
fig = plt.figure(figsize = (15,6))

ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP_After_Gap.index, y = 'depth', data = The_ADCP_After_Gap,  s=9.7, c='speed', cmap='cmo.tempo', marker='s')
ax1.set_title('Post Gap ADCP Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
fig.autofmt_xdate()
cbar.set_ticks(np.arange(0,1.62,0.2))

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/After.png',bbox_inches='tight',dpi=400)


#%%

fig = plt.figure(figsize = (15,6))

ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP_janfebmar_19.index, y = 'depth', data = The_ADCP_janfebmar_19,  s=9.7, c='speed', cmap='cmo.tempo', marker='s')
ax1.set_title('January-March 2019 ADCP Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
plt.xlim('2018-12-31','2019-03-05')
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
#cbar.ax.invert_yaxis()
fig.autofmt_xdate()
cbar.set_ticks(np.arange(0,1.62,0.2))

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/janfebmar_19.png',bbox_inches='tight',dpi=400)



#%%

fig = plt.figure(figsize = (25,3))

ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP_after19gap.index, y = 'depth', data = The_ADCP_after19gap,  s=1.9, c='speed', cmap='cmo.tempo', marker='s')
ax1.set_title('After 2019 Gap ADCP Current Velocity at Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
plt.xlim('2019-02-18', '2019-03-05')
#cbar.ax.invert_yaxis()
fig.autofmt_xdate()
cbar.set_ticks(np.arange(0,1.62,0.2))
plt.tight_layout()

#plt.savefig('Documents/Classes/OCNG491/THEMO/All_start-19_01_29/Time_series/ADCP_plots/after_19_long_gap.png',bbox_inches='tight',dpi=400)






























#%%

The_ADCP_Deep = pd.read_csv('Documents/Classes/OCNG491/THEMO/Data_tabs225/Deep_m11/',
                  parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)


fig = plt.figure(figsize = (10,5))

# Plot all
ax1 = fig.add_subplot(1,1,1)
mappable = ax1.scatter(x = The_ADCP.index, y = 'depth', data = The_ADCP,  s=0.3, c='speed', cmap='cmo.tempo', marker='s')
ax1.set_title('All ADCP Current Velocity at Depths', fontsize=10)
ax1.set_xlabel('Date')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Speed (m/s)')
ax1.tick_params(axis='both', which='major', labelsize=8)
#cbar.ax.invert_yaxis()
cbar.set_ticks(np.arange(0,1.62,0.2))
plt.tight_layout()



