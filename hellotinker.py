from tkinter import*

root = Tk()

label = Label()
label.pack()

def write():
    file=open("file1.txt","r")
    label.config(textvariable=file, text=file.read())
    file.close()

def clear():
    label.config(text="")

Button(text="write", command=write).pack()
Button(text="clear", command=clear).pack()

root.mainloop()