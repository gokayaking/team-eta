import pandas as pd 
from scipy import stats


# do T Test and Log
def doTTestForTeam( team, df_before, df_after, columnName ): 
    results = stats.ttest_ind( df_before[columnName], df_after[columnName], equal_var=True )
    print( " T Test for Team:", team, " for statistic:", columnName, " ", results )


filename = "NBA Team Data Game Logs.xlsx"
df = pd.read_excel( "./data/" + filename )
pre_df=df[df.Date<"07/30/2020"]
post_df=df[df.Date>"07/30/2020"]


print( "\n" )

teams = ['LAL','MIL','IND','DEN']
columns = [ 'FG%', 'FT', 'FTA', 'FT%', 'FTr', 'TS%', 'eFG%', 'DRtg' ]
for team in teams:
    pre_df_team = pre_df[pre_df['Team'] == team ]
    post_df_team = post_df[post_df['Team'] == team ]
    
    print( "\n" )
    for column in columns:
        doTTestForTeam( team, pre_df_team, post_df_team, column )


