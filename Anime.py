#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
data1 = pd.read_csv("Downloads/anime.csv")
data2=pd.read_csv('Downloads/rating.csv')
data1.head()
data2.head()


# In[7]:


data1.head()


# In[8]:


data2.head()


# In[9]:


data2.user_id.value_counts().sort_index(ascending=True)


# In[10]:


data1.isnull().sum()


# In[12]:


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[16]:


data1.rating.describe()


# In[18]:


plt.hist(data1.rating, bins=np.arange(1,11,0.5))
plt.xticks(np.arange(1,11,1))

plt.xlabel('Avg. ratings')
plt.ylabel('No.of anime')

plt.title('Average ratings of animes')
plt.show()


# In[19]:


anime_types = data1.type.value_counts()
anime_types


# In[20]:


anime_types.plot.pie(label = ' ', title = 'Anime Type')
plt.show()


# In[ ]:




