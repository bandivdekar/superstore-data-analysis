#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[40]:


import pandas as pd
import seaborn as sbn
import numpy as np


# # Loading the Dataset

# In[41]:


df = pd.read_csv(r'C:\Users\HP\Downloads\superstoredataset.csv')
df


# In[42]:


df.head()


# In[43]:


df.tail()


# # Statistical Summary of the Dataset

# In[44]:


df[['Sales', 'Quantity', 'Discount', 'Profit']].describe()


# # Data Imputation for Missing Values

# Fill missing values with 0

# In[45]:


df['Sales_new'] = df['Sales'].fillna(0)


# Fill missing values with the median of the column

# In[46]:


df['Sales_new1'] = df['Sales'].fillna(df['Sales'].median())


# # Data Visualization

# Count plot for Category

# In[47]:


sbn.countplot(data=df, x='Category')


# In[48]:


df.info()


# In[49]:


# Convert date columns to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])


# In[51]:


df['Order Date']


# In[53]:


df['Ship Date']


# In[54]:


#cheack for missing values 
missing_values=df.isnull().sum()


# In[55]:


missing_values


# In[56]:


# Drop unnecessary columns for analysis
df_clean = df.drop(columns=['Row ID', 'Postal Code', 'Product ID'])


# In[57]:


df_clean


# In[58]:


# Ensure data types are appropriate and remove duplicates
df_clean = df_clean.drop_duplicates()


# In[59]:


df_clean


# In[60]:


# Summary after cleaning
cleaning_summary = {
    "Missing Values": missing_values[missing_values > 0],
    "Data Shape After Cleaning": df_clean.shape
}


# In[61]:


cleaning_summary


# In[63]:


# Descriptive statistics for numerical features
desc_stats = df_clean[['Sales', 'Quantity', 'Discount', 'Profit']].describe()


# In[64]:


desc_stats


# In[66]:


# Aggregated metrics
total_sales = df_clean['Sales'].sum()
total_profit = df_clean['Profit'].sum()
avg_discount = df_clean['Discount'].mean()
avg_quantity = df_clean['Quantity'].mean()


# In[67]:


summary_metrics = {
    "Total Sales": total_sales,
    "Total Profit": total_profit,
    "Average Discount": avg_discount,
    "Average Quantity per Order Line": avg_quantity
}


# In[68]:


desc_stats, summary_metrics


# In[69]:


# Top categories and sub-categories by total sales and profit
category_sales_profit = df_clean.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
subcategory_sales_profit = df_clean.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)


# In[70]:


category_sales_profit


# In[71]:


subcategory_sales_profit


# In[72]:


# Regional performance
region_performance = df_clean.groupby('Region')[['Sales', 'Profit']].sum().sort_values(by='Profit', ascending=False)


# In[73]:


region_performance


# In[74]:


# State performance (top 10 by profit)
top_states_profit = df_clean.groupby('State')[['Sales','Profit']].sum().sort_values(by='Profit', ascending=False).head(10)


# In[75]:


top_states_profit


# In[76]:


category_sales_profit, subcategory_sales_profit, region_performance, top_states_profit


# In[ ]:




