#!/usr/bin/env python
# coding: utf-8

# 
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset Euro_2012_stats_TEAM

# In[3]:


pd.read_csv("Euro_2012_stats_TEAM.csv")


# ### Step 3. Assign it to a variable called euro12.

# In[4]:


euro12=pd.read_csv("Euro_2012_stats_TEAM.csv")


# ### Step 4. Select only the Goal column.

# In[7]:


euro12['Goals']


# ### Step 5. How many team participated in the Euro2012?

# In[63]:


euro12['Team'][0:16]


# ### Step 6. What is the number of columns in the dataset?

# In[55]:


len(euro12.columns)


# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[80]:


discipline=euro12[['Team','Yellow Cards','Red Cards']]
discipline


# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[85]:


discipline.sort_values('Red Cards')
discipline.sort_values('Yellow Cards')


# ### Step 9. Calculate the mean Yellow Cards given per Team

# In[88]:


discipline['Yellow Cards'].mean()


# ### Step 10. Filter teams that scored more than 6 goals

# In[117]:


euro12[euro12['Goals'] > 6]


# ### Step 11. Select the teams that start with G

# In[145]:


euro12[euro12['Team'].str.contains("^G")]


# ### Step 12. Select the first 7 columns

# In[169]:


euro12[['Team','Goals','Shots on target','Shots off target','Shooting Accuracy','% Goals-to-shots','Total shots (inc. Blocked)']]


# ### Step 13. Select all columns except the last 3.

# In[183]:


euro12[euro12.columns[0:32]]


# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[224]:


euro12['Shooting Accuracy'][[2,7,12]]


# ### Step 15. Use apply method on Goal Column to make a new column called Performance, using following conditions
# 
# 1. If Goals are less than or equal to 2, peformance is **Below Avg**
# 2. If Goals are more than 2 and less than or equal to 5, peformance is **Average**
# 3. If Goals are more than 5 and less than or equal to 10, peformance is **Above Average**
# 4. If Goals are more than 10 then peformance is **Excellent**

# In[188]:





# In[ ]:




