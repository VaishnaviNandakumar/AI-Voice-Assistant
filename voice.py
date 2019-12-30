import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=11:
        speak("Good Morning!")
    if hour>=12 and hour<=16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hi Varsha! How can I help you?")

if __name__ == "__main__":
    WishMe()