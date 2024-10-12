#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("Diabetes Missing Data.csv")


# In[3]:


data.head(5)


# In[4]:


data.info()


# In[5]:


data.describe()


# In[6]:


data.shape


# In[7]:


data.isnull().sum()


# In[8]:


data.set_index('Glucose', inplace=True)


# In[9]:


data


# In[10]:


new_data =  data.fillna(0)


# In[11]:


new_data.head(4)


# In[12]:


new_data = data.fillna({
    
    'Skin_Fold' : 27.0,
    'Serum_Insulin': 175.0,
    'BMI' : 33.4
})


# In[13]:


new_data


# In[14]:


new_data = data.fillna(method="ffill")


# In[15]:


new_data


# In[16]:


new_data.isnull().sum()


# In[17]:


new_data = data.fillna(method="bfill")


# In[18]:


new_data


# In[19]:


new_data.isnull().sum()


# In[20]:


new_data = data.fillna(method="ffill", limit=1)


# In[21]:


new_data


# In[22]:


new_data = data.interpolate()


# In[23]:


new_data


# In[24]:


new_data = data.dropna()
new_data


# In[25]:


new_data.shape


# In[26]:


new_data = data.dropna(how='all')


# In[27]:


new_data


# In[28]:


new_data = data.dropna(thresh=1)


# In[29]:


new_data


# # Handling missing data 
# 
# # replacing values

# In[34]:


new_data = data.replace(33.6,np.NaN)
new_data


# In[36]:


new_data = data.replace([33.6, 47],np.NaN)
new_data


# In[37]:


new_data = data.replace({
    
    'Diastolic_BP': 64.0,
    'Diabetes_Pedigree': 0.672,
    'Age': 50.0
    
},np.NaN)
new_data


# In[38]:


new_data.isnull().sum()


# In[45]:


new_data = data.replace({
    
    48.0 : 54.0,
    60.0 : 'Amit'
    
})
new_data


# # using regex

# In[53]:


new_data = data.replace('[A-Za-z]','', regex =True)
new_data


# In[ ]:


new_data = data.replace({
    
    'Diastolic_BP' : '[A-Za-z]',
    'BMI' : '[A-Za-z]'
}), '', regex=True)
new_data


# In[56]:


data = pd.DataFrame({
    'score':['exceptional','average','good','poor','average','exceptional'],
    'student': ['rob','maya','parthiv','tom','julian','erica']
})
data


# In[57]:


data.replace(['poor','average','good','exceptional'],[1,2,3,4])


# In[ ]:




