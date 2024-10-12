#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df1 = pd.DataFrame({
    
    "city":['mumbai','delhi','banglore'],
    "temperature":[21,13,35],
   
})
df1


# In[5]:


df2 = pd.DataFrame({
    
    "city":['newn york','delhi','toranto'],
    "humidity":[80,60,78]
})
df2


# In[10]:


df3 = pd.merge(df1,df2,on='city', how="inner", indicator=True)
df3


# In[11]:


df1 = pd.DataFrame({
    
    "city":['mumbai','delhi','banglore'],
    "temperature":[32,45,30],
    "humidity":[80,60,78]
})
df1


# In[12]:


df2 = pd.DataFrame({
    
    "city":['newyork','chicago','orlando'],
    "temperature":[21,25,20],
    "humidity":[68,50,58]
})
df2


# In[15]:


df3 = pd.merge(df1,df2,on="city", suffixes=('_left','_right'))
df3


# In[ ]:




