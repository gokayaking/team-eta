# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:14:46 2020

@author: johnn
"""

import pandas as pd
import scipy.stats as stats
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt

df = pd.read_csv("data/NBA Team Data Game Logs.csv")
df = df.sort_values(by=['Season','Date'], ascending = False)
df = df.reset_index(drop = True)
df = df.drop(df.columns[[0, 1, 2, 3, 4, 5]], axis=1)

df_2019 = df.iloc[344:, :]
df_pre = df.iloc[81:344, :]
df_post = df.iloc[:81, :]

result = stats.f_oneway(df_2019, df_pre, df_post)


stats = ['FG%', 'FT', 'FTA', 'FT%', 'DRtg', 'FTr', 'TS%', 'eFG%', 'FT/FGA']

for i in range(9):
    print('Stat: ' + stats[i])
    print('F: ' + str(result[0][i]))
    print('P Value: ' + str(result[1][i]) + "\n")
    
    
left = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
plt.bar(left, result[1], tick_label = stats, width = .8, color = ['red', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'green'])
plt.xlabel('Statistics')
plt.ylabel('P Value')
plt.title('NBA Team ANOVA Test P Values')
plt.show()
    
left = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
plt.bar(left, result[0], tick_label = stats, width = .8, color = ['red', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'green'])
plt.xlabel('Statistics')
plt.ylabel('F Value')
plt.title('NBA Team ANOVA Test F Values')


