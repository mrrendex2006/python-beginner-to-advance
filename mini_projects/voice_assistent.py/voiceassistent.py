import speech_recognition as sr
import pyttsx3
import os
import pyautogui
import webbrowser
import time

'''WAKE_WORD = "assistant"

def listen_for_wake_word():
    command = listen()
    return WAKE_WORD in command'''





# ------------------ INITIALIZATION ------------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

recognizer = sr.Recognizer()

# ------------------ FUNCTIONS ------------------
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Speech service is not available")
        return ""

# ------------------ COMMAND HANDLER ------------------
def handle_command(command):

    if "open chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open vscode" in command or "open visual studio code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open gpt" in command:
        speak("Opening chat gpt")
        webbrowser.open("https://chatgpt.com/")
    
    

    elif "search for" in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "create folder" in command:
        try:
            folder_name = command.split("named")[-1].strip()
            os.mkdir(folder_name)
            speak(f"Folder {folder_name} created")
        except:
            speak("Unable to create folder")

    elif "take screenshot" in command:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot taken and saved")

    elif "shutdown system" in command:
        speak("Are you sure you want to shut down? Say confirm to proceed")
        confirmation = listen()
        if "confirm" in confirmation:
            speak("Shutting down system")
            os.system("shutdown /s /t 5")

    elif "restart system" in command:
        speak("Restarting system")
        os.system("shutdown /r /t 5")

    elif "exit" in command or "stop assistant" in command:
        speak("Goodbye")
        exit()

    else:
        speak("Sorry, command not recognized")

# ------------------ MAIN LOOP ------------------
'''while True:
    if listen_for_wake_word():
        speak("Yes?")
        command = listen()
        if command:
            handle_command(command)'''

speak("Voice automation assistant started")

while True:
    command = listen()
    if command != "":
        handle_command(command)
    time.sleep(1)

