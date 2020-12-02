# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:31:14 2020

@author: johnn
"""

import pandas as pd
import scipy.stats as scipy

df = pd.read_excel("data/NBA Team Data Game Logs.xlsx")
df = df.sort_values(by=['Season','Date'], ascending = False)
df = df.reset_index(drop = True)
df = df.drop(df.columns[[0, 1, 2, 3, 4, 5]], axis=1)

df_2019 = df.iloc[344:, :]
df_pre = df.iloc[86:344, :]
df_post = df.iloc[:86, :]


stats = ['FG%', 'FT', 'FTA', 'FT%', 'DRtg', 'FTr', 'TS%', 'eFG%', 'FT/FGA']

for i in range(9):
        print(stats[i] + ': ')
        print(scipy.bartlett(df_2019[stats[i]], df_pre[stats[i]], df_post[stats[i]]))