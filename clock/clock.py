from tkinter import *
import pygame  #for tick tick sound in clock
from time import strftime,sleep
root=Tk()
root.title('Digital Clock')
root.geometry("300x120")

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.mixer.init()

def time(): 
    string = strftime(' %I:%M:%S %p ') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

def clocktick():  #playing Ticking Sound
    pygame.mixer.music.load("ClockTick.mp3")
    pygame.mixer.music.set_volume(0.5) #range b/w 0 to 1
    pygame.mixer.music.play(-1)

def clocktickPause():  #Pausing Ticking Sound
    pygame.mixer.music.pause()

lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'grey', 
            foreground = 'white')
lbl.grid(row=1,column=0,columnspan=2)

b2=Button(root,text='Play',width=43,command=clocktick,background='green')
b2.grid(row=4,column=0)

b3=Button(root,text='Pause',width=43,command=clocktickPause,background='red') 
b3.grid(row=5,column=0)

time()
root.after_idle(clocktick)
root.mainloop()