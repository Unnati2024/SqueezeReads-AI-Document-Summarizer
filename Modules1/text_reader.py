# modules/text_reader.py

import pyttsx3

def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)  # Speed
        engine.setProperty('volume', 0.9)  # Volume
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"❌ Text-to-speech error: {e}")
