# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:32:30 2020

@author: johnn
"""
import pandas as pd
import scipy.stats as stats


df = pd.read_excel("data/NBA Player Game Log Data.xlsx")
df = df.sort_values(by=['Season','Date'], ascending = False)
df = df.drop(df.columns[[0, 1, 2, 3, 4, 5]], axis=1)
df = df.reset_index(drop = True)

df_2019 = df.iloc[1161:, :]
df_2019 = df_2019.dropna()
df_pre = df.iloc[194:1161, :]
df_pre = df_pre.dropna()
df_post = df.iloc[:194, :]
df_post = df_post.dropna()

result = stats.f_oneway(df_2019, df_pre, df_post)


stats = ['FG%', 'FT', 'FTA', 'FT%', 'TS%', 'eFG%', 'DRtg']

for i in range(7):
   print(stats[i] + ': ' + 'F-ratio: ' + str(result[0][i]) + ' ' + 'P-value: ' + str(result[1][i]))
    
import matplotlib.pyplot as plt
    
left = [1, 2, 3, 4, 5, 6, 7]

plt.bar(left, result[1], tick_label = stats, width = .8, color = ['red', 'green', 'green', 'red', 'red', 'red', 'green'])
plt.xlabel('Statistics')
plt.ylabel('P Value')
plt.title('NBA Player ANOVA Test P Values')

plt.show()

plt.bar(left, result[0], tick_label = stats, width = .8, color = ['red', 'green', 'green', 'red', 'red', 'red', 'green'])
plt.xlabel('Statistics')
plt.ylabel('F Value')
plt.title('NBA Team ANOVA Test F Values')

plt.show()