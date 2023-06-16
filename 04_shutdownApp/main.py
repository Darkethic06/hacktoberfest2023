from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')

def shutdown():
    os.system('shutdown /s /t 1')
def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


st = Tk()

st.title("Shutdown App")

st.geometry("550x200")

r_button = Button(st, text="Restart",font=("Times New Roman",16),relief=RAISED, command=restart)
r_button.place(x=30,y=85,height=30,width=150)

s_button = Button(st, text="Shutdown",font=("Times New Roman",16),relief=RAISED, command=shutdown)
s_button.place(x=200,y=85,height=30,width=150)

sl_button = Button(st, text="Sleep",font=("Times New Roman",16),relief=RAISED,command=sleep)
sl_button.place(x=370,y=85,height=30,width=150)


st.mainloop()
