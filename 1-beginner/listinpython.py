# list in python
#lists are mutable data types 



name=["krish","sarthak","anurag","ritikesh","kartik","yogesh"]# we are using data as string here "  "
'''print(len(name))
print(name[0])#asscesing elements of a list
print(name[1])#asscesing elements of a list
print(name[2])#asscesing elements of a list
print(name[3])#asscesing elements of a list
print(name[4])'''
print(name[5])
#updating elements of a list 
name[5]="yash"
print("after updatig the elements at index 5")
'''print(name[5])
#accessing elements using slicing 
print(name[0:6])#forward indexing
print(name[-7:]) 
print(max(name))# to find the maximum of a list
print(min(name))'''
#mathods and opertions of list ==
name.append("kumar")#adds elements at the end of a list
print(name[0:6])
name.insert(5,"ravi")#insert element at indexing 
print("at 5 we have ",name[5])
name.remove("kartik")#delete first occurance an element from list 
print(name[0:6])
name.pop(5)# delete na elemnet using index
print(name [0:6])
#sorting a list == making list turn into accending order 
name.sort()# very important operationn 
print(name [0:6])
name.reverse()
print(name[0:6])




