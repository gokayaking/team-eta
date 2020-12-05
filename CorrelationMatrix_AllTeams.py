import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt  


filename = "NBA Team Data Game Logs.xlsx"
df = pd.read_excel( "./data/" + filename )
# pre_df=df[df.Date<"07/30/2020"]
# post_df=df[df.Date>="07/30/2020"]

# make smaller dataframe
df_small = df[[ 'FG%', 'FT%', 'DRtg', 'FTr', 'PF']]

# generate matrix
correlation_matrix = df_small.corr()

# plot it
sns.heatmap( correlation_matrix, annot = True ).set_title( "NBA Correlation Matrix for All Teams" )
plt.show()


# ScatterPlots


# Create the default pairplot
# sns.pairplot( df )

# for specific columns
# sns.pairplot( data=df, y_vars=['ProductionBudget'], x_vars=['WorldwideGross', 'RunningTime', 'RottenTomatoesRating','IMDBRating'])

