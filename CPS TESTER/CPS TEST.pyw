#im genuinely sorry for this code, i just wanted to make a simple cps test but it turned into this monstrosity. I know how to optimize it but im too lazy.
#PLS download this, it took me 2 days (because im not a robot and kinda a noob) but in reality it took 1 day.
#and i just noticed i could made the possible paths into a single list after i did all this, but again im too lazy to change it, sorry.
#but if you want to optimize it be my guest:-)
import tkinter as t
import os
home=os.path.expanduser("~")         
username=os.getlogin()
possible_icon_paths=[
    os.path.join(home,"Documents","CPS TEST","mouse.png"),
    os.path.join(home,"OneDrive","Documents","CPS TEST", "mouse.png"),
    os.path.join(home,"Desktop","CPS TEST","mouse.png"),
    os.path.join(home,"Downloads","CPS TEST","mouse.png"),
    os.path.join(os.path.dirname(os.path.abspath(__file__)),"mouse.png")
]
root=t.Tk()
root.geometry("400x400")
root.title("CPS Test")
root.configure(bg="#1A1818")
root.resizable(False, False)
for p in possible_icon_paths:
    if os.path.exists(p):
        root.wm_iconphoto(True, t.PhotoImage(file=p))
        break

clicks=0
is_running=False
possible_paths=[
    os.path.join(home,"Documents","CPS TEST","buttonimagecps.png"),
    os.path.join(home,"OneDrive","Documents","CPS TEST", "buttonimagecps.png"),
    os.path.join(home,"Desktop","CPS TEST","buttonimagecps.png"),
    os.path.join(home,"Downloads","CPS TEST","buttonimagecps.png"),
    os.path.join(os.path.dirname(os.path.abspath(__file__)),"buttonimagecps.png")
]
possible_paths2=[
    os.path.join(home,"Documents","CPS TEST","redbuttoncps.png"),
    os.path.join(home,"OneDrive","Documents","CPS TEST", "redbuttoncps.png"),
    os.path.join(home,"Desktop","CPS TEST","redbuttoncps.png"),
    os.path.join(home,"Downloads","CPS TEST","redbuttoncps.png"),
    os.path.join(os.path.dirname(os.path.abspath(__file__)),"redbuttoncps.png")
]
for p in possible_paths:
    if os.path.exists(p):
        img=t.PhotoImage(file=p)
        break
for p in possible_paths2:
    if os.path.exists(p):
        img2=t.PhotoImage(file=p)
        break
greyblock=t.Label(root,bg="#242424",width=50,height=25)
greyblock.place(relx=0.5,rely=0.5,anchor="center")

test_duration=5

def add_click():
    global clicks, is_running
    if is_running:
        clicks+=1


def reset_test():
    global clicks, is_running
    final_cps=clicks/test_duration
    text.config(text=f"Clicks per second: {final_cps:.2f}")
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
    global clicks, is_running
    if not is_running:
        clicks+=1
        is_running=True
        cps=clicks/test_duration        
        global img2
        button.config(image=img2,command=add_click)
        button.image=img2
        root.after(test_duration * 1000, reset_test)

button=t.Button(root,image=img,bg="#242424",bd=0,command=start_test,highlightthickness=0,highlightbackground="#242424",padx=0, pady=0,relief="flat",activebackground="#242424")
button.place(anchor="center", relx=0.5,rely=0.4)

text=t.Label(root,text="Clicks per second: ",font=("Segoe UI", 16, "bold"),bg="#242424",fg="white",relief="flat")
text.place(relx=0.5, rely=0.7, anchor="center")

yourrole=t.Label(root,text="Your CPS Level: " ,font=("Segoe UI", 16, "bold"),bg="#242424",fg="#FFFFFF",width=25,height=1)
yourrole.place(relx=0.5,rely=0.1,anchor="center")
root.mainloop()