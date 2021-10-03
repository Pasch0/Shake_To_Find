# Import PyAutoGUI library
import pyautogui as p
# Import sleep function
from time import sleep
# Import OS to execute system commands
import os

# Define variables to insert actual X and Y positions
posx = 0
posy = 0

# Difine variables to insert before X and Y positions
b4_posx = 0
b4_posy = 0

# Define cursor size
size = ['normal']
# You can change this sizes
normal_size = 24
bigger = 72

def increase():
    os.system(f"xfconf-query --channel xsettings --property /Gtk/CursorThemeSize --set {bigger}")

def decrease():
    os.system(f"xfconf-query --channel xsettings --property /Gtk/CursorThemeSize --set {normal_size}")

while True:
    # Get cursor position
    position = p.position()
    x, y = position
    # Save last positions before save actual positions
    b4_posx = posx
    b4_posy = posy
    # Save actual positions
    posx = x
    posy = y
    # Calculate displacement average
    x_avg = posx - b4_posx
    y_avg = posy - b4_posy
    if x_avg > 130:
        if size[0] == 'normal':
            increase()
            size[0] = 'big'
    else:
        if x_avg < 130:
            if size[0] == 'big':
                sleep(0.5)
                decrease()
                size[0] = 'normal'
                sleep(0.5)
    sleep(0.03)