import pyttsx3
import speech_recognition as sr
import os
import time
import datetime
import webbrowser
import pyjokes
#sppech to text
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not understanding")
#text to sppech
def speechtxt(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    #male voice 0
    #female voice 1
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ =='__main__':
    
  if "hey ana" in speechtxt().lower() :
        print("test")
        while True:
          data1=sptext().lower()
          if "your name" in data1:
             name ="my name is ana"
             speechtxt(name) 
          elif "old are you" in data1:
             age="i am 5 years old "
             speechtxt(age)
          elif 'time' in data1:
             time=datetime.datetime.now().strftime("%1%M%p")
             speechtxt(time)
          elif 'youtube' in data1:
             webbrowser.open("https://www.youtube.com")
          elif "joke" in data1:
             joke_1=pyjokes.get_joke(language="en",category="natural")
             speechtxt(joke_1)
          elif "play song " in data1:
             add="path address"
             listesong=os.listdir(add)
             print(listesong)
             os.startfile(os.path.join(add,listesong[1]))
          elif "exit" in data1:
             speechtxt("thank you") 
             break
          time.sleep(5)       
  else:
     print("thank")   
        
   
