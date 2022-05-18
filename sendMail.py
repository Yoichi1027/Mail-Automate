import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def sendEmails(cmail, msg):
    #Loads the login information
    if os.path.isfile('login.txt'):
        with open('login.txt', 'r') as f:
            tempData = f.read()
            tempData = tempData.split(',')
            userMail = tempData[0]
            userPass = tempData [1]

    #Creates the server and trys to login in the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(userMail, userPass)
        print('Logged in sucessfully')
    except:
        print('Email credentials are wrong or we are not allowed to login')

    #Creates the email
    email_msg = MIMEMultipart()
    email_msg['Subject'] = "A Coutada deseja-lhe os mais sinceros parabéns"
    email_msg.attach(MIMEText(msg, 'Html'))
    img = open('imagem.jpg', 'rb').read()
    email_msg.attach(MIMEImage(img, 'jpg'))

    try:
        #Sends the email
        server.sendmail(userMail, cmail, email_msg.as_string())
        server.quit()
        print("Email sent sucessfully to: " + cmail)
    except:
        print("Error while sending the email to: " + cmail)
