# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:32:30 2020

@author: johnn
"""
import pandas as pd
import scipy.stats as stats
import numpy as np


df = pd.read_excel("data/NBA Player Game Log Data.xlsx")
df = df.sort_values(by=['Season','Date'], ascending = False)
df = df.drop(df.columns[[0, 1, 2, 3, 4, 5, 6, 18]], axis=1)
df = df.reset_index(drop = True)

df_2019 = df.iloc[1161:, :]
df_2019 = df_2019.dropna()
df_pre = df.iloc[194:1161, :]
df_pre = df_pre.dropna()
df_post = df.iloc[:194, :]
df_post = df_post.dropna()

ANOVA = stats.f_oneway(df_2019, df_pre, df_post)
t_2019_2020 = stats.ttest_ind(df_2019, df_pre)
t_2020_post = stats.ttest_ind( df_pre, df_post)
t_2019_post = stats.ttest_ind(df_2019, df_post)


stats = ['FG%', 'FT', 'FTA', 'FT%', '3P', '3PA', '3P%', 'PF', 'TS%', 'eFG%', 'DRtg']

for i in range(11):
   print(stats[i] + ': ' + 'F-ratio: ' + str(ANOVA[0][i]) + ' ' + 'P-value: ' + str(ANOVA[1][i]))
   if ANOVA[1][i] < .05:
        print('2019/2020 Pre Covid T test: ' + str(t_2019_2020[1][i]))        
        print('2019/2020 Post Covid T test: ' + str(t_2019_post[1][i]))
        print('2020 Pre/Post Covid T test: ' + str(t_2020_post[1][i]))
   print()
    
import matplotlib.pyplot as plt
    
ind = np.arange(11)
plt.barh(ind, ANOVA[1], tick_label = stats)
plt.xlabel('Statistics')
plt.ylabel('P Value')
plt.title('NBA Player ANOVA Test P Values')
plt.axvline(x=.05, color='red')
plt.show()

ind = np.arange(6)  
width = .30
plt.bar(ind, [t_2019_2020[1][1], t_2019_2020[1][2], t_2019_2020[1][4], t_2019_2020[1][5], t_2019_2020[1][7], t_2019_2020[1][10]], width, label = '2019/2020')
plt.bar(ind + width, [t_2020_post[1][1], t_2020_post[1][2], t_2020_post[1][4], t_2020_post[1][5], t_2020_post[1][7], t_2020_post[1][10]], width, label = '2019/Post')
plt.bar(ind + (2 * width), [t_2019_post[1][1], t_2019_post[1][2], t_2019_post[1][4], t_2019_post[1][5], t_2019_post[1][7], t_2019_post[1][10]], width, label = '2020/Post')
plt.axhline(y=.05, xmin=0, xmax=3.5, color='red')

plt.xticks(ind + 2 * width / 3, ('FT', 'FTA', '3P', '3PA', 'PF', 'DRtg'))
plt.xlabel('Statistics')
plt.ylabel('P Value')
plt.title('NBA Team T Tests\' P Values')
plt.legend(loc='best')
plt.ylim(0, .5)
plt.show()