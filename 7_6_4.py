import pandas as pd
import numpy as np


#Transforming data using a function or mapping
df_person = pd.DataFrame([
    ['Person 1', 'Melbourne', '3024'],
    ['Person 2', 'Sydney', '3003'],
    ['Person 3', 'Delhi', '100001'],
    ['Person 4', 'Kolkata', '700007'],
    ['Person 5', 'London', 'QA3023']
], columns=['Name','City','Pin'])
print(df_person)


#Next, let us create a dictionary for the city and the country
dict_mapping = {
    "Melbourne":"Australia",
    "Sydney":"Australia",
    "Delhi":"India",
    "Kolkata":"India",
    "London":"United Kingdom"
}
print(dict_mapping)


#Detecting and filtering outliers
#let’s create a DataFrame with random numbers. You will extract particular rows based on a filter applied to values in a particular column.
data = pd.DataFrame(np.random.randint(5, 1000, size=(1000,4)), columns = ['Col A', 'Col B', 'Col C','Col D'])
print(data.head())

#Then, describe the DataFrame, and statistical summary of the DataFrame
print(data.describe())

#Let's say you want to filter all the records where the value in Col D is less than 400. For this, create a boolean filter on Col D and then apply that filter to the DataFrame as an index to get the subset of the data.
#Create a filter
boolean_filter = data['Col D'] < np.abs(400)
print(boolean_filter.head())


#Apply this filter on the DataFrame
data_filtered = data[boolean_filter]
print(data_filtered.describe())


#You can apply this filter inline as well, and to all the columns:
data_filtered_new = data[np.abs(data)<400]
print(data_filtered_new.describe())


#Removing duplicates
#Pandas has an easy-to-use function, drop_duplicates(), that removes duplicate records from a DataFrame.
df1 = pd.DataFrame({'k1': ['A']*3 + ['B']*4,
                    'k2': [1,1,2,2,3,3,4]
                   })
print(df1)

#Now, use the function to drop the duplicates.
df_dedup = df1.drop_duplicates()

print(df_dedup)

#Next, try this example with a specified column
#Remove Duplicate Values from Column k1

df_dedup_k1= df1.drop_duplicates('k1')

print(df_dedup_k1)

