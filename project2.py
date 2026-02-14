import datetime
import time 
# datetime works in 24 hours clock 

name=input("welcome , enter your name : ")
presenthour=datetime.datetime.now().hour 
if 5<= presenthour <=11:
    print("good morning ", name )
elif 11<= presenthour <=17:
    print("good afternoon ", name )
elif 17<= presenthour <=20:
    print("good evening ", name )
else:
    print ("gppd night ", name )

print("hello , i am your personal chatbot")
print("You can ask me basic questions , type 'bye' to exit from bot ")
#responses is a dictionary 
responses={
    "hello":"Hii wellcome. how can i help you ?",
    "how are you":"i am very fine. thank you ",
    "who are you":"i am smart ai chatbot ",
    "motivate me ":"keep going. every bug you fix of your project makes you a better coder ",
    "happy":"great to hear that ",
    "function kya hota hai ":"jaker chapter 7 padh lo "
  
}

#method/funtion to get responce of chatbot 
def getresponsebot(userquestion):
    userquestion=userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey] 
        
    return "i am not able to tell that yet,i am still in learning mode "
# takes user input 
while True :
    userinput=input(" please ask your questions  ")
    reply=getresponsebot(userinput)
    print("bot responce :",reply )

    if "bye" in userinput.lower():
        break
