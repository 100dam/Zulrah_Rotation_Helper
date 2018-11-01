# Zulrah_Rotation_Helper
# Python (Python 3.7 for me)
I use windows so yea mac idk, dont use mac? lol jk, but if just use google for some of this stuff
linux should be some minor alterations, basically just different key words 
This should be in just installing the files but I am not a software guru.

# Disclaimer: This program is what I made and I have made it to literally just run through pictures, check the code if you dont believe me. Dont trust the images? than create your own i dont really care. I am listing helpful resources i used to download the necessary libraries I needed to make this program. Use your head, verify the links and download at your own risk.

I used a couple of third party Python libraries: 
Tkinter: Graphical User Interface(GUI)-allows it to run in a window
PIL: Image library for python
Python:I use the newest vesrion 3.7.1 if you need python -> link if you can't be bothered to google it: https://www.python.org/downloads/
# Note
Tkinter should be build in with Python so yeah, incase it isnt and you can't be bother to google "install Tkinter"
if using Python 2 you need to change line 9 to import Tkinter as tk (the first T in Tkinter needs to be capitalized) 
https://tkdocs.com/tutorial/install.html

# Getting PIP
honestly just follow the link below, Idk why i tried to copy paste it in here to be nice but just use the link or just google it.
im just copy-pasting from the link below:
https://dev.to/el_joft/installing-pip-on-windows credit: el-joft
open command line(cmd) and type in:
python- check to have it return its version if not install python
download get-pip.py: https://bootstrap.pypa.io/get-pip.py
navigate to the directory(the file place in windows) where you saved that file:
ie: cd \user\username\Programs\python37-32\lib   
cd is change directory in windows if you messed up cd .. goes back one directory and if you want to see what file are in the current directory you are in type in:
dir and press enter
Once you found the got into the directory where you installed get-pip.py enter in the following command:
python get-pip.py
let it do its thing, than to verify use the following command:
pip --version
you should get back something like:
pip 18.1 from c:\python37-32\lib\site-packages\pip (python 3.7)

# Getting PIL
PIL: This was for using images
Using pip, enter the following line in the command window if you don't have both python 2 and 3 installed:
 pip install Pillow
Or if you have both Python versions installed (2.X and 3.X) credit: Ahmad https://stackoverflow.com/questions/20060096/installing-pil-with-pip
 python3 -m pip install Pillow
https://pypi.org/project/Pillow/2.2.1/




# Creating an executable
Since opening Python IDLE is hard (it makes running this program neater than having the console behind, you can just minimize it which is fine, but I got curious and its quite easy. Before I went through and actually made it a .exe I would simply open Python IDLE and open the zulrah script, then proceed to run it.). I used Pyinstaller (https://pyinstaller.readthedocs.io/en/stable/usage.html) found via this post:
https://bytes.com/topic/python/insights/579554-simple-guide-using-pyinstaller  (subsuquintly found via this post credit: https://stackoverflow.com/questions/2136837/process-to-convert-simple-python-script-into-windows-executable)
bascially, install pyinstaller, i like using pip, once you set it up it makes life a lot easier(imho). pip install pyinstaller , in command windows(cmd) 
Once you have pyinstaller simply enter in the command line:
pyinstaller Zulrah_Rotation_Helper.py
Then proceed to copy the image files into the newly created dist folder and that should be it.

 # Upon actually trying it out it seems to still pop up its own commandline type window, so idk if this is even worth it but now you have insight into making a .py file into a .exe. Your Welcome, lol.

# Actual Program
This is a program that allows you to choose one of the 4 Zulrah rotations in OldSchool Runescape. This makes Killing this boss easier and less mistakes when referring to the rotation map.

The Images used in this program are from the reddit post linked below by the redditor u/acy2fast
https://www.reddit.com/r/2007scape/comments/61qfog/easy_peasy_zulrah_rotation_guide/

This guide/ Helper is meant to help illeviate the confusion of having all 4 rotations up in one image, which I found to be very annoying and led me to many mistakes. I would much rather kill the boss than die a bunch because when I glanced at the map I looked at the wrong rotation.

This application only needs to be opened once and will run until it is closed. There is a close button on the bottom of the main screen, upon clicking this button, the application will close.

# How to use this application
There will be 4 pictures, denoted as Alpha, Bravo, Charlie, and Delta. These are the 4 rotations of Zulrah. These are simply the most amount of rotations before you can decern which rotation it is, with Alpha and Bravo needing 4 steps and Charlie and Delta only needing 2 steps.
When you have figure out which rotation you are currently facing simply click on the image. This will then bring up the rotation that you are on.

After you finish the rotation simply click on the image and it will go back to the home screen/main menu showing all 4 rotations again.

# Note
if you misclick simply click the image and once you have the 4 rotations on the screen again click the right rotation.
