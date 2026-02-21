import numpy as np
#arr=np.array({1,2,3,4,5})# here we have used list datatype
'''arr=np.array((1,2,3,4,5))#here we are using turple datatype
print("array ",arr)
print("array type",type(arr))
print(np.__version__)

# dimention of an array 
# zero dimentional array

arr0=np.array(42)
print("array no 0=",arr)
#1D (one dimentional) array
arr1=np.array((1,2,3,4,5))
print("array no 1",arr)

#2D (two dimentional )ARRAY

arr2=np.array([[1,2,3],[4,5,6]])
print("array no 2=",arr)

#3D (three dimentional array)
# a 3d array is array of 2d array (matrices).

arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("array no 3=",arr)
print(arr3.shape)


# checking dimention of array
print("dim of array0 ",arr0.ndim)
print("dim of array1 ",arr1.ndim)
print("dim of array2 ",arr2.ndim)
print("dim of array3 ",arr3.ndim)

#define the dimention of an array using the 'ndmin' argument 

a=np.array([1,2,3,4,5])
print(arr)
print('num of dimentions :',a.ndim)

# accessing element of an array by indexing 
#indexing in numpy array starts with 0
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
# can perform arithmetics 
print(a[3]+a[4])

print(a.shape)
for i in range(5):
    print(a[i])

#access 2D arrays 

b=np.array([[1,2,3],[4,5,6]])
print('1st element on 1st row:',b[0,0])
print('2nd element on 1st row:',b[0,1])
print('3nd element on 2st row:',b[1,2])

#accessing element 3D array
arr3=np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
    ])
print(arr3[0,0,0])#1
print(arr3[0,0,1])
print(arr3[0,0,2])

print(arr3[0,1,0])
print(arr3[0,1,1])
print(arr3[0,1,2])#6
print(arr3[1,0,0])
print(arr3[1,0,1])
print(arr3[1,0,2])
print(arr3[1,1,0])
print(arr3[1,1,1])
print(arr3[1,1,2])

# SLICING array 
a=np.array([1,2,3,4,5,6,7])
print(a[1:4])# from 1st index to 4th
print(a[:4])# from begining to the 4th indexing 
print(a[-3:-1])#from index 3 from the end to 1 index from the end 
print(a[::2])#return every other element from the entire array

#checking data type

alpha=np.array(['apple','banana','cherry'])
num=np.array([1,3,2,3,4,3,2,6,7])
fl=np.array([23.34,45.56,55.66,543.454])
print(alpha.dtype)
print=(num.dtype)
#print(fl.dtype)

#CREATING ARRAY WITH A DEFINED DATATYPE
arr=np.array([1,2,3,4,5],dtype='S')
print(arr)
print(arr.dtype)

#we can also define size as well.
arr=np.array([1,2,3,4,5],dtype='i')
print(arr)
print(arr.dtype)

#converting data type on existing arrays

arr=np.array([1.1,2.1,3.1])
newarr=arr.astype('i')
newarr1=arr.astype(int)
print(newarr)
print(newarr.dtype)
print(newarr1)
print(newarr1.dtype)

ar=np.array([1,0,3])
newar=ar.astype(bool)
print(newar)
print(newar.dtype)


#copy & view of an array

arr=np.array([1,2,3,4,5])
x=arr.copy()# changes made to the copy will not affect oringinal array and
# any changes made in original array will not affect the copy 
arr[0]=42
print(arr)
print(x)

arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=42
print(arr)
print(x)

x=arr.copy()
y=arr.view()
print(x.base)#every numpy array has the attribute base that returns none if the array own the date 
#otherwise the base attribute refers to the original object.
print(y.base)'''
'''output:
None
[1 2 3 4 5]'''
#numpy arrays have an attribute called shape that returns a tuple with each index
#having the number of corresponding elements.
'''
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)
#output :(2, 4)

arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print('shape of array:',arr.shape)
#output:'''
'''[[[[[1 2 3 4]]]]]
shape of array: (1, 1, 1, 1, 4)'''
#integers at every index tells about the number of elements the corresponding demension has 
#above at index 4 we have value 4 so we can say that 5 th (4 + 1 th)dimensio has 4 elements 

#RESHAPING ARRAYS (reshaping from 1 D to 2 D )
'''
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)'''
'''output 
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]'''

 # reshaping from 1D to 3D
'''newarr=arr.reshape(2,3,2)
print(newarr)'''
'''output
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]'''

# returns copy or view (check if the return array is copy or view )
'''arr=np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)
#output '''
'''[1 2 3 4 5 6 7 8]
the above code results orignal array it means it is a view'''

#note: you are allowed to have one "unknown" deminsion.
'''meaning that you dont have to specify an exact number of 
one of the dementions in the reshape method.
pass -1 as the value and numpy will calculate this number for you.'''
'''
arr=np.array([1,2,3,4,5,6,7,8])
newarr=arr.reshape(2,2,-1)
print(newarr)

#FLATTENING THE ARRAYS
#flattening any array means converting a multidimensional array into 1D array. we can reshape -1 to do this 

arr=np.array([[1,2,3],[4,5,6]])
newarr=arr.reshape(-1)
print(newarr)
#output: [1 2 3 4 5 6]

#iterating arrays 

arr=np.array([1,2,3])
for x in arr:
    print(x)

arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y)


arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x)


arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

#iterating array using nditer()

arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in np.nditer(arr):
    print(x)

#Iterating Array With Different Data Types
'''
'''We can use op_dtypes argument and pass it the expected datatype
 to change the datatype of elements while iterating.
NumPy does not change the data type of the element in-place
 (where the element is in array) so it needs some other space
  to perform this action, that extra space is called buffer,
 and in order to enable it in nditer() we pass flags=['buffered'].
'''

'''

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

#Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
  
#np.(zero,one ,empty,arange ,linspace)
arr=np.zeros([2,3,7])
print(arr)

arr=np.ones([3,3])
print(arr)

arr=np.empty([2,3])# random numbers will be there 
print(arr)

arr=np.arange(5,20)#creating range of values (start,end(n-1),step size)
print(arr)
#You can also use np.linspace() to create an array with values that are spaced linearly
#in a specified interval:'''
'''
arr=np.arange(2, 9, 2)
print(arr)

#Specifying your data type

arr=np.ones([3,4],dtype=np.float64)
print(arr)

#shorting and concatenation::::
arr=np.array([1,5,2,4,3,6,7,8,9])
print(np.sort(arr))
#In addition to sort, which returns a sorted copy of an array, you can use:
#**argsort, which is an indirect sort along a specified axis,
arr=np.array([1,5,2,4,3,6,7,8,9])
print(np.argsort(arr))# will give and in the form of indexing

#**lexsort, which is an indirect stable sort on multiple keys,
arr=np.array([1,5,2,4,3,6,7,8,9])
print(np.lexsort(arr))

#**partition, which is a partial sort.
arr=np.array([11,78,88,89,98,45])
print(np.partition(arr,3))
#output:--[11 45 78 88 89 98] 
# saying that these first three elements are shorted and smaller then the rest of the values  

#concatenate
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))# means the result will be ontop in one axis 
'''

#How to create an array from existing data
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])
x=np.vstack((a1, a2))               
print(x)  #stack them vertically with vstack:
x=np.hstack((a1, a2))
print(x) #stack them horizontally with vstack:

x = np.arange(1, 25).reshape(2, 12)# 1 to 25 numbers in 2 rows and 12 colums 
print(x)
c=np.hsplit(x, 3)#If you wanted to split this array into three equally shaped arrays
print(c)