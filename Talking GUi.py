import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import os
import pyautogui
import psutil
import pyjokes

import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voices','greek')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date)
    print(month)
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour>=6 and hour<12:
        speak("Good Morning AK47!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon AK47!")

    elif hour>=18 and hour<24:
        speak("Good Evening AK47!")

    else:
        speak("Good Night AK47!")

    speak("Jarvis at your Service. Please tell me how can I help You ")
#wishMe()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"AK47 Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('Your email','your password')
    server.sendmail('your email',to,content)

def screenshot():
    img=pyautogui.screenshot()
    img.save('/home/sai_krupa_reddy/Pictures/img.jpg')

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                print(":")
                to='the email that you are sending'
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email!!")
        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()
        elif 'search in firefox' in query:
            speak("What should i search ?")
            #In linux
            # chromepath='/bin/google-chrome'
            chromepath='C:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'logout' in query:
            os.system('shutdown -l')
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system('shutdown /r /t l')
        elif 'play songs' in query:
            songs_dir='D:\\Music'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'rememeber that' in query:
            speak("what should i remember?")
            data=takeCommand()
            speak("you said me to remmeber that"+data)
            remember = open('data.txt','w')
            remember.close()
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak('you said me to remember that'+remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
