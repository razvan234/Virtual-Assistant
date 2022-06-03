import requests
import speech_recognition as sr
import pyttsx3
import datetime
from functions import find_my_ip, play_on_youtube, search_on_google,get_random_joke
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



        if "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in degrees unit is " +
                      "{:n}".format(int(current_temperature - 273.15))
                      +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in degrees unit = " +
                      "{:n}".format(int(current_temperature - 273.15))
                      +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
        elif 'ip address' in statement:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen.')
            print(f'Your IP Address is {ip_address}')
        elif 'youtube' in statement:
            speak('What do you want to play on Youtube?')
            video = takeCommand().lower()
            play_on_youtube(video)
        elif 'google' in statement:
            speak('What do you want to search on Google?')
            statement = takeCommand().lower()
            search_on_google(statement)
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif 'the time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            speak("For your convenience,I am printing it on the screen")
            print(strTime)
        elif 'joke' in statement:
            speak(f"Hope you like this one ")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen.")
            print(joke)



