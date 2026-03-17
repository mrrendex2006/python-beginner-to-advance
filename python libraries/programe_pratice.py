import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

calorie_dataset=pd.read_csv(r'D:\yash - Copy\archive.zip', compression='zip')

#print(calorie_dataset.head())

# print(calorie_dataset.shape)
# print(calorie_dataset.size)
# print(calorie_dataset.describe())

# print(calorie_dataset.info)
# print(calorie_dataset.isnull().sum())# check for null and empty values 
#print(calorie_dataset.columns)
# print(calorie_dataset.index)
# print(calorie_dataset.loc[0:10,'carbs_g':'fat_g'])

# Which food has the most calories? 10 highest
#print(calorie_dataset.nlargest(10, 'calories'))
# print(calorie_dataset[['carbs_g','fiber_g','sugar_g']].mean())
# print('---------------------------------------------------------------------')
# print(calorie_dataset[['carbs_g','fiber_g','sugar_g']].mode())
# print('---------------------------------------------------------------------')
# print(calorie_dataset[['carbs_g','fiber_g','sugar_g']].median())

#filtering & conditions
# foods withn more than 500 calories 

# healthy=calorie_dataset[(calorie_dataset['protein_g']>20) & (calorie_dataset['fat_g']<10)]
# #note: Put both conditions inside the same bracket
# print(healthy)

# add a new column health score [health_score = protein + fiber − fat − sugar]
calorie_dataset.insert(7,'health score',calorie_dataset['protein_g']+calorie_dataset['fiber_g']-calorie_dataset['fat_g']-calorie_dataset['sugar_g'])
# print(calorie_dataset.head(10))
# now let s find healthiest and least healthy
# print(calorie_dataset.nlargest(10,'health score'))
# print(calorie_dataset.nsmallest(10,'health score'))
n=calorie_dataset.sort_values('protein_g', ascending=False).head(10)
print(n)
calorie_dataset['calorie_rank'] = (calorie_dataset.groupby('category')['calories'].rank(ascending=False))

















