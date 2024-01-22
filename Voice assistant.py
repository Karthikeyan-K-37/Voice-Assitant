from click import command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyowm
from tkinter.filedialog import *
from key import OPENWEATHER
import requests
import webbrowser as wb
import tkinter as tk
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def take_command():
    
    try:
        with sr.Microphone() as source:
            global command
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()        
    except:
        pass
    return command

def talk(text):
    engine.say(text)
    engine.runAndWait()
 

def news(command): 
    
    if "news" in command:
        def get_news(api_key):
            url = "https://newsapi.org/v2/top-headlines"
            params = {
                'country': 'in',  
                'apiKey': api_key,
            }

            response = requests.get(url, params=params)
            data = response.json()

            if response.status_code == 200 and data['status'] == 'ok':
                articles = data['articles']
                if articles:
                    first_article = articles[0]
                    title = first_article['title']
                    link = first_article['url']
                    return title, link
                else:
                    return None, None
            else:
                print(f"Failed to retrieve news. Status code: {response.status_code}")
                return None, None

        def main():
            api_key = 'GET YOUR OWN API FROM https://newsapi.org/'
            title, link = get_news(api_key)
            
            if title and link:
                talk(f"The first trending topic in the news in India is:")
                talk(title)
                talk("Let me open the article for you in your webbrowser")
                wb.open_new(link)
            else:
                print("No news available or there was an issue fetching the news.")

        if __name__ == "__main__":
            main()



def get_weather(command):
    home = 'Chennai, India'
    owm = pyowm.OWM(OPENWEATHER)
    mgr = owm.weather_manager()
    if "weather" in command:
        observation = mgr.weather_at_place(home)
        w = observation.weather
        temp = w.temperature('celsius')
        status = w.detailed_status
        talk("It is currently " + str(int(temp['temp'])) + " degrees and " + status)

      

def stop_travis():
    print("Stopping Travis...")
    talk("Goodbye!")
    sys.exit()


def run_Travis():
    
    command = take_command()
    if "travis" in command:
        command=command.replace('travis',' ')

        print(command)
        if 'play' in command:
        
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            pass
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            pass
        elif 'who is'  in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
            pass
        
        elif "weather" in command:
            talk(get_weather(command))
            pass
        
        elif "news" in command:
            talk(news(command))
            pass

        elif "exit" in command:
            talk("boiiiiiiiii")
            pass
        else:
            return None
    
      
while True:
    window = tk.Tk()
    window.title("Travis")
    start_button = tk.Button(window, text="Start Travis", command=run_Travis)
    start_button.pack()
    stop_button = tk.Button(window, text="Stop Travis", command=stop_travis)
    stop_button.pack()
    window.mainloop()
    run_Travis()  