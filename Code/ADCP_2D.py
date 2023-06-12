#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:16:28 2019

@author: jacobarnold

purpose: 
Figure out how to make ADCP data two dimensional

"""
import numpy as np
import pandas as pd
from math import pi
#%%

adcp = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp.csv', 
            parse_dates=[[0,1]],
            infer_datetime_format=True,
            index_col=0
            )
adcp.rename(columns = {'d_stamp_t_stamp':'date',
                           'depth[m]':'depth',
                           'direction[deg]':'direction',
                           'speed[m/s]':'speed'},
                            inplace=True)

adcp.drop('threshold', axis=1, inplace=True)
adcp.drop('const_err', axis=1, inplace=True)
adcp.speed[adcp.speed > 3] = np.nan
adcp.depth[adcp.depth > 91] = np.nan
adcp.depth[adcp.depth < 7] = np.nan
adcp.dropna(axis=0, inplace=True)

adcp['counter'] = np.arange(len(adcp))


#%%
def Give_UV (dataframe, dir_col, spd_col):
    '''
    Calculate U (east) and V (north) velocity components from a dataframe containing 
    direction and speed measurements.
    
    Parameters
    ----------
    dataframe: var
        The dataframe that will be processed
        dataframe must contain the dir_col and spd_col parameters
    dir_col: str
        The column in dataframe that contains directional data
        Directional data are expected to be in degrees from north growing
        in the clockwise direction: 
               0/360
                -N-
         270-W-      -E- 90
                -S-
                180
    spd_col: str
        The column in dataframe that contains speed data
    '''
    dataframe['dir_rad'] = dataframe[dir_col]/180 * pi
    dataframe['U_Component'] = dataframe[spd_col] * (np.sin(dataframe['dir_rad']))
    dataframe['V_Component'] = dataframe[spd_col] * (np.cos(dataframe['dir_rad']))
    
#%%
Give_UV(adcp, 'direction', 'speed')
    


#%%
# This is the line of code that makes the matrix

adcp2 = adcp[['depth','speed']]
adcp_u2 = adcp[['depth','U_Component']]
adcp_v2 = adcp[['depth','V_Component']]

adcpN = adcp2.groupby([adcp.index, 'depth']).sum().unstack('depth')
adcp_uN = adcp_u2.groupby([adcp_u2.index, 'depth']).sum().unstack('depth')
adcp_vN = adcp_v2.groupby([adcp_v2.index, 'depth']).sum().unstack('depth')

# Figure out how to groupby with direction for adcpN to create 3D variable. 
# This will require some interpolation

adcpN.to_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D.csv')
adcp_uN.to_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp_u2D.csv')
adcp_vN.to_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp_v2D.csv')



#%%

adcp_array = np.array(adcpN)

adcp_u_array = np.array(adcp_uN)

adcp_v_array = np.array(adcp_vN)


#%%

np.savetxt('Documents/Classes/THEMO/TABS225m09/Data/adcp_array_2d.csv', X=adcp_array, delimiter=',')
np.savetxt('Documents/Classes/THEMO/TABS225m09/Data/adcp_u_array_2d.csv', X=adcp_u_array, delimiter=',')
np.savetxt('Documents/Classes/THEMO/TABS225m09/Data/adcp_v_array_2d.csv', X=adcp_v_array, delimiter=',')





















#%%

Depth = np.array(adcp['depth'], dtype='float64')
Speed = np.array(adcp['speed'])
U_vel = np.array(adcp['U_Component'])
V_vel = np.array(adcp['V_Component'])
dates = np.array(adcp.index)

#%%
#first = adcp[:][2:49]

depths = Depth[0:43]
speed_1 = Speed[0:43]
dates_1 = dates[0:43]

test = np.vstack((depths, speed_1))
speed_2 = Speed[43:86]
test=np.vstack((test,speed_2))

speed_3 = Speed[86:129]
test=np.vstack((test,speed_3))
#%%
# I need a while loop to make this iterate through correctly

def add_2d(begin, end):
    global test
    end = end+42
#    while end < 785506
    test = np.vstack((test, Speed[begin:end]))
    
#%%

add_2d(129, 172)
    

    
    
    
    



