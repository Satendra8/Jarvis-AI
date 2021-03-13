import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import webbrowser



def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if (hour<12 or hour ==12):
        speak(f"Good Morning. its {datetime.datetime.now().hour}:{datetime.datetime.now().minute} AM. ")
    
    elif(hour>12 and hour < 18):
        speak(f"Good Afternoon. its {datetime.datetime.now().hour}:{datetime.datetime.now().minute} PM.")
    else:
        speak(f"Good evening. its {datetime.datetime.now().hour}:{datetime.datetime.now().minute} PM")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say someting ')
        print('Listening...')
        audio = r.listen(source,phrase_time_limit=3)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f'user said : {query} ')
        except:
            print('say that again')
            return 'None'
    return query

def TaskExecution():
    wish()
    while True:
        query = takeCommand()
        if 'how are you' in query:
            speak('I am fine sir.   and you')
            print('jarvis : I am fine sir,  and you')
        elif 'hi' in query:
            speak('hello sir')
            print('Jarvis : Hello sir')
            speak('opening sir')
        elif 'Google' in query:
            webbrowser.open_new('www.google.com')
        elif 'YouTube' in query:
            speak('opening sir')
            webbrowser.open('www.youtube.com')
        elif 'sleep' in query:
            speak('ok sir. i am going to sleep. wake up me when you need')
            print('jarvis : ok sir. i am going to sleep. wake up me when you need')
            break
        elif 'goodbye' in query:
            speak('ok sir, Thanks for using me')


        





if __name__ == "__main__":
    wish()
    speak('I am Jarvis sir. Tell me how may i help you')

    while True:
        permission = takeCommand()
        if 'wake up' in permission:
            TaskExecution()
        elif 'goodbye' in permission:
            speak('ok sir, thanks for using me')
            exit()
    
        