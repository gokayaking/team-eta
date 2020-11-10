import csv
import os

import pandas as pd 
from scipy import stats

pd.set_option('display.max_columns', None)

compareColumn = "FG%"
pre_filename = "NBATeamDataGameLogs_Pre.csv"
post_filename = "NBATeamDataGameLogs_Post.csv"

pre_df = pd.read_csv( "./data/" + pre_filename )
post_df = pd.read_csv( "./data/" + post_filename )

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


lal_res = stats.ttest_ind( pre_df_lal['FG%'], post_df_lal['FG%'], equal_var=True )
print( " pre_df_lal_five ", pre_df_lal_five )
print( " post_df_lal_five ", post_df_lal_five )

mil_res = stats.ttest_ind( pre_df_mil['FG%'], post_df_mil['FG%'], equal_var=True )
print( " pre_df_mil_five ", pre_df_mil_five )
print( " post_df_mil_five ", post_df_mil_five )

ind_res = stats.ttest_ind( pre_df_ind['FG%'], post_df_ind['FG%'], equal_var=True )
print( " pre_df_ind_five ", pre_df_ind_five )
print( " post_df_ind_five ", post_df_ind_five )

den_res = stats.ttest_ind( pre_df_den['FG%'], post_df_den['FG%'], equal_var=True )
print( " pre_df_den_five ", pre_df_den_five )
print( " post_df_den_five ", post_df_den_five )

print( " lil res ", lal_res )
print( " mil res ", mil_res )
print( " ind res ", ind_res )
print( " den res ", den_res )
