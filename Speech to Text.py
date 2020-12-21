import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print('say something')
    audio =r.listen(source)
    print('time over thnks.')
    try:
        print("text:" +r.recognize_google(audio))
    except:
        print('check internet connectivity')