import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning...Sir!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon...Sir!!")
    else:
        speak("Good Evening...Sir!!")

    speak("I am Jarvis    Please tell me how can i help you")                

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query        

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #add the email and password from which you have to send email
    server.login('your email','password')
    server.sendmail('your email',to,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
    #logic for excuting takes based on query
        if  'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            gaana = os.listdir(music_dir)
            print(gaana)
            os.startfile(os.path.join(music_dir,gaana[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'email' in query:
            try:
                speak("What should i say?    Sir")
                content = takeCommand()
                # add the email to whom you have to send email
                to = "other email"
                sendEmail(to,content)
                speak("Email has been sent   Sir")
            except Exception as e:
                print(e)
                speak("Sorry sir    Email has not been sent ")                  
                
        elif 'thank you' in query:
            speak ("You are welcome...Sir....Call me if you need any help")
            exit()
