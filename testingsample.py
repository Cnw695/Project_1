#!/usr/bin/env python
# coding: utf-8

# In[1]:


#%matplotlib notebook
#get_ipython().system('jupyter nbextension enable --py gmaps')


# In[2]:


import csv, os, requests, time, gmaps, pandas as pd, matplotlib.pyplot as plt, numpy as np
from config import *
gmaps.configure(api_key=gkey)


# In[3]:


yelpapi_csv = os.path.join("yelpapidata.csv")
yelp_raw = pd.read_csv(yelpapi_csv)
yelp_raw.head()


# In[4]:


yelp_raw.describe()


# In[5]:


yelp_format_rd1 = yelp_raw.copy()
#yelp_format_rd1["review_count"] = yelp_format_rd1.loc[:, "review_count"].astype(float)
#yelp_format_rd1["rating"] = yelp_format_rd1.loc[:, "rating"].astype(float)
yelp_format_rd1['price_attribute'] = yelp_format_rd1['price'].replace(
    {'$': '1.Affordable', '$$': '2.Moderate', '$$$': '3.Expensive'})
yelp_format_rd1.head()


# In[6]:


yelp_format_rd1.columns


# In[7]:


yelp_format_rd1.count()


# In[8]:


yelp_format_rd1.dtypes


# In[9]:


yelp_gb_cities = yelp_format_rd1.groupby(['search_city'])
yelp_gb_cities.sum().head()


# In[10]:


yelp_gb_cuisines = yelp_format_rd1.groupby(['search_cuisine'])
yelp_gb_cuisines.sum().head()


# In[11]:


yelp_gb_price = yelp_format_rd1.groupby(['price'])
yelp_gb_price.sum().head()


# In[12]:


yelp_gb_citiescount = yelp_format_rd1.groupby(['search_city'])
yelp_gb_citiescount.count().head()


# In[13]:


yelp_gb_cuisinescount = yelp_format_rd1.groupby(['search_cuisine'])
yelp_gb_cuisinescount.count().head()


# In[14]:


yelp_gb_citiesavg = yelp_format_rd1.groupby(['search_city'])
yelp_gb_citiesavg.mean().head()


# In[15]:


yelp_gb_cuisinesavg = yelp_format_rd1.groupby(['search_cuisine'])
yelp_gb_cuisinesavg.mean().head()


# In[16]:


yelp_gb2_citiesavg = yelp_format_rd1.groupby(['search_city','search_cuisine'])
yelp_gb2_citiesavg.mean().head()


# In[17]:


yelp_gb2_cuisinesavg = yelp_format_rd1.groupby(['search_cuisine','search_city'])
yelp_gb2_cuisinesavg.mean().head()


# In[18]:


yelp_gb3_citiesavg = yelp_format_rd1.groupby(['search_city','search_cuisine'])
yelp_gb3_citiesavg.mean().head()


# In[19]:


yelp_gb3_cuisinesavg = yelp_format_rd1.groupby(['search_cuisine','search_city'])
yelp_gb3_cuisinesavg.mean().head()


# In[20]:


#This is where we are going to start charting, I have provided some exmaples for you. 


# In[21]:


chartme1 = yelp_gb_cuisinesavg['rating'].mean()
cuisine_chart = chartme1.plot(kind='bar', title='mean rating by cuisine')
cuisine_chart.set_xlabel("cuisine group")
cuisine_chart.set_ylabel("yelp rating")

plt.show()
plt.tight_layout()


# In[22]:


chartme2 = yelp_gb_citiesavg['rating'].mean()
cuisine_chart = chartme2.plot(kind='bar', title='mean rating by cuisine')
cuisine_chart.set_xlabel("yelp rating")
cuisine_chart.set_ylabel('our cities')

plt.show()
plt.tight_layout()


# In[23]:


#For Clinton


# In[24]:


variable = yelp_gb_cuisinescount['review_count'].sum()
variable

#cuisines_label = variable['search_cuisine'].values.tolist()
#cuisines_label


# In[25]:


specific_city = 'Albany, New York'
yelp_gb_cc_city = yelp_format_rd1[yelp_format_rd1['search_city'] == specific_city].groupby(['search_cuisine'])
variable2 = yelp_gb_cc_city['review_count'].sum()
variable2


# In[26]:


# For Nell


# In[27]:


specific_city = 'Albany, New York'
yelp_gmaps = yelp_format_rd1[yelp_format_rd1['search_city'] == specific_city]
yelp_gmaps = yelp_gmaps[['lat','long','review_count']]
yelp_gmaps.head()


# In[28]:


fig = gmaps.figure()
heatmap_layer = gmaps.heatmap_layer(
    yelp_gmaps[['lat','long']],
    weights=yelp_gmaps['review_count'],
    max_intensity=30,
    point_radius=3.0
)
fig.add_layer(heatmap_layer)
fig


# In[29]:


fig = gmaps.figure()
fig

