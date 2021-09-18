# importing libraries
import os
import re
import time
import smtplib
import imghdr
from email.message import EmailMessage
from email.utils import formataddr
import pandas as pd

EMAIL_ADDRESS = 'bhoranuj3@gmail.com'
EMAIL_PASSWORD = 'anujb109$'

i = 1
with open("emaillogs.txt", 'a') as f:
    for filename in os.listdir('certificates'):
        try:
            with open(os.path.join('certificates', filename), 'rb') as fp:
                file_data = fp.read()
                msg = EmailMessage()
                msg['Subject'] = 'Email Ka Subject Here'
                msg['From'] = formataddr(
                    ('Sender Name', 'sender email'))
                mail_to = filename.rsplit(".", 1)[0]
                msg['To'] = mail_to
                msg.set_content('''Email ka Content Goes Here''')
                msg.add_attachment(file_data, maintype='application',
                                   subtype='pdf', filename='event.pdf')
                print('read file '+str(i)+" "+str(filename))
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)
                print(str(mail_to) + " Sending Success")
                f.write(str(mail_to) + " Sending Success")
                f.write("\n")
                i += 1
        except:
            print(str(mail_to) + " Sending Failed")
            f.write("\n")
            f.write(str(mail_to)+" Sending Failed")
    f.close()
