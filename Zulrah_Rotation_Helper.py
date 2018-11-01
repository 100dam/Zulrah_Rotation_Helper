#Zulrah Rotation Buddy
#100dam
#This program uses Tkinter in python to create a GUI
#This program is meant to be opened alongside an OSRS client
#To aid in killing the Zulrah Boss

import sys
import os
import tkinter as tk
from PIL import Image, ImageTk

# --- functions ---
def clearScreen(event=None):
    widget_list = all_children(root)
    for item in widget_list:
        item.grid_forget()

def Rotation(imagename, bind, gridnum, commandval):
    image = Image.open(imagename)
    photo = ImageTk.PhotoImage(image)

    # label with image
    l = tk.Label(root, image=photo)
    l.image = photo

    if 0 <= gridnum <= 3:
        l.grid(row=1, column=gridnum)
    else:
        l.pack()

    if bind == 1:
        l.bind('<Button-1>', commandval)
        
        b = tk.Button(root, image=photo, command= lambda: RotationBtn(commandval))
        b.grid(row=1, column=gridnum)

def RotationBtn(imagename):
    clearScreen()

    image = Image.open(imagename)
    photo = ImageTk.PhotoImage(image)

    # label with image
    l = tk.Label(root, image=photo)
    l.image = photo

    l.grid(row=1, column=0)

    #if bind == 1:
    l.bind('<Button-1>', homeMenu)

    b = tk.Button(root, image=photo, command=homeMenu)
    b.grid(row=1, column=0)
  
    
def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

   

def homeMenu():
    clearScreen()
    PossibleRoatation=["ChooseAlpha.PNG","ChooseBravo.PNG","ChooseCharlie.PNG","ChooseDelta.PNG"]
    CurrentRotation = ["Alpha.PNG","Bravo.PNG","Charlie.PNG","Delta.PNG"]

    for index, commandval in enumerate(zip(PossibleRoatation,CurrentRotation)):
        Rotation(commandval[0],1,index,commandval[1])

    # button with text closing window
    b = tk.Button(root, text="Close", command=root.destroy)
    b.grid(row=2, column=1)

   
# --- main ---

# init    
root = tk.Tk()

homeMenu()

# "start the engine"
root.mainloop()
