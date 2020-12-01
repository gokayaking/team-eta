import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plot


# do Shapiro Test and Display Histogram
# Select the correct print statement if using player or team data
def doShapiroForPre(df, stat): 
    results = stats.shapiro(df[stat])
    print( " Shapiro Test for pre-COVID Teams for statistic:", stat, " ", results )
    #print("Shapiro Test for pre-COVID Players for statistic:", stat, " ", results)
    plot.hist(df[stat])
    plot.title('Pre-COVID ' + stat + ' distribution')
    plot.show()
    

def doShapiroForPost(df, stat): 
    results = stats.shapiro(df[stat])
    print( " Shapiro Test for post-COVID Teams for statistic:", stat, " ", results )
    #print("Shapiro Test for post-COVID Players for statistic:", stat, " ", results)
    plot.hist(df[stat])
    plot.title('Post-COVID ' + stat + ' distribution')
    plot.show()

pd.set_option('display.max_columns', None)

filename = "NBA Team Data Game Logs.xlsx" # Team level data
#filename = "NBA Player Game Log Data.xlsx" #Player level data
data = pd.read_excel( "./data/" + filename )
pre_COVID = data[data.Date<"07/30/2020"]
post_COVID = data[data.Date>"07/30/2020"]


print( "\n" )

# Shapiro Wilk Test
columns = ['FG%', 'FT', 'FTA', 'FT%', 'FTr', 'DRtg', 'PF', 'TS%', 'eFG%', 'FT/FGA', '3P', '3PA', '3P%']
for column in columns:
    doShapiroForPre(pre_COVID, column)
    doShapiroForPost(post_COVID, column)
    print ("\n")

# Shapiro Wilk Test
columns = ['FG%', 'FT', 'FTA', 'FT%',  'FTr', 'DRtg', 'PF', 'TS%', 'eFG%', 'FT/FGA', '3P', '3PA', '3P%']
for column in columns:
    doShapiroForPost(data, column)
    print ("\n")


