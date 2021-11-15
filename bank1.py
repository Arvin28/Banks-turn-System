########Window1######
from datetime import *
from tkinter import *
import tkinter
counter=0


win=Tk()
win.title ("Bank services")
win.geometry("600x400")
win.configure (bg =("#5e34eb"))
#########Operators########

def press(label_name):
    global counter_list
    if counter_list:
        con[label_name]["textvariable"].set(counter_list.pop(0))


def get_time():
    dt = datetime.now()
    return dt.strftime("%H:%M:%S")


def get_date():
    dt = datetime.now()
    return dt.strftime("%d %b %Y")


def get_number():
    global counter, counter_list
    counter +=1
    counter_list.append(counter)
    con["turning"]["textvariable"].set(f"Your turn: {counter}")
    con["waiting"]["textvariable"].set(f"Waiting: {len(counter_list)}")
    con["time"]["textvariable"].set(f"time: {get_time()}")
    con["date"]["textvariable"].set(f"date: {get_date()}")
    
    


#########DEFS################
button1 = Button (text="operator1",height=5,width=15,bd=5,bg=("#bc05ff"))
button1.place (x=70,y=120)

Entery1= Entry (text="operator1",width=10,bd=("3"))
Entery1.place (x=90,y=230)

button2 = Button (text="operator2",height=5,width=15,bd=5,bg=("#8c03ab"))
button2.place (x=250,y=120)

Entery2= Label(wi) 
Entery2.place (x=270,y=230)

button3 = Button (text="operator3",height=5,width=15,bd=5,bg=("#600175"))
button3.place (x=420,y=120)

Entery3= Entry (text="operator3",width=10,bd=("3"))
Entery3.place (x=440,y=230)
##########Ticket########

win2=Tk()
win2.title("Ticket")
win2.configure(bg=("#ffc800"))
win2.geometry("300x400")
Button4= Button  (win2,text="Get a number",width=20,height=6,bd=5,bg="#00ff1a")
Button4.place(x=75,y=60)
Button5= Button  (win2,text="Cancel",width=20,height=6,bd=5,bg="red",command=quit)
Button5.place(x=75,y=200)

#########Information window#######

win3=Tk()
win3.title("Information")
win3.configure(bg=("#d9d9d9"))
win3.geometry("300x300")










mainloop()