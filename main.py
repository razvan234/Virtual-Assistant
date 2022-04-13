import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os


print ('Loading your  AI personal assistant - Fred')
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >=0 and hour <12:
        speak("Good morning")
        print("Good morning")
    elif hour>= 12 and hour<18:
        speak("Good afternoon")
        print("Good afternoon")
    else:
        speak("Good evening")
        print("Good evening")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio,language='en-US')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
speak("Loading your AI personal assistant Fred")
wishMe()
if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Fred is shutting down,Good bye')
            print('your personal assistant Fred is shutting down,Good bye')
            break


