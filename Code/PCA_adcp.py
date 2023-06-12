#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:25:39 2019

@author: jacobarnold

Purpose:
    PCA of ADCP data
    
"""

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%


adcp2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcp2D_F.csv', 
                       index_col=0)
adcpU2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcpU2D_F.csv', 
                       index_col=0)
adcpV2D_F = pd.read_csv('Documents/Classes/THEMO/TABS225m09/Data/adcpV2D_F.csv', 
                       index_col=0)

# To keep the date reference around
date_index = pd.date_range(start='2017-07-25 14:07:00', end='2019-05-30 13:37:00', periods=32352)

#%%

z_data = stats.zscore(adcp2D_F).T
z_data = pd.DataFrame(z_data)
z_data = z_data.dropna(axis=0)
z_data = np.array(z_data)
#%%

mean_vec = np.mean(z_data, axis=0)
cov_mat = (z_data - mean_vec).T.dot((z_data - mean_vec))/(z_data.shape[0]-1)


#%%

from sklearn.decomposition import PCA

test_z2 = pd.DataFrame(test_z)
test_z3 = test_z2.dropna(axis=0)

pca = PCA(n_components=2)
pca.fit(test_z3)
pca.get_covariance(test_z3)
pca.get_covariance()

# Covariance
covariance = pca.get_covariance()

# Score
score = pca.score(test_z3)

# Transform
transform = pca.transform(test_z3)









