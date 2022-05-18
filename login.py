import os
import smtplib

def accLogin():
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
        print('Email credentials are wrong or we are not allowed to login on it')