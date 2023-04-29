from tkinter import *
from tkinter import ttk
from main import call
win= Tk()
win.geometry("750x250")
def get_value():
   e_text=entry.get()
   Label(win, text="Loading....", font= ('Century 15 bold')).pack(pady=20)
   call(e_text)
   return

entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)

button= ttk.Button(win, text="Enter", command= get_value)
button.pack()
win.mainloop()