# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:59:13 2020

@author: johnn
"""
import pandas as pd
import scipy.stats as stats
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
import os

pd.set_option('display.max_columns', None)

filename = "NBA Team Data Game Logs.xlsx" # Team level data
#filename = "NBA Player Game Log Data.xlsx" #Player level data
data = pd.read_excel( "./data/" + filename )
pre_COVID = data[data.Date<"07/30/2020"]
post_COVID = data[data.Date>"07/30/2020"]

stats = ['FG%', 'FT', 'FTA', 'FT%', 'DRtg', 'FTr', 'TS%', 'eFG%', 'FT/FGA']

for i in range(9):
    qqplot(pre_COVID[stats[i]], line = 's')
    plt.title('Pre Covid ' + stats[i])
    plt.show()
    
for i in range(9):
    qqplot(post_COVID[stats[i]], line = 's')
    plt.title('Post Covid ' + stats[i])
    plt.show()