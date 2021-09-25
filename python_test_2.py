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