# a calculator that handles different types of error you have to use functions 
def calculator():
    print("\nCHOICE::")
    print("1.   ADDITION")
    print("2.   SUBSTRACTION")
    print("3.   MULTIPLICATION")
    print("4.   DIVISION")

    def multiply(a, b):
        return a * b

    def add(a, b):
        return a+b 
    
    def subtract(a, b):
        return a-b
     
    def divide(a, b):
        if(b==0):
            raise ZeroDivisionError("can not divide by zero")
        
        return a/b

    try:
        choice = int(input("Choose operation (1-4): "))
        num1=int(input("enter the first number: "))
        num2=int(input("enter the 2nd  number : "))

        if(choice==1):
            print("the addition of the numbers is :",add(num1,num2))
        elif(choice==2):
            print("the subtraction of the number is :",subtract(num1,num2))
        elif(choice==3):
            print("the multiplication of the numbers is :",multiply(num1,num2))
        elif(choice==4):
            print("the division of the numbers is:",divide(num1,num2))
        else:
            print("invalid choice ")
    except ValueError:
        print("please! , enter valid numbers ")
    except ZeroDivisionError as e:
        print("error",e)


while True:
    calculator()
    again = input("Do another calculation? (y/n): ")
    if again.lower() != 'y':
        break