import csv
import os

import pandas as pd 
from scipy import stats

pd.set_option('display.max_columns', None)

compareColumn = "FG%"
filename = "NBA Team Data Game Logs.xlsx"
df = pd.read_excel( "./data/" + filename )
pre_df=df[df.Date<"07/30/2020"]
post_df=df[df.Date>"07/30/2020"]

pre_df_lal = pre_df[pre_df['Team'] == "LAL" ]
pre_df_mil = pre_df[pre_df['Team'] == "MIL" ]
pre_df_ind = pre_df[pre_df['Team'] == "IND" ]
pre_df_den = pre_df[pre_df['Team'] == "DEN" ]

post_df_lal = post_df[post_df['Team'] == "LAL" ]
post_df_mil = post_df[post_df['Team'] == "MIL" ]
post_df_ind = post_df[post_df['Team'] == "IND" ]
post_df_den = post_df[post_df['Team'] == "DEN" ]

lal_res = stats.ttest_ind( pre_df_lal['FG%'], post_df_lal['FG%'], equal_var=True )
mil_res = stats.ttest_ind( pre_df_mil['FG%'], post_df_mil['FG%'], equal_var=True )
ind_res = stats.ttest_ind( pre_df_ind['FG%'], post_df_ind['FG%'], equal_var=True )
den_res = stats.ttest_ind( pre_df_den['FG%'], post_df_den['FG%'], equal_var=True )

print( "\n" )
print( " lil res ", lal_res )
print( " mil res ", mil_res )
print( " ind res ", ind_res )
print( " den res ", den_res )
print( "\n" )

all_res = stats.ttest_ind( pre_df['FG%'], post_df['FG%'], equal_var=True )
print( " all res ", all_res )
print( "\n" )

all_res = stats.ttest_ind( pre_df['DRtg'], post_df['DRtg'], equal_var=True )
print( " all drtg ", all_res )
print( "\n" )