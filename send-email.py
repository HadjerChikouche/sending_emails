import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

imgFileName = 'image.png'
server = 'smtp.gmail.com'
port = 587
img_data = open(imgFileName, 'rb').read()
msg = MIMEMultipart()
msg['Subject'] = 'Image'
msg['From'] = 'piege.photographique1@gmail.com'
msg['To'] = 'chikouche.hadjer@gmail.com'

text = MIMEText("This is My Image ... :) ")
msg.attach(text)
image = MIMEImage(img_data, name=os.path.basename(imgFileName))
msg.attach(image)


s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()

s.login('piege.photographique1@gmail.com', 'azertyuiop1')
s.sendmail('piege.photographique1@gmail.com', 'chikouche.hadjer@gmail.com', msg.as_string())
s.quit()
