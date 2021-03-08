#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#import external modules
from pathlib import Path

#select the source and target folders
def getuserinfo():
    global fsource
    global fdest
    fsource = r"C:\Users\yams\Downloads"
    fdest = r"C:\Users\yams\OneDrive\Desktop\TBDestroyed"

#modification of the path
def move(x, y):
    Path(x).rename(y)

#useless??
def restart():
    press = input('restart ? press Y for yes')
    if press == "y" or press == "Y":
        move()


#execution

getuserinfo()  
listfichier = os.listdir(fsource)

print("===== EXECUTION DU TRI ======")

i = 0
for f in listfichier:
    if "torrent" in f:
        i = i + 1
        cheminsrc = fsource + '\\' + f
        chemind = fdest + '\\' + f
        if not os.path.exists(fdest):
            os.makedirs(fdest)
        move(cheminsrc, chemind)
        print(f + " MOVED")
        
print(" ===== OPERATION TERMINEE ======")
print(str(i) + " ELEMENTS DEPLACES")
os.system("pause")
