import speech_recognition as sr 
import datetime 
import subprocess
import pywhatkit 
import pyttsx3 
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('clearing background noises..please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('ask me anything.....')
        recorded_audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(recorded_audio)
            print('Your message:', format(command))
            
            if 'open' in command:
                a = 'opening youtube..'
                engine.say(a)
                engine.runAndWait()
                pywhatkit.playonyt(command)  

            else: 
                'run' in command
                b = 'opening whats app..'
                engine.say(b)
                engine.runAndWait()
                pywhatkit.sendwhatmsg("+917569201154", "Hello!", 12, 30)(command)   

        except Exception as ex:
            print(ex)

cmd() 