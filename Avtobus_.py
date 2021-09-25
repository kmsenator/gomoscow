#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as datetime
import calendar

import plotly.express as px


# In[2]:


url = 'https://drive.google.com/file/d/1ItTzwYAQ6uVTTIRriKCBDlbEEaYPaXTI/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path, delimiter = ';', header = None)


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


df.head(5)


# In[6]:


df2=df.copy(deep = True)


# In[7]:


df2.columns = ['тип билета','№ билета','№ кристалла','дата прохода','время прохода','№ маршрута','№ выхода','№ валидатора']


# In[8]:


df2.head(10)


# In[9]:


df2_marshrut = df2[['№ маршрута']]
df2_n_mar_valid = df2[['№ маршрута', '№ валидатора']]

df2_marshrut.to_csv(r'C:\Users\Zodiac\Desktop\Саше\маршрут.csv', sep=';')
df2_n_mar_valid.to_csv(r'C:\Users\Zodiac\Desktop\Саше\маршрут_валидатор.csv', sep=';')


# In[10]:


df2.corr()


# In[11]:


check = df2['дата прохода'].min()
print(check)


# In[12]:


df2['дата прохода'] = pd.to_datetime(df2['дата прохода'], format = '%d.%m.%Y')
df2[['час','минуты','секунды']] = df2['время прохода'].str.split(':', expand=True)
df2=df2.drop(columns=['время прохода','секунды'])
df2=df2.sort_values(by=['дата прохода'], ascending=True)
df2.head()


# In[13]:


# df_road = df2
# df_road = df_road.drop_duplicates()
# df_road.count(axis=1)
# df_road = df_road.groupby(by=['тип билета']).count()
# px.scatter_3d(x='дата прохода', y='час', z='№ выхода',data_frame=df_road, size_max=0.4, opacity=1)


# In[14]:


# признак_выходного = datetime.datetime.today().weekday()
# календарь = pd.date_range(start=df2['дата прохода'].min(), end=df2['дата прохода'].max(),freq='D')


# In[15]:


# print(календарь)


# In[16]:


df2['день_недели'] = df2['дата прохода'].dt.dayofweek
weekend=[6,7]

df2['признак_выходного'] = df2['день_недели'].isin(weekend)*1


# In[17]:


df_wnd = df2.loc[(df2['признак_выходного']==1)]
df_act = df2.loc[~(df2['признак_выходного']==1)]


# In[18]:


df_wnd = df_wnd.groupby(['дата прохода', 'час'],as_index=False)['признак_выходного'].count().sort_values(                                                    by=['признак_выходного'],ascending=False).reset_index(drop=True)
df_wnd


# In[20]:


df_wnd_top = df_wnd[df_wnd['признак_выходного']>40]
df_wnd_top = df_wnd_top.groupby(['час'])['признак_выходного'].sum()
df_wnd_top


# In[21]:


df_act = df_act.groupby(['дата прохода', 'час'],as_index=False)['признак_выходного'].count().sort_values(                                                    by=['признак_выходного'],ascending=False).reset_index(drop=True)
df_act


# In[23]:


df_act_top = df_act[df_act['признак_выходного']>40]
df_act_top = df_act_top.groupby(['час'])['признак_выходного'].sum()
df_act_top


# In[ ]:




