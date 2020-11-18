import csv
import os

import pandas as pd 
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


pd.set_option('display.max_columns', None)

compareColumn = "FG%"
filename = "NBA Team Data Game Logs.xlsx"
df = pd.read_excel( "./data/" + filename )
pre_df=df[df.Date<"07/30/2020"]
post_df=df[df.Date>"07/30/2020"]

print( df.head(10))

pre_df_subset = pre_df[pre_df["Team", "FG%", "DRtg"]]
print( pre_df_subset.head() )
                      
                      
                       
print( pre_df_subset.head() )                       

pre_df['Day'] = pd.to_datetime(pre_df['Date'], format='%d%b%Y')
post_df['Day'] = pd.to_datetime(post_df['Date'], format='%d%b%Y')
                                      
pre_df_lal = pre_df[pre_df['Team'] == "LAL" ]
pre_df_mil = pre_df[pre_df['Team'] == "MIL" ]
pre_df_ind = pre_df[pre_df['Team'] == "IND" ]
pre_df_den = pre_df[pre_df['Team'] == "DEN" ]

post_df_lal = post_df[post_df['Team'] == "LAL" ]
post_df_mil = post_df[post_df['Team'] == "MIL" ]
post_df_ind = post_df[post_df['Team'] == "IND" ]
post_df_den = post_df[post_df['Team'] == "DEN" ]

pre_df_lal_five = pre_df_lal.describe() 
pre_df_mil_five = pre_df_mil.describe() 
pre_df_ind_five = pre_df_ind.describe() 
pre_df_den_five = pre_df_den.describe() 

post_df_lal_five = post_df_lal.describe() 
post_df_mil_five = post_df_mil.describe() 
post_df_ind_five = post_df_ind.describe() 
post_df_den_five = post_df_den.describe() 


print( " pre_df_lal_five ", pre_df_lal_five )
print( " post_df_lal_five ", post_df_lal_five )

print( " pre_df_mil_five ", pre_df_mil_five )
print( " post_df_mil_five ", post_df_mil_five )

print( " pre_df_ind_five ", pre_df_ind_five )
print( " post_df_ind_five ", post_df_ind_five )

print( " pre_df_den_five ", pre_df_den_five )
print( " post_df_den_five ", post_df_den_five )

# print( pre_df_lal.columns )
# table = pd.DataFrame(pre_df_lal)   
# print("Data Types of The Columns in Data Frame") 
# print(table.dtypes) 

# BOXPLOT 
# y-axis is dependent variable
sns.boxplot(  x=post_df_lal["Day"], y=post_df_lal["FG%"] )
plt.xlabel('Day')
plt.ylabel('Field Goal Percentage', color='red')
plt.title('Field Goal Percentage')
plt.show()
