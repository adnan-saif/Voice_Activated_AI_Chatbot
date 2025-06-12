# Importing required module
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import schedule
import threading
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Converts the given text to speech and speaks it aloud
def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

# Greets the user based on the current time of day
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you?")

# Listens to user's voice command and converts it to text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        # Listen with timeout
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"You: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, Didn't catch that.")
            return "None"
        except sr.RequestError:
            print("Network error.")
            return "None"
        except Exception as e:
            print("Error:", e)
            return "None"

# List to Hold Reminders
scheduled_reminders=[]

# Schedules a reminder at a specific time
def schedule_reminder(reminder_text, reminder_time):
    schedule.every().day.at(reminder_time).do(lambda : speak(f"Reminder: {reminder_text}"))
    scheduled_reminders.append((reminder_text, reminder_time))

# Background thread for scheduled reminders
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Executes actions based on the given command string
def execute_command(query):

    # Wikipedia search
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        try:
            topic = query.replace("search", "").replace("wikipedia", "").strip()
            result = wikipedia.summary(topic, sentences=2)
            speak("According to Wikipedia")
            speak(result)
        except:
            speak("Couldn't fetch information from Wikipedia.")
    
    # Open Google
    elif "open google" in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    # Open YouTube
    elif "open youtube" in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    # Search on Google
    elif "search" in query:
        search_query = query.replace("search", "")
        if search_query:
            speak(f"Searching Google for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        
        else:
            speak("What should I search for?")
            query = take_command()

    # General Interaction
    elif "hi" in query or "hello" in query:
        speak("Hello! How can I help you?")

    elif "how are you" in query:
        speak("I'm just a bunch of code, but I'm functioning as expected! How can I assist you today?")

    # Tell the current time
    elif "time" in query:
        time_str = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time_str}")

    # Shutdown the computer
    elif "shutdown" in query:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    # Restart the computer
    elif "restart" in query:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")

    # Write a note
    elif "write a note" in query or "take a note" in query:
        speak("What should I write?")
        note = take_command()
        if note != "None":
            with open("note.txt", "a") as f:
                f.write(f"{datetime.datetime.now()}: {note}\n")
            speak("Note saved.")

    # Read saved notes
    elif "read notes" in query or "show notes" in query:
        try:
            with open("note.txt", "r") as f:
                notes = f.read()
                speak("Here are your saved notes.")
                speak(notes)
        except FileNotFoundError:
            speak("No notes found.")

    # Set a Reminders
    elif "set a reminder" in query:
        speak("What should I remind you about?")
        reminder_text = take_command()
        speak("At what time should I remind you? Say it in 24-hour format.")
        reminder_time = take_command()
        reminder_time = str(reminder_time[:-2] + ":" + reminder_time[-2:])

        # Normalize and validate time format
        try:
            time_obj = datetime.datetime.strptime(reminder_time, "%H:%M")
            formatted_time = time_obj.strftime("%H:%M")
            schedule_reminder(reminder_text, formatted_time)
            speak(f"Reminder set for {formatted_time}")
        except ValueError:
            speak("Invalid time format.")

    # Show Reminders
    elif "show reminders" in query or "read reminders" in query:
        if scheduled_reminders:
            speak("Here are your scheduled reminders:")
            for text, time_ in scheduled_reminders:
                speak(f"At {time_}, reminder: {text}")
        else:
            speak("You have no scheduled reminders.")

    # Exit command
    elif "exit" in query or "quit" in query or "bye" in query:
        speak("Goodbye! Have a nice day.")
        exit()

    # Unknown command
    else:
        speak("Sorry, I didn't understand that command.")

# Main execution starts here
if __name__ == "__main__":
    
    # Greets
    wish_me()

    # Start Scheduler
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    # Main Loop
    while True:
        query = take_command()
        if query != "None":
            execute_command(query)
