#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as datetime
import calendar
import matplotlib.pyplot as plt
import plotly.express as px


# ## "Какой русский не любит парсить?" (Н.В. Гоголь)

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


#Даём выборку под БД

df2_marshrut = df2[['№ маршрута']]
df2_n_mar_valid = df2[['№ маршрута', '№ валидатора']]

df2_marshrut.to_csv(r'C:\Users\Zodiac\Desktop\Саше\маршрут.csv', sep=';')
df2_n_mar_valid.to_csv(r'C:\Users\Zodiac\Desktop\Саше\маршрут_валидатор.csv', sep=';')


# In[10]:


df2.corr()


# In[11]:


#Смотрим на реперную точку выборки

check = df2['дата прохода'].min()
print(check)


# In[12]:


#Работаем над фреймом для получения пиковых часов

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


#Получаем разбивку по рабочим/выходным дням

df2['день_недели'] = df2['дата прохода'].dt.dayofweek
weekend=[6,7]

df2['признак_выходного'] = df2['день_недели'].isin(weekend)*1


# In[17]:


#Сплитим основной фрейм на два парта под нужды анализа (выходной-рабочий)

df_wnd = df2.loc[(df2['признак_выходного']==1)]
df_act = df2.loc[~(df2['признак_выходного']==1)]


# ## отработка выходных дней

# In[18]:


#Формируем фрейм под пиковые часы по выходным
df_wnd_date = df_wnd.groupby(['час'],as_index=False)['признак_выходного'].count().sort_values(                                                    by=['признак_выходного'],ascending=False).reset_index(drop=True)

#Формируем фрейм под способы оплаты по выходным

df_wnd_ticket = df_wnd.groupby(['тип билета'],as_index=False)['признак_выходного'].count().sort_values(                                                    by=['признак_выходного'],ascending=False).reset_index(drop=True)

print(f'{df_wnd_date.head(3)}'+ '\n'*4  + f'{df_wnd_ticket.head(3)}', sep = '\n')


# In[19]:


#Выбираем пиковые часы по выходным
df_wnd_top_date = df_wnd_date.loc[(df_wnd_date['признак_выходного']>40)]
df_wnd_top_date = df_wnd_top_date.groupby(['час'])['признак_выходного'].sum()

#Выбираем наиболее популярные способы оплаты по выходным
df_wnd_top_ticket = df_wnd_ticket.loc[(df_wnd_ticket['признак_выходного']>100)]
df_wnd_top_ticket = df_wnd_top_ticket.groupby(['тип билета'])['признак_выходного'].sum()


# ## Отработка будних дней

# In[20]:


#Формируем фрейм под пиковые часы
df_act_date = df_act.groupby(['час'],as_index=False)['признак_выходного'].count().sort_values(                                                    by=['признак_выходного'],ascending=False).reset_index(drop=True)

#Формируем фрейм под способы оплаты

df_act_ticket = df_act.groupby(['тип билета'],as_index=False)['признак_выходного'].count().sort_values(                                                    by=['признак_выходного'],ascending=False).reset_index(drop=True)

print(f'{df_act_date.head(3)}'+ '\n'*4  + f'{df_act_ticket.head(3)}', sep = '\n')


# In[21]:


#Выбираем пиковые часы
df_act_top_date = df_act_date.loc[(df_act_date['признак_выходного']>100)]
df_act_top_date = df_act_top_date.groupby(['час'])['признак_выходного'].sum()

#Выбираем наиболее популярные способы оплаты
df_act_top_ticket = df_act_ticket.loc[(df_act_ticket['признак_выходного']>500)]
df_act_top_ticket = df_act_top_ticket.groupby(['тип билета'])['признак_выходного'].sum()


# In[22]:


df_wnd_top_ticket.plot(figsize=(8,3), grid='on', title='Наиболее популярные способы оплаты в выходные',color='green')


# In[26]:


df_wnd_top_date.plot(figsize=(5,3), grid='on', title='Пиковые часы в выходные',color='orange')


# In[24]:


df_wnd_top_ticket.plot(figsize=(8,3), grid='on', title='Наиболее популярные способы оплаты в будние',color='green')


# In[27]:


df_wnd_top_date.plot(figsize=(5,3), grid='on', title='Пиковые часы в будние',color='orange')


# In[ ]:




