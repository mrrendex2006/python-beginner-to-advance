#loops for , while in python

'''i=1
while(i<=5):
   print(" hello yash")
   i+=1

a=int(input("enter a number"))
b=int(input("enter a number"))
n=1
while(n>a):
   print("addition=" , a+b )'''

'''i=1
count=0
while(i<=10):
   count+=i
   print(count)
   i+=1'''
# reverse counting 
'''i=10
while(i>=1):
   print(i)
   i=i-1'''
# printing even no till 50 :  
'''i=1
while(i<=50):
   if(i%2==0):
      print(i)
   i+=1'''
#multiplication table 

'''a=4
i=1
while(i<=10):
   print(f"{a}x{i}={a*i}") # use f"  " to put the values of variables 
   i+=1'''

'''heros=["army","navy","airforce"]
for items in heros:
    print(" indians are proud of there ",items)'''


'''name=["nikki","yash","nidhi","krish","manish"]
for item in name:
    print("name of student",item)
for i in range(1,6):# for iteration 
    print("name",i)'''



#multiplication table 
'''num=int(input("enter a number=="))
i=0
while(i<=10):
   print(f"{num}x{i}={num*i}")
   i=i+1
   '''
# printing odd no till 100;

'''i=0
while(i<=100):
   if(i%2!=0):
      print(i)
   i+=1'''

# fibunachui siries 
def fibonacci_rec(n):
   if (n==0):
      print("0")
   elif(n<=1):
      print( n)
   else:
      print(fibonacci_rec(n-1)*fibonacci_rec(n-2))

n=int(input("enter the number till you want the series = " ))
fibonacci_rec(n)