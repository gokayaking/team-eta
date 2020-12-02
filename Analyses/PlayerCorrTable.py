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

import seaborn as sn
import matplotlib.pyplot as plt

sn.heatmap(corrMatrix, annot=True)
plt.show()