#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[22]:


data = pd.read_csv('City wise.csv')


# In[23]:


data


# In[24]:


g = data.groupby('city')
g


# In[25]:


for city, city_data in g:
    print(city)
    print(city_data)


# In[26]:


g.get_group('Mumbai')


# In[27]:


g.max()


# In[28]:


g.min()


# In[29]:


g.mean()


# In[30]:


g.describe()


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
g.plot()


# In[32]:


g = data.groupby('event')
g


# In[35]:


g.max()


# In[ ]:





# In[ ]:




