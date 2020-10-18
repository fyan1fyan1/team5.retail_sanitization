from cmu_112_graphics import *
from gtts import gTTS 
import os


def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.insA1="Hello,"
    app.insA2="can I help you sanitize your items?"
    
    app.insB1="To start sanitization,"
    app.insB2="tap the screen"
    app.insB3="or step on foot paddle"
    
    app.insC="System processing...Please wait untill the drawer comes out."
    app.insC1="System processing..."
    app.insC2="Please wait untill"
    app.insC3="the drawer comes out"
    
    app.insD="Please put your items in the drawer. Then step on foot paddle or tap the screen. I will take care of them."
    app.insD1="Please put your items in the drawer."
    app.insD2="Then step on foot paddle,"
    app.insD3="or tap the screen."
    app.insD4="I will take care of them."
    
    app.insE="You are all set. I will sanitize them for you. The whole process shall take 2 minutes. "
    app.insE1="You are all set."
    app.insE2="I will sanitize them for you."
    app.insE3="The whole process shall take 2 minutes."
    app.insE4="Meanwhile you can check the process."
    app.insE5="I will soon show you the video."
    
    
    app.insABTimeCounter=0
    app.insCCounter=0
    app.insDCounter=0
    app.insECounter=0
    
    app.isStarted=False
    app.isInsAB=1
    app.isInsC=True
    app.isInsD=False
    app.isInsE=False
    app.isInsF=False
    
    app.language = 'en'
    
    
    


def mousePressed(app, event):
    if (app.isStarted==False):
        if (0<event.x<app.width and 0<event.y<app.height):
            app.isStarted=True
            print("Process Started")
    elif(app.isInsD==True):
        if (0<event.x<app.width and 0<event.y<app.height):
            app.isInsE=True
            app.isInsD=False
    
            
def drawInsA(app,canvas):
    if (app.isStarted==False and app.isInsAB==1):
        canvas.create_text(app.width/2, app.height/2-50, text=app.insA1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+50, text=app.insA2,
                            font='Times 50 bold')
    
def drawInsB(app,canvas):
    if (app.isStarted==False and app.isInsAB==-1):
        canvas.create_text(app.width/2, app.height/2-100, text=app.insB1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2, text=app.insB2,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+100, text=app.insB3,
                            font='Times 50 bold')
def drawInsC(app,canvas):
    if (app.isStarted==True and app.isInsC==True):
            
        canvas.create_text(app.width/2, app.height/2-100, text=app.insC1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2, text=app.insC2,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+100, text=app.insC3,
                            font='Times 50 bold')

def drawInsD(app,canvas):
    if (app.isStarted==True and app.isInsD==True):
            
        canvas.create_text(app.width/2, app.height/2-150, text=app.insD1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2-50, text=app.insD2,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+50, text=app.insD3,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+150, text=app.insD4,
                            font='Times 50 bold')

def drawInsE(app,canvas):
    if (app.isStarted==True and app.isInsE==True):
            
        canvas.create_text(app.width/2, app.height/2-200, text=app.insE1,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2-100, text=app.insE2,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2, text=app.insE3,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+100, text=app.insE4,
                            font='Times 50 bold')
        canvas.create_text(app.width/2, app.height/2+200, text=app.insE5,
                            font='Times 50 bold')
        
        
def insABSwitch(app):
    if (app.insABTimeCounter==50):
        app.insABTimeCounter=0
        app.isInsAB*=-1
    
def timerFired(app):
        if (app.isStarted==False):
            app.insABTimeCounter+=1
            insABSwitch(app)
        if (app.isStarted==True):
            if (app.isInsC==True):
                app.insCCounter+=1
                if (app.insCCounter//100==0):
                    voiceIns = gTTS(text=app.insC, lang=app.language, slow=False) 
                    voiceIns.save("voiceInstruction.wav") 
                    os.system("start voiceInstruction.wav") 
                if (app.insCCounter==20):
                    app.isInsC=False
                    app.isInsD=True
            elif (app.isInsD==True):
                app.insDCounter+=1
                if (app.insDCounter//100==0):
                    voiceIns = gTTS(text=app.insD, lang=app.language, slow=False) 
                    voiceIns.save("voiceInstruction.wav") 
                    os.system("start voiceInstruction.wav") 
            elif (app.isInsD==True):
                app.insECounter+=1
                if (app.insDCounter//100==0):
                    voiceIns = gTTS(text=app.insE, lang=app.language, slow=False) 
                    voiceIns.save("voiceInstruction.wav") 
                    os.system("start voiceInstruction.wav") 
                if (app.insDCounter==20):
                    app.isInsE=False
                    app.isInsF=True

            
    
    
def redrawAll(app, canvas):
    drawInsA(app,canvas)
    drawInsB(app,canvas)
    drawInsC(app,canvas)
    drawInsD(app,canvas)
    drawInsE(app,canvas)


runApp(width=800, height=600)