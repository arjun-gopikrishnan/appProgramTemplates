
from tkinter import *
import sqlite3
import tkinter  as tk
from tkinter import messagebox

rk_652 = Tk()
rk_652.geometry("1100x900")
rk_652.title("SET 5 - ARJUN" )


date=IntVar()
receipt=IntVar()
company=StringVar()
rep=StringVar()
loc=StringVar()
csz=StringVar()
phone=IntVar()
name=StringVar()
license=StringVar()
address=StringVar()
csz1=StringVar()
phone1=IntVar()
VIN1=StringVar()
make=StringVar()
year=IntVar()
color=StringVar()
reg=StringVar()
model=StringVar()
milg=IntVar()
cash=IntVar()
deb=IntVar()
cred=IntVar()
oth=IntVar()
rp_name=StringVar()
sig=StringVar()



def Database():
    
    dat=date.get()
    recp=receipt.get()
    comp=company.get()
    repnt=rep.get()
    locn=loc.get()
    city=csz.get()
    phn=phone.get()
    nm=name.get()
    lic=license.get()
    adds=address.get()
    sz1=csz1.get()
    phn1=phone1.get()
    vehic=VIN1.get()
    mk=make.get()
    yr=year.get()
    clr=color.get()
    regis=reg.get()
    mdl=model.get()
    mileage=milg.get()
    cs=cash.get()
    tx=deb.get()
    ttl=cred.get()
    amount=oth.get()
    repres=rp_name.get()
    sign=sig.get()
    
    
    db = sqlite3.connect('car1.db')
    cursor=db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS CAR1(date INT,receipt INT,company TEXT,rep TEXT,loc TEXT,csz TEXT,phone INT,name TEXT,license TEXT,address TEXT,csz1 TEXT,phone1 INT,VIN1 TEXT,make TEXT,year INT,color TEXT,reg TEXT,model TEXT,milg INT,cash INT,deb INT,cred INT,oth INT,rp_name TEXT,sig TEXT)')
    cursor.execute('INSERT INTO CAR1(date,receipt,company,rep,loc,csz,phone,name,license,address,csz1,phone1,VIN1,make,year,color,reg,model,milg,cash,deb,cred,oth,rp_name,sig) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (dat,recp,comp,repnt,locn,city,phn,nm,lic,sz1,phn1,adds,vehic,mk,yr,clr,regis,mdl,mileage,cs,tx,ttl,amount,repres,sign))
    db.commit()
    msg = messagebox.showinfo( "DB Demo","SUBMITTED SUCCESSFULLY")
    


def display():
    db = sqlite3.connect('car1.db')
    with db:
      cursor=db.cursor()
      my_w = tk.Tk()
      my_w.geometry("400x250") 

      r_set=cursor.execute('''SELECT * from CAR1 ''');
      i=0  
      for CAR1 in r_set: 
            for j in range(len(CAR1)):
                e = Entry(my_w, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, CAR1[j])
            i=i+1  
   
title = Label(rk_652,text="CAR RENTAL RECEIPT",foreground="blue",font=("Calibri Bold",30),anchor=N).grid(row=0,column=2)
date = Label(rk_652,text="DATE:- ").grid(row=3,column=0)
date = Entry(rk_652)
date.grid(row=3,column=1)

receipt = Label(rk_652,text="RECEIPT#:- ").grid(row=3,column=3)
receipt = Entry(rk_652)
receipt.grid(row=3,column=4)

subhd1 = Label(rk_652,text="COMPANY INFO",foreground="red",font=("Calibri Bold",16)).grid(row=7,column=1)

company = Label(rk_652,text="COMPANY:- ").grid(row=9,column=0)
company = Entry(rk_652)
company.grid(row=9,column=1)

rep = Label(rk_652,text="REPRESENTATIVE:-").grid(row=10,column=0)
rep = Entry(rk_652)
rep.grid(row=10,column=1)

loc = Label(rk_652,text="LOCATION:-").grid(row=11,column=0)
loc = Entry(rk_652)
loc.grid(row=11,column=1)

csz = Label(rk_652,text="CITY/STATE/ZIP:-").grid(row=12,column=0)
csz = Entry(rk_652)
csz.grid(row=12,column=1)

phone = Label(rk_652,text="PHONE:-").grid(row=13,column=0)
phone = Entry(rk_652)
phone.grid(row=13,column=1)

subhd2 = Label(rk_652,text="LESSEE INFO",foreground="red",font=("Calibri Bold",16)).grid(row=7,column=4)

name = Label(rk_652,text="NAME:-").grid(row=9,column=3)
name = Entry(rk_652)
name.grid(row=9,column=4)

license = Label(rk_652,text="LICENSE#:-").grid(row=10,column=3)
license = Entry(rk_652)
license.grid(row=10,column=4)

address = Label(rk_652,text="ADDRESS:-").grid(row=11,column=3)
address = Entry(rk_652)
address.grid(row=11,column=4)

csz1 = Label(rk_652,text="CITY/STATE/ZIP:-").grid(row=12,column=3)
csz1 = Entry(rk_652)
csz1.grid(row=12,column=4)

phone1 = Label(rk_652,text="PHONE:-").grid(row=13,column=3)
phone1 = Entry(rk_652)
phone.grid(row=13,column=4)

vi = Label(rk_652,text="VEHICLE INFORMATION",foreground="blue",font=("Calibri Bold",26)).grid(row=16,column=2)

VIN1 = Label(rk_652,text="VIN:-").grid(row=18,column=0)
VIN1 = Entry(rk_652)
VIN1.grid(row=18,column=1)

make = Label(rk_652,text="MAKE:-").grid(row=19,column=0)
make = Entry(rk_652)
make.grid(row=19,column=1)

year = Label(rk_652,text="YEAR:-").grid(row=20,column=0)
year = Entry(rk_652)
year.grid(row=20,column=1)

color = Label(rk_652,text="COLOR:-").grid(row=21,column=0)
color = Entry(rk_652)
color.grid(row=21,column=1)

reg = Label(rk_652,text="REGISTRATION#:-").grid(row=18,column=3)
reg = Entry(rk_652)
reg.grid(row=18,column=4)

model = Label(rk_652,text="MODEL:-").grid(row=19,column=3)
model = Entry(rk_652)
model.grid(row=19,column=4)

milg = Label(rk_652,text="MILEAGE:-").grid(row=20,column=3)
milg = Entry(rk_652)
milg.grid(row=20,column=4)

VIN = Label(rk_652,text="VIN",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=0)
cd = Label(rk_652,text="COST/DAY",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=1)
of = Label(rk_652,text="OF DAYS#",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=2)
ac = Label(rk_652,text="ADDITIONAL COST",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=3)
lc = Label(rk_652,text="LINE COST",foreground="orange",font=("Calibri Bold",16)).grid(row=50,column=4)

pm = Label(rk_652,text="PAYMENT METHOD:-",foreground="purple",font=("Calibri Bold",14)).grid(row=57,column=0)
st = Label(rk_652,text="SUBTOTAL:-",font=("Calibri",14)).grid(row=57,column=2)
st = Entry(rk_652).grid(row=57,column=3)

tax= Label(rk_652,text="TAX(5%):-",font=("Calibri",12)).grid(row=58,column=2)
tax = Entry(rk_652)
tax.grid(row=58,column=3)

total= Label(rk_652,text="TOTAL:-",font=("Calibri",12)).grid(row=59,column=2)
total= Entry(rk_652)
total.grid(row=59,column=3)

ap = Label(rk_652,text="AMOUNT PAID:-",font=("Calibri",12)).grid(row=60,column=2)
ap = Entry(rk_652)
ap.grid(row=60,column=3)

sig = Label(rk_652,text="AUTHORIZED SIGNATURE:-",font=("Calibri",12)).grid(row=62,column=3)
sig = Entry(rk_652)
sig.grid(row=62,column=4)

rp_name = Label(rk_652,text="REPRESENTATIVE NAME:-",font=("Calibri",12)).grid(row=63,column=3)
rp_name = Entry(rk_652)
rp_name.grid(row=63,column=4)

a=Checkbutton(rk_652,text="CASH:-",font=("Calibri",12)).grid(row=58,column=0)
b=Checkbutton(rk_652,text="DEBIT:-",font=("Calibri",12)).grid(row=59,column=0)
c=Checkbutton(rk_652,text="CREDIT:-",font=("Calibri",12)).grid(row=60,column=0)
d=Checkbutton(rk_652,text="OTHER:-",font=("Calibri",12)).grid(row=61,column=0)

cash=Entry(rk_652)
cash.grid(row=58,column=1)
deb=Entry(rk_652)
deb.grid(row=59,column=1)
cred=Entry(rk_652)
cred.grid(row=60,column=1)
oth=Entry(rk_652)
oth.grid(row=61,column=1)

e=Entry(rk_652)
e.grid(row=51,column=0)
f=Entry(rk_652)
f.grid(row=52,column=0)
g=Entry(rk_652)
g.grid(row=53,column=0)

h=Entry(rk_652)
h.grid(row=51,column=1)
i=Entry(rk_652)
i.grid(row=52,column=1)
j=Entry(rk_652)
j.grid(row=53,column=1)

k=Entry(rk_652)
k.grid(row=51,column=2)
l=Entry(rk_652)
l.grid(row=52,column=2)
m=Entry(rk_652)
m.grid(row=53,column=2)

n=Entry(rk_652)
n.grid(row=51,column=3)
o=Entry(rk_652)
o.grid(row=52,column=3)
p=Entry(rk_652)
p.grid(row=53,column=3)

q=Entry(rk_652)
q.grid(row=51,column=4)
r=Entry(rk_652)
r.grid(row=52,column=4)
s=Entry(rk_652)
s.grid(row=53,column=4)
t=Entry(rk_652)
t.grid(row=54,column=4)
u=Entry(rk_652)
u.grid(row=55,column=4)
v=Entry(rk_652)
v.grid(row=56,column=4)
w=Entry(rk_652)
w.grid(row=60,column=4)

msg=Button(rk_652, text='SUBMIT',command=Database,width=20).place(x=400,y=730)
msg=Button(rk_652,text="DISPLAY RECORD(s)",command=display,width=20).place(x=600,y=730) 

rk_652.mainloop()