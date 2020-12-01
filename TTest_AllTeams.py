import pandas as pd 
from scipy import stats


# do T Test and Log
def doTTestForAllTeams( df_before, df_after, columnName ): 
    results = stats.ttest_ind( df_before[columnName], df_after[columnName], equal_var=True )
    print( " T Test for All Teams for statistic:", columnName, " ", results )


pd.set_option('display.max_columns', None)

filename = "NBA Team Data Game Logs.xlsx"
df = pd.read_excel( "./data/" + filename )
pre_df=df[df.Date<"07/30/2020"]
post_df=df[df.Date>"07/30/2020"]


print( "\n" )

columns = [ 'FG%', 'FT', 'FTA', 'FT%', 'FTr', 'TS%', 'eFG%', 'DRtg' ]
for column in columns:
    doTTestForAllTeams( pre_df, post_df, column )


