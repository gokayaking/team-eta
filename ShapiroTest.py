import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plot


# do Shapiro Test and Display Histogram
# Select the correct print statement if using player or team data
def doShapiroForPre( df, columnName ): 
    results = stats.shapiro( df[columnName])
    print( " Shapiro Test for pre-COVID Teams for statistic:", columnName, " ", results )
    # print("Shapiro Test for pre-COVID Players for statistic:", columnName, " ", results)
    plot.hist(df[columnName])
    plot.title('Pre-COVID ' + columnName + ' distribution')
    plot.show()
    

def doShapiroForPost( df, columnName ): 
    results = stats.shapiro( df[columnName])
    print( " Shapiro Test for post-COVID Teams for statistic:", columnName, " ", results )
    # print("Shapiro Test for post-COVID Players for statistic:", columnName, " ", results)
    plot.hist(df[columnName])
    plot.title('Post-COVID ' + columnName + ' distribution')
    plot.show()

pd.set_option('display.max_columns', None)

filename = "NBA Team Data Game Logs.xlsx" # Team level data
# filename = "NBA Player Game Log Data.xlsx" #Player level data
df = pd.read_excel( "./data/" + filename )
pre_df=df[df.Date<"07/30/2020"]
post_df=df[df.Date>"07/30/2020"]


print( "\n" )

# Shapiro Wilk Test
columns = ['FG%', 'FT', 'FTA', 'FT%', 'DRtg', 'FTr', 'TS%', 'eFG%', 'FT/FGA']
for column in columns:
    doShapiroForPre(pre_df, column)
    doShapiroForPost(post_df, column)
    print ("\n")


