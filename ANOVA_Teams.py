# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:14:46 2020

@author: johnn
"""

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("data/NBA Team Data Game Logs.xlsx")
df = df.sort_values(by=['Season','Date'], ascending = False)
df = df.reset_index(drop = True)
df = df.drop(df.columns[[0, 1, 2, 3, 4, 5, 19]], axis=1)

df_2019 = df.iloc[344:, :]
df_pre = df.iloc[86:344, :]
df_post = df.iloc[:86, :]

ANOVA = stats.f_oneway(df_2019, df_pre, df_post)
t_2019_2020 = stats.ttest_ind(df_2019, df_pre)
t_2020_post = stats.ttest_ind( df_pre, df_post)
t_2019_post = stats.ttest_ind(df_2019, df_post)


stats = ['FG%', 'FT', 'FTA', 'FT%', '3p', '3PA', '3P%', 'DRtg', 'FTr', 'TS%', 'eFG%', 'FT/FGA', 'PF']

for i in range(13):
    print(stats[i] + ': ' + 'F-ratio: ' + str(ANOVA[0][i]) + ' ' + 'P-value: ' + str(ANOVA[1][i]))
    if ANOVA[1][i] < .05:
        print('2019/2020 Pre Covid T test: ' + str(t_2019_2020[1][i]))        
        print('2019/2020 Post Covid T test: ' + str(t_2019_post[1][i]))
        print('2020 Pre/Post Covid T test: ' + str(t_2020_post[1][i]))
    print()
    
    
ind = np.arange(13)     
plt.barh(ind, ANOVA[1], tick_label = stats)
plt.xlabel('Statistics')
plt.ylabel('P Value')
plt.title('NBA Team ANOVA Test P Values')
plt.axvline(x=.05, color='red')

plt.show()
 

ind = np.arange(9)  
width = .2
plt.bar(ind, [t_2019_2020[1][1], t_2019_2020[1][2], t_2019_2020[1][3], t_2019_2020[1][5],t_2019_2020[1][6], t_2019_2020[1][7], t_2019_2020[1][8], t_2019_2020[1][11], t_2019_2020[1][12]], width, label = '2019/2020 Pre COVID')
plt.bar(ind + width, [t_2019_post[1][1], t_2019_post[1][2], t_2019_post[1][3], t_2019_post[1][5], t_2019_post[1][6], t_2019_post[1][7], t_2019_post[1][8], t_2019_post[1][11], t_2019_post[1][12]], width, label = '2019/Post COVID')
plt.bar(ind + (2 * width), [t_2020_post[1][1], t_2020_post[1][2], t_2020_post[1][3], t_2020_post[1][5], t_2020_post[1][6], t_2020_post[1][7], t_2020_post[1][8], t_2020_post[1][11], t_2020_post[1][12]], width, label = '2020 Pre/Post COVID')
plt.axhline(y=.05, xmin=0, xmax=3.5, color='red')

plt.xticks(ind + 2 * width / 3, ('FT', 'FTA', 'FT%', '3PA', '3P%', 'DRtg', 'FTr', 'FT/FGA', 'PF'))
plt.xlabel('Statistics')
plt.ylabel('P Value')
plt.title('NBA Team T Tests\' P Values')
plt.legend(loc='best')
plt.ylim(0, 1)
plt.show()
