from cmu_112_graphics import *
from gtts import gTTS
import os
import time
import speech_recognition as sr  


def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.insA1="Hello,I am COVID Killer."
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
    app.countdown=120
    
    


def mousePressed(app, event):
    if (app.isStarted==False):
        if (0<event.x<app.width and 0<event.y<app.height):
            app.isStarted=True
            app.isInsC=True
            app.timer=0
            print("Process Started")
    elif(app.isInsD==True):
        if (0<event.x<app.width and 0<event.y<app.height):
            app.isInsE=True
            app.isInsD=False
            app.timer=0
    elif(app.isInsG==True):
        if (0<event.x<app.width and 0<event.y<app.height):
            app.isInsH=True
            app.isInsG=False
            app.timer=0
            
def drawInsA(app,canvas):
    if (app.isStarted==False and app.isInsAB==1):
        canvas.create_text(app.width/2, app.height/2-100, text=app.insA1,
                            font='Times 60 bold')
        canvas.create_text(app.width/2, app.height/2+100, text=app.insA2,
                            font='Times 60 bold')
    
def drawInsB(app,canvas):
    if (app.isStarted==False and app.isInsAB==-1):
        canvas.create_text(app.width/2, app.height/2-200, text=app.insB1,
                            font='Times 60 bold')
        canvas.create_text(app.width/2, app.height/2, text=app.insB2,
                            font='Times 60 bold')
        canvas.create_text(app.width/2, app.height/2+200, text=app.insB3,
                            font='Times 60 bold')
def drawInsC(app,canvas):
    if (app.isStarted==True and app.isInsC==True):
            
        canvas.create_text(app.width/2, app.height/2-200, text=app.insC1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2, text=app.insC2,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+200, text=app.insC3,
                            font='Times 50 bold')

def drawInsD(app,canvas):
    if (app.isStarted==True and app.isInsD==True):
            
        canvas.create_text(app.width/2, app.height/2-240, text=app.insD1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2-80, text=app.insD2,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+80, text=app.insD3,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+240, text=app.insD4,
                            font='Times 50 bold')

def drawInsE(app,canvas):
    if (app.isStarted==True and app.isInsE==True):
            
        canvas.create_text(app.width/2, app.height/2-240, text=app.insE1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2-80, text=app.insE2,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+80, text=app.insE3,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+240, text=app.insE4,
                            font='Times 50 bold')
def drawInsG(app,canvas):
    if (app.isStarted==True and app.isInsE==True):
            
        canvas.create_text(app.width/2, app.height/2-240, text=app.insG1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2-80, text=app.insG2,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+80, text=app.insG3,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+240, text=app.insG4,
                            font='Times 50 bold')   
def insABSwitch(app):
    if (app.timer%500==0):
        app.isInsAB*=-1
        if app.timer>=1000:
            speechRecognition(app)
            if len(app.speechRecognized)>=9 and app.speechRecognized[0,9]=="hey let's":
                app.isStarted=True
                app.isInsC=True
            else:os.system("omxplayer errorMessage.mp3") 
            
            
def speechRecognition(app):
    
    with sr.Microphone() as source:  
        #print("Please wait. Calibrating microphone...")  
        # listen for 5 seconds and create the ambient noise energy level
        os.system("omxplayer beep.wav")
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
                if (app.timer==50):
                    #voiceIns = gTTS(text=app.insC, lang=app.language, slow=False) 
                    #voiceIns.save("voiceInstruction1.mp3") 
                    os.system("omxplayer voiceInstruction1.mp3") 
                if (app.timer==200):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    app.isInsC=False
                    app.isInsD=True
                    app.timer=0
            elif (app.isInsD==True):
                if app.timer==50:os.system("omxplayer voiceInstruction2.wav") 
                if (app.timer>=1000 and app.timer%200==0):
                    #voiceIns = gTTS(text=app.insD, lang=app.language, slow=False) 
                    #voiceIns.save("voiceInstruction2.wav") 
                    speechRecognition(app)
                    if len(app.speechRecognized)>=9 and app.speechRecognized[0,9]=="i'm ready":
                        app.isInsE=True
                        app.isInsD=False
                        app.timer=0
                    else:os.system("omxplayer errorMessage.mp3") 
            elif (app.isInsE==True):
                if (app.timer==50):
                    #voiceIns = gTTS(text=app.insE, lang=app.language, slow=False) 
                    #voiceIns.save("voiceInstruction.wav") 
                    os.system("omxplayer voiceInstruction3.wav")  
                    app.isInsE=False
                    app.isInsF=True
                    app.timer=0
            elif (app.isInsF==True):
                app.countDown-=10
            elif (app.isInsG==True):
                if app.timer==50:os.system("omxplayer voiceInstruction4.wav") 
                if (app.timer>=1000 and app.timer%200==0):
                    #voiceIns = gTTS(text=app.insD, lang=app.language, slow=False) 
                    #voiceIns.save("voiceInstruction2.wav") 
                    speechRecognition(app)
                    if len(app.speechRecognized)>=8 and app.speechRecognized[0,7]=="mission":
                        app.isInsH=True
                        app.isInsG=False
                        app.timer=0
                    else:os.system("omxplayer errorMessage.mp3")
            elif (app.isInsH==True):
                if (app.timer==50):
                    #voiceIns = gTTS(text=app.insE, lang=app.language, slow=False) 
                    #voiceIns.save("voiceInstruction.wav") 
                    os.system("omxplayer voiceInstruction5.wav")
                if (app.timer==100)
                    appStarted(app)
    
def redrawAll(app, canvas):
    #drawBG(app,canvas)
    drawInsA(app,canvas)
    drawInsB(app,canvas)
    drawInsC(app,canvas)
    drawInsD(app,canvas)
    drawInsE(app,canvas)
    drawInsF(app,canvas)
    drawInsG(app,canvas)
    drawInsH(app,canvas)


runApp(width=1280, height=800)