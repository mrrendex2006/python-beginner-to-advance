# voting age verification
age=int(input("enter the age of user= ")) 
if(age>=18):
    print("user is eligible to vote ")
elif(age<=18):
    print("user is not eligible to vote")
else:
    print("error")        