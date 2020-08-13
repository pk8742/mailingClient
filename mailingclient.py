import smtplib
# importing message library
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# connecting to mail server
server = smtplib.SMTP('smtp.gmail.com', 25)  # mail server address and port

server.ehlo()  # starting the server

with open('mailclient_password.txt', 'r') as f:
    password = f.read()

# login to mail account using mail_id and password
server.login('sharmapk8742@gmail.com', password)

msg = MIMEMultipart()  # creating email header
msg['From'] = 'sharmapk8742@gmail.com'
msg['To'] = 'sharmapravesh655@gmail.com'
msg['Subject'] = 'mail of my PyBot'

# message
with open('message.txt', 'r') as f:
    message = f.read()

# attaching plain text message
msg.attach(MIMEText(message, 'plain'))

# attaching an image
filename = 'coding.jpg'
attachment = open(filename, 'rb')  # open image in read binary mode

# processing the message
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)  # encoding the image data in base64

# adding headers
p.add_header('Content-Disposition', f'attachment; filename={filename}')

msg.attach(p)  # attaching the actual payload

text = msg.as_string()  # converting as text

server.sendmail('sharmapk8742@gmail.com', 'sharmapravesh655@gmail.com', text)
