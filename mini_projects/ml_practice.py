# import numpy as np 
# import pandas as pd 
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error,r2_score

# df=sns.load_dataset("tips")#loading library from seaborn


# X=df.drop("tip",axis=1) # sklearn expect 2 D array 
# y=df['tip']

# x_test,x_train,y_test,y_train=train_test_split(X,y,test_size=0.2,random_state=42)

# regression=LinearRegression()
# regression.fit(x_train,y_train)

# y_pred=regression.predict(x_test)


# print("MSE : ",mean_squared_error(y_test,y_pred))
# print("r2 score : ",r2_score(y_test,y_pred))
import numpy as np 
import pandas as pd 
import seaborn as sns
df=sns.load_dataset("mpg")#loading library from seaborn
df.head()