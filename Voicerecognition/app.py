import speech_recognition as sr
import pyttsx3
import requests
import datetime
import flask
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return
engine = pyttsx3.init()
text = "Voice Recognition"
engine.say(text)
print("Assistant: Welcome to Voice Recognition")
engine.runAndWait()

while True:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Please Say Something")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text= recognizer.recognize_google(audio, language="en-US").lower()
            print("You:",text)
        except sr.UnknownValueError:
            print("Sorry Could not understand audio")
        if "weather" in text:
            city="jammu"
            api_key="67c6a0f786beeb59d786ab0ae73def1d"
            url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                weather = weather_data["weather"][0]["description"]
                temperature = weather_data["main"]["temp"]
                print(f"Assistant:Current Weather is {weather} and temperature is {temperature}")
                engine.say(f"Current Weather for {city} is {weather} and temperature is {temperature}")
            else:
                print("Assistant: Sorry I could'nt fetch the weather data")
                engine.say(f"Sorry I could'nt fetch the weather data")

            engine.runAndWait()
        elif "news" in text:
            api_key_news="56169085e769467f8a7cd30cf945dfc3"
            url_news= f"https://newsapi.org/v2/top-headlines?country=us&apikey={api_key_news}&language=en"
            response = requests.get(url_news)
            if response.status_code == 200:
                articles = response.json().get("articles",[])
                headlines = [article["title"] for article in articles[:5]]
                print(f"Here are top news")
                for i,headline in enumerate(headlines,1):
                    print(f"{i}. {headline}")
                engine.say(f"Here are top news","+".join(headlines))
                engine.runAndWait()
        elif "time" in text:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"The current time is {time}")
            engine.say(time)
            engine.runAndWait()
        elif "exit" or "quit" in text:
            break
        else:
            print("Could'nt understand the command")