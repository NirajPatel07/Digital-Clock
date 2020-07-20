from tkinter import *
import time
from datetime import date

root=Tk()
root.title("Digital Clock")
root.geometry("1920x1080+0+0")
root.config(bg="#0C090A")




def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    
    if int(h)>12 and int(m)>0:
        labelAm.config(text="PM")

    if int(h)>12:
        h=int(h)-12
    
    labelhr.config(text=h)
    labelMin.config(text=m)
    labelSec.config(text=s)

    today = date.today()

    day = today.strftime("%d")
    month = today.strftime("%B")
    year = today.strftime("%Y")

    labeldate.config(text=day)
    labelmonth.config(text=month)
    labelyear.config(text=year)
 
    labelhr.after(200,clock)

    
    
    
labelhr=Label(root,text="12",font=("times new roman",50,"bold"),bg="#2B65EC",fg='white')
labelhr.place(x=450,y=130,width=150,height=150)

labelhr2=Label(root,text="HOUR",font=("times new roman",20,"bold"),bg="#2B65EC",fg='white')
labelhr2.place(x=450,y=290,width=150,height=50)

labelMin=Label(root,text="12",font=("times new roman",50,"bold"),bg="#C47451",fg='white')
labelMin.place(x=620,y=130,width=150,height=150)

labelMin2=Label(root,text="MINUTE",font=("times new roman",20,"bold"),bg="#C47451",fg='white')
labelMin2.place(x=620,y=290,width=150,height=50)

labelSec=Label(root,text="12",font=("times new roman",50,"bold"),bg="#FF0000",fg='white')
labelSec.place(x=790,y=130,width=150,height=150)

labelSec2=Label(root,text="SECOND",font=("times new roman",20,"bold"),bg="#FF0000",fg='white')
labelSec2.place(x=790,y=290,width=150,height=50)

labelAm=Label(root,text="AM",font=("times new roman",50,"bold"),bg="#008080",fg='white')
labelAm.place(x=960,y=130,width=150,height=150)

labelAm2=Label(root,text="NOON",font=("times new roman",18,"bold"),bg="#008080",fg='white')
labelAm2.place(x=960,y=290,width=150,height=50)

##############

labelsep=Label(root,text="Niraj Patel",font=("times new roman",20,"bold"),bg="#808080",fg='white')
labelsep.place(x=260,y=390,width=1050,height=30)

##############

labeldate=Label(root,text="01",font=("times new roman",50,"bold"),bg="#2B65EC",fg='white')
labeldate.place(x=450,y=500,width=150,height=150)

labelmonth=Label(root,text="January",font=("times new roman",50,"bold"),bg="#FF0000",fg='white')
labelmonth.place(x=620,y=500,width=310,height=150)

labelyear=Label(root,text="2019",font=("times new roman",50,"bold"),bg="#008080",fg='white')
labelyear.place(x=960,y=500,width=150,height=150)

clock()
root.mainloop()
