import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")   
    else:
        speak("Good Evening")  

    speak("Hello Sir. Please tell me how may I help you ")      

def takeCommand():
    """It takes microphone from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tejasgathadi@gmail.com', 'fackihhbixncdngf')
    server.sendmail('tejasgathadi@gmail.com', to ,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Acording to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")

        elif 'play music' in query:
            music_dir = 'T:\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"Sir, the time is {strTime}")

        elif 'email to tejas' in query:
            try:
                print("What should I send")
                speak("What should I say")
                content = takeCommand()
                to = "tejasgathadi@gmail.com"
                sendEmail(to, content)
                print("Mail has been sent")
                speak("Email has been sent!..")
            except Exception as e:
                speak("Sorry there was an error while sending email, try again")    

        elif 'quit' in query:
            print("Hope I have helped you with your request, see you around, till then bye bye")
            speak("Hope I have helped you with your request, see you around, till then bye bye")
            exit()        
            





    

