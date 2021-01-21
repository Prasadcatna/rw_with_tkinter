from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("250x250")

T=Text(root,height=5 , width=52)

def write():
  file=open("File1.txt","a")
  file.write(T.get("1.0",'end-1c'))
  file.close()
  print("Data is written")

def exit():
  title='Save'
  text='Are you sure not to save it?'
  reply= messagebox.askquestion(title,text)
  if reply=='yes':
    write()
    root.destroy()
  else:
    root.destroy()


def read():
  global file
  root.geometry("400x400")
  file=open("file1.txt","r")
  msg.config(textvariable=file, text=file.read())

def clean_file():                   # Clean's the file completly
  title='Clean'
  text='Are you sure U want to clean it?'
  reply= messagebox.askquestion(title,text)
  if reply=='yes':
    file=open("file1.txt","r+")
    file.truncate(0)
    file.close()

def clear():
  msg.config(text="")

  


file=StringVar()
file.set('default')
Label(root,textvariable=file).pack()
T.pack()
b=Button(root,text='SUBMIT',command=write).pack()

b1=Button(root, text='EXIT' ,command= exit).pack()

b2=Button(root,text='Read',command=read).pack()

b3=Button(root,text='Clean the file', command=clean_file).pack()

b4=Button(root,text='Clean the O/P space', command=clear).pack()


msg=Label()
msg.pack()
root.mainloop()