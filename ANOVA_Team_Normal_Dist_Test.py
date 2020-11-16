# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:30:12 2020

@author: johnn
"""

import pandas as pd
import scipy.stats as stats
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
import os

os.getcwd()
os.chdir('/Users/Omar/Documents/GitHub/team-eta')
os.getcwd()

df = pd.read_excel("data/NBA Team Data Game Logs with attendance.xlsx")
df = df.sort_values(by=['Season','Date'], ascending = False)
df = df.reset_index(drop = True)
df = df.drop(df.columns[[0, 1, 2, 3, 4, 5]], axis=1)

df_2019 = df.iloc[344:, :]
df_pre = df.iloc[81:344, :]
df_post = df.iloc[:81, :]

for i in range(9):
    qqplot(df_2019[stats[i]], line = 's')
    plt.show()
    qqplot(df_pre[stats[i]], line = 's')
    plt.show()
    qqplot(df_post[stats[i]], line = 's')
    plt.show()
