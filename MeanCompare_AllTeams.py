import pandas as pd 


# do T Test and Log
def doMeanCompare( df_before, df_precovid, df_after, columnName ): 
    print( "\n" )
    print( "2018-2019           ", column, "mean for all teams", df_before[column].mean() )
    print( "2018-2019 pre-covid ", column, "mean for all teams", df_precovid[column].mean() )
    print( "2019-2020 covid     ", column, "mean for all teams", df_after[column].mean() )


compareColumn = "FG%"
filename = "NBA Team Data Game Logs.xlsx"
df = pd.read_excel( "./data/" + filename )
pre_df=df[df.Date<"07/30/2020"]
post_df=df[df.Date>="07/30/2020"]

pre_2018_2019_df = pre_df[pre_df.Season == "2018-19"]
pre_2019_2020_df = pre_df[pre_df.Season == "2019-20"]



columns = ['FG%', 'FT', 'FTA', 'FT%', 'DRtg', 'FTr', 'TS%', 'eFG%', 'FT/FGA']
for column in columns:
    doMeanCompare( pre_2018_2019_df, pre_2019_2020_df, post_df, column )






