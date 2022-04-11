import pandas as pd
import numpy as np

#First, create a dummy DataFrame
data = pd.DataFrame(np.arange(6).reshape((2,3)),     index=pd.Index(['Victoria', 'NSW'], name='state'),       columns=pd.Index(['one','two','three'], name='number'))
print(data)


#Next, we use the stack() function—we will pivot the columns into rows.
data_stack = data.stack()
print(data_stack)

print(type(data_stack))

print(data_stack.index)

print(data_stack['Victoria']['one'])


#rearrange the data back into a DataFrame
orig_data = data_stack.unstack()
print(orig_data)

#try this code that unstacks data_stack at the level of state, rather than number
data_state = data_stack.unstack('state')
print(data_state)

#Splitting an object into groups
#example that uses the column name as the splitting criterion:
df_animals = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                   ('bird', 'Psittaciformes', 24.0),
                   ('mammal', 'Carnivora', 80.2),
                   ('mammal', 'Primates', np.nan),
                   ('mammal', 'Carnivora', 58)],
                  index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                  columns=('class', 'order', 'max_speed'))
print(df_animals)

grp_class= df_animals.groupby('class')
print(grp_class)

grp_class_order = df_animals.groupby(['class', 'order'])
print(grp_class_order)

#once you call a .sum() method on the two GroupBy objects, the split occurs and returns the summation result
print(grp_class.sum())

print(grp_class_order.sum())


#GroupBy sorting
#By default, the group keys are sorted during the GroupBy operation. If you don't want group keys to be sorted, pass the parameter sort=false.

df2 = pd.DataFrame({'X': ['B', 'B', 'A', 'A','C','C','C'], 'Y': [2, 4, 3, 4,2,5,6]})
print(df2)

#Observer that in the output, Keys are sorted lexicographically
print(df2.groupby(['X']).sum())

#In this statement we are passing sort=False, now group keys will not be sorted
print(df2.groupby(['X'], sort=False).sum())


#GroupBy object attributes
#If you want to check the created groupings, you can look at the groups attribute of the GroupBy object
df=pd.DataFrame({'X': ['A', 'B', 'A', 'B'], 'Y': [1, 4, 3, 2]})
print(df)

print(df.groupby(['X']).groups)
