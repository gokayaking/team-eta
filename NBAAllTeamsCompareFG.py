import csv
import os

import pandas as pd 
from scipy import stats

pd.set_option('display.max_columns', None)

compareColumn = "FG%"
filename = "NBA Team Data Game Logs.xlsx"
df = pd.read_excel( "./data/" + filename )
pre_df=df[df.Date<"07/30/2020"]
post_df=df[df.Date>="07/30/2020"]

pre_2018_2019_df = pre_df[pre_df.Season == "2018-19"]
pre_2019_2020_df = pre_df[pre_df.Season == "2019-20"]

#pre_2018_2019_df_fgpercent_mean = pre_2018_2019_df.mean()
#pre_2019_2020_df_fgpercent_mean = pre_2019_2020_df.mean()
#post_df_fgpercent_mean = post_df.mean()

#print( " 2018-2019 all teams mean", pre_2018_2019_df_fgpercent_mean)
#print( " 2019-2020 all teams mean", pre_2019_2020_df_fgpercent_mean)
#print( " 2019-2020 covid all teams mean", post_df_fgpercent_mean)


# pre_2018_2019_df_five = pre_2018_2019_df.describe() 
# pre_2019_2020_df_five = pre_2019_2020_df.describe() 

# print( " pre_df_lal_five ", pre_2018_2019_df_five )
# print( " post_df_lal_five ", pre_2019_2020_df_five )

all_2018_2019_fg_percent_mean = pre_2018_2019_df["FG%"].mean()
print( "2018-2019 FG% mean for all teams", all_2018_2019_fg_percent_mean)

all_2019_2020_fg_percent_mean = pre_2019_2020_df["FG%"].mean()
print( "2019-2020 pre-covid FG% mean for all teams", all_2019_2020_fg_percent_mean)

all_2019_2020_covid_fg_percent_mean = post_df["FG%"].mean()
print( "2019-2020 covid FG% mean for all teams", all_2019_2020_covid_fg_percent_mean)


all_2018_2019_dvtg_percent_mean = pre_2018_2019_df["DRtg"].mean()
print( "2018-2019 DRtg mean for all teams", all_2018_2019_dvtg_percent_mean)

all_2019_2020_dvtg_percent_mean = pre_2019_2020_df["DRtg"].mean()
print( "2019-2020 pre-covid DRtg mean for all teams", all_2019_2020_dvtg_percent_mean)

all_2019_2020_covid_dvtg_percent_mean = post_df["DRtg"].mean()
print( "2019-2020 covid DRtg mean for all teams", all_2019_2020_covid_dvtg_percent_mean)


drtg_2018_2019_ttest = stats.ttest_ind( all_2018_2019_dvtg_percent_mean, all_2019_2020_dvtg_percent_mean, equal_var=True )
print( " drtg_2018_2019_ttest ", drtg_2018_2019_ttest )
