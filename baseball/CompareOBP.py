import csv
import os

import pandas as pd 
from scipy import stats

df_team2019 = pd.read_csv( "team2019.csv" )


df_team2020 = pd.read_csv( "team2020.csv" )


pd.set_option('display.max_columns', None)

print( df_team2019 )

print( df_team2019.info() )

my_list = list(df_team2019 )
print( my_list )

df_team2019_obp = df_team2019[['Team','OBP','OBP+']]
df_team2020_obp = df_team2020[['Team','OBP','OBP+']]

df_team2019_obp_five = df_team2019_obp.describe() 
df_team2020_obp_five = df_team2020_obp.describe() 


print( stats.shapiro( df_team2019_obp['OBP'] ))
print( stats.shapiro( df_team2020_obp['OBP'] ))

res = stats.ttest_ind( df_team2019_obp['OBP'], df_team2020_obp['OBP'], equal_var=True )
print( res )
