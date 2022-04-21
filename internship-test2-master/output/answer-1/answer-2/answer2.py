#!/usr/bin/env python
# coding: utf-8

# In[11]:




import pandas as pd

df = pd. read_csv ("main.csv")
df["sales_amount"]=df["sales_quantity"].where(df["unit"]!="pcs", df["product_description"].str.split("-",expand=True)[1].astype("float")*                                               df["sales_quantity"])
df.to_csv('answer1.csv')


# In[9]:





# In[ ]:




