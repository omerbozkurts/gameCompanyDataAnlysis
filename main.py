import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)

df = pd.read_csv('persona.csv')
df.head()

df['SOURCE'].nunique()
df['SOURCE'].value_counts()

df['PRICE'].nunique()

df.groupby('PRICE')['PRICE'].count()

df.groupby('COUNTRY')['PRICE'].count()

df.groupby('COUNTRY')['PRICE'].sum()

df.groupby('SOURCE')['SOURCE'].count()

df.groupby('COUNTRY')['PRICE'].mean()

df.groupby('SOURCE')['PRICE'].mean()

df.groupby(['COUNTRY','SOURCE'])['PRICE'].mean()

df.groupby(['COUNTRY','SOURCE','SEX','AGE'])['PRICE'].mean()

agg_df = df.groupby(['COUNTRY','SOURCE','SEX','AGE'])['PRICE'].mean().reset_index().sort_values('PRICE',ascending=False)

agg_df.reset_index(inplace = True)

bins = [0,18,23,30,40,df['AGE'].max()]
labels = ['0_18','19_23','24_30','31_40','41_70']
agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins, labels = labels)
agg_df.head()



persona = pd.DataFrame()
persona['customer_level_based'] = [val[0].upper() + '_' + val[1].upper() + '_' + val[2].upper() + '_' + val[5] for val in agg_df.values]

persona['PRICE'] = agg_df['PRICE']

persona.groupby('PRICE').head()

persona['segment'] = pd.qcut(persona['PRICE'], 4, labels=['D','C','B','A'])

persona.head()

new_user = 'TUR_ANDROID_FEMALE_31_40'
persona[persona['customer_level_based'] == new_user]

new_user = 'FRA_IOS_FEMALE_31_40'
persona[persona['customer_level_based'] == new_user]