#a=int(input("enter numer= "))
#b=int(input("enter numer= "))
#avg=(a+b)/2
#print("average of the two numbers =",avg)

num=input("enter a number =")
convertedvalue=float(num)
new=str(convertedvalue)
print("orignal value is =",num,"data type",type(num))
print("converted value is =",convertedvalue,"data type",type(convertedvalue))
if(float(num)==convertedvalue):
    print("same")
elif(str(convertedvalue)==new):
    print("same data string")    
else:
    print("different")

#c=int(input("enter thr temperature in celcious= "))
#f=float(c*(9/5))+32
#print("the temperature in farenhite is =",f)


# string in python :--
'''str1=str(input("enter name of the user ="))
p=int(len(str1))
print(str1[:p])

#if(p<=20):
    #print(p)
#if(str1[0]=="y"):
    #print(str1[0])
  
#print(str1[p-1])

print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.find("yash"))
print(str1.replace("singh","best"))
print(str1.count("s"))
print(f"my namr is {str1}")'''


