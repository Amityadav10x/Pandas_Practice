#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


wheather_data = {
    'day': ['1/1/2017','1/2/2018','1/3/2019','1/4/2020','1/5/2021','1/6/2022'],
    'temperature' :[21,23,54,34,23,43],
    'event':['rain','sunny','snow','rain','sunny','snow']
}

df = pd.DataFrame(wheather_data)


# In[9]:


df


# In[10]:


df.columns


# In[11]:


df.temperature


# In[13]:


df.event


# In[14]:


type(df['event'])


# In[15]:


df['temperature'].max()


# In[16]:


df.describe()


# In[17]:


df.info()


# In[18]:


df[df.temperature>=32]


# In[20]:


df[df.temperature==df.temperature.min()]


# In[24]:


df[['day','temperature']][df.temperature==df.temperature.max()]


# In[25]:


df.index


# In[31]:


df.set_index('day',inplace = True)


# In[30]:


df.reset_index('day')


# In[ ]:




