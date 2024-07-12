import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import pyautogui
import time
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)
camera_open=False

#text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#convert voice to text    

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=10)
    try:
        print("recogning...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        speak("say that again please...")
        return "none"
    return query
#wish
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning!")
    elif hour >12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening!")
    speak(" i am jarvis sir please tell me how can i help you")  
# def sendEmail(to, subject, content):
#     try:
#         sender_email = '28manomanu@gmail.com'
#         sender_password = 'ugwz colo huvo iemi'
        
#         # Setting up the MIME
#         message = MIMEMultipart()
#         message['From'] = sender_email
#         message['To'] = to
#         message['Subject'] = subject
#         message.attach(MIMEText(content, 'plain'))
        
#         # Connecting to the server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.ehlo()
#         server.login(sender_email, sender_password)
        
#         # Sending the email
#         server.sendmail(sender_email, to, message.as_string())
#         server.close()
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email. Error: {e}") 


def open_camera():
    global camera_open
    camera_open = True
    cap = cv2.VideoCapture(0)
    while camera_open:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        if cv2.waitKey(50) == 27:  # Press ESC to close manually
            break
    cap.release()
    cv2.destroyAllWindows()
    camera_open=False

def handle_query(query):
    global camera_open
    if "close camera" in query.lower():
        print(camera_open)
        if camera_open:
            speak("Okay sir, closing camera")
            camera_open = False  # Set flag to stop camera loop
        else:
            speak("Camera is not open, sir.")
    elif "open camera" in query.lower():
        if not camera_open:
            speak("Okay sir, opening camera")
            camera_thread = threading.Thread(target=open_camera)
            camera_thread.start()
        else:
            speak("Camera is already open, sir.")
def sendEmail(to, subject, content):
    try:
        sender_email = '2manomanu@gmail.com'
        sender_password = 'ugwz colo huvo iemi'
        
        # Setting up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to
        message['Subject'] = subject
        message.attach(MIMEText(content, 'plain'))
        
        # Connecting to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.ehlo()
        server.login(sender_email, sender_password)
        
        # Sending the email
        server.sendmail(sender_email, to, message.as_string())
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")



if __name__ =="__main__":
    wish()
    # takecommand()
    # speak("fuck you!")
    while True:
    # if 1:
        query=takecommand().lower()
        #logic building for tasks
        if "open notepad" in query:
            npath='C:\\Windows\\System32\\notepad.exe'
            os.startfile(npath)
        elif "close notepad" in query:
            speak("okay sir,closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif'open command prompt' in query:
            os.system("start cmd") 
        elif 'open camera' in query:
            handle_query(query)
        elif 'close camera' in query:
            handle_query(query) 
        elif "play music" in query:
            music_dir="C:\\Users\\28man\\OneDrive\\Pictures\\song" 
            songs=os.listdir(music_dir)
            rd= random.choice(songs) 
            os.startfile(os.path.join(music_dir,rd))       
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
        elif "wikipedia" in query: 
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com") 
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")  
        elif "open twitter" in query:
            webbrowser.open("twitter.com") 
        elif "open google" in query:
            speak("sir,what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm.replace(' ', '+')}")  
        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com")
        elif "open chatgpt" in query.lower():
           webbrowser.open("https://chatgpt.com")
        elif "send message" in query:
            pywhatkit.sendwhatmsg("+919353660321", "This is a test message!", 19,21)
        elif "on youtube" in query:
            query=query.replace("on youtube","")
            pywhatkit.playonyt(query)
        elif "send email" in query:
            try:
                speak("what should i say?")
                content=takecommand().lower()
                to="28manomanu@gmail.com"
                subject=" This is Jarvis"
                sendEmail(to,subject,content)
                speak("Email has been sent to manoj")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this email to manoj")
        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")    
        elif "no thanks" in query:
            speak("thanks for using me, Have a Good day")
            sys.exit()
        speak("sir,do you have any other work")           



