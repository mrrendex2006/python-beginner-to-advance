
import datetime
import time 
import os
# datetime works in 24 hours clock 

#files
BRAIN_FILE="brain.txt"
HISTORY_FILE="history.txt"
# Create files if not exist
for file in (BRAIN_FILE, HISTORY_FILE):
    if not os.path.exists(file):
        open(file, "w", encoding="utf-8").close()
        
# pre installed responcess are :--
responses={
    "hello":"Hii wellcome. how can i help you ?",
    "hii":"Hello! how can i help you",
    "how are you":"i am very fine. thank you ",
    "who are you":"i am smart ai chatbot ",
    "happy":"Great to hear that ",
    
    
  
}
# LOAD KNOWLEDG
with open(BRAIN_FILE,"r",encoding="utf-8")as f:
    for line in f:
        if "::" in line :
            q,a=line.strip().split("::",1)
            responses[q]=a

name=input("welcome , enter your name : ")

presenthour=datetime.datetime.now().hour 
if 5<= presenthour <=12:
    print("good morning ", name )
elif 12<= presenthour <=17:
    print("good afternoon ", name )
elif 17<= presenthour <=21:
    print("good evening ", name )
else:
    print ("good night ", name )

print("\nHello , I am your personal chatbot")
print("I can learn new things!")
print ("type 'bye' to exit from bot ")



#SAVE HISTORY FUNCTION
def save_history(user, bot):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write("User: " + user + "\n")
        f.write("Bot: " + bot + "\n\n")

# BOT FUNCTION 
def get_response(user_question):
    user_question = user_question.lower().strip()

    for key in responses:
        if key in user_question:
            return responses[key]

    return None  # Means: I don't know

#CHAT LOOP
while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    if "bye" in user_input.lower():
        print("Bot: Bye! Have a great day 👋")
        break

    reply = get_response(user_input)

    # If bot knows answer
    if reply:
        print("Bot:", reply)
        save_history(user_input, reply)

    # If bot doesn't know answer -> learn
    else:
        print("Bot: I don't know this yet 🤔")
        teach = input("Can you teach me the answer? (type answer or 'skip'): ")

        if teach.lower() != "skip":
            responses[user_input.lower()] = teach

            with open(BRAIN_FILE, "a", encoding="utf-8") as f:
                f.write(user_input.lower() + "::" + teach + "\n")

            print("Bot: Thanks! I learned something new 😊")

            save_history(user_input, teach)
        else:
            print("Bot: Okay, let's skip it 🙂")

print("Chat ended.")

