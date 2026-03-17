import random 

def guessing_game():
    number=random.randint(1,100)
    attempts=0
    print("="*40)
    print("WELCOME TO NUMBER GUESSING GAME !!")
    print("="*40)
    print("I am thinking of a nnumber between 1 to 100")
    print("can you guess it ? \n")
    while True:
        try:
            guess=int(input("Enter the number you have guessed : "))
        except ValueError:
            print("Please ! enter valid number")
            continue
        if(guess<1 or guess >100):
            print("Please! enter number between 1 to 100")
            continue
        attempts+=1

        if(guess < number):
            print("📈 Too Low! Try higher.\n")

        elif(guess > number ):
            print("Too High! Try lower .\n")
        else:
            print("="*40)
            print(f"🎉 CORRECT! The number was {number}!")
            print(f"✅ You got it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            print("=" * 40)
            break

    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again in ("yes", "y"):
        guessing_game()
    else:
        print("Thanks for playing. Goodbye! 👋")

guessing_game()
