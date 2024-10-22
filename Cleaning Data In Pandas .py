#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning in Pandas 

# In[1]:


import pandas as pd 


# In[2]:


df = pd.read_excel("Customer Call List.xlsx")
df


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()


# In[6]:


df = df.drop_duplicates()
df


# In[7]:


df = df.drop(columns = 'Not_Useful_Column')


# In[8]:


df


# In[9]:


df["Last_Name"].str.lstrip()


# In[10]:


df["Last_Name"].str.lstrip("...")


# In[11]:


df["Last_Name"].str.lstrip("/")


# In[12]:


df["Last_Name"].str.rstrip("_")


# In[13]:


df = df["Last_Name"] = df["Last_Name"].str.lstrip("...")
df = df["Last_Name"] = df["Last_Name"].str.lstrip("/")
df = df["Last_Name"] = df["Last_Name"].str.lstrip("_")


# In[14]:


df.info()


# In[15]:


df["Last_Name"] = df["Last_Name"].str.strip("123._/")


# In[16]:


df


# In[17]:


#df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')


# In[18]:


#df["Phone_Number"] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')


# In[19]:


#df['Phone_Number'].apply(lambda x: x[0:3]+ '-' + x[3:6]+ '-' + x[6:10])


# In[21]:


#df['Phone_Number'] = df['Phone_Number'].str.replace('Na', '')
#df


# In[23]:


df1 = df["Last_Name"] = df["Last_Name"].str.strip("123._/")


# In[24]:


df1


# In[44]:


data = pd.read_excel("Customer Call List.xlsx")
data


# In[45]:


data['Address'].str.split(',',2, expand = True)


# In[49]:


data[['Stree_Address','State','Zip_Code']] = data['Address'].str.split(',',2,expand=True)
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




