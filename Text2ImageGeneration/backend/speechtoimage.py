import speech_recognition as sr
import os
from openai import OpenAI
import requests
import webbrowser



# api_key = ""
# monsterapi = Client(api_key)
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    try:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Please Say Something")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        text = recognizer.recognize_google(audio, language="en-US")
        print("You:", text)
    except sr.UnknownValueError:
        print("Sorry Could not understand audio")
os.environ["NEBIUS_API_KEY"] = ""

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)
response = client.images.generate(
    model="stability-ai/sdxl",
    response_format="url",
    extra_body={
        "response_extension": "png",
        "width": 512,
        "height": 512,
        "num_inference_steps": 30,
        "negative_prompt": "",
        "seed": -1,
        "loras": None
    },
    prompt="Astronaut riding a horse"
)
# while True:
file_name = 3
image = requests.get(response.data[0].url)
with open(f"astronaut{file_name}.png", "wb") as f:
    f.write(image.content)
    # image.save(f"astronaut_horse{file_name}.png")
    file_name += 1

