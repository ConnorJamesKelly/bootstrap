#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:31:33 2023

@author: connorkelly
"""

#%% From wed 10/18
import pandas as pd


dat = pd.DataFrame({"handspan": [20, 20, 19, 24.2, 20, 20.2, 21.5, 17, 19.5, 
            21.5, 18, 18, 20.5, 20, 20.3, 21.5, 19, 20.4, 22.7, 22.9, 17, 23, 
            23.8, 22, 21.5, 21.5]})




boot_means = []

for i in range(10000):
    
    boot_sample = dat.sample(26, replace = True)

    boot_means.append(float(boot_sample.mean()))



#%% New work (Wed 10/25)

from plotnine import *




df = pd.DataFrame(boot_means)
df.columns=["x"]

# or

df = pd.DataFrame({'x': boot_means})


(
 ggplot(df, aes(x = "x")) +
 geom_histogram()
 )


#%%

stat = "median"


boot_stat = []

for i in range(10000):
    
    boot_sample = dat.sample(26, replace = True)

    boot_stat.append(float(boot_sample.median()))


df = pd.DataFrame({'x': boot_stat})


(
 ggplot(df, aes(x = "x")) +
 geom_histogram()
 )


#%%



boot_stat = []
stat = "std dev"


for i in range(10000):
    
    boot_sample = dat.sample(26, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
        
    else:
        raise TypeError("Wrong statistic name")


df = pd.DataFrame({'x': boot_stat})



(
 ggplot(df, aes(x = "x")) +
 geom_histogram()
 )

#%%

import os

os.chdir("/Users/connorkelly/Downloads")

dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat["Combined Mileage (mpg)"]

n = len(dat)
n_boot = 10000
stat = "mean"

boot_stat = []
for i in range(n_boot):
    
    boot_sample = dat.sample(n, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
        
    else:
        raise TypeError("Wrong statistic name")

df = pd.DataFrame({'x': boot_stat})

(
 ggplot(df, aes(x = "x")) +
 geom_histogram()
 )






#HI!

















































