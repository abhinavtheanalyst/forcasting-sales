#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[31]:


df=pd.read_csv("train.csv")


# In[32]:


df


# In[33]:


df.head(2)


# # FORCASTING THE SALE OF SUPER MARKET

# In[34]:


df.tail()


# In[35]:


df.info()


# In[36]:


df.describe()


# In[37]:


df.isnull()


# In[38]:


df.isnull().sum()*100/len(df)


# In[39]:


df.isnull().sum()


# In[40]:


df['Postal Code']=df['Postal Code'].fillna(0)
df


# In[41]:


df.info()


# # Segments for value available

# In[42]:


seg=pd.DataFrame(df['Segment'].value_counts())
seg


# In[43]:


sns.barplot(seg,x=seg.index,y="Segment")


# # 10 state of us giving maximum sales count

# In[44]:


state=pd.DataFrame(df['State'].value_counts())[0:10]
state


# In[45]:


sns.barplot(state,y=state.index,x='State')


# # 10 Cities that give maximum sales count

# In[50]:


city=pd.DataFrame(df['City'].value_counts())[0:10]
city


# In[51]:


sns.barplot(city,y=city.index,x="City")


# In[52]:


region=pd.DataFrame(df['Region'].value_counts())
region


# In[53]:


sns.barplot(region,x=region.index,y='Region')


# # what kind of product they are selling and their  quality

# In[55]:


category=pd.DataFrame(df['Category'].value_counts())
category


# In[56]:


sns.barplot(category,x=category.index,y='Category')


# # under furniture supplies what kind of product they are selling 

# In[57]:


fr_data=df[df['Category']=='Furniture']
fr_data=pd.DataFrame(fr_data['Sub-Category'].value_counts())
fr_data


# In[59]:


sns.barplot(fr_data,y=fr_data.index,x='Sub-Category')


# # under technology what kinds of product they are selling

# In[63]:


tc_data=df[df['Category']=='Technology']
tc_data=pd.DataFrame(tc_data['Sub-Category'].value_counts())
tc_data


# In[64]:


sns.barplot(tc_data,y=tc_data.index,x='Sub-Category')


# # under office what kind of product they are selling

# In[65]:


oc_data=df[df['Category']=='Office Supplies']
oc_data=pd.DataFrame(oc_data['Sub-Category'].value_counts())
oc_data


# In[66]:


sns.barplot(oc_data,y=oc_data.index,x='Sub-Category')


# # what is the companies prefered mode of shipping

# In[67]:


ship_data=pd.DataFrame(df['Ship Mode'].value_counts())
ship_data


# In[68]:


sns.barplot(ship_data,y="Ship Mode",x=ship_data.index)


# # what is the average shipping cost per ship mode

# In[69]:


sms_data=pd.DataFrame(df.groupby('Ship Mode')['Sales'].mean())
sms_data


# In[72]:


sms_data=sms_data.sort_values(by='Sales')
sns.barplot(sms_data,y=sms_data.index,x='Sales')


# # Top 10 highest buyer in their 4 year journey

# In[73]:


top10=pd.DataFrame(df['Customer Name'].value_counts())[0:10]
top10


# In[74]:


sns.barplot(top10,y=top10.index,x='Customer Name')


# # Top 10 city,state and region gives maximum sales

# In[76]:


max_city=pd.DataFrame(df.groupby('City')['Sales'].mean().sort_values(ascending=False))[0:10]
max_city


# In[78]:


max_state=pd.DataFrame(df.groupby('State')['Sales'].mean().sort_values(ascending=False))[0:10]
max_state


# In[80]:


max_zone=pd.DataFrame(df.groupby('Region')['Sales'].mean().sort_values(ascending=False))
max_zone

