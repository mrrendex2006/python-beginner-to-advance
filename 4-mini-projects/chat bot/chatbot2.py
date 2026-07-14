import datetime
import os
import speech_recognition as sr
import pyttsx3


# ================= VOICE SETUP =================
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()


'''engine = pyttsx3.init()
engine.setProperty("rate", 170)

engine.say("Hello, I can speak now")
engine.runAndWait()'''


def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            speak("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            print("Speech service error.")
            return ""

# ================= FILE SETUP =================
BRAIN_FILE = "brain.txt"
HISTORY_FILE = "history.txt"

for file in (BRAIN_FILE, HISTORY_FILE):
    if not os.path.exists(file):
        open(file, "w", encoding="utf-8").close()

# ================= RESPONSES =================
responses = {
    "hello": "Hi! Welcome. How can I help you?",
    "hi": "Hello! How can I help you?",
    "how are you": "I am very fine, thank you",
    "who are you": "I am a smart AI chatbot",
    "happy": "Great to hear that"
}

# Load learned knowledge
with open(BRAIN_FILE, "r", encoding="utf-8") as f:
    for line in f:
        if "::" in line:
            q, a = line.strip().split("::", 1)
            responses[q] = a

# ================= GREETING =================
name = input("Enter your name: ")
speak(f"Welcome {name}")

hour = datetime.datetime.now().hour
if 5 <= hour < 12:
    greet = "Good morning"
elif 12 <= hour < 17:
    greet = "Good afternoon"
elif 17 <= hour < 21:
    greet = "Good evening"
else:
    greet = "Good night"

print(greet, name)
speak(f"{greet} {name}")

print("\nI am your personal chatbot.")
print("Say or type 'bye' to exit.\n")
speak("I am your personal chatbot. You can talk to me.")

# ================= FUNCTIONS =================
def save_history(user, bot):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"User: {user}\nBot: {bot}\n\n")

def get_response(user_question):
    user_question = user_question.lower()
    for key in responses:
        if key in user_question:
            return responses[key]
    return None

# ================= CHAT LOOP =================
while True:
    mode = input("\nPress ENTER to speak or type message: ").strip()

    if mode == "":
        user_input = listen()
    else:
        user_input = mode

    if not user_input:
        speak("I didn't catch that. Please say it again.")
        continue

    if "bye" in user_input.lower():
        print("Bot: Bye! Have a great day 👋")
        speak("Bye! Have a great day")
        break

    reply = get_response(user_input)

    if reply:
        print("Bot:", reply)
        speak(reply)
        save_history(user_input, reply)
    else:
        print("Bot: I don't know this yet.")
        speak("I don't know this yet. Can you teach me?")
        teach = input("Teach me or type 'skip': ").strip()

        if teach.lower() != "skip" and teach:
            responses[user_input.lower()] = teach
            with open(BRAIN_FILE, "a", encoding="utf-8") as f:
                f.write(f"{user_input.lower()}::{teach}\n")

            print("Bot: Thanks! I learned something new.")
            speak("Thanks! I learned something new.")
            save_history(user_input, teach)
        else:
            speak("Okay, skipping.")

print("Chat ended.")
