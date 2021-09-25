import pandas as pd
import numpy as np
import datetime as datetime
import calendar

import plotly.express as px


url = 'https://drive.google.com/file/d/1ItTzwYAQ6uVTTIRriKCBDlbEEaYPaXTI/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path, delimiter = ';', header = None)

df.columns


df.info()

df.head(5)

df2=df.copy(deep = True)

df2.columns = ['��� ������','� ������','� ���������','���� �������','����� �������','� ��������','� ������','� ����������']

df2.head(10)

df2_marshrut = df2[['� ��������']]
df2_n_mar_valid = df2[['� ��������', '� ����������']]

df2_marshrut.to_csv(r'C:\Users\Zodiac\Desktop\����\�������.csv', sep=';')
df2_n_mar_valid.to_csv(r'C:\Users\Zodiac\Desktop\����\�������_���������.csv', sep=';')

df2.corr()

check = df2['���� �������'].min()
print(check)

df2['���� �������'] = pd.to_datetime(df2['���� �������'], format = '%d.%m.%Y')
df2[['���','������','�������']] = df2['����� �������'].str.split(':', expand=True)
df2=df2.drop(columns=['����� �������','�������'])
df2=df2.sort_values(by=['���� �������'], ascending=True)
df2.head()

# df_road = df2
# df_road = df_road.drop_duplicates()
# df_road.count(axis=1)
# df_road = df_road.groupby(by=['��� ������']).count()
# px.scatter_3d(x='���� �������', y='���', z='� ������',data_frame=df_road, size_max=0.4, opacity=1)

# �������_��������� = datetime.datetime.today().weekday()
# ��������� = pd.date_range(start=df2['���� �������'].min(), end=df2['���� �������'].max(),freq='D')

# print(���������)

df2['����_������'] = df2['���� �������'].dt.dayofweek
weekend=[6,7]

df2['�������_���������'] = df2['����_������'].isin(weekend)*1

df_wnd = df2.loc[(df2['�������_���������']==1)]
df_act = df2.loc[~(df2['�������_���������']==1)]

df_wnd = df_wnd.groupby(['���� �������', '���'],as_index=False)['�������_���������'].count().sort_values(\
                                                    by=['�������_���������'],ascending=False).reset_index(drop=True)
df_wnd




df_wnd_top = df_wnd[df_wnd['�������_���������']>40]
df_wnd_top = df_wnd_top.groupby(['���'])['�������_���������'].sum()
df_wnd_top