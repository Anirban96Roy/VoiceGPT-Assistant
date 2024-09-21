import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import datetime
import google.generativeai as genai
import re

str=""
def ai_say(data1):
    global str
    
    print(data1)
    
    genai.configure(api_key=os.environ["API_KEY"])

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message({data1})
    response_text = response.text


    # Remove emojis and *
    response_text = re.sub(r'[^\w\s,.?!]', '', response_text)


    print(response_text)
    text_to_audio(x=response_text)

def ai_to_text(q):
    genai.configure(api_key=os.environ["API_KEY"])

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message({q})
    response_text = response.text

 

    # Remove emojis
    response_text = re.sub(r'[^\w\s,.?!]', '', response_text)


    print(response_text)

def audio_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as input:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(input)
        audio = recognizer.listen(input)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            return data
        except:
            print("Don't understand. Please try again")

def text_to_audio(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    text_to_audio("Hello sir  I am Baymax How can i help you?")
    while True:
        data1 = audio_to_text().lower()
        sites = [["youtube", "https://www.youtube.com/"], ["google", "https://www.google.com/"]]

        if "open" in data1:
            for site in sites:
                if f"open {site[0]}".lower() in data1:
                    text_to_audio(f"Opening {site[0]} sir")
                    webbrowser.open(site[1])
                    break
                
        elif "your name" in data1:
            name = "I am Baymax"
            text_to_audio(name)
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%H,%M,%S")
            text_to_audio(f"Sir the time is {time}")
        elif "mail" in data1:
            text_to_audio(f"Opening mail sir")
            outlook_path = r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"
            os.startfile(outlook_path)
        elif "ai".lower() in data1:
            ai_to_text(q=data1)
        elif "stop".lower() in data1:
            exit()
        else:
            ai_say(data1)
