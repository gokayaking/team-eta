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
#print(prePlayer)
postPlayer= playerData[playerData.Date>'07/30/2020']
#print(postPlayer)

players= ['Aaron Gordon','CJ McCollum','Dennis Schroder','Donovan Mitchell','Dorian Finney-Smith','Doug McDermott','Evan Fournier','Jakob Poeltl','Jarrett Allen','Joe Ingles','Montrezl Harrell','Myles Turner','Nerlens Noel','Rudy Gay','Terrence Ross']

playerNominal=['Season','Player','Date','Home/Away','Opp','Win/Loss','Tm']


import seaborn as sn
import matplotlib.pyplot as plt


for player in players :
    playerData= pd.read_excel("NBA Player Game Log Data.xlsx")
    prePlayer= playerData[playerData.Date<"07/30/2020"]
    postPlayer= playerData[playerData.Date>'07/30/2020']
    individualPre= prePlayer[prePlayer['Player']== player]
    individualPost= postPlayer[postPlayer['Player']== player]
    preNumeric= individualPre
    postNumeric= individualPost
    for nom in playerNominal:
        del preNumeric[nom]
        del postNumeric[nom]
        #del postNumeric['Attendance']
    imatrixPre= preNumeric.corr()
    imatrixPost= postNumeric.corr()
    print(imatrixPost)
    print(imatrixPre)
    sn.heatmap(imatrixPost, annot=True)
    plt.title("Post COVID Correlation Table for" + " " + player)
    plt.show()
    sn.heatmap(imatrixPre, annot=True)
    plt.title("Pre COVID Correlation Table for" + " " + player)
    plt.show()
    





