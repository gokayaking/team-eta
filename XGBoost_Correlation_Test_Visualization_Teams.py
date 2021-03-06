#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import pandas as pd
# Read source data
df = pd.read_excel(r"C:\GitHub\team-eta\data\NBA Team Data Game Logs.xlsx")
df.head()


# In[4]:


#Plot Heatmap to find the correlation

import matplotlib.pyplot as plt

corr = df.corr()
# plot the heatmap
plt.figure(figsize = (14,5))
sns.heatmap(corr, 
     xticklabels=corr.columns,
       yticklabels=corr.columns)


# In[5]:


df.dtypes


# In[6]:


#convert object type to numeric type.
cat_columns = df.select_dtypes(['object']).columns

df[cat_columns] = df[cat_columns].apply(lambda x: x.astype('category'))

df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)


# In[7]:


df.dtypes


# In[8]:


import matplotlib.pyplot as plt

corr = df.corr()
# plot the heatmap
plt.figure(figsize = (14,5))
sns.heatmap(corr, 
     xticklabels=corr.columns,
       yticklabels=corr.columns,cmap='coolwarm',
 annot=True)


# In[9]:


import seaborn as sns
import pandas as pd
# Read source data
df = pd.read_excel(r"C:\Users\e7crpmf\Downloads\NBATeamDataGameLogs.xlsx")
df.head()
df_precovid=df[df.Date<"07/30/2020"]
df_postcovid=df[df.Date>"07/30/2020"]


# In[10]:


df_precovid.dtypes


# In[11]:


df_postcovid.dtypes


# In[12]:


#convert object type to numeric type for precovid
cat_columns = df_precovid.select_dtypes(['object']).columns

df_precovid[cat_columns] = df_precovid[cat_columns].apply(lambda x: x.astype('category'))

df_precovid[cat_columns] = df_precovid[cat_columns].apply(lambda x: x.cat.codes)


# In[13]:


#convert object type to numeric type for postcovid
cat_columns = df_postcovid.select_dtypes(['object']).columns

df_postcovid[cat_columns] = df_postcovid[cat_columns].apply(lambda x: x.astype('category'))

df_postcovid[cat_columns] = df_postcovid[cat_columns].apply(lambda x: x.cat.codes)


# In[14]:


#Precovid heat map.
import matplotlib.pyplot as plt

corr = df_precovid.corr()
# plot the heatmap
plt.figure(figsize = (14,5))
sns.heatmap(corr, 
     xticklabels=corr.columns,
       yticklabels=corr.columns,cmap='coolwarm',
 annot=True)


# In[15]:


#Postcovid heat map.
import matplotlib.pyplot as plt
#corr = df_postcovid.corr()
corr = df_postcovid.drop(['Attendance','Season'],axis=1).corr()
# plot the heatmap
plt.figure(figsize = (14,5))
sns.heatmap(corr, 
     xticklabels=corr.columns,
       yticklabels=corr.columns,cmap='coolwarm',
 annot=True)


# In[16]:


df_postcovid.head()


# In[17]:


df_postcovid = df_postcovid.drop(['Date'],axis=1)


# In[18]:


df_postcovid.head()


# In[19]:


df_precovid = df_precovid.drop(['Date','Attendance','Season'],axis=1)


# In[20]:


df_precovid.head()


# In[21]:


df_merge = pd.concat([df_postcovid,df_precovid])


# In[22]:


len(df_merge)


# In[23]:


len(df_postcovid)


# In[24]:


len(df_precovid)


# In[25]:


# pip install xgboost executed this command in command prompt .


# In[26]:


from sklearn.model_selection import train_test_split, cross_val_predict
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

#Split data set to train the model on subset of data and validate it on the other subset/hold dataset.
x= df_merge.drop(['W/L'],axis=1) #X axis is with all the variables with target
y=df_merge["W/L"]    #Y axis with only target variable.
X_train,X_test,y_train,y_test= train_test_split(x,y,test_size=0.20,random_state=1) #training dataset will be 80% and testing/hold dataset will be 20%


# In[ ]:





# In[40]:


from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,classification_report
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

def xgbModel_Validate(X_train,X_test,y_train,y_test,xgboost):
    xgboost.fit(X_train, y_train)
    preds = xgboost.predict(X_test)
        #accuracy = (preds == y_test).sum().astype(float) / len(preds)*100
    print("Prediction accuracy using optimal parameters is: %3.2f" % (accuracy_score(y_test,preds)*100))
    print("Prediction Recall using optimal parameters is: %3.2f" % (recall_score(y_test,preds)*100))
    print("Prediction Precision using optimal parameters is: %3.2f" % (precision_score(y_test,preds)*100))
    print("Confusion Matrix :")
    print(confusion_matrix(y_test,preds))
    print("Classification report",classification_report(y_test,preds))
    return preds


#xgboost hyper parameter - classifier - Classification problem.
xgboost_hyp= XGBClassifier(subsample = 1.0,min_child_weight = 5,max_depth = 3,gamma = 5,colsample_bytree = 1.0)
#xgbModel_Validate(X_train,X_test,y_train,y_test,xgboost_hyp)
preds=xgbModel_Validate(X_train,X_test,y_train,y_test,xgboost_hyp)


# In[41]:


from sklearn.metrics import confusion_matrix
#labels = ['Win', 'Loss']
cm = confusion_matrix(y_test,preds)
print(cm)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion matrix of the classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Actual values')
plt.ylabel('Predicted')
plt.show()
#list_1 = cm.tolist()
#df = pd.DataFrame(list_1,column='Confusion_Matrix', index=False)
#DataFrame.plot.pie(y='Confusion_Matrix')


# In[ ]:





# In[28]:


import matplotlib.pyplot as plt

plt.bar(y_test,preds)
plt.title('title name')
plt.xlabel('xAxis name')
plt.ylabel('yAxis name')
plt.show()


# In[29]:


#!pip install pandas-profiling - ran this in Cmd prompt.

from pandas_profiling import ProfileReport
prof = ProfileReport(df_merge)


# In[30]:


prof


# In[ ]:




