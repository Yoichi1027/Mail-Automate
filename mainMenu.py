from genericpath import exists
import tkinter as tk
from tkinter import filedialog, Canvas, Text
from turtle import width
import os

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
        f.write(fileName + ',')

#Loads save.txt
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        fileName = f.read()

#Creates App Canvas (background)
canvas = tk.Canvas(root, height=800, width=600, bg ="#4C4C4C")
canvas.pack()

#Creates the Bar at the Top
topBar = tk.Frame(root, bg="#171717")
topBar.place(relheight=0.1, relwidth=1)

#Creates a Button to Open Files
openFileButton = tk.Button(root, bg="#BFBFBF", text="Open File", padx=20, pady=5, command=readFile)
openFileButton.place(relx=0.1, rely=0.2)

#Creates the bar to show the Open File
openFileLabel = tk.Label(root, bg="#4C4C4C", fg="white", text="Open File:")
openFileLabel.place(relx=0.32, rely=0.21)

openFileBar = tk.Frame(root, bg="#BFBFBF")
openFileBar.place(relwidth=0.5, relheight=0.03, relx=0.43, rely=0.21)

#Shows the name of the file
showOpenFile = tk.Label(openFileBar, bg="#BFBFBF", text=fileName)
showOpenFile.pack()

#Runs the app
root.mainloop()