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



sns.set_style( "whitegrid" )
sns.boxplot( x=df["Type Of Play"], y=df["DRtg"], showfliers = False).set_title( "Comparing Defensive Rating for All Teams" )
plt.show()

sns.set_style( "whitegrid" )
sns.boxplot( x=df["Type Of Play"], y=df["FTA"], showfliers = False).set_title( "Comparing Free Throw Attempts for All Teams" )
plt.show()

sns.set_style( "whitegrid" )
sns.boxplot( x=df["Type Of Play"], y=df["FTr"], showfliers = False).set_title( "Comparing Free Throw Attempts Rate for All Teams" )
plt.show()

sns.set_style( "whitegrid" )
sns.boxplot( x=df["Type Of Play"], y=df["PF"], showfliers = False).set_title( "Comparing Personal Fouls for All Teams" )
plt.show()


