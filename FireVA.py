#! python3
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import pyaudio
import time
import os
import webbrowser

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
r = sr.Recognizer()

def talk(text):
    
    engine.say(text)
    print(text)
    engine.runAndWait()
    
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        command = r.listen(source)
        
    try:
        print("you said - " + r.recognize_google(command))
        return r.recognize_google(command)
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def run_alexa():
    command = take_command()
    
    if "play" in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        
    elif "search" in command:
        command = command.replace("search",'')
        pywhatkit.search(command)
        
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('current time is' + time)
        
    elif "joke" in command:
        joke=pyjokes.get_joke()
        talk(joke)

    elif "tell me about yourself" in command:
        talk('Hello, I am Pushkar\'s Virtual Assistant Fire-VA')
        talk('Nice to meet you!')

    elif "weather" in command:
        pywhatkit.search(command)
        
    else:
        talk('please say another command, I am good at telling jokes maybe you wanna hear?')

talk("how can i help you")      
run_alexa()
time.sleep(20)




