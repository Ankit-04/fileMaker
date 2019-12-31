from tkinter import *
from tkinter.scrolledtext import ScrolledText

root= Tk()
root.resizable(False , False)
root.geometry("450x250+500+150")

Label(root, text= "   Welcome to File Maker", font = "Helvetica 24").place(x = 29, y = 0)
Label(root, text="File name").place(x = 0, y = 44)
Label(root, text="Name").place(x = 0, y = 74)
Label(root, text="Date").place(x = 0, y = 104)
Label(root, text="Description").place(x = 0, y = 135)

fileName = Entry(root, justify = CENTER, width = 30)
Author = Entry(root, justify = CENTER, width = 30)
Date = Entry(root, justify = CENTER, width = 30)
Description = ScrolledText(root, width=30, height=5,font = "Helvetica 8")

fileName.place(x = 87, y = 46, height = 23)
Author.place(x = 87, y = 75, height = 23)
Date.place(x = 87, y = 104, height = 23)
Description.place(x = 86, y = 135)

fileName = Button(root, text="Make a random name")
defualtName = Button(root, text ="Use the default name")
defualtDate = Button(root, text ="Use today's date")
create = Button(root, text = "create file")

fileName.place(x = 278, y = 44, width = 130)
defualtName.place(x = 278, y = 73, width = 130)
defualtDate.place(x = 278, y = 102, width = 130)
create.place(x = 120, y = 215, width = 200)

root.mainloop()