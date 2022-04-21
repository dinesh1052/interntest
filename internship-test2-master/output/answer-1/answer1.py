#!/usr/bin/env python
# coding: utf-8

# In[8]:




import pandas as pd

df = pd. read_csv ("main.csv")

df ["price_new"] = df['price'].fillna(

df.groupby('product_description') ['price'].transform("mean")

)
df.to_csv('answer1.csv')


# In[ ]:




