from flask import *
import _thread
import threading
start=3
import glob
import time
import pygame
import time as t
def get():
    return str(time.asctime())
paused=False
pygame.init()
window=pygame.display.set_mode((500,500))
pygame.mixer.init()
stand="not logged in"
mp3=glob.glob("*.mp3")
pygame.mixer.music.load(mp3[start])
pygame.mixer.music.play(1)
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    val='''<h1>Hello!<h1><strong>Mp3 server running<strong><p>'''+mp3[start]+'''</p>

<a href="/next">Next song</a>
<a href="/p">pause or resume</a>
<a href="/pre">Previous song</a>
<a href="/vold">Volume down</a>
<a href="/volu">Volume up</a>
<P>Server using flask</p>
<a href="/mlog">Log</a>
    

<p>
this web music server was created by java archive
</p>
    
    '''
    for x in mp3:
        val=val+'''<p align="center">'''+x+"</p>"
    return val
#####def
        
@app.route('/listen')
def req():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('temp.html',
                           title='Home',
                           user=user)

medialog=["Start server"]
visits=10
@app.route('/d')
def x():
    global visits
    visits = visits+1
    return"<p> you are the     "+str(visits)+"th visitor </p>"
@app.route('/p')

def pause():
    
    global paused
    print("pause   "+str(paused))
    if not paused:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    paused=not paused
    medialog.append(get()+"  pause  "+str(paused))
    return  redirect("/", code=302)

medialog=["Start server"]
@app.route('/vold')
def vold():
    try:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.1)
        medialog.append(get()+"  Volume down "+str(pygame.mixer.music.get_volume()))
    except:
        print("error down")
    
    return  redirect("/", code=302)
    
@app.route('/volu')
def volu():
    print("""set volume up""")
    try:
        print("""set volume up """)
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.1)
        medialog.append(get()+" Volume up "+str(pygame.mixer.music.get_volume()))
    except:
        print("down error")
    return  redirect("/", code=302)
@app.route("/mlog")

def mlog():
    global medialog
    
    output="<h1>Log</h1>"
    for x in medialog:
        output=output+"<p>"+x+"  </p> "
    return output
@app.route('/next')

def avoidkeywordnext():
    global mp3
    global paused
    global start
    global medialog
    fadesecs=1500
    print("pause   "+str(paused))
    try:
        mp3=glob.glob("*.mp3")
        start=start+1
        pygame.display.set_caption(mp3[start])
    
        if start==-1:
            start=len(mp3)-1
        if start==len(mp3):
            start=0
        pygame.mixer.music.stop()
        good=False
        while not good:
            try:
                pygame.mixer.music.load(mp3[start])
                good=True
            except:
                start=start+1
                
        pygame.mixer.music.play(1)
        medialog.append("next   "+mp3[start]+"   "+get())
    except:
        print("error:right")
    return  redirect("/", code=302)
@app.route('/pre')

def pre():
    global mp3
    global paused
    global start
    global medialog
    fadesecs=500
    print("pause   "+str(paused))
    try:
        print("1")
        mp3=glob.glob("*.mp3")
        print("2")
        start=start-1
        print("3")
        pygame.display.set_caption(mp3[start])
        print("4")
        if start==-1:
            start=len(mp3)-1
        if start==len(mp3):
            start=0
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load(mp3[start])
        except:
            print("A load error started")

        pygame.mixer.music.play(1)
               
        medialog.append("previous   "+mp3[start]+"\t"+get())
    except:
        print("error:left")
        print("finish execute")
    return  redirect("/", code=302)
@app.route("/stop")
def stop():
    pygame.mixer.music.stop()

@app.route('/login', methods=['GET', 'POST'])

def login():
    global stand
    if request.method == 'POST':
        stand="loged in"
        return "<h1>logging in please refresh</h1>"
        
    else:
        return stand
def print_time( threadName, delay):
    while True:
        if not pygame.mixer.music.get_busy():
            mp3=glob.glob("*.mp3")
            try:
                start=start+1
                if start==-1:
                    start=len(mp3)-1
                if start==len(mp3):
                    start=0
                pygame.display.set_caption(mp3[start])

                
                pygame.mixer.music.stop()
                pygame.mixer.music.load(mp3[start])
                pygame.mixer.music.play(1)
            except:
                print("error:auto")
   

class d (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
      
   def run(self):
      while True:
        if not pygame.mixer.music.get_busy():
            mp3=glob.glob("*.mp3")
            try:
                start=start+1
                if start==-1:
                    start=len(mp3)-1
                if start==len(mp3):
                    start=0
                pygame.display.set_caption(mp3[start])

                
                pygame.mixer.music.stop()
                pygame.mixer.music.load(mp3[start])
                pygame.mixer.music.play(1)
            except:
                print("error:auto")

@app.route('/logdirect')
def logindirect():
    global stand
    
    stand="loged in"
    return "<h1>logging</h1>"


import sys
if len(sys.argv)==2:
    if sys.argv[1]=="cmdline":
        print('''
cmdline mode    
Starting server
Go to ip:5000


        ''')
        medialog.append("Started with cmdline")
#auto=d()
#auto.start()
print("rest")


app.run(host= '192.168.29.193')































