import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt  



pd.set_option('display.max_columns', None)

filename = "NBA Team Data Game Logs.xlsx"
df = pd.read_excel( "./data/" + filename )
print( df.columns )
# pre_df=df[df.Date<"07/30/2020"]
# post_df=df[df.Date>"07/30/2020"]

df['Type Of Play'] = np.where( df.Date<"07/30/2020", 'PreCovid', 'Covid' )
teams = ["LAL","MIL","IND","DEN"]
sns.set_style( "whitegrid" )

df_LAL = df[df['Team'] == "LAL" ]
sns.boxplot( x=df_LAL["Type Of Play"], y=df_LAL["DRtg"], showfliers = False, showmeans=True).set_title( "Comparing Defensive Rating for Lakers" )
plt.show()
sns.boxplot( x=df_LAL["Type Of Play"], y=df_LAL["FTA"], showfliers = False, showmeans=True).set_title( "Comparing Free Throw Attempts for Lakers" )
plt.show()
sns.boxplot( x=df_LAL["Type Of Play"], y=df_LAL["FTr"], showfliers = False, showmeans=True).set_title( "Comparing Free Throw Attempts Rate for Lakers" )
plt.show()

df_MIL = df[df['Team'] == "MIL" ]
sns.boxplot( x=df_MIL["Type Of Play"], y=df_MIL["DRtg"], showfliers = False, showmeans=True).set_title( "Comparing Defensive Rating for Bucks" )
plt.show()
sns.boxplot( x=df_MIL["Type Of Play"], y=df_MIL["FTA"], showfliers = False, showmeans=True).set_title( "Comparing Free Throw Attempts for Bucks" )
plt.show()
sns.boxplot( x=df_MIL["Type Of Play"], y=df_MIL["FTr"], showfliers = False, showmeans=True).set_title( "Comparing Free Throw Attempts Rate for Bucks" )
plt.show()

df_IND = df[df['Team'] == "IND" ]
sns.boxplot( x=df_IND["Type Of Play"], y=df_IND["DRtg"], showfliers = False, showmeans=True).set_title( "Comparing Defensive Rating for Pacers" )
plt.show()
sns.boxplot( x=df_IND["Type Of Play"], y=df_IND["FTA"], showfliers = False, showmeans=True).set_title( "Comparing Free Throw Attempts for Pacers" )
plt.show()
sns.boxplot( x=df_IND["Type Of Play"], y=df_IND["FTr"], showfliers = False, showmeans=True).set_title( "Comparing Free Throw Attempts Rate for Pacers" )
plt.show()

df_DEN = df[df['Team'] == "DEN" ]
sns.boxplot( x=df_DEN["Type Of Play"], y=df_DEN["DRtg"], showfliers = False, showmeans=True).set_title( "Comparing Defensive Rating for Nuggets" )
plt.show()
sns.boxplot( x=df_DEN["Type Of Play"], y=df_DEN["FTA"], showfliers = False, showmeans=True).set_title( "Comparing Free Throw Attempts for Nuggets" )
plt.show()
sns.boxplot( x=df_DEN["Type Of Play"], y=df_DEN["FTr"], showfliers = False, showmeans=True).set_title( "Comparing Free Throw Attempts Rate for Nuggets" )
plt.show()



# ax = sns.boxplot( x=df1["Type Of Play"], y=df1["DRtg"], showfliers = False).set_title( "Comparing Defensive Rating for All Teams" )
# ax.set_xticklabels(ax.get_xticklabels(),rotation=30)

