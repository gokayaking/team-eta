#!/usr/bin/env python
# coding: utf-8

# In[8]:


import seaborn as sns
import pandas as pd
# Read source data
df = pd.read_excel(r"C:\Users\e7crpmf\Downloads\NBATeamDataGameLogs.xlsx")
df.head()


# In[9]:


#Plot Heatmap to find the correlation

import matplotlib.pyplot as plt

corr = df.corr()
# plot the heatmap
plt.figure(figsize = (14,5))
sns.heatmap(corr, 
     xticklabels=corr.columns,
       yticklabels=corr.columns)


# In[10]:


df.dtypes


# In[11]:


#convert object type to numeric type.
cat_columns = df.select_dtypes(['object']).columns

df[cat_columns] = df[cat_columns].apply(lambda x: x.astype('category'))

df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)


# In[6]:


df.dtypes


# In[12]:


import matplotlib.pyplot as plt

corr = df.corr()
# plot the heatmap
plt.figure(figsize = (14,5))
sns.heatmap(corr, 
     xticklabels=corr.columns,
       yticklabels=corr.columns,cmap='coolwarm',
 annot=True)


# In[15]:


import seaborn as sns
import pandas as pd
# Read source data
df = pd.read_excel(r"C:\Users\e7crpmf\Downloads\NBATeamDataGameLogs.xlsx")
df.head()
df_precovid=df[df.Date<"07/30/2020"]
df_postcovid=df[df.Date>"07/30/2020"]


# In[16]:


df_precovid.dtypes


# In[17]:


df_postcovid.dtypes


# In[18]:


#convert object type to numeric type for precovid
cat_columns = df_precovid.select_dtypes(['object']).columns

df_precovid[cat_columns] = df_precovid[cat_columns].apply(lambda x: x.astype('category'))

df_precovid[cat_columns] = df_precovid[cat_columns].apply(lambda x: x.cat.codes)


# In[19]:


#convert object type to numeric type for postcovid
cat_columns = df_postcovid.select_dtypes(['object']).columns

df_postcovid[cat_columns] = df_postcovid[cat_columns].apply(lambda x: x.astype('category'))

df_postcovid[cat_columns] = df_postcovid[cat_columns].apply(lambda x: x.cat.codes)


# In[20]:


#Precovid heat map.
import matplotlib.pyplot as plt

corr = df_precovid.corr()
# plot the heatmap
plt.figure(figsize = (14,5))
sns.heatmap(corr, 
     xticklabels=corr.columns,
       yticklabels=corr.columns,cmap='coolwarm',
 annot=True)


# In[21]:


#Postcovid heat map.
import matplotlib.pyplot as plt

corr = df_postcovid.corr()
# plot the heatmap
plt.figure(figsize = (14,5))
sns.heatmap(corr, 
     xticklabels=corr.columns,
       yticklabels=corr.columns,cmap='coolwarm',
 annot=True)


# In[ ]:




