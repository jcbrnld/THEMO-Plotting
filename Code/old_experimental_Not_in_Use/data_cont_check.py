#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:36:27 2019

@author: Jacob

Purpose:
    Check small datasets to see if irregularities 
    or drops are still progressing
"""

import pandas as pd

#flour_data = pd.read_csv('Documents/Classes/OCNG491/THEMO/Temporary-small-data_checking/Flour_18_12_01-19-01-25.csv', 
  #          parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)
#still no data transmission since 2018-12-17


#%%

ADCP = pd.read_csv('Documents/Classes/OCNG491/THEMO/Data_tabs225/ABC_17_07_26-19_01_21/start_to_19-01-29ADCP.csv',
                   parse_dates=[[0,1]], infer_datetime_format = True, index_col=0)