# team-eta
Project repository for team Eta

You main python code and files will be on inside 
main folder. Then if you are using any particular libraries, 
they will go into lib\ folder. If you are using data, then data 
files will go into data\ folder. Finally create a Readme file 
which contains all the instructions on how to use your script. You can put this readme file in main folder as well.


Describe_Teams.py 

Description - prints summary level statistics for the 4 teams
Input - NBA Team Data Game Logs.xlsx
Output - output of summary level statistics 


MeanCompare_AllTeams.py 

Description - prints mean for statistics for all teams
Input - NBA Team Data Game Logs.xlsx
Output - output of summary level statistics 


TTest_Teams.py 

Description - Performs T Test for key statistics for 4 teams to compare pre and post covid
Input - NBA Team Data Game Logs.xlsx
Output - output of summary level statistics 


TTest_AllTeams.py 

Description - Performs T Test for key statistics for all teams to compare pre and post covid
Input - NBA Team Data Game Logs.xlsx
Output - output of summary level statistics for all teams.



NBA_TEAM_PRE-POST_COVID_correlation.py

Description - HEATMAP INDEX -Predicts Correlation coefficients for available variables for all teams to pre and post covid data.
              xgboost algorithm is used for classification problem, 80% data is used for training and 20% data is used for testing.  
Input - NBA Team Data Game Logs.xlsx - in the code change the file path and run the code.
Output - HEATMAP INDEX for pre and post covid dataset.
         XGBOOST algorithm - Prediction accuracy ,Recall,Precision ,confusion matrix and classification report.
                
