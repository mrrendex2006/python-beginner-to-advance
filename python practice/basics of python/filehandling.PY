# write a program to read a text from a given certificate.txt and find whether it contains the word live  .

'''file= open("certificate.txt","r")
dataoffile=file.read()

dataoffile=dataoffile.lower()

if"live" in dataoffile:
    print("yes, live word is there in the text file ")
else:
    print("no , not present ")
file.close()
'''


# write a program to open a file in wright mode and write a  number of text to save in the file

file=open("newfile.txt","w")
file.write(" prthon is fun to learn and i am currently injoying it \n ")
file.close()

# if i open a file in "a" append mode it add everything you write in it .

file=open("newfile.txt","a")
file.write(" this is another line im am adding into this file in append mode \n")
file.write(" i am going vwer well with is filehandeling  thing")
file.close()

# every time when we open file it is require to close it at the end 
# to overcome this problem we have "with" open keyword 
#with open("newfile.txt","r") as f
#  line1=f.readline()  
    line2=f.readline()   
    line3=f.readline()  
    print("line1",line1)
    print("line2",line2)
    print("line3",line3)
    data=f.read()
    print( "file data : ", data)#pointer comes to the end

#(to copy file )
# import shutil 
# shutil.copy("demo.txt","new_demo.txt")   


#TO DELETE FILE
#impost os 
#os.remove("oldfile.txt")

#rename a file 
#import os 
#os.remove("oldfile.txt")

#try and except in python 
import os
try:
    with open("newfile.txt","r") as f:
    line1=f.readline()  
    line2=f.readline()   
    line3=f.readline()  
    print("line1",line1)
    print("line2",line2)
    print("line3",line3)
    data=f.read()
    print( "file data : ", data)
except:
    print("this file doesn't exist ")
