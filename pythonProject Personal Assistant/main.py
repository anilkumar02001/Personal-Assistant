import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Personal Assistant Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Say that again please...")
        return ""

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)



def main():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open invertis university website' in query:
            webbrowser.open("www.invertisuniversity.ac.in")

        elif 'search' in query:
            x = query.split()
            q = "http://www.google.com/search?q="+str(x[1])
            webbrowser.open(q)

        elif 'youtube play' in query:
            x = query.split()
            q = "http://www.youtube.com/search?q=" + str(x[2:])
            webbrowser.open(q)

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("www.twitter.com")

        elif 'open whatsapp' in query:
            webbrowser.open("www.whatsapp.com")

        elif 'open infosys website' in query:
            webbrowser.open("www.infosys.com")

        elif 'open accenture website' in query:
            webbrowser.open("www.accenture.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif "open c drive" in query:
            os.startfile("C:")

        elif "open d drive" in query:
            os.startfile("D:")

        elif "open file manager" in query:
            codePath = "C:\\Windows\\explorer.exe"
            os.startfile(codePath)


        elif 'open vs code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open downloads' in query:
            codePath = "C:\\Users\\DELL\\Downloads"
            os.startfile(codePath)


        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            elif shutdown == "no":
                break

main()