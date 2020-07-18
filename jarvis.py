import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hours = int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak ("Good Morning!!")
    elif hours>=12 and hours<18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")

    speak("I am Jarvis sir . Please tell me how may I  help you !!")
def takecomand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing......")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        
        print("Say that again please...")
        return "None"
    return query
#you need to enable control access to less secure app from who so ever email id you wanted to send mail
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kkr@aiet.edu.in','***********password**here*******') #senders email and password here
    server.sendmail('abc@gmail.com', to, contnet() #recievers email id here
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecomand().lower()

    #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia!!')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        #elif 'play music' in query:
        #    music_dir = "insert directory path local"
        #    songs = os.listdir(music_dir)
        #    print(songs)
        #    os.startfile(os.path.join(music_dir,songs[1]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\tonys\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to tony' in query:
            try:
                speak("what should I say ??")
                content = takecomand()
                to = "abc@gmail.com" #recievers email id 
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to sent this email to recepient")

        else:
            speak('Good bye!!')

else :
    speak('jarvis not working! Good bye!!')    