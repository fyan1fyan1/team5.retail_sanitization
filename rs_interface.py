from cmu_112_graphics import *
from gtts import gTTS
import os
import time
import speech_recognition as sr
import threading
from playsound import playsound
from audioplayer import AudioPlayer
from picamera import PiCamera
import random
import serial
camera = PiCamera()
ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser.flush()


def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.insA1="Hello, this is COVID Killer."
    app.insA2="Can I help you sanitize your items?"
    
    app.insB1="To start sanitization,"
    app.insB2="tap the screen"
    app.insB3="or say 'Hey, let's start'"
    
    app.insC="System processing.Please wait until the drawer comes out."
    app.insC1="System processing..."
    app.insC2="Please wait until"
    app.insC3="the drawer comes out"
    
    app.insD="Please put your items in the drawer. Then say I'm ready or tap the screen. I will take care of them."
    app.insD1="Please put your items in the drawer."
    app.insD2="Then say 'I'm ready',"
    app.insD3="or tap the screen."
    app.insD4="I will take care of them."
    
    app.insE="You are all set. I will sanitize them for you. The whole process shall take 2 minutes.Meanwhile you can check the process. I will soon show you the video."
    app.insE1="I will sanitize them for you."
    app.insE2="The whole process shall take 2 minutes."
    app.insE3="Meanwhile you can check the process."
    app.insE4="I will soon show you the video."
    
    app.insG="Your items are now sanitized. Please take your items and say mission complete when you finish."
    app.insG1="Your items are now sanitized."
    app.insG2="Please take your items"
    app.insG3="and say 'mission complete'"
    app.insG4="when you finish."
    
    app.insH="Thank you. I hope you enjoy your day."
    app.insH1="Thank you."
    app.insH2="I hope you enjoy your day."
    
    app.timer=0
    
    app.isStarted=False
    app.isInsAB=1
    app.isInsC=False
    app.isInsD=False
    app.isInsE=False
    app.isInsF=False
    app.isInsG=False
    app.isInsH=False
    
    app.language = 'en'
    app.r = sr.Recognizer()
    app.speechRecognized=""
    app.countDown=120
    app.camera = camera
    app.camera.resolution = (1366, 600)
    app.demo=[]
    for i in range (30):
        x=random.randint(10,1350)
        y=random.randint(300,500)
        r=random.randint(10,50)
        vx=random.randint(-3,3)
        vy=random.randint(-3,3)
        G=random.randint(170,200)
        R=random.randint(170,220)
        B=random.randint(220,255)
        app.demo.append([x,y,r,R,G,B,vx,vy])
    #app.textColor=250
def drawDemo(app,canvas):
    for i in range (30):
        x,y,r,R,G,B,vx,vy=app.demo[i]
        canvas.create_oval(x-r,y-r,x+r,y+r,outline=transRGB(R,G,B),fill=transRGB(R,G,B))

def moveDemo(app):
    if app.timer%20==0:
        for i in range (30):
            app.demo[i][0]+=app.demo[i][6]
            app.demo[i][1]+=app.demo[i][7]
def transRGB(r,g,b):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % (r,g,b)

def mousePressed(app, event):
    if (app.isStarted==False):
        if (0<event.x<app.width and 0<event.y<app.height):
            app.isStarted=True
            app.isInsC=True
            app.timer=0
            ser.write("c".encode('utf-8'))
            print("Process Started")
    elif(app.isInsD==True):
        if (0<event.x<app.width and 0<event.y<app.height):
            app.isInsE=True
            app.isInsD=False
            app.timer=0
            ser.write("d".encode('utf-8'))
    elif(app.isInsG==True):
        if (0<event.x<app.width and 0<event.y<app.height):
            app.isInsH=True
            app.isInsG=False
            app.timer=0
            ser.write("g".encode('utf-8'))
            
def drawInsA(app,canvas):
    if (app.isStarted==False and app.isInsAB==1):
        tcm=app.timer%500
        if tcm <=120:textColor=250-tcm*2
        #elif tcm>400:textColor=10+(tcm-400)*2
        else: textColor=10
        canvas.create_text(app.width/2, app.height/2-100, text=app.insA1,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50')
        canvas.create_text(app.width/2, app.height/2+100, text=app.insA2,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50')
    
def drawInsB(app,canvas):
    if (app.isStarted==False and app.isInsAB==-1):
        tcm=app.timer%500
        if tcm <=120:textColor=250-tcm*2
        #elif tcm>400:textColor=10+(tcm-400)*2
        else: textColor=10
        canvas.create_text(app.width/2, app.height/2-200, text=app.insB1,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 60')
        canvas.create_text(app.width/2, app.height/2, text=app.insB2,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 60')
        canvas.create_text(app.width/2, app.height/2+200, text=app.insB3,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 60')
def drawInsC(app,canvas):
    if (app.isStarted==True and app.isInsC==True):
        tcm=app.timer
        if tcm <=120:textColor=250-tcm*2
        else: textColor=10
        canvas.create_text(app.width/2, app.height/2-200, text=app.insC1,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2, text=app.insC2,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2+200, text=app.insC3,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')

def drawInsD(app,canvas):
    if (app.isStarted==True and app.isInsD==True):
        tcm=app.timer
        if tcm <=120:textColor=250-tcm*2
        else: textColor=10
        canvas.create_text(app.width/2, app.height/2-240, text=app.insD1,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2-80, text=app.insD2,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2+80, text=app.insD3,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2+240, text=app.insD4,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')

def drawInsE(app,canvas):
    if (app.isStarted==True and app.isInsE==True):
        tcm=app.timer
        if tcm <=120:textColor=250-tcm*2
        else: textColor=10
        canvas.create_text(app.width/2, app.height/2-240, text=app.insE1,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2-80, text=app.insE2,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2+80, text=app.insE3,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2+240, text=app.insE4,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
def drawInsF(app,canvas):
    if(app.isStarted==True and app.isInsF==True):
        textColor=10
        mins, secs = divmod(app.countDown, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        canvas.create_text(app.width/2, app.height/2+300, text=timer,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50')
def drawInsG(app,canvas):
    if (app.isStarted==True and app.isInsG==True):
        tcm=app.timer
        if tcm <=120:textColor=250-tcm*2
        else: textColor=10
        canvas.create_text(app.width/2, app.height/2-240, text=app.insG1,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2-80, text=app.insG2,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2+80, text=app.insG3,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2+240, text=app.insG4,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
def drawInsH(app,canvas):
    if (app.isStarted==True and app.isInsH==True):
        tcm=app.timer
        if tcm <=120:textColor=250-tcm*2
        else: textColor=10
        canvas.create_text(app.width/2, app.height/2-100, text=app.insH1,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
        canvas.create_text(app.width/2, app.height/2+100, text=app.insH2,fill=transRGB(textColor,textColor,textColor),
                            font='Futura 50  ')
def insABSwitch(app):
    if (app.timer%500==0):
        app.isInsAB*=-1
        if app.timer>=1000:
            speechRecognition(app)
            if len(app.speechRecognized)>=9 and app.speechRecognized[0:9]=="hey let's":
                app.isStarted=True
                app.isInsC=True
                app.timer=0
                ser.write("c".encode('utf-8'))
            else:AudioPlayer("errorMessage.mp3").play(block=True)
    return None
            
            
def speechRecognition(app):
    
    with sr.Microphone() as source:  
        print("Please wait. Calibrating microphone...")  
        # listen for 5 seconds and create the ambient noise energy level

        AudioPlayer("beep.wav").play(block=True)
        app.r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!") 
        audio = app.r.listen(source)  
   
         # recognize speech using Sphinx  
    try:
        app.speechRecognized=app.r.recognize_sphinx(audio)
        print("Sphinx thinks you said '" + app.speechRecognized + "'")  
    except sr.UnknownValueError:  
        print("Sphinx could not understand audio")  
    except sr.RequestError as e:  
        print("Sphinx error; {0}".format(e))  
    
def timerFired(app):
        app.timer+=10
        if (app.isStarted==False):
            insABSwitch(app)
        elif (app.isStarted==True):
            if (app.isInsC==True):
                if (app.timer==100):
                    voiceIns = gTTS(text=app.insC, lang=app.language, slow=False) 
                    voiceIns.save("voiceInstruction1.mp3") 
                    #os.system("omxplayer voiceInstruction1.mp3")
                    AudioPlayer("voiceInstruction1.mp3").play(block=True)
                if (app.timer==200):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    app.isInsC=False
                    app.isInsD=True
                    app.timer=0
            elif (app.isInsD==True):
                if app.timer==100:AudioPlayer("voiceInstruction2.mp3").play(block=True)
                if (app.timer>=500 and app.timer%200==0):
                    voiceIns = gTTS(text=app.insD, lang=app.language, slow=False) 
                    voiceIns.save("voiceInstruction2.wav") 
                    speechRecognition(app)
                    if len(app.speechRecognized)>=9 and app.speechRecognized[0:9]=="i'm ready":
                        app.isInsE=True
                        app.isInsD=False
                        app.timer=0
                        ser.write("d".encode('utf-8'))
                    else:AudioPlayer("errorMessage.mp3").play(block=True) 
            elif (app.isInsE==True):
                
                if (app.timer==100):
                    voiceIns = gTTS(text=app.insE, lang=app.language, slow=False) 
                    voiceIns.save("voiceInstruction.wav") 
                    AudioPlayer("voiceInstruction3.mp3").play(block=True)
                if (app.timer==200):
                    app.isInsE=False
                    app.isInsF=True
                    app.timer=0
                    app.camera.start_preview(alpha=240)
            elif (app.isInsF==True):
                if (app.timer==50):ser.write("f".encode('utf-8'))
                if app.timer%50==0:
                    app.countDown-=1
                if app.timer==6000:
                    app.isInsG=True
                    app.isInsF=False
                    app.timer=0
                    app.camera.stop_preview()
                    ser.write("g".encode('utf-8'))
            elif (app.isInsG==True):
                if app.timer==100:AudioPlayer("voiceInstruction4.mp3").play(block=True)
                if (app.timer>=1000 and app.timer%200==0):
                    voiceIns = gTTS(text=app.insD, lang=app.language, slow=False) 
                    voiceIns.save("voiceInstruction2.wav") 
                    speechRecognition(app)
                    if len(app.speechRecognized)>=8 and app.speechRecognized[0:7]=="mission":
                        app.isInsH=True
                        app.isInsG=False
                        app.timer=0
                        ser.write("g".encode('utf-8'))
                    else:AudioPlayer("errorMessage.mp3").play(block=True)
            elif (app.isInsH==True):
                if (app.timer==100):
                    ser.write("h".encode('utf-8'))
                    voiceIns = gTTS(text=app.insE, lang=app.language, slow=False) 
                    voiceIns.save("voiceInstruction.wav") 
                    AudioPlayer("voiceInstruction5.mp3").play(block=True)
                if (app.timer==1000):
                    appStarted(app)
        
        moveDemo(app)
    
def redrawAll(app, canvas):
    drawDemo(app,canvas)
    drawInsA(app,canvas)
    drawInsB(app,canvas)
    drawInsC(app,canvas)
    drawInsD(app,canvas)
    drawInsE(app,canvas)
    drawInsF(app,canvas)
    drawInsG(app,canvas)
    drawInsH(app,canvas)


runApp(width=1366, height=704)