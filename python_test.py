import pandas as pd
import numpy as np
import datetime as datetime
import calendar

import plotly.express as px321

url = 'https://drive.google.com/file/d/1ItTzwYAQ6uVTTIRriKCBDlbEEaYPaXTI/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path, delimiter = ';', header = None)

df.columns

