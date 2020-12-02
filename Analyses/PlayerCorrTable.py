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
os.chdir("../data/")
os.getcwd()

playerData= pd.read_csv("NBA Player Game Log Data.csv")

<<<<<<< HEAD
del playerData['Unnamed: 13']
del playerData['Unnamed: 14']

print(playerData)

playerData= playerData.dropna()

print(playerData)

playerNominal=['Season','Player','Date','Home/Away','Opp','Win/Loss']

playerNumeric= playerData

for nom in playerNominal:
    del playerNumeric[nom]


print(playerNumeric)

corrMatrix= playerNumeric.corr()

print(corrMatrix)
=======
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
<<<<<<< HEAD
>>>>>>> parent of f19fa74... Charts for Every Player
=======
>>>>>>> parent of f19fa74... Charts for Every Player

import seaborn as sn
import matplotlib.pyplot as plt

<<<<<<< HEAD
<<<<<<< HEAD
sn.heatmap(corrMatrix, annot=True)
=======
sn.heatmap(preMatrix, annot=True)
>>>>>>> parent of f19fa74... Charts for Every Player
=======
sn.heatmap(preMatrix, annot=True)
>>>>>>> parent of f19fa74... Charts for Every Player
plt.show()