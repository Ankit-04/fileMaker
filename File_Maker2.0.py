from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import os
from random import randint
import datetime
import shutil

Title = "Helvetica 24"

users = {

    #enter user permissions here
}


def starterWin():
    starter= Tk()
    starter.resizable(False , False)
    starter.geometry("405x170+500+150")
    starter.title("File Maker")

    Label(starter, text  = "Log In :P", font = Title).place(x = 130, y =0)
    Label(starter, text = "Username:").place(x = 0, y = 50, height = 23)
    Label(starter, text = "Password:").place(x = 0, y = 80, height = 23)

    userPin = Entry(starter, justify = CENTER, width = 30)
    userPin.place(x = 130, y = 55)
    Pass = Entry(starter, justify = CENTER, width = 30)
    Pass.place(x = 130, y = 83)

    def check():
        username = userPin.get()
        password = Pass.get()
        correctpass = users.get(username)

        if (username in users and password == correctpass):
            filemarkerWin(username)
        elif(username in users and password != correctpass):
            messagebox.showinfo("whoops!","looks like you have an account but your password is wrong" )
        else:
            messagebox.showinfo("Error", "Sorry you don't have permission, Ask ankit to make you an account! ")

    User = Button(starter, text = "Login", command = check)
    User.place(x = 45, y = 115, width = 300)    

    starter.mainloop()

def filemarkerWin(username):
    maker= Tk()
    maker.resizable(False , False)
    maker.geometry("450x250+500+150")
    maker.title("File Maker")

    Label(maker, text= "Welcome to File Maker", font = Title).place(x = 50, y = 0)
    Label(maker, text="File name").place(x = 0, y = 44)
    Label(maker, text="Name").place(x = 0, y = 74)
    Label(maker, text="Date").place(x = 0, y = 104)
    Label(maker, text="Description").place(x = 0, y = 135)

    fileName = Entry(maker, justify = CENTER, width = 30)
    Author = Entry(maker, justify = CENTER, width = 30)
    Date = Entry(maker, justify = CENTER, width = 30)
    Description = ScrolledText(maker, width=30, height=5,font = "Helvetica 8")

    fileName.place(x = 87, y = 46, height = 23)
    Author.place(x = 87, y = 75, height = 23)
    Date.place(x = 87, y = 104, height = 23)
    Description.place(x = 86, y = 135)

    def file_call():
        fileName.delete(0, END)
        fileName.insert(0,"file"+str(randint(0,999))+".py")

    def Name_call(username):
        Author.delete(0, END)
        Author.insert(0,username)

    def Date_call():
        Date.delete(0, END)
        today = datetime.date.today()
        Date.insert(0, today.strftime("%A,%B %d, %Y"))

    def Create():

        def error():
            messagebox.showinfo("Error","You are missing crucial information")

        AuthorFeild = Author.get()
        DateFeild = Author.get()
        FileNamefeild = fileName.get()
        desciptionFeild = Description.get(1.0, END)

        if(AuthorFeild == "" or DateFeild == "" or FileNamefeild == ""):
            error()

        fileAuthor = "# Author:      "+ Author.get()
        fileDate = "# Date:        " + Date.get()
        if(desciptionFeild == ""):
            fileDescription = ""
        else:
            fileDescription = "# Description: " + Description.get(1.0,END)

        f = open( "C:/Users/ganki/Desktop/python/personal_projects/" + fileName.get() + ".py", "w+")
        f.write(fileAuthor + "\n")
        f.write(fileDate + "\n")
        f.write(fileDescription + "\n\n\n\n")
        f.close()
        maker.destroy()

    randomFile = Button(maker, text="Make a random name", command = file_call)
    defualtAuthor = Button(maker, text ="Use the default name", command = lambda : Name_call(username))
    defualtDate = Button(maker, text ="Use today's date", command = Date_call)
    create = Button(maker, text = "create file", command = Create)

    randomFile.place(x = 278, y = 44, width = 130)
    defualtAuthor.place(x = 278, y = 73, width = 130)
    defualtDate.place(x = 278, y = 102, width = 130)
    create.place(x = 120, y = 215, width = 200)

    maker.mainloop()

starterWin()