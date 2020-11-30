#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:18:57 2020

@author: gtrailv5
"""

import csv
import os

import pandas as pd 
from scipy import stats

os.getcwd()
os.chdir("/Users/gtrailv5/CS504/GitHub/team-eta/data")
os.getcwd()

playerData= pd.read_excel("NBA Player Game Log Data.xlsx")

prePlayer= playerData[playerData.Date<"07/30/2020"]
print(prePlayer)
postPlayer= playerData[playerData.Date>'07/30/2020']
print(postPlayer)
"""del playerData['Unnamed: 13']
del playerData['Unnamed: 14']"""

"""print(playerData)"""

playerData= playerData.dropna()
prePlayer= prePlayer.dropna()
postPlayer= postPlayer.dropna()

print(playerData)
print(prePlayer)
print(postPlayer)

players= ['Aaron Gordon','CJ McCollum','Dennis Schroder','Donovan Mitchell','Dorian Finney-Smith','Doug McDermott','Evan Fournier','Jakob Poeltl','Jarrett Allen','Joe Ingles','Montrezl Harrell','Myles Turner','Nerlens Noel','Rudy Gay','Terrence Ross']

playerNominal=['Season','Player','Date','Home/Away','Opp','Win/Loss','Tm']

#playerNumeric= playerData
preNumeric= prePlayer
#postNumeric= postPlayer

for nom in playerNominal:
   # del playerNumeric[nom]
    del preNumeric[nom]
   # del postNumeric[nom]
del preNumeric['Tm']

print(preNumeric)

#corrMatrix= playerNumeric.corr()
preMatrix= preNumeric.corr()

print(preMatrix)

import seaborn as sn
import matplotlib.pyplot as plt

sn.heatmap(preMatrix, annot=True)
plt.show()