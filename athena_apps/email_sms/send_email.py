# https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151
import os
from email.message import EmailMessage
import ssl
import smtplib


email_sender = "crazymartell@gmail.com" # has to the email that you se made with the two-factor 
email_password = "woloibeitqzyabfm" #two-factor pass code
# email_password = os.environ.get("email_passsword: ")
email_receiver = "Tinybob00@gmail.com "


subject = "i love you baby"
body = """
nothing


"""

em = EmailMessage()

em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject

em.set_content(body)

context =  ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())

