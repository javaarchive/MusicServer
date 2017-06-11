import pygame
import threading
from tkinter import *
from pygame.constants import *
import sys
pygame.init()
fadesecs=2000
display=pygame.display.set_mode((800,800),pygame.RESIZABLE)
import glob
class gui (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def update(self):
        global mp3
        mp3=glob.glob("*.mp3")
    def run(self):
        
        win=Tk()
        win.title("Controller")
        updater=Button(win,text="update",command=self.update)
        updater.pack()
        win.mainloop()
        
        
mp3=glob.glob("*.mp3")
start=1
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.load(mp3[start])
pygame.mixer.music.play(1)
paused=False
print("enter loop")
display.fill((255,255,255))
img=pygame.image.load("logo.jpg")
display.blit(img,(0,0))
pygame.display.set_caption(mp3[start])
thickarrow_strings = (               #sized 24x24
  "XX                      ",
  "XXX                     ",
  "XXXX                    ",
  "XX.XX                   ",
  "XX..XX                  ",
  "XX...XX                 ",
  "XX....XX                ",
  "XX.....XX               ",
  "XX......XX              ",
  "XX.......XX             ",
  "XX........XX            ",
  "XX........XXX           ",
  "XX......XXXXX           ",
  "XX.XXX..XX              ",
  "XXXX XX..XX             ",
  "XX   XX..XX             ",
  "     XX..XX             ",
  "      XX..XX            ",
  "      XX..XX            ",
  "       XXXX             ",
  "       XX               ",
  "                        ",
  "                        ",
  "                        ")
void=pygame.cursors.compile(thickarrow_strings)
pygame.mouse.set_cursor(*
pygame.cursors.broken_x)

pygame.display.flip()
window=gui()
window.start()
def fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    pygame.display.quit()
    pygame.display.init()
    
    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??

    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007
    
    return screen
#fullscreen()
while True:
    
    if not pygame.mixer.music.get_busy():
        mp3=glob.glob("*.mp3")
        try:
            start=start+1
            pygame.display.set_caption(mp3[start])

            if start==-1:
                start=len(mp3)-1
            if start==len(mp3):
                start=0
            pygame.mixer.music.fadeout(fadesecs)
            pygame.mixer.music.load(mp3[start])
            pygame.mixer.music.play(1)
        except:
            print("error:auto")
    for event in pygame.event.get():
        l=pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            print('Forward')
            mp3=glob.glob("*.mp3")
        elif event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            mp3=glob.glob("*.mp3")
            print("exit")
            pygame.display.quit()
            pygame.quit()  
            sys.exit(1)
        
            
        if event.type==pygame.KEYDOWN:
            print("\ndouble")
            if event.key==pygame.K_RIGHT:
                try:
                    mp3=glob.glob("*.mp3")
                    start=start+1
                    pygame.display.set_caption(mp3[start])
                
                    if start==-1:
                        start=len(mp3)-1
                    if start==len(mp3):
                        start=0
                    pygame.mixer.music.fadeout(fadesecs)
                    pygame.mixer.music.load(mp3[start])
                    pygame.mixer.music.play(1)
                except:
                    print("error:right")
                
            if event.key==pygame.K_LEFT:
                
              
                try:
                    mp3=glob.glob("*.mp3")
                    start=start-1
                    pygame.display.set_caption(mp3[start])

                    if start==-1:
                        start=len(mp3)-1
                    if start==len(mp3):
                        start=0
                    pygame.mixer.music.fadeout(fadesecs)
                    pygame.mixer.music.load(mp3[start])
                    pygame.mixer.music.play(1)
                except:
                    print("error:left")
                
            if event.key==K_UP:
                try:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.1)
                except:
                    print("up error")
                    
            if event.key==K_DOWN:
                try:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.1)
                except:
                    print("down error")
                
            if event.key==K_SPACE:
                mp3=glob.glob("*.mp3")
                if paused:
                    pygame.mixer.music.unpause()
                    paused=False
                else:
                    pygame.mixer.music.pause()
                    paused=True
            if event.type == VIDEORESIZE:
                # The main code that resizes the window:
                # (recreate the window with the new size)
                surface = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                
        if event.type==pygame.QUIT:
            pygame.quit()
            break
        
        if event.type==pygame.QUIT:
            pygame.display.quit()
            pygame.quit()      
                
                    
                
            
