#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Transform cols
for col in ['neighbourhood', 'neighbourhood_group', 'room_type', 'host_id']:
    df[col] = df[col].astype('category')

df['last_review'] = pd.to_datetime(df['last_review'], format="%Y/%m/%d")

#Replace 0s with mean and handle null values
df['price'] = df['price'].replace(0, np.NaN)
df['price'] = df['price'].fillna(df.groupby('neighbourhood_group')['price'].transform('mean'))
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
df['last_review'] = df['last_review'].fillna(0)
df['name'].fillna('unknown', inplace = True)
df['host_name'].fillna('unknown', inplace = True)

#Handling outliers
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
ub = Q3+(1.5*IQR)
lb = Q1-(1.5*IQR)
df = df[(df.price>lb) & (df.price<ub)]
