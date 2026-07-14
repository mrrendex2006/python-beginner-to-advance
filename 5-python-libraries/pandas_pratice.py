import pandas as pd  
import numpy as np


'''data=[1,2,3,4,5,6]
index=['a','b','c','d','e','f']
series=pd.Series(data,index=index)# remember in pandas it must be writtrn as "Series" s capital
print(series)

# creating data frames==A DataFrame is a table. It contains an array of individual entries, 
# each of which has a certain value. Each entry corresponds to a row (or record) and a column.
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['c0','c1','c2'], index=['r0','r1','r2'])
print(df)

data=pd.DataFrame({'bob':['i like it','it was awful.'] ,
                'sue':['pretty good.','bland']},
                index=['product a','product b'])
print(data)'''

'''students_data=pd.DataFrame({'name of students':['yash singh','kartik chaudhary','yogesh ','aditya','nivruti'],'students id':['100','101','102','103','104']},
index=['1','2','3','4','5'])
print(students_data)
print(students_data.columns)
print(students_data.index)


fruits = pd.DataFrame({'Apples':'30','Bananas':'21'},index=['0','1'])
print(fruits)
print(fruits.columns)
print(list(fruits.index))
#dealing with csv files 
'''

student_data_practice = pd.read_csv(
 #r"C:\Users\nidhi\Downloads\student_data_practice.csv",index_col=0)
 r"C:\Users\nidhi\Downloads\student_data_practice.csv")
#student_data_practice.columns = student_data_practice.columns.str.strip() #some times csv have some hidden spaces 
#print(student_data_practice.head())#Returns the first n rows of a DataFrame

'''
#We can examine the contents of the resultant DataFrame using
#the head() command, which grabs the first five rows:
print(student_data_practice.head(5))
print(student_data_practice.tail(5))#Returns the last n rows of a DataFrame

print(student_data_practice.sample(10))

print(student_data_practice.sample(10,random_state=34)) # gives same result every time 

print(student_data_practice.columns.tolist())#you will get the list

#We can use the shape attribute to check how large the resulting DataFrame is:
print(student_data_practice.shape)
print(student_data_practice.size)
print(student_data_practice.describe())
#common stads related to the data like mean max %
print(student_data_practice.info())
'''

#ASSECESSING DATA FROM FILES 
#lable based lookers (loc,at)
#print(student_data_practice.loc[0:10,'Age':'Math_Score'])
#print(student_data_practice.loc[5:,'Age':'Math_Score'])
# integer bases asscessing (iloc,iat)
#print(student_data_practice.iloc[0:10, 0:5])# iloc['rows':'columns']
#print(student_data_practice.iloc[1,2])  #1    102    Diya "result"=19  
#print(student_data_practice.iloc[[5,7,8],[0,3,5]])
#print(student_data_practice.iloc[:,[1,2]])
'''print(student_data_practice.at[0,'Age'])# Access a single value for a row/column label pair
print(student_data_practice.iat[3,3])
print(student_data_practice['Age'])# package location
print(student_data_practice.Age)'''
# slicing using loc;
#print(student_data_practice.loc[student_data_practice['Gender']=="M"])
#print(student_data_practice[student_data_practice['Gender']=="M"])# shoert hand notation 
'''three ways 1 df[df[condition]]
           2 df.loc[df[condition]]
           3 df.query(condition)'''

#Query the DataFrame using a boolean expression
#print(student_data_practice.query('Age>18 and Science_Score>80'))
#print(student_data_practice.query('Attendance_Percentage>75 & Gender=="M"'))

# --------------------UPDATEING DATA-------------------
'''student_data_practice.loc[0,'Age'] = 23
print(student_data_practice.loc[0,'Age'])'''
# for all rows updating age as 20:
#student_data_practice.loc[:,'Age'] = 23
#print(student_data_practice['Age'])
'''print(student_data_practice.head(5))
student_data_practice.iloc[4,3]="F"
print(student_data_practice.head(5))
student_data_practice.iloc[0,1]="Yash"
print(student_data_practice.head(5))
student_data_practice['Gender']='M'
print(student_data_practice.head(5))'''
'''
#TRANSFORMATION FUNCTIONS :'apply' add new column
def increment_age(x):
    return x+5

a=(student_data_practice['Age'].apply(increment_age))
print(a)
# now instead of writing a seprate function we can use lambda :
print(student_data_practice['Age'].apply(lambda x:x+6))


#student_data_practice['Age catogary']=student_data_practice['Age'].apply(lambda x:'Adult' if x>=18 else 'minor')
print(student_data_practice.head())
student_data_practice['result maths ']=student_data_practice['Math_Score'].apply(lambda x:'A' if x>80 else ' need to do better')
print(student_data_practice.head(10))

print(student_data_practice.insert(2,'Bmi',20))# to add new column having same value
#print(student_data_practice.head(3))

#to delete a column use drop (it does not change the data )
print(student_data_practice.drop(columns='Bmi'))
#print(student_data_practice.head())
# to make the chanpe parmanently in the dataset use drop inplace
#print(student_data_practice.drop(columns='Bmi',inplace=True))
#print(student_data_practice.head())
#TO INSERT A NEW COLUMNS HAVING COME ALGEBRIC FUNCTION ASSOCIATED 
student_data_practice.insert(3,'kd', student_data_practice['Attendance_Percentage']/student_data_practice['Age']**2)
# NOW LEST DROP BOTH COLUMNS TOGETHER
print(student_data_practice.insert(2,'Bmi',20))
student_data_practice.insert(3,'kd', student_data_practice['Attendance_Percentage']/student_data_practice['Age']**2)

print(student_data_practice.drop(columns=['Bmi','kd'],inplace=True))
print(student_data_practice)
# renaming a existing column 
#student_data_practice=student_data_practice.rename(columns={'Math_Score':'math'})# assign it 
print(student_data_practice)
print(student_data_practice.head())# but it doesnot affect the main data base 
#another method that will change in original data frame 
student_data_practice.rename(columns={'Math_Score':'math'},inplace=True)
print(student_data_practice)'''

# ---------------------MERGING TWO DATA FRAMS TOGETHER-----------------------------
'''df1=pd.DataFrame({'id':[1,2,3,4],'name':['yash','yogi','kartik','niv']})
df2=pd.DataFrame({'id':[3,4,5,6],'work':['AI','med','def','chem']})
inner_result=pd.merge(df1,df2,how ='inner',on='id')
print(inner_result)
print("-----------------------------------------------------------------------------------------------------------")
outer_result=pd.merge(df1,df2,how ='outer',on='id')
print(outer_result)
print("-----------------------------------------------------------------------------------------------------------")
left_result=pd.merge(df1,df2,how ='left',on='id')
print(left_result)
print("-----------------------------------------------------------------------------------------------------------")
right_result=pd.merge(df1,df2,how ='right',on='id')
print(right_result)
# if dataframes donot share the same id
# ---------------------MERGING TWO DATA FRAMS TOGETHER-----------------------------
df3=pd.DataFrame({'id':[1,2,3,4],'name':['yash','yogi','kartik','niv']})
df4=pd.DataFrame({'emp_id':[3,4,5,6],'work':['AI','med','def','chem']})
#inner_result=pd.merge(df3,df4,how ='inner',left_on='id',right_on='emp_id')
#print(inner_result)

#result=pd.concat([df3,df4],axis=0) #concatenation of two data frames
#print(result )

#result=pd.concat([df3,df4],axis=0,ignore_index=True)

#result=pd.concat([df3,df4],axis=1,ignore_index=True)# horizontal 
#print(result)
result=pd.concat([df3,df4],axis=0,keys=['df3','df4'])# diffentiable dataframes representation
print(result)
print(result.isna())
print(result.notna())
print(result.isna().sum())
print(student_data_practice.isna().sum())'''


student_data_practice.loc[0,'Age']=np.nan
student_data_practice.loc[4,'Math_Score']=np.nan
student_data_practice.loc[3,'English_Score']=np.nan
print(student_data_practice.head())
#NOW LATS FILL ALL THIS NULL PLACES WITH A VALUE 
#student_data_practice.fillna(0,inplace=True)
#print(student_data_practice.head())
#NOW LETS FILL NULLS OF A PERTICULAR COLUMN
student_data_practice['Age']=student_data_practice['Age'].fillna(student_data_practice['Age'].mean(),inplace=True)
print(student_data_practice.head())





















