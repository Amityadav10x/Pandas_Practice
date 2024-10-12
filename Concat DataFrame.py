#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


india_weather = pd.DataFrame({
    
    "city":['mumbai','delhi','banglore'],
    "temperature":[32,45,30],
    "humidity":[80,60,78]
})
india_weather


# In[4]:


us_weather = pd.DataFrame({
    
    "city":['newyork','chicago','orlando'],
    "temperature":[21,25,20],
    "humidity":[68,50,58]
})
us_weather


# In[5]:


df = pd.concat([india_weather,us_weather])
df


# In[6]:


df = pd.concat([india_weather, us_weather], ignore_index=True)


# In[7]:


df


# In[10]:


df = pd.concat([india_weather, us_weather] , keys=['india','us'])
df


# In[11]:


df.loc['india']


# In[12]:


df.loc['us']


# In[41]:


temperature_df = pd.DataFrame ({
    
    "city":['newyork','chicago','orlando'],
    "temperature":[21,25,20],
    
})
temperature_df


# In[33]:


windspeed_df = pd.DataFrame ({
    "city": ['mumbai','delhi','banglore'],
    "windspeed": [7,12,9],
})
windspeed_df


# In[35]:


df = pd.concat([temperature_df, windspeed_df], axis = 1)
df


# In[36]:


windspeed_df = pd.DataFrame ({
    "city": ['delhi','mumbai'],
    "windspeed": [7,12],
})
windspeed_df


# In[39]:


df = pd.concat([temperature_df, windspeed_df], axis =1)
df


# In[42]:


temperature_df


# In[43]:


s = pd.Series(['Rain','Dry','Rain'], name='event')
s


# In[47]:


df = pd.concat([temperature_df, s ],axis=1)
df


# In[ ]:




