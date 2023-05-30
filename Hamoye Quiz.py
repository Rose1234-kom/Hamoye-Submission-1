#!/usr/bin/env python
# coding: utf-8

# In[22]:


pip install pandas


# In[2]:


import pandas as pd


# In[21]:


food = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding='latin-1')
food.head()


# In[24]:


food.groupby("Element")["Y2014","Y2015","Y2016","Y2017","Y2018"].agg([ "max"])


# In[26]:


# Select columns 'Y2017' and 'Area'
selected_columns = food[['Y2017', 'Area']]

# Group by 'Area' and calculate the sum of 'Y2017' for each area
grouped = selected_columns.groupby('Area')['Y2017'].sum().reset_index()

# Find the area with the highest sum in 2017
max_area = grouped.loc[grouped['Y2017'].idxmax(), 'Area']

print("Area with the highest sum in 2017:", max_area)


# In[27]:


# Calculate the correlation coefficient between 'Element Code' and each year
correlations = food.iloc[:, 3:].corr()['Element Code']

# Find the year with the lowest correlation coefficient
min_corr_year = correlations.idxmin()

print("Year with the least correlation with 'Element Code':", min_corr_year)


# In[34]:


# Filter the DataFrame for Madagascar in 2015
filtered_df = food[(food['Area'] == 'Madagascar') & (food['Y2015'] == 2015)]

# Calculate the total Protein supply quantity
total_protein = filtered_food['Protein Supply Quantity'].sum()

print("Total Protein supply quantity in Madagascar in 2015:", total_protein)


# In[35]:


# Select columns 'Y2017' and 'Area'
food_2017 = food[['Y2017', 'Area']]

# Groupby 'Area' and calculate the sum for 2017
grouped = food_2017.groupby('Area')['Y2017'].sum().reset_index()

# Sort the sums in ascending order
sorted_sums = grouped.sort_values('Y2017')

# Get the area with the 7th lowest sum
seventh_lowest_area = sorted_sums.iloc[6]['Area']

print("Area with the 7th lowest sum in 2017:", seventh_lowest_area)


# In[36]:


# Count the number of missing values in Y2014 column
missing_count = food['Y2014'].isnull().sum()

# Calculate the total number of rows
total_rows = len(food)

# Calculate the percentage of missing data
percentage_missing = (missing_count / total_rows) * 100

# Print the total number and percentage of missing data
print("Total number of missing data in 2014:", missing_count)
print("Percentage of missing data in 2014: {:.3f}%".format(percentage_missing))


# In[37]:


# Calculate the mean and standard deviation for the year 2017
mean_2017 = food['Y2017'].mean()
std_2017 = food['Y2017'].std()

# Print the mean and standard deviation
print("Mean for the year 2017: {:.2f}".format(mean_2017))
print("Standard deviation for the year 2017: {:.2f}".format(std_2017))


# In[43]:


# Filter the dataframe for the years 2015 and 2018
filtered_food = food[food.isin([2015, 2018])]

# Perform a groupby sum aggregation on 'Item'
sum_wine = filtered_food.groupby('Item')['Value'].sum()

# Print the total sum of Wine produced in 2015 and 2018
print("Total sum of Wine produced in 2015:", sum_wine.loc['Wine', 2015])
print("Total sum of Wine produced in 2018:", sum_wine.loc['Wine', 2018])


# In[42]:


# Filter the dataframe for the year 2017 and 'Processing' element
filtered_food = food[(food['Y2017']) & (food['Element'] == 'Processing')]

# Calculate the total sum of 'Processing' in 2017
total_sum = filtered_food.sum()

# Print the total sum of 'Processing' in 2017
print("Total sum of Processing in 2017:", total_sum)


# In[ ]:




