#V0.4 Big optimization to some parts of code.
import tkinter as t
from tkinter import ttk as tt
from pathlib import Path as c

root=t.Tk()
root.geometry("400x400")
root.title("CPS Test")
root.configure(bg="#1A1818")
root.resizable(False, False)

path=c(__file__).parent
img=t.PhotoImage(file=path/"buttonimagecps.png")
img2=t.PhotoImage(file=path/"redbuttoncps.png")
img3=t.PhotoImage(file=path/"GearCPS.png").subsample(2,2)
icon=root.wm_iconphoto(False, t.PhotoImage(file=str(path/"mouse.png")))

clicks=0
is_running=False

greyblock=t.Label(root,bg="#242424",width=50,height=25)
greyblock.place(relx=0.5,rely=0.5,anchor="center")

test_duration=5

def add_click():
    global clicks, is_running
    if is_running:
        clicks+=1

def reset_test():
    global clicks, is_running, test_duration
    final_cps=clicks/test_duration
    if test_duration<1:
        text.configure(text=f"Clicks in under a second: {final_cps:.2f}")
    elif test_duration==1:
        text.configure(text=f"Clicks in a second: {final_cps:.2f}")
    elif test_duration>1:
        text.configure(text=f"Clicks per second: {final_cps:.2f}")
    clicks=0
    is_running=False
    global img
    button.image=img
    button.config(image=img,command=start_test)
    if final_cps>=15:
        yourrole.config(text="Your CPS Level: Master Clicker")
    elif final_cps>=10:
        yourrole.config(text="Your CPS Level: Expert")    
    elif final_cps>=7:
        yourrole.config(text="Your CPS Level: Average Joe")    
    elif final_cps<=7:
        yourrole.config(text="Your CPS Level: Beginner")

def start_test():
    try:
        global clicks, is_running
        if not is_running:
            clicks+=1
            is_running=True
            cps=clicks/test_duration        
            global img2
            button.config(image=img2,command=add_click)
            button.image=img2
            root.after(test_duration * 1000, reset_test)
    except Exception as e:
        print("ERROR: ",e)

frameset=None
timechangerset=None
texttimeset=None
bool2=False
def timechanger():
    global bool2,test_duration
    test_duration=int(float(timechangerset.get()))
    if test_duration<1:
        text.configure(text="Clicks in under a second")
    elif test_duration==1:
        text.configure(text="Clicks in a second")
    elif test_duration>1:
        text.configure(text="Clicks per second")

def opensettings():
    try:
        global bool2
        if bool2==False:
            global frameset,timechangerset,texttimeset
            frameset=t.Frame(root,bg="#242424",bd=0,highlightthickness=0,highlightbackground="#242424",relief="flat",width=260,height=350)
            frameset.place(relx=0.5,rely=0.5,anchor="center")
            timechangerset=tt.Entry(root,background="#242424",font=("Segoe UI", 16, "bold"), width=12, justify="center")
            settingsbutton.bind("<Button-1>", lambda e:timechanger())
            timechangerset.place(relx=0.09, rely=0.15, anchor="sw")
            texttimeset=t.Label(root,text=r"              Time Changer(secs)           \
click to continue",background="#FFFFFF",fg="#242424",justify="center",width=21,height=2)
            texttimeset.bind("<Button-1>", lambda e:texttimeset.destroy())
            texttimeset.place(relx=0.09, rely=0.15, anchor="sw")
            bool2=True
        else:
            frameset.destroy()
            timechangerset.destroy()
            texttimeset.destroy()
            bool2=False
    except Exception as e:
        print("ERROR:",e)

button=t.Button(root,image=img,bg="#242424",bd=0,command=start_test,highlightthickness=0,highlightbackground="#242424",padx=0, pady=0,relief="flat",activebackground="#242424")
button.place(anchor="center", relx=0.5,rely=0.4)

text=t.Label(root,text="Clicks per second: ",font=("Segoe UI", 16, "bold"),bg="#242424",fg="white",relief="flat")
text.place(relx=0.5, rely=0.7, anchor="center")

yourrole=t.Label(root,text="Your CPS Level: " ,font=("Segoe UI", 16, "bold"),bg="#242424",fg="#FFFFFF",width=23,height=1)
yourrole.place(relx=0.5,rely=0.1,anchor="center")
settingsbutton=t.Button(root,image=img3,bg="#242424",bd=0,command=opensettings,highlightthickness=0,highlightbackground="#242424",padx=0,pady=0,relief="flat",activebackground="#242424")
settingsbutton.place(anchor="center",relx=0.88,rely=0.09)
root.mainloop()
