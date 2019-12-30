import pyttsx3
import datetime
import speech_recognition as speech
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
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

    speak("Hi Kuki! How can I help you?")

def takeCommand():
    r = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said : {query}\n")
    
    except Exception as e:
        print(e)
        print("I didn't hear you..")
        return "None"

    return query

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
    
    # Execution Logic
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            speak(results)    
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\ACER\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H: %M: %S")
            speak(f"The time is, {Time}")