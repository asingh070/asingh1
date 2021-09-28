#!/usr/bin/env python
# coding: utf-8

# # Working on Real Project Using Python

# ## The Weather Dataset
# The weather dataset is time series dataset with per hour information aboout the weather condition at a particular location. It records temperature, dew point temperature ,relative humidity, wind speed, visibility, pressure and conditions.
#      
# The data is present as a csv file and we are going to analyze tyhe data using the Panda dataframe.

# In[2]:


import pandas as pd


# In[4]:


data= pd.read_csv(r"C:\Users\Sonu Admin\Downloads\1. Weather Data.csv")


# In[5]:


data


# ## How to analyze dataframes?

# ### .head()
# It shows the N roows in the data( default N=5)

# In[6]:


data.head()


# ### .shape
# It shows the total no of rows and columns of the dataframe.

# In[7]:


data.shape


# ### .index
# This attribute provides the index of the dataframe.

# In[8]:


data.index


# ### .columns
# It shows the name of each column
# 

# In[10]:


data.columns


# ### .dtypes
# It shows the datatype of each column.

# In[11]:


data.dtypes


# ### .unique()
# In a column it shows all the unique values . It can be applied in a single column only not in whole dataframe.
# 

# In[12]:


data["Weather"].unique()


# ### .nunique()
# It shows the total no of unique values in each column. It can be applied on a single column or whole dataframe.

# In[13]:


data.nunique()


# ### .count
# It shows the total no of not null values in each column. It can be applied in a single column or whole dataframe.

# In[15]:


data.count()


# ### .value_counts
# In a column it shows the unique values with their counts . It can be applied in single column only
# 

# In[16]:


data["Weather"].value_counts()


# ### .info()
# Provides basic information about the dataframe.

# In[17]:


data.info()


# ##  Q1 .Find all the unique "Wind Speeed " values in the data.

# In[18]:


data.head(2)


# In[20]:


data.nunique()


# In[21]:


data["Wind Speed_km/h"].nunique()


# In[22]:


data["Wind Speed_km/h"].unique()  #ANSWER


# ## Q2. Find the number of times when the "weather is exactly clear".

# In[23]:


data.head(2)


# In[25]:


#value_counts()
data.Weather.value_counts()


# In[28]:


#Filtering
data.head(2)
data[data.Weather =='Clear']


# In[30]:


#groupby()
data.head(2)
data.groupby('Weather').get_group('Clear')


# ## Q3. Find the number of time when the wind speed was exactly 4km/hr.

# In[31]:


data.head(2)


# In[32]:


data[data["Wind Speed_km/h"] == 4]   #ANSWER


# ## Q4 Find the null values in the data.

# In[34]:


data.isnull().sum()


# In[37]:


data.notnull().sum()


# ## Q5 Rename the column name " Weather " of the dataframe to "Weather condition"

# In[38]:


data.head(2)


# In[39]:


data.rename(columns ={'Weather':'Weather condition'})


# ## Q6 What is the mean visibility?

# In[40]:


data.head(2)


# In[41]:


data.Visibility_km.mean()


# ## Q7. What is the standard deviation of ' Pressure ' in this data?

# In[42]:


data.head(2)


# In[43]:


data.Press_kPa.std()


# ## Q8. What is variance of 'Relative humidity ' In this data?

# In[44]:


data.head(2)


# In[46]:


data['Rel Hum_%'].var()


# ## Q9 Find all the instances when 'Snow' was recorded.

# In[47]:


#value_counts()
data.head(2)


# In[48]:


data['Weather'].value_counts()


# In[49]:


#Filtering
data[data['Weather'] == 'Snow']


# In[51]:


#str.contains
data[data['Weather'].str.contains('Snow')]


# ## Q10. Find all the instances when wind speed is above 24 and visibility is 25.

# In[52]:


data.head(2)


# In[54]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]


# ## Q11. What is the mean value of each column against each 'Wearther Condition'

# In[55]:


data.head(2)


# In[56]:


data.groupby('Weather').mean()


# ## Q12. What is the Minimumn and Maximum value of each column against each " Weather Condition"?

# In[57]:


data.head(2)


# In[58]:


data.groupby("Weather").min()


# In[59]:


data.groupby("Weather").max()


# ## Q13. Show all the records where weather condition is Fog.

# In[60]:


data.head(2)


# In[64]:


data[data['Weather'] == 'Fog']


# ## Q14. Find all the instances when "Weather is clear" or "Visibility is above 40"

# In[65]:


data.head(2)


# In[67]:


data[(data['Weather']=='Clear') | (data['Visibility_km']>40)]


# ## Q15. find all the instances when:
# A. Wather is Clear and Relative Humidity is greater than 50.
# 
# OR
# 
# B. Visibility is above 40.
# 

# In[68]:


data.head(2)


# In[73]:


data[(data['Weather'] =='Clear') & (data['Rel Hum_%'] >50) | (data['Visibility_km'] > 40)]

