import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import datetime as dt
import converthtml
import os

RES_PATH = os.path.normpath('../resources/{date}'.format(date=dt.datetime.now().date()))

port = 465
sender_email = ''
receiver_email = ''

message = MIMEMultipart('related')
message['Subject'] = 'Stock Report - {date}'.format(date=dt.datetime.today().date())
message['From'] = sender_email
message['To'] = receiver_email

with open(converthtml.HTML_PATH, 'r') as f:
        mail_html = MIMEText(f.read(), 'html')
        print(mail_html)
        message.attach(mail_html)

def attach_images():
    count = 1
    for file in os.listdir(RES_PATH):
        with open(os.path.normpath('{RES_PATH}/{file}'.format(RES_PATH=RES_PATH,file=file)), 'rb') as f:
            msgImage = MIMEImage(f.read())
            msgImage.add_header('Content-Disposition', 'msgImage', filename=file)
            msgImage.add_header('Content-ID', '<image{count}>'.format(count=count))
            message.attach(msgImage)
        count += 1


def send_report():
    attach_images()
    context = ssl.create_default_context()
    password = getpass.getpass()
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        print('Success!')