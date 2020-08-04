import os
import smtplib
from email.message import EmailMessage
import base64


# to check out environment variable goto .bash_profile if using mac
# if you haven't set up environment variable just wirte your ...
usermail = os.environ.get("usermail")    #GmailID here
password = os.environ.get("password")    #and here enter your password

msg=EmailMessage()
msg["Subject"]= "Hey There"
msg["From"]= usermail
msg["To"]= "write_receiptent_mail_id"
msg=msg.set_content("How are you buddy. This is just for testing my mail sender code...")


with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:    # port = 587 when not using ssl


#with smtplib.SMTP("localhost", 1025) as smtp:          # To check in ur local host uncomment it

# Comment this if u r using SMTP_SSL
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()

    smtp.login(usermail,password)

# Comment these when u r using EmailMessage() which is a convinient way to use message details
    # subject="Testing"
    # body="So this is an mail for testing"
    # msg= f'Subject: {subject}\n\n{body}'

# No need of giving all details here as we have already given in EmailMessage
    # smtp.sendmail(usermail,"abhinav.11803384@lpu.in",msg)

    smtp.send_message(msg)
