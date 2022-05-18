import tkinter as tk
from tkinter import filedialog, Canvas
import os
from sendMail import sendEmails
import pandas as pd
import datetime

root = tk.Tk()

#Defines a function to read a file
def readFile():

    #Clears the currently file being shown
    for widget in openFileBar.winfo_children():
        widget.destroy()

    #Opens the actual file
    fileName= filedialog.askopenfilename(initialdir="/", title="Choose the file", filetypes=(("Excel File", "*.xlsx"), ("all files", "*.*")))

    #Shows the name of the file
    showOpenFile = tk.Label(openFileBar, bg="#BFBFBF", text=fileName)
    showOpenFile.pack()

    #Saves the loaded file into save.txt
    with open('save.txt', 'w') as f:
        f.write(fileName)

#Defines a function to read mail and password entrys
def login():
    userMail = mailEntry.get()
    userPass = passEntry.get()
    
    #Stores the data in login.txt
    with open('login.txt', 'w') as f:
        f.write(userMail + ',')
        f.write(userPass)
    
    #Reads the date
    date = datetime.date.today()
    
    xl= pd.ExcelFile(fileName)
    
    mail_list = []

    #Sends happy birthday mails
    for e in xl.sheet_names:
        if int(e) == date.month:
            excel_file = fileName
            df = pd.read_excel(excel_file, sheet_name=e)
            for i, row in df.iterrows():
                dia = df.at[i, 'Dia']
                if int(dia) == date.day:
                    nome = df.at[i, 'Nome']
                    dia = df.at[i, 'Dia']
                    mes = df.at[i, 'Mes']
                    cmail = df.at[i, 'Email']
                    folio = df.at[i, 'Fólio']
                    if cmail not in mail_list:
                        msg = "<b>A Coutada</b></br>Desde já lhe endereçamos os nossos mais sinceros parabéns e por esse facto o <b>Hotel Rural - A Coutada</b>, tem todo o gosto em lhe oferecer um desconto de 10% na sua próxima reserva. </br>Ao efectuar a mesma, agradecemos que mencione o código que lhe foi atribuido abaixo.</br><b>Código:</b> {0} </br></br><b>Contactos:</b></br>Telefone: +351262757050</br>Email: info@coutada-turismo.com</br></br>Com os votos de um feliz aniversário, </br><b>A Coutada</b>".format(
                            str(folio))

                        sendEmails(cmail, msg)
                        mail_list.append(cmail)
                    else:
                        print("Email não enviado para:", nome)
                        print("Email repetido.")
    

#Loads save.txt
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        fileName = f.read()

#Creates App Canvas (background)
root.geometry('600x800')
root.config(bg="#4C4C4C")
root.resizable(width=0, height=0)

#Creates the Bar at the Top
topBar = tk.Frame(root, bg="#171717")
topBar.place(relheight=0.1, relwidth=1)

#Creates a Button to Open Files
openFileButton = tk.Button(root, bg="#BFBFBF", text="Open File", padx=20, pady=5, command=readFile)
openFileButton.place(relx=0.1, rely=0.2, relwidth=0.2)

#Creates the bar to show the Open File
openFileLabel = tk.Label(root, bg="#4C4C4C", fg="white", text="Open File:")
openFileLabel.place(relx=0.32, rely=0.21)

openFileBar = tk.Frame(root, bg="#BFBFBF")
openFileBar.place(relwidth=0.5, relheight=0.03, relx=0.43, rely=0.21)

#If there was a file open last session it writes it on the screen
try:
    #Shows the name of the file
    showOpenFile = tk.Label(openFileBar, bg="#BFBFBF", text=fileName)
    showOpenFile.pack()
except:
    showOpenFile = tk.Label(openFileBar, bg="#BFBFBF", text="There is no Open File")
    showOpenFile.pack()

#Creates the email and password entrys
mailLabel = tk.Label(root, bg="#4C4C4C", fg="white", text="Email:")
mailLabel.place(relx=0.32, rely=0.31)
mailEntry = tk.Entry(width=50, bg="#BFBFBF")
mailEntry.place(relx=0.43, rely=0.31, relwidth=0.5, relheight=0.03)
passLabel = tk.Label(root, bg="#4C4C4C", fg="white", text="Pass:")
passLabel.place(relx=0.32, rely=0.41)
passEntry = tk.Entry(width=50, bg="#BFBFBF")
passEntry.place(relx=0.43, rely=0.41, relwidth=0.5, relheight=0.03)

#Creates the send email button
sendMailBut = tk.Button(root, text="Send Emails", bg="#BFBFBF", padx=20, pady=5, command=login)
sendMailBut.place(rely=0.8, relx=0.375, relwidth=0.25)

#Runs the app
root.mainloop()