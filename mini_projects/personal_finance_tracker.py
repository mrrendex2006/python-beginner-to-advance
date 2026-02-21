# personal finance app
print("Welcome to your personal expances app")
expances=[]
while True:
    print("MENU\n","1. add expances\n","2. view all expances \n","3. view total expamces\n","4. exit\n")
    choice=int(input("Enter your choice (1-4)\n "))
    #to add expances 
    if(choice==1):
        date=int(input("enter the date of expance== "))
        catogray=(input("enter thr catogry of expances(personal care,travel,books,purches etc)== "))
        amount=float(input("enter thr amount== "))
        expance={
            "date":date,
            "catogray":catogray,
            "amount":amount 
        }
        expances.append(expance)
        print("details are added succesfully")
    #veiw all expances 
    elif(choice==2):
        if(len(expances)==0):
            print("you haven't expand any money yet")
        else:
            print("********these are your expances**********")   
            count=1
            for eachexpance in expances:
                print(f"expance no {count} ---> {eachexpance["date"]},{eachexpance["catogray"]},{eachexpance["amount"]}")
                #formated string (f"....")when we need any value of variable in double ""
                count=count+1
    # veiw total expances             
    elif(choice==3):
        total=0
        for eachexpance in expances:
            total=total+eachexpance["amount"]
        print("total expances =",total)
    elif(choice==4):
        print("thankyou ") 
        break
    else:
        print("invalid choice ")   
