import pyttsx3
import speech_recognition as sr

def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    id=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice',id)
    engine.say(text=text)
    engine.runAndWait()
    
def speechrecognition():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognition...")   
        query=r.recognize_google(audio,language="en")
        return query.lower()
    except:
        return ""
print(speechrecognition())

            
    
        
