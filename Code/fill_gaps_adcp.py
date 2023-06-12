#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:01:47 2019

@author: jacobarnold

Purpose:
    Fill in all the gaps where there were no data with NaN
    Export the filled file to csv
    
"""

import pandas as pd

#%%

adcp2D = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D.csv',
                     infer_datetime_format=True,
                     index_col=0,
                     header=1,
                     skiprows=[2]
                     ).T


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

# Create the new date index with no missing values
date_index = pd.date_range(start='2017-07-25 14:07:00', end='2019-05-30 13:37:00', periods=32352)


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


# Create the filled dataframe
adcp2D_F = adcp2D.T.reindex(date_index).T
adcpU2D_F = adcpU2D.T.reindex(date_index).T
adcpV2D_F = adcpV2D.T.reindex(date_index).T
#%%
adcp2D_F.to_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D_F.csv')
adcpU2D_F.to_csv('Documents/Classes/THEMO/TABS225m09/Data/adcpU2D_F.csv')
adcpV2D_F.to_csv('Documents/Classes/THEMO/TABS225m09/Data/adcpV2D_F.csv')

