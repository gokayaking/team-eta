import pandas as pd 
from scipy import stats

# import needed libraries
import pandas as pd  # for data frame creation
import os  # for OS interface (to get/change directory)
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
import numpy as np




pd.set_option('display.max_columns', None)

filename = "NBATeamDataGameLogs.xlsx"
df = pd.read_excel( "./data/" + filename )
df.columns
pre_df=df[df.Date<"07/30/2020"]
post_df=df[df.Date>"07/30/2020"]


# print( "\n" )

# columns = ['FG%', 'FT', 'FTA', 'FT%', 'DRtg', 'FTr', 'TS%', 'eFG%', 'FT/FGA']
# for column in columns:
#     doTTestForAllTeams( pre_df, post_df, column )


# (e) Histogram: use Python and/or R to produce the analyses; include the tables and graphics output in your assignment file (PDF).
# y=pre_df['DRtg']
# x=sd['Country']
# plt.bar(x, y, width=0.5)
# plt.xlabel('Country')
# plt.ylabel('Gold Medals')
# plt.title('Scatterplot of Population and Gold Medals', color='red')
# plt.show()

comparedf = pre_df["DRtg"]
comparedf["DRtgAfter"] = post_df["DRtg"]

 
sns.boxplot( x=df["species"], y=df["sepal_length"] )
#sns.plt.show()
