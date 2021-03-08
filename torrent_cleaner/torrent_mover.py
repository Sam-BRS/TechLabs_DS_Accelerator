#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' A small script that I wrote months ago when I learned Python. It is a 'torrent cleaner'.
The script aims to detects all torrent files in a directory
(by default 'My downloads' dir) and move them to a folder (by default a dir called 'TBDestroyed' on the Desktop) '''

import os
from pathlib import Path

# select the source and target folders
def get_user_directory():
    global file_source
    global file_destination
    default_source = r"C:\Users\yams\Downloads"
    default_destination = r"C:\Users\yams\OneDrive\Desktop\TBDestroyed"
    input_source = input(r"Enter the directory of the folder to clean or leave as blank and press enter to leave as default")
    input_destination = input(r"Enter the directory of the destination folder or leave as blank and press enter to leave as default")
    if input_source == '':
        file_source = default_source
    else:
        file_source = input_source
    if input_destination =='':
        file_destination = default_destination
    else:
        file_destination = input_destination

# modification of the path
def move(x, y):
    Path(x).rename(y)

# execution
get_user_directory()
list_files = os.listdir(file_source)

print("===== STARTING CLEANING ======")

i = 0
for f in list_files:
    if "torrent" in f:
        i = i + 1
        cheminsrc = file_source + '\\' + f
        chemind = file_destination + '\\' + f
        if not os.path.exists(file_destination):
            os.makedirs(file_destination)
        move(cheminsrc, chemind)
        print(f + " MOVED")

print(" ===== CLEANING COMPLETED ======")
print(str(i) + " ELEMENTS MOVED")
os.system("pause")
