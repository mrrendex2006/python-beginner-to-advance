import random
attempts=0
def dice_rolling():
    global attempts 
    
    number=random.randint(1,6)
   
    print("----"*10,"********WELCOME********","-----"*10)
    print(" LET'S ROLL A DICE AND SEE HOW LUCKY YOU ARE")
    print("do you want to roll the dice? (y/n)\n")
    response=input("enter your responce :")
    if(response=="y"):
        if (number==6):
            print("your output is ::",number )
            print("impressive , i are great with your luck ")
            attempts+=1
            
        elif(number==1):
            print("your output is ::",number )
            print("i think you should try again  ")
            attempts+=1
           
        elif(2<=number<=4  ):
            print("your output is ::",number )
            print("good ....")
            attempts+=1
        elif(number==5):
            print("you are very close try again")


    else:
        for i in range(0,3):
            print("do you really don't wnat to continue")
            confirm=input("enter your response(y/n):")
            if   ( confirm=="y"):
                print("Great! Let's roll 🎲")
                return dice_rolling()
            elif  (confirm=="n"):
                if(i<2):
                    print("do you really not want to roll the dice ")
                     
                else:
                    print(f"✅ You rollef dice  {attempts} times")
                    print("oook thik hai jao byeee")   
                    return 

            else:
                print("enter a valid s :(y/n)")   

while True:
    dice_rolling()
    print("do you want to continue playing ? (y/n)\n")
    responce=input("enter your response :")
    if(responce=="n"):
        print("thenk you! byeeee ")
        break
