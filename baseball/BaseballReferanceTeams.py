import csv
import os

# Import needed libraries for reading and parsing Web pages:
#  pip install pybaseball
from pybaseball import team_batting
from pybaseball import team_batting_bref

from pybaseball import batting_stats_bref

def processPlayerStats( year ):
      print( "Processing  player stats for ", year )
      df = batting_stats_bref(  year )
      filename = "player" + year + ".csv"
      df.to_csv ( filename, index = False, header=True ) 

def processTeamStats( year ):
      print( "Processing  team stats for ", year )
      df = team_batting(  year )
      filename = "team" + year + ".csv"
      df.to_csv ( filename, index = False, header=True ) 


processPlayerStats( "2019" ) 
processPlayerStats( "2020" ) 

processTeamStats( "2019" ) 
processTeamStats( "2020" ) 



# old
# get the Yankees (NYY) player batting stats for 2020
# dataplayer2020 = team_batting_bref('NYY', 2020 )
# dataplayer2020.to_csv (r'nyy_players_2020.csv', index = False, header=True)

# get the Yankees (NYY) player batting stats for for 2019
# dataplayer2019 = team_batting_bref('NYY', 2019)
# dataplayer2019.to_csv (r'nyy_players_2019.csv', index = False, header=True)