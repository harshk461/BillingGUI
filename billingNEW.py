from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import math
import random
import os
import pymysql
from PIL import ImageTk
import datetime


get=Tk()
get.geometry('1600x800')
bg_color='#074463'
get.config(background=bg_color)

uname=StringVar()
passwd=StringVar()

def login():
    db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
    con=db.cursor()
    con.execute("SELECT * FROM LOGIN")
    res=con.fetchall()
    if uname.get()=="" or passwd.get()=="":
            mb.showerror("Alert","All Field are required")
    for i in res:
            un=i[0]
            pas=i[1]
            
            if uname.get()==un and passwd.get()==pas:
                
                mb.showinfo("Sucessful",f"Welcome {uname.get()}")
                F121.destroy()
                

                Main=Label(get,text="Harsh Project",bg=bg_color,relief=GROOVE,fg='gold',font=('castellar',42,'bold'),pady=5).pack(fill=BOTH)
                
                
                def loan():
                    loan=Tk()
                    loan.geometry('850x400')
                    bg_color='#074463'
                    db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                    con=db.cursor()

                    id_no=StringVar()
                    def fetch():
                        
                        con.execute("select * from loan")
                        res=con.fetchall()
                        for i in res:
                            w=f"    {str(i[0])}      {str(i[1])}     {str(i[2])}"
                            
                            textarea.insert(END,f'\n{w}')
                        
                    def add():
                        nam=name_ent.get()
                        bal=bal_ent.get()
                        _id=id_ent.get()
                        con.execute(f"insert into loan values('{_id}','{nam}',{bal})")
                        db.commit()
                    def delete():
                        nam=name_ent.get()
                        _id=id_ent.get()
                        con.execute(f"delete from loan where name='{nam}' and id='{_id}'")
                        db.commit()

                    def update():
                        nam=name_ent.get()
                        _id=id_ent.get()
                        try:
                            con.execute(f"update loan set bal={bal_ent.get()} where id='{_id}' and name='{nam}'")
                        except Exception as e:
                            print(e)
                        db.commit()
                    def ref():
                        
                        id_no.set('')
                        textarea.delete('1.0')
                    F1=LabelFrame(loan,text="Customer Detail",bd=10,font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    F1.place(x=0,y=0,width=800,height=400)

                    ref=Button(F1,text="Refresh",command=ref,bd=2,relief=RAISED,bg=bg_color,fg='gold')
                    ref.place(x=470,y=0)

                    id_lbl=Label(F1,text="Phone No.",font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    id_lbl.place(x=80,y=40)

                    name=Label(F1,text="Customer Name",font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    name.place(x=80,y=87)

                    bal=Label(F1,text="Balance",font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    bal.place(x=80,y=130)

                    id_ent=Entry(F1,textvariable=id_no,bd=10,relief=SUNKEN,font="arial 12 bold",fg='blue')
                    id_ent.place(x=290,y=30)

                    name_ent=Entry(F1,bd=10,relief=SUNKEN,font="arial 12 bold",fg='blue')
                    name_ent.place(x=290,y=80)

                    bal_ent=Entry(F1,bd=10,relief=SUNKEN,font="arial 12 bold",fg=bg_color)
                    bal_ent.place(x=290,y=130)

                    add=Button(F1,text="Add",font=('times of new roman',16,'bold'),command=add,fg='gold',bg='grey',bd=3,relief=SUNKEN,height=1,width=6)
                    add.place(x=80,y=200)

                    update=Button(F1,text="Update",command=update,font=('times of new roman',15,'bold'),fg='gold',bg='grey',bd=3,relief=SUNKEN,height=1,width=6)
                    update.place(x=200,y=200)

                    clear=Button(F1,text="Delete",command=delete,font=('times of new roman',15,'bold'),fg='gold',bg='grey',bd=3,relief=SUNKEN,height=1,width=6)
                    clear.place(x=310,y=200)

                    fetch=Button(F1,text="Fetch",command=fetch,font=('times of new roman',15,'bold'),fg='gold',bg='grey',bd=3,relief=SUNKEN,height=1,width=6)
                    fetch.place(x=410,y=200)

                    F2=Frame(loan,bd=10,relief=GROOVE)
                    F2.place(x=550,y=0,width=300,height=400)

                    Bill_title=Label(F2,text="Phone no.   Name    Balance",bd=7,relief=GROOVE,font="arial 14 bold").pack(fill=X)

                    scrol_y=Scrollbar(F2,orient=VERTICAL)
                    textarea=Text(F2,yscrollcommand=scrol_y.set)
                    scrol_y.pack(side=RIGHT,fill=Y)
                    scrol_y.config(command=textarea.yview)
                    textarea.pack(fill=BOTH,expand=1)


                def bill():
#==============fuctions==================================
                    
                    bg_color='#074463'
                    ne=Frame(get,height=1000,width=1800,bg=bg_color)
                    ne.pack(fill=BOTH)
                    
                    
                    def welcome_bill():
                        txtarea.delete('1.0',END)
                        txtarea.insert(END,"\tWelcome To Harsh Store")
                        txtarea.insert(END,"\n ")
                        txtarea.insert(END,"\n ")
                        txtarea.insert(END,f"\nBill No. :{bill_entry.get()}")
                        txtarea.insert(END,f"\nCustumer Name :{str(Cust_entry.get()).capitalize()}")
                        txtarea.insert(END,f"\nPhone No. :{phone_entry.get()}")
                        txtarea.insert(END,"\n ")
                        txtarea.insert(END,"\n--------------------------------------")
                        txtarea.insert(END,"\n Product\t\tQty.\t\tPrice")
                        txtarea.insert(END,"\n--------------------------------------")
    #======custumer detail=====

                    cust=StringVar()
                    phn=StringVar()
                    billno=StringVar()
                    x=random.randint(1000,9999999)
                    billno.set(str(x))
                    date =StringVar()
                    db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                    con=db.cursor()
                    con.execute("select Curdate()")
                    res=con.fetchall()
                    for  i in res:
                        date.set(i)
                        
                    
                    #=========beverages var===================
                    burg=StringVar()
                    piz=StringVar()
                    french=StringVar()
                    chillis=StringVar()
                    momos=StringVar()
                    springr=StringVar()
                    eggroll=StringVar()
                    #===    ========sweet var==================
                    icec=StringVar()
                    lad=StringVar()
                    donutt=StringVar()
                    brownn=StringVar()
                    kulfii=StringVar()
                    rass=StringVar()
                    cakes=StringVar()
                    #===============drinks var===============
                    limcaa=StringVar()
                    Frootii=StringVar()
                    spritt=StringVar()
                    cocaa=StringVar()
                    water=StringVar()
                    appyy=StringVar()
                    pepp=StringVar()
                    #============billing var========
                    beveragES=StringVar()
                    SWEETS=StringVar()
                    DRINKS=StringVar()
                    
                    beverages_tax=StringVar()
                    sweet_tax=StringVar()
                    drink_tax=StringVar()
                    
                    burg.set('0')
                    piz.set('0')
                    french.set('0')
                    chillis.set('0')
                    momos.set('0')
                    springr.set('0')
                    eggroll.set('0')
                    icec.set('0')
                    lad.set('0')
                    donutt.set('0')
                    brownn.set('0')
                    kulfii.set('0')
                    rass.set('0')
                    cakes.set('0')
                    
                    limcaa.set('0')
                    Frootii.set('0')
                    spritt.set('0')
                    cocaa.set('0')
                    water.set('0')
                    appyy.set('0')
                    pepp.set('0')
                    
                    beveragES.set('0')
                    SWEETS.set('0')
                    DRINKS.set('0')
                    
                    beverages_tax.set('0')
                    sweet_tax.set('0')
                    drink_tax.set('0')   
                    def bill_area():
                        welcome_bill()
        #=======================================
                        total_beverage_price=(
                                (float(burger_ent.get())*60)+
                                (float(pizza_ent.get())*100)+
                                (float(French_ent.get())*40)+
                                (float(chilli_ent.get())*80)+
                                (float(momo_ent.get())*40)+
                                (float(spring_ent.get())*60)+
                                (float(egg_ent.get())*30))
                        total_sweet_price=(
                                (float(ice_ent.get())*20)+
                                (float(laddo_ent.get())*100)+
                                (float(donut_ent.get())*40)+
                                (float(brown_ent.get())*30)+
                                (float(kulfi_ent.get())*20)+
                                (float(ras_ent.get())*120)+
                                (float(cake_ent.get())*170)) 
                        total_drink_price=(
                                (float(limca_ent.get())*40)+
                                (float(frooti_ent.get())*50)+
                                (float(sprit_ent.get())*40)+
                                (float(coca_ent.get())*30)+
                                (float(pep_ent.get())*30)+
                                (float(wat_ent.get())*10)+
                                (float(app_ent.get())*20))
        #================================================    
        #======================================================
                        if Cust_entry.get()=="" or phone_entry.get()=="":
                            mb.showerror("Alert","Please Enter Name First")
                        else:
                    
                             if int(burger_ent.get()) !=0:
                                txtarea.insert(END,f"\n Burger\t\t{int(burger_ent.get())}\t\t{int(burger_ent.get())*60}")
                             if int(pizza_ent.get()) !=0:
                                txtarea.insert(END,f"\n Pizza\t\t{int(pizza_ent.get())}\t\t{int(pizza_ent.get())*60}")
                             if int(French_ent.get()) !=0:
                                txtarea.insert(END,f"\n French Fries\t\t{int(French_ent.get())}\t\t{int(French_ent.get())*100}")
                             if int(chilli_ent.get()) !=0:
                                txtarea.insert(END,f"\n Chilli Potato\t\t{int(chilli_ent.get())}\t\t{int(chilli_ent.get())*40}")    
                             if int(momo_ent.get()) !=0:
                                txtarea.insert(END,f"\n Momos\t\t{int(momo_ent.get())}\t\t{int(momo_ent.get())*80}")
                             if int(spring_ent.get()) !=0:
                                txtarea.insert(END,f"\n Spring Roll\t\t{int(spring_ent.get())}\t\t{int(spring_ent.get())*60}")
                             if int(egg_ent.get()) !=0:
                                txtarea.insert(END,f"\n Egg Roll\t\t{int(egg_ent.get())}\t\t{int(egg_ent.get())*30}")
                             if int(ice_ent.get()) !=0:
                                txtarea.insert(END,f"\n Ice Cream\t\t{int(ice_ent.get())}\t\t{int(ice_ent.get())*20}")
                             if float(laddo_ent.get()) !=0:
                                txtarea.insert(END,f"\n Laddo\t\t{round(float(laddo_ent.get()))}\t\t{round(float(laddo_ent.get()))*100}")
                             if int(donut_ent.get()) !=0:
                                txtarea.insert(END,f"\n Donut\t\t{int(donut_ent.get())}\t\t{int(donut_ent.get())*40}")
                             if int(brown_ent.get()) !=0:
                                txtarea.insert(END,f"\n Brownies\t\t{int(brown_ent.get())}\t\t{int(brown_ent.get())*30}")
                        
                             if int(kulfi_ent.get()) !=0:
                                txtarea.insert(END,f"\n Kulfi\t\t{int(kulfi_ent.get())}\t\t{int(kulfi_ent.get())*20}")
                        
                             if int(ras_ent.get()) !=0:
                                txtarea.insert(END,f"\n Rasgulla\t\t{int(ras_ent.get())}\t\t{int(ras_ent.get())*120}")
                             if int(cake_ent.get()) !=0:
                                txtarea.insert(END,f"\n Cake\t\t{round(float(cake_ent.get()))}\t\t{round(int(cake_ent.get()))*170}")
                             if float(limca_ent.get()) !=0:
                                txtarea.insert(END,f"\n Limca\t\t{round(float(limca_ent.get()))}\t\t{round(float(limca_ent.get()))*40}")

                             if int(frooti_ent.get()) !=0:
                                txtarea.insert(END,f"\n Frooti\t\t{round(int(brown_ent.get()))}\t\t{round(int(frooti_ent.get()))*50}")

                             if int(sprit_ent.get()) !=0:
                                txtarea.insert(END,f"\n Sprit\t\t{round(int(sprit_ent.get()))}\t\t{round(int(sprit_ent.get()))*40}")

                             if int(coca_ent.get()) !=0:
                                txtarea.insert(END,f"\n Coca-Cola\t\t{round(int(coca_ent.get()))}\t\t{round(int(coca_ent.get()))*30}")
                            
                             if int(pep_ent.get()) !=0:
                                txtarea.insert(END,f"\n Pepsi\t\t{round(int(pep_ent.get()))}\t\t{round(int(pep_ent.get()))*30}")

                             if int(wat_ent.get()) !=0:
                                txtarea.insert(END,f"\n Water\t\t{round(int(wat_ent.get()))}\t\t{round(int(wat_ent.get()))*10}")

                             if int(app_ent.get()) !=0:
                                txtarea.insert(END,f"\n Appy\t\t{round(int(app_ent.get()))}\t\t{round(int(app_ent.get()))*20}")
                                
                             total=total_beverage_price+total_sweet_price+total_drink_price
                             totaltax=(int(total_beverage_price)*0.1)+(int(total_sweet_price)*0.1)+(int(total_drink_price)*0.1)
                             txtarea.insert(END,f"\n--------------------------------------")
                             if (int(total_beverage_price)*0.1) !=0:
                                 txtarea.insert(END,f"\nBeverages Tax\t\tRs {(int(total_beverage_price))*0.1}")
                             if (int(total_sweet_price)*0.1) !=0:         
                                 txtarea.insert(END,f"\nSweets Tax\t\tRs {(int(total_sweet_price))*0.1}")
                             if (int(total_drink_price)*0.1)!=0:         
                                 txtarea.insert(END,f"\nDrinks Tax\t\tRs {(int(total_drink_price))*0.1}")
                             txtarea.insert(END,f"\n--------------------------------------")
                             txtarea.insert(END,f"\nTotal Amount :\t\tRs {str(math.fabs(int(total+totaltax)))}")
                             txtarea.insert(END,f"\n--------------------------------------")
                     
                             txtarea.insert(END,f"\nCreated By :    Harsh Kumar     ")
                             sql()
                             save_bill()
                    def total_price():
        
                        total_beverage_price=(
                                    (float(str(burger_ent.get()))*60)+
                                    (float(str(pizza_ent.get()))*100)+
                                    (float(str(French_ent.get()))*40)+
                                    (float(str(chilli_ent.get()))*80)+
                                    (float(str(momo_ent.get()))*40)+
                                    (float(str(spring_ent.get()))*60)+
                                    (float(str(egg_ent.get()))*30))
                        total_sweet_price=(
                                    (float(str(ice_ent.get()))*20)+
                                    (float(str(laddo_ent.get()))*100)+
                                    (float(str(donut_ent.get()))*40)+
                                    (float(str(brown_ent.get()))*30)+
                                    (float(str(kulfi_ent.get()))*20)+
                                    (float(str(ras_ent.get()))*120)+
                                    (float(str(cake_ent.get()))*170)) 
                        total_drink_price=(
                                    (float(str(limca_ent.get()))*40)+
                                    (float(str(frooti_ent.get()))*50)+
                                    (float(str(sprit_ent.get()))*40)+
                                    (float(str(coca_ent.get()))*30)+
                                    (float(str(pep_ent.get()))*30)+
                                    (float(str(wat_ent.get()))*10)+
                                    (float(str(app_ent.get()))*20))
                        beveragES.set("Rs "+str(total_beverage_price))
                        SWEETS.set("Rs "+str(total_sweet_price))
                        DRINKS.set("Rs "+str(total_drink_price))
                            
                        beverages_tax.set("Rs "+str(total_beverage_price*0.1))
                        sweet_tax.set("Rs "+str(total_sweet_price*0.1))
                        drink_tax.set("Rs "+str(total_drink_price*0.1))
                        sql()
                    def clear():
                                burg.set('0')
                                piz.set('0')
                                french.set('0')
                                chillis.set('0')
                                momos.set('0')
                                springr.set('0')
                                eggroll.set('0')
                            
                                icec.set('0')
                                lad.set('0')
                                donutt.set('0')
                                brownn.set('0')
                                kulfii.set('0')
                                rass.set('0')
                                cakes.set('0')
                            
                                limcaa.set('0')
                                Frootii.set('0')
                                spritt.set('0')
                                cocaa.set('0')
                                water.set('0')
                                appyy.set('0')
                                pepp.set('0')

                                beveragES.set('0')
                                SWEETS.set('0')
                                DRINKS.set('0')
                            
                                beverages_tax.set('0')
                                sweet_tax.set('0')
                                drink_tax.set('0')
                                Cust_entry.delete(0,END)
                                phone_entry.delete(0,END)
                                t=random.randint(1000,100000)
                                billno.set(str(t))
                                
                    def save_bill():
        
                            op=mb.askyesno("Save Bill","Do you wnat to save the bill")
                            if op>0:
                            
                                bill_data=txtarea.get('1.0',END)
                                f1=open("bill/"+str(bill_entry.get())+".txt","w")
                                f1.write(bill_data)
                                f1.close()
                                mb.showinfo("Saved",f"Bill with {str(bill_entry.get())}  is saved")
                            else:
                                return
                    def search():
                                present="no"
                                
                                for i in os.listdir("bill/"):
                                    if i.split('.')[0]== bill_entry.get():
                                        txtarea.delete('1.0',END)
                                        f1=open(f"bill/{i}","r")
                                        for d in f1:
                                            txtarea.insert(END,d)
                                            f1.close()
                                        present="yes"
                                if present=="no.":
                                    mb.showerror("Error","Invalid Entry")
                    def sql():
                            total_beverage_price=(
                                (float(burger_ent.get())*60)+
                                (float(pizza_ent.get())*100)+
                                (float(French_ent.get())*40)+
                                (float(chilli_ent.get())*80)+
                                (float(momo_ent.get())*40)+
                                (float(spring_ent.get())*60)+
                                (float(egg_ent.get())*30))
                            total_sweet_price=(
                                (float(ice_ent.get())*20)+
                                (float(laddo_ent.get())*100)+
                                (float(donut_ent.get())*40)+
                                (float(brown_ent.get())*30)+
                                (float(kulfi_ent.get())*20)+
                                (float(ras_ent.get())*120)+
                                (float(cake_ent.get())*170)) 
                            total_drink_price=(
                                (float(limca_ent.get())*40)+
                                (float(frooti_ent.get())*50)+
                                (float(sprit_ent.get())*40)+
                                (float(coca_ent.get())*30)+
                                (float(pep_ent.get())*30)+
                                (float(wat_ent.get())*10)+
                                (float(app_ent.get())*20))
                            amount=total_sweet_price+total_beverage_price+total_drink_price
                            tax=(int(total_beverage_price)*0.1)+(int(total_sweet_price)*0.1)+(int(total_drink_price)*0.1)
                            total=amount+tax
                            qty=float(burger_ent.get())+float(pizza_ent.get()) +float(French_ent.get())+  float(chilli_ent.get())+     float(momo_ent.get())+      float(spring_ent.get())+       float(egg_ent.get())+       float(ice_ent.get())+        float(laddo_ent.get())+        float(donut_ent.get())+        float(brown_ent.get())+        float(kulfi_ent.get())+        float(ras_ent.get())+        float(cake_ent.get())+         float(limca_ent.get())+        float(frooti_ent.get())+        float(sprit_ent.get())+        float(coca_ent.get())+        float(pep_ent.get())+        float(wat_ent.get())+        float(app_ent.get())
                            db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                            con=db.cursor()
                            try:
                                con.execute("select current_date,current_time")
                                res=con.fetchall()
                                for i in res:
                                    con.execute(f"INSERT INTO BILL_NEW VALUES('{Cust_entry.get()}',{phone_entry.get()},{bill_entry.get()},{qty},{total},'{i[0]}','{i[1]}') ")
                                con.execute("select stock from stock where product='ice cream'")
                                re1=con.fetchall()
                                for j in re1:
                                    if ice_ent.get() > j[0]:
                                        mb.showerror("Alert","Qty out of stock")
                                        txtarea.insert(None)
                                    else:
                                        if ice_ent.get() != 0:
                                            con.execute(f"update stock set stock  =stock - {int(ice_ent.get())} where product='ice cream'  ")
                                if laddo_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(laddo_ent.get())} where product='laddo'  ")
                                if donut_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(donut_ent.get())} where product='donut'  ")
                                if brown_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(brown_ent.get())} where product='brownies'  ")
                                if kulfi_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(kulfi_ent.get())} where product='kulfi'  ")
                                if ras_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(ras_ent.get())} where product='rassgula'  ")
                                if cake_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(cake_ent.get())} where product='cake'  ")
                                if limca_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(limca_ent.get())} where product='limca'  ")
                                if frooti_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(frooti_ent.get())} where product='frooti'  ")
                                if sprit_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(sprit_ent.get())} where product='sprit'  ")
                                if coca_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(coca_ent.get())} where product='coca-cola'  ")
                                if pep_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(pep_ent.get())} where product='pepsi'  ")
                                if wat_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(wat_ent.get())} where product='water'  ")
                                if app_ent.get() != 0:
                                    con.execute(f"update stock set stock  =stock - {int(app_ent.get())} where product='appy'  ")
                                                
                                db.commit()
                            except Exception as e:
                                print(e)
        #x=random.randint(1000,9999999)
                    def add_item():
                            add=Tk()
        
    #===========================variables===========================================================================
                    
                    F1=LabelFrame(ne,text="Customer Detail",bd=10,font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    F1.place(x=0,y=10,relwidth=1)
        
                    CustName=Label(F1,text='Name',font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    CustName.grid(row=0,column=0,padx=10,pady=4)
                    
                    Cust_entry=Entry(F1,textvariable=cust,width=25,bd=5,relief=SUNKEN,font=('times of new roman',15,'bold'))
                    Cust_entry.grid(row=0,column=1,padx=10,pady=4)
                    
                    Phone=Label(F1,text="Phone No.",font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    Phone.grid(row=0,column=2,padx=10,pady=4)

                    phone_entry=Entry(F1,textvariable=phn,width=25,bd=5,relief=SUNKEN,font=('times of new roman',15,'bold'))
                    phone_entry.grid(row=0,column=3,padx=10,pady=4)
                        
                    Bill=Label(F1,text="Bill No.",font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    Bill.grid(row=0,column=4,padx=10,pady=4)

                    bill_entry=Entry(F1,textvariable=billno,width=25,bd=5,relief=SUNKEN,font=('times of new roman',15,'bold'))
                    bill_entry.grid(row=0,column=5,padx=10,pady=4)

                    search_btn=Button(F1,text="Search",height=1,width=10,bg='blue',fg='gold',command=search,font=('times of new roman',10,'bold'),pady=15)
                    search_btn.grid(row=0,column=8)

                    date_entry=Entry(F1,textvariable=date,bg=bg_color,fg='gold',width=10,font=('arial',21,'bold'))
                    date_entry.grid(row=0,column=9,padx=10,pady=4)
                        #================================Beverages Frame=====================================================================

                    F2=LabelFrame(ne,text='Cosmetic',bd=10,relief=GROOVE,font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    F2.place(x=0,y=100,width=330,height=430)
                        
                    Burger=Label(F2,text="Burger",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    Burger.grid(row=0,column=0,padx=10,pady=10,sticky='w')

                    burger_ent=Entry(F2,textvariable=burg,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    burger_ent.grid(row=0,column=1,padx=10,pady=10)
                        
                    Pizza=Label(F2,text="Pizza",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    Pizza.grid(row=1,column=0,padx=10,pady=10,sticky='w')

                    pizza_ent=Entry(F2,textvariable=piz,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    pizza_ent.grid(row=1,column=1,padx=10,pady=10)

                    French=Label(F2,text="French Fries",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    French.grid(row=2,column=0,padx=10,pady=10,sticky='w')
                        
                    French_ent=Entry(F2,textvariable=french,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    French_ent.grid(row=2,column=1,padx=10,pady=10)

                    chilli=Label(F2,text="Chilli Potato",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    chilli.grid(row=3,column=0,padx=10,pady=10,sticky='w')

                    chilli_ent=Entry(F2,textvariable=chillis,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    chilli_ent.grid(row=3,column=1,padx=10,pady=10)

                    momo=Label(F2,text="Momos",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    momo.grid(row=4,column=0,padx=10,pady=10,sticky='w')
                        
                    momo_ent=Entry(F2,textvariable=momos,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    momo_ent.grid(row=4,column=1,padx=10,pady=10)
                        
                    spring=Label(F2,text="Spring Roll",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    spring.grid(row=5,column=0,padx=10,pady=10,sticky='w')
                        
                    spring_ent=Entry(F2,textvariable=springr,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    spring_ent.grid(row=5,column=1,padx=10,pady=10)

                    egg=Label(F2,text="Egg Roll",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    egg.grid(row=6,column=0,padx=10,pady=10,sticky='w')
                        
                    egg_ent=Entry(F2,textvariable=eggroll,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    egg_ent.grid(row=6,column=1,padx=10,pady=10)
                        

                    #================================Beverages Frame End=====================================================================

                    #================================sweets===============================================================================

                    F3=LabelFrame(ne,text='Sweets',bd=10,relief=GROOVE,font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    F3.place(x=330,y=100,width=330,height=430)

                    ice=Label(F3,text="Ice Cream",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    ice.grid(row=0,column=0,padx=10,pady=10,sticky='w')
                        
                    ice_ent=Entry(F3,textvariable=icec,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    ice_ent.grid(row=0,column=1,padx=10,pady=10)
                        
                    laddo=Label(F3,text="Laddo",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    laddo.grid(row=1,column=0,padx=10,pady=10,sticky='w')
                        
                    laddo_ent=Entry(F3,textvariable=lad,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    laddo_ent.grid(row=1,column=1,padx=10,pady=10)
                        
                    donut=Label(F3,text="Donut",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    donut.grid(row=2,column=0,padx=10,pady=10,sticky='w')
                        
                    donut_ent=Entry(F3,textvariable=donutt,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    donut_ent.grid(row=2,column=1,padx=10,pady=10)

                    brown=Label(F3,text="Brownies",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    brown.grid(row=3,column=0,padx=10,pady=10,sticky='w')

                    brown_ent=Entry(F3,textvariable=brownn,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    brown_ent.grid(row=3,column=1,padx=10,pady=10)

                    kulfi=Label(F3,text="Kulfi",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    kulfi.grid(row=4,column=0,padx=10,pady=10,sticky='w')

                    kulfi_ent=Entry(F3,textvariable=kulfii,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    kulfi_ent.grid(row=4,column=1,padx=10,pady=10)

                    ras=Label(F3,text="Rasgulla",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    ras.grid(row=5,column=0,padx=10,pady=10,sticky='w')
                        
                    ras_ent=Entry(F3,textvariable=rass,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    ras_ent.grid(row=5,column=1,padx=10,pady=10)

                    cake=Label(F3,text="Cake",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    cake.grid(row=6,column=0,padx=10,pady=10,sticky='w')

                    cake_ent=Entry(F3,textvariable=cakes,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    cake_ent.grid(row=6,column=1,padx=10,pady=10)

                    #============================sweet end================================================================================
                    #=========================================Drink=======================================================================

                    F4=LabelFrame(ne,text='Drinks',bd=10,relief=GROOVE,font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    F4.place(x=660,y=100,width=330,height=430)
                        
                    limca=Label(F4,text="Limca",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    limca.grid(row=0,column=0,padx=10,pady=10,sticky='w')

                    limca_ent=Entry(F4,textvariable=limcaa,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    limca_ent.grid(row=0,column=1,padx=10,pady=10)

                    frooti=Label(F4,text="Frooti",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    frooti.grid(row=1,column=0,padx=10,pady=10,sticky='w')

                    frooti_ent=Entry(F4,textvariable=Frootii,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    frooti_ent.grid(row=1,column=1,padx=10,pady=10)

                    sprit=Label(F4,text="Sprit",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    sprit.grid(row=2,column=0,padx=10,pady=10,sticky='w')

                    sprit_ent=Entry(F4,textvariable=spritt,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    sprit_ent.grid(row=2,column=1,padx=10,pady=10)

                    coca=Label(F4,text="Coco Cola",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    coca.grid(row=3,column=0,padx=10,pady=10,sticky='w')
                        
                    coca_ent=Entry(F4,textvariable=cocaa,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    coca_ent.grid(row=3,column=1,padx=10,pady=10)

                    pep=Label(F4,text="Pepsi",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    pep.grid(row=4,column=0,padx=10,pady=10,sticky='w')

                    pep_ent=Entry(F4,textvariable=pepp,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    pep_ent.grid(row=4,column=1,padx=10,pady=10)

                    wat=Label(F4,text="Water",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    wat.grid(row=5,column=0,padx=10,pady=10,sticky='w')

                    wat_ent=Entry(F4,textvariable=water,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    wat_ent.grid(row=5,column=1,padx=10,pady=10)

                    app=Label(F4,text="Appy",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    app.grid(row=6,column=0,padx=10,pady=10,sticky='w')

                    app_ent=Entry(F4,textvariable=appyy,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    app_ent.grid(row=6,column=1,padx=10,pady=10)

                    #=====================bill area=======================================================================================
                    F5=Frame(ne,bd=10,relief=GROOVE)
                    F5.place(x=990,y=100,width=350,height=430)

                    Bill_title=Label(F5,text="Bill Area",bd=7,relief=GROOVE,font="arial 15 bold").pack(fill=X)
                    scrol_y=Scrollbar(F5,orient=VERTICAL)
                    txtarea=Text(F5,yscrollcommand=scrol_y.set)
                    scrol_y.pack(side=RIGHT,fill=Y)
                    scrol_y.config(command=txtarea.yview)
                    txtarea.pack(fill=BOTH,expand=1)
                    #============================Button Frame=============================================================================
                    F6=LabelFrame(ne,text='Billing Amount',bd=10,relief=GROOVE,font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    F6.place(x=0,y=530,width=1334,height=185)
                        
                        #======butttons=========#
                    F7=Frame(F6,bd=10,relief=GROOVE)
                    F7.place(x=750,width=580,height=152)
                    
                    b1=Button(F7,text='Total',bg='blue',fg='gold',command=total_price,font=('times of new roman',14,'bold'),pady=20,width=10).place(x=0,y=20)
                    
                    b2=Button(F7,text='Generate Bill',bg='blue',command=bill_area,fg='gold',font=('times of new roman',14,'bold'),pady=20,width=10).place(x=140,y=20)

                    b3=Button(F7,text='Clear',bg='blue',fg='gold',command=clear,font=('times of new roman',14,'bold'),pady=20,width=10).place(x=280,y=20)

                    b4=Button(F7,text='Exit',bg='blue',command=ne.destroy,fg='gold',font=('times of new roman',14,'bold'),pady=20,width=10).place(x=420,y=20)
                    welcome_bill()
                    #=============================billing frame===========================================================================
                    tb=Label(F6,text="Total Beverages Price",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    tb.grid(row=0,column=0,padx=10,pady=3,sticky='w')

                    tb_ent=Entry(F6,textvariable=beveragES,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    tb_ent.grid(row=0,column=1,padx=10,pady=3)

                    ts=Label(F6,text="Total Sweets Price",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    ts.grid(row=1,column=0,padx=10,pady=3,sticky='w')

                    ts_ent=Entry(F6,textvariable=SWEETS,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    ts_ent.grid(row=1,column=1,padx=10,pady=3)
                        
                    td=Label(F6,text="Total Drinks Price",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    td.grid(row=2,column=0,padx=10,pady=3,sticky='w')

                    td_ent=Entry(F6,textvariable=DRINKS,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    td_ent.grid(row=2,column=1,padx=10,pady=3)

                    tbT=Label(F6,text="Beverages Taxes",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    tbT.grid(row=0,column=3,padx=10,pady=3,sticky='w')

                    tbT_ent=Entry(F6,textvariable=beverages_tax,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    tbT_ent.grid(row=0,column=4,padx=10,pady=3)

                    tsT=Label(F6,text="Sweets Taxes",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    tsT.grid(row=1,column=3,padx=10,pady=3,sticky='w')

                    tsT_ent=Entry(F6,textvariable=sweet_tax,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    tsT_ent.grid(row=1,column=4,padx=10,pady=3)

                    tdT=Label(F6,text="Drinks Taxes",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    tdT.grid(row=2,column=3,padx=10,pady=3,sticky='w')

                    tdT_ent=Entry(F6,textvariable=drink_tax,width=12,bd=5,relief=SUNKEN,font=('arial',15,'bold'))
                    tdT_ent.grid(row=2,column=4,padx=10,pady=3)

                    F7=LabelFrame(ne,text='Extra',bd=10,relief=GROOVE,font=('times of new roman',15,'bold'),fg='gold',bg=bg_color)
                    F7.place(x=1330,y=100,width=200,height=615)

                    prod=Button(F7,text="Pricing",font='arial 13 bold',bd=10,height=2,width=15,background="red")
                    prod.grid(row=0,column=0)
                    # def loan():
                    #         import loan
                    khata=Button(F7,text="loan",font='arial 13 bold',bd=10,height=2,width=15,background="red",command=loan)
                    khata.grid(row=1,column=0)

                    add_item=Button(F7,text="Add Item",font='arial 12 bold',bd=10,height=2,width=15,background="red",command=add_item)
                    add_item.grid(row=2,column=0)
                def stock_present():
                    stock=Frame(get,bg='yellow')
                    stock.pack(fill=BOTH)
                    Fmain=Frame(stock,bd=3,width=250,height=720,bg='white')
                    Fmain.pack(side=LEFT,fill=BOTH)
                    M1_var=StringVar()
                    M2_var=StringVar()
                    M3_var=StringVar()
                    def add():
                        
                        db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                        con=db.cursor()
                        con.execute(f"INSERT INTO STOCK VALUES('{M1_var.get()}','{M2_var.get()}','{M3_var.get()}')")
                        db.commit()
                    def update():
                        db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                        con=db.cursor()
                        con.execute(f'SELECT STOCK FROM STOCK WHERE PRODUCT="{M2_var.get()}" and COMP="{M1_var.get()}"')
                        initial=con.fetchall()
                        print(initial)
                        con.execute(f"UPDATE stock SET stock='{int(initial[0][0])+int(M3_var.get())}' WHERE product='{M2_var.get()}' and comp='{M1_var.get()}'")
                        db.commit()
                        mb.showinfo('Update','Update successfully')                        

                        
                    def fetch():
                        db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                        con=db.cursor()
                        con.execute("SELECT * FROM STOCK")
                        res=con.fetchall()
                        txtarea.delete('2.0',END)
                        for i in res:
                            txtarea.insert(END,f"\n{i[0]}\t\t\t\t{i[1]}\t\t\t\t{i[2]}")
                    def clear():
                        txtarea.delete('2.0',END)
                        M1_var.set('')
                        M2_var.set('')
                        M3_var.set('')
                    M1=Label(Fmain,text="Company",font=('arial',20,'bold'),fg='gold',bg='white').place(x=0,y=30)

                    M1_ent=Entry(Fmain,textvariable=M1_var,font=('arial',15,'bold'),bd=3,relief=GROOVE).place(x=0,y=80)
                    
                    M2=Label(Fmain,text="Product",font=('arial',20,'bold'),fg='gold',bg='white').place(x=0,y=130)

                    M2_ent=Entry(Fmain,textvariable=M2_var,font=('arial',15,'bold'),bd=3,relief=GROOVE).place(x=0,y=180)
                    
                    M3=Label(Fmain,text="Add Stock",font=('arial',20,'bold'),fg='gold',bg='white').place(x=0,y=230)

                    M3_ent=Entry(Fmain,textvariable=M3_var,font=('arial',15,'bold'),bd=3,relief=GROOVE).place(x=0,y=280)

                    M_add=Button(Fmain,text="Add",bd=2,command=add,height=1,width=8,font=('arial',20,'bold')).place(x=0,y=330)

                    M_up=Button(Fmain,text="Update",command=update,bd=2,height=1,width=8,font=('arial',20,'bold')).place(x=80,y=410)

                    M_fet=Button(Fmain,text="Fetch",bd=2,command=fetch,height=1,width=8,font=('arial',20,'bold')).place(x=0,y=490)

                    M_clr=Button(Fmain,text="Clear",bd=2,command=clear,height=1,width=8,font=('arial',20,'bold')).place(x=80,y=570)

                    M_ext=Button(Fmain,text="Exit",bd=2,height=1,command=stock.destroy,width=8,font=('arial',20,'bold')).place(x=0,y=650)
                    
                    
                    scrol_y=Scrollbar(stock,orient=VERTICAL)
                    txtarea=Text(stock,yscrollcommand=scrol_y.set,font=('arial',15,'bold'))
                    scrol_y.pack(side=RIGHT,fill=Y)
                    scrol_y.config(command=txtarea.yview)
                    txtarea.pack(padx=2,pady=100,expand=1)
                    txtarea.insert('1.0',"Company\t\t\t\tProduct\t\t\t\tStock")
                    txtarea.insert(END,"\t\t\t\t\t\t\t\t")
                def register():
                        regF=Frame(get,bg=bg_color)
                        regF.pack(fill=BOTH,expand=1)
                        
                        un=StringVar()
                        pas=StringVar()
                        paC=StringVar()
                        
                        def reg():
                            use=un.get()
                            pa=pas.get()
    
                            db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                            con=db.cursor()
                            if pa != paC.get():
                                mb.showerror("Alert","Please Enter correct password in both field")
                            else:
                                
                                try:
                                    con.execute(f"INSERT INTO LOGIN VALUES('{use}','{pa}')")
                                    db.commit()
                                    mb.showinfo("Successful","Registerd Successfully")
                                except:
                                    mb.showerror("Alert","Use another Username it is used")
                                    
                        title_label=Label(regF,text="Register",bd=5,relief=RAISED,font=('arial',40,'bold'),bg='powder blue',fg='gold').place(x=0,y=10,width=1550)
                        userR=Label(regF,text="Username",font=('arial',15,'bold'),bg=bg_color,fg='gold',compound=LEFT)
                        userR.place(x=10,y=150)

                        passW=Label(regF,text="Password",font=('arial',15,'bold'),bg=bg_color,fg='gold',compound=LEFT)
                        passW.place(x=10,y=250)

                        passC=Label(regF,text="Confirm Password",font=('arial',15,'bold'),bg=bg_color,fg='gold',compound=LEFT)
                        passC.place(x=10,y=350)

                        userent=Entry(regF,textvariable=un,bd=4,relief=GROOVE,font=("",15)).place(x=10,y=200)
                        passent=Entry(regF,textvariable=pas,bd=4,relief=GROOVE,font=("",15),show='*').place(x=10,y=300)
                        passCent=Entry(regF,textvariable=paC,bd=4,relief=GROOVE,font=("",15),show='*').place(x=10,y=400)

                        reg_btn=Button(regF,text="Register",command=reg,bd=3,relief=GROOVE,fg='gold',bg=bg_color,font=('arial',16,'bold')).place(x=10,y=450,height=60,width=500)

                        ext=Button(regF,text="Exit",command=regF.destroy,bd=3,relief=GROOVE,fg='gold',bg=bg_color,font=('arial',16,'bold')).place(x=10,y=550,height=60,width=500)
                
                def  sale():
                     sal=Frame(get,bg='red')
                     sal.pack(fill=BOTH,expand=1)
                     
                     def update():
                           try:
                                db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                                con=db.cursor()
                                I=prod_ent.get()
                                P=price_ent.get()
                                con.execute(f"UPDATE PRICE SET price={P} WHERE product='{I}' ")
                                db.commit()
                           except Exception as e:
                               print(e)

                     def fetch():
                           if prod_ent.get()=="" and comp_ent.get()=="" and price_ent.get()=="":
                                 
                                 db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                                 con=db.cursor()
                                 con.execute('SELECT * FROM PRICE ')
                                 res=con.fetchall()
                                 for i in res:
                                       txtarea.insert(END,"\n ")
                                       txtarea.insert(END,f"\n{i[0]}\t\t\t{i[1]}")
                           elif comp_ent.get() !="":
                                
                                 
                                      
                                 if str(comp_ent.get()).capitalize() =="Beverage" :
                                     db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                                     con=db.cursor()
                                     con.execute("SELECT * FROM BEVERAGE")
                                     res=con.fetchall()
                                     for i in res:
                                         txtarea.insert(END,"\n  ")
                                         txtarea.insert(END,f"\n{i[0]}\t\t\t{i[1]}")
                                     db.commit()
                                 elif str(comp_ent.get()).capitalize() =="Sweets" :
                                     db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                                     con=db.cursor()
                                     con.execute("SELECT * FROM sweet")
                                     res=con.fetchall()
                                     for i in res:
                                         
                                         txtarea.insert(END,"\n  ")
                                         txtarea.insert(END,f"\n{i[0]}\t\t\t{i[1]}")
                                     db.commit()
                                 elif str(comp_ent.get()).capitalize() =="Drinks" :
                                     db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                                     con=db.cursor()
                                     con.execute("SELECT * FROM drink")
                                     res=con.fetchall()
                                     for i in res:
                                         txtarea.insert(END,"\n ")
                                         txtarea.insert(END,f"\n{i[0]}\t\t\t{i[1]}")
                                     db.commit()
                           elif str(prod_ent.get()).capitalize() !="":
                               
                                       db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                                       con=db.cursor()
                                       P=prod_ent.get()
                                       con.execute(f"SELECT * FROM PRICE WHERE product='{P}' ")
                                       res=con.fetchall()
                                       for i in res:
                                             txtarea.insert(END,"\n")
                                             txtarea.insert(END,f"{i[0]}\t\t\t{i[1]}")
                                       db.commit()
                     def clear():
                         txtarea.delete('2.0',END)
                     F=Frame(sal,bd=5,relief=SUNKEN,bg='white',height=550,width=400)
                     F.place(x=10,y=80)
                     TIT=Label(F,text="Search Product",font=('arial',25,'bold'),fg='gold')
                     TIT.place(x=10,y=50)

                     tit_prod=Label(F,text="Product",fg='gold',font=('arial',15,'bold'))
                     tit_prod.place(x=10,y=170)

                     prod_ent=Entry(F,fg='red',font=('arial',15,'bold'),bd=5,relief=SUNKEN)
                     prod_ent.place(x=120,y=170)
                     
                     tit_comp=Label(F,text="Category",fg='gold',font=('arial',15,'bold'))
                     tit_comp.place(x=10,y=230)

                     comp_ent=Entry(F,fg='red',font=('arial',15,'bold'),bd=5,relief=SUNKEN)
                     comp_ent.place(x=120,y=230)

                     tit_price=Label(F,text="Price",fg='gold',font=('arial',15,'bold'))
                     tit_price.place(x=10,y=290)

                     price_ent=Entry(F,fg='red',font=('arial',15,'bold'),bd=5,relief=SUNKEN)
                     price_ent.place(x=120,y=290)
                     
                     B1=Button(F,text="Fetch",command=fetch,fg='gold',font=('arial',15,'bold'),height=2,width=12)
                     B1.place(x=10,y=370)

                     B2=Button(F,text="Update",command=update,fg='gold',font=('arial',15,'bold'),height=2,width=12)
                     B2.place(x=170,y=370)
                     
                     B3=Button(F,text="Exit",command=sal.destroy,fg='gold',font=('arial',15,'bold'),height=2,width=12)
                     B3.place(x=170,y=450)

                     B4=Button(F,text="Clear",command=clear,fg='gold',font=('arial',15,'bold'),height=2,width=12)
                     B4.place(x=10,y=450)
                     
                     F12=Frame(sal,bd=5,relief=SUNKEN,bg='white',height=500,width=400)
                     F12.place(x=500,y=80)

                     
                     
                     scrol_y=Scrollbar(F12,orient=VERTICAL)
                     txtarea=Text(F12,yscrollcommand=scrol_y.set,font=('arial',15,'bold'),height=20,width=35)
                     scrol_y.pack(side=RIGHT,fill=Y)
                     scrol_y.config(command=txtarea.yview)
                     txtarea.pack()
                     txtarea.insert('1.0','Product\t\t\tPrice')
                     
                     
                     F13=Frame(sal,bd=5,relief=SUNKEN,bg='white',height=500,width=450)
                     F13.place(x=1000,y=80)
                def chng_passwd():
                    F1=Frame(get,bd=0,relief=SUNKEN,bg=bg_color)
                    F1.pack(fill=BOTH,expand=1)
                    
                    def up():
                        db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                        try:
                            con=db.cursor()
                            P=userF.get()
                            Q=newF.get()
                            R=oldF.get()
                        
                            con.execute(f"UPDATE LOGIN SET pass='{Q}' where user='{P}' and pass='{R}' ")
                            db.commit()
                        except Exception as e:
                            print(e)
                        
                    tit=Label(F1,text="Change Password",font=('arial',40,'bold'),bd=7,relief=SUNKEN,bg='yellow',fg='red').pack(side=TOP,fill=X)

                    user=Label(F1,text="Username",font=('arial',20,'bold'),fg='gold',bg=bg_color)
                    user.place(x=10,y=150)

                    userF=Entry(F1,font=('arial',20,'bold'),fg='gold',bd=3,relief=SUNKEN)
                    userF.place(x=10,y=200)

                    old=Label(F1,text="Old Password",font=('arial',20,'bold'),fg='gold',bg=bg_color)
                    old.place(x=10,y=250)

                    oldF=Entry(F1,font=('arial',20,'bold'),fg='gold',bd=3,relief=SUNKEN)
                    oldF.place(x=10,y=300)

                    new=Label(F1,text="New Password",font=('arial',20,'bold'),fg='gold',bg=bg_color)
                    new.place(x=10,y=350)

                    newF=Entry(F1,font=('arial',20,'bold'),fg='gold',bd=3,relief=SUNKEN)
                    newF.place(x=10,y=400)

                    B1=Button(F1,text="Update",command=up,font=('arial',20,'bold'),fg='gold',bd=3,relief=SUNKEN,height=1,width=20).place(x=10,y=470)

                    B2=Button(F1,text="Exit",font=('arial',20,'bold'),command=F1.destroy,fg='gold',bd=3,relief=SUNKEN,height=1,width=20).place(x=10,y=550)
                def employ():
                    FX=Frame(get,bd=2,relief=SUNKEN,bg=bg_color)
                    FX.pack(fill=BOTH,expand=1)
                    def srch():
                          db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                          con=db.cursor()
                          O=te_ent.get()
                          con.execute(f'SELECT * FROM EMP WHERE ID={O}')
                          res=con.fetchall()
                          txtarea.delete('3.0',END)
                          for i in res:
                              txtarea.insert(END,f"\n{i[0]}\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[5]}")
                          db.commit()
                          
                    def add():
                          db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                          con=db.cursor()
                          con.execute(f"INSERT INTO EMP VALUES({id_var.get()},'{nam_ent.get()}',{cnc_ent.get()},'{gen.get()}',{pass_ent.get()},'{des_ent.get()}')")
                          db.commit()
                          mb.showinfo("Sucessful","Data Inserted")
                          te_ent.delete(0,END)
                          y=random.randint(1000,1000000)
                          id_var.set(y)
                          te_ent.delete(0,END)
                          nam_ent.delete(0,END)
                          cnc_ent.delete(0,END)
                          des_ent.delete(0,END)
                          pass_ent.delete(0,END)
                          mail_ent.delete(0,END)
                          proof_ent.delete(0,END)
                          
                    def update():
                          db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                          con=db.cursor()
                          db.commit()
                    def  fetch():
                          db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                          con=db.cursor()
                          con.execute("SELECT * FROM EMP")
                          res=con.fetchall()
                          txtarea.delete('3.0',END)
                          for i in res:
                              txtarea.insert(END,f"\n{i[0]}\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[5]}")
                          db.commit()

                    def clear():
                        txtarea.delete('3.0',END)
                        te_ent.delete(0,END)
                        y=random.randint(1000,1000000)
                        id_var.set(y)
                        te_ent.delete(0,END)
                        nam_ent.delete(0,END)
                        cnc_ent.delete(0,END)
                        des_ent.delete(0,END)
                        pass_ent.delete(0,END)
                        mail_ent.delete(0,END)
                        proof_ent.delete(0,END)
                    f1=LabelFrame(FX,text="Search Employee",bg=bg_color,bd=4,relief=SUNKEN,font=('arial',15,'bold'))
                    f1.place(x=450,y=30,height=100,width=600)

                    te=Label(f1,text="Employee ID",font=('arial',15,'bold'),bg=bg_color)
                    te.place(x=10,y=15)

                    te_ent=Entry(f1,bd=3,relief=SUNKEN,font=('arial',15,'bold'))
                    te_ent.place(x=200,y=15)

                    BTN=Button(f1,text="Search",command=srch,font=('arial',15,'bold'))
                    BTN.place(x=470,y=14)

                    f2=Frame(FX,bd=5,relief=GROOVE,bg=bg_color)
                    f2.place(x=30,y=170,height=530,width=400)
                    
                    id_var=IntVar()
                    s=random.randint(1000,1000000)
                    id_var.set(s)
                    
                    emp_id=Label(f2,text="Employee ID",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    emp_id.place(x=10,y=30)

                    emp_nam=Label(f2,text="Name",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    emp_nam.place(x=10,y=90)

                    emp_con=Label(f2,text="Contact No.",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    emp_con.place(x=10,y=150)

                    emp_gen=Label(f2,text="Select Gender",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    emp_gen.place(x=10,y=210)

                    emp_des=Label(f2,text="Designation",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    emp_des.place(x=10,y=270)

                    emp_pass=Label(f2,text="Password",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    emp_pass.place(x=10,y=330)

                    emp_proof=Label(f2,text="Proof Of ID",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    emp_proof.place(x=10,y=390)

                    emp_mail=Label(f2,text="Email",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                    emp_mail.place(x=10,y=450)

                    id_ent=Entry(f2,textvariable=id_var,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                    id_ent.place(x=150,y=30)

                    nam_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                    nam_ent.place(x=150,y=90)

                    cnc_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                    cnc_ent.place(x=150,y=150)

                    gen=ttk.Combobox(f2,values=['Male','Female','Others'],font=('arial',13,'bold'))
                    gen.place(x=150,y=210)

                    des_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                    des_ent.place(x=150,y=270)

                    pass_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                    pass_ent.place(x=150,y=330)

                    proof_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                    proof_ent.place(x=150,y=390)

                    mail_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                    mail_ent.place(x=150,y=450)

                    F12=Frame(FX,bd=5,relief=SUNKEN,bg=bg_color)
                    F12.place(x=1300,y=170,height=530,width=180)
                    B1=Button(F12,text="Add",command=add,height=2,width=14,font=('arial',15,'bold')).grid(row=0,column=0,pady=15)

                    B2=Button(F12,text="Update",command=add,height=2,width=14,font=('arial',15,'bold')).grid(row=1,column=0,pady=15)

                    B3=Button(F12,text="Clear",command=clear,height=2,width=14,font=('arial',15,'bold')).grid(row=2,column=0,pady=15)

                    B4=Button(F12,text="Fetch",command=fetch,height=2,width=14,font=('arial',15,'bold')).grid(row=3,column=0,pady=15)

                    B5=Button(F12,text="Exit",command=FX.destroy,height=2,width=14,font=('arial',15,'bold')).grid(row=4,column=0,pady=15)

                    F13=Frame(FX,bd=5,relief=SUNKEN,height=530,width=700)
                    F13.place(x=490,y=170)

                    scrol_y=Scrollbar(F13,orient=VERTICAL)
                    txtarea=Text(F13,yscrollcommand=scrol_y.set,font=('arial',15,'bold'),height=21,width=67)
                    scrol_y.pack(side=RIGHT,fill=Y)
                    scrol_y.config(command=txtarea.yview)
                    txtarea.pack()
                    txtarea.insert('1.0',"ID\tName\t\tContact\t\tGender\t\tDesigination")
                    txtarea.insert('2.0',"\n  ")

                new_frame=Frame(get,bd=3,relief=GROOVE,height=690,width=200)
                new_frame.place(x=10,y=90)                
                
                b1=Button(new_frame,text="Billing",compound=TOP,font=('arial',20,'bold'),height=2,width=11,command=bill).grid(row=0,column=0,pady=7)

                b2=Button(new_frame,text="Stock",font=('arial',20,'bold'),height=2,width=11,command=stock_present).grid(row=1,column=0,pady=7)

                b3=Button(new_frame,text="Employee",font=('arial',20,'bold'),height=2,width=11,command=employ).grid(row=2,column=0,pady=7)

                b4=Button(new_frame,text="Register",font=('arial',20,'bold'),height=2,width=11,command=register).grid(row=3,column=0,pady=7)

                b6=Button(new_frame,text="Change Password",font=('arial',16,'bold'),height=3,width=14,command=chng_passwd).grid(row=5,column=0,pady=7)

                b7=Button(new_frame,text="Pricing",font=('arial',20,'bold'),height=2,width=11,command=sale).grid(row=6,column=0)
                def log():
                    get.destroy()
                         
                b8=Button(get,text="Log Out",command=log,font=('arial',10,'bold'),height=1,width=15)
                b8.place(x=1300,y=120)
                def time():
                            now=datetime.datetime.now()
                            string2=now.strftime('''(%H:%M:%S) ''')
                            
                            
                            lbl2.config(text=string2)
                            lbl2.after(1000,time)

                lbl2=Label(get,font=('calibri',30,'bold'),
                                  background=bg_color,
                                  foreground='white')
                lbl2.place(x=1260,y=10)
                time()
                def salary():
                        sal=Frame(get,bd=5,relief=SUNKEN,bg='yellow')
                        sal.pack(fill=BOTH,expand=1)
                        def srch():
                          db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                          con=db.cursor()
                          O=te_ent.get()
                          con.execute(f'SELECT * FROM EMP WHERE ID={O}')
                          res=con.fetchall()
                          for i in res:
                              txtarea.insert(END,f"\n{i[0]}\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[5]}")
                          db.commit()
                          
                        def add():
                              db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                              con=db.cursor()
                              con.execute(f"INSERT INTO salary VALUES({id_var.get()},'{nam_ent.get()}','{des_ent.get()}',{sal_ent.get()},{cnc_ent.get()})")
                              db.commit()
                              mb.showinfo("Sucessful","Data Inserted")
                        def update():
                              db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                              con=db.cursor()
                              db.commit()
                        def  fetch():
                              db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                              con=db.cursor()
                              con.execute("SELECT * FROM salary")
                              res=con.fetchall()
                              txtarea.delete('2.0',END)
                              for i in res:
                                  txtarea.insert(END,f"\n{i[0]}\t{str(i[1]).capitalize()}\t\t{i[4]}\t\t{str(i[2]).capitalize()}\t\t{i[3]}")
                              db.commit()

                        def clear():
                            txtarea.delete('3.0',END)
                            te_ent.delete(0,END)
                            y=random.randint(1000,1000000)
                            id_var.set(y)
                            te_ent.delete(0,END)
                            nam_ent.delete(0,END)
                            cnc_ent.delete(0,END)
                            des_ent.delete(0,END)
                            pass_ent.delete(0,END)
                            mail_ent.delete(0,END)
                            proof_ent.delete(0,END)
                        #F11=Frame(sal,bd=5,relief=SUNKEN,bg='white',height=680,width=250)
                        #F11.place(x=960,y=100)
                        
                        

                        f2=Frame(sal,bd=5,relief=GROOVE,bg=bg_color)
                        f2.place(x=30,y=120,height=530,width=400)
                        
                        id_var=IntVar()
                        s=random.randint(1000,1000000)
                        id_var.set(s)
                        
                        emp_id=Label(f2,text="Employee ID",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        emp_id.place(x=10,y=30)

                        emp_nam=Label(f2,text="Name",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        emp_nam.place(x=10,y=90)

                        emp_con=Label(f2,text="Contact No.",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        emp_con.place(x=10,y=150)

                        emp_gen=Label(f2,text="Select Gender",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        emp_gen.place(x=10,y=210)

                        emp_des=Label(f2,text="Designation",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        emp_des.place(x=10,y=270)

                        emp_pass=Label(f2,text="Salary",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        emp_pass.place(x=10,y=330)

                        id_ent=Entry(f2,textvariable=id_var,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                        id_ent.place(x=150,y=30)

                        nam_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                        nam_ent.place(x=150,y=90)

                        cnc_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                        cnc_ent.place(x=150,y=150)

                        gen=ttk.Combobox(f2,values=['Male','Female','Others'],font=('arial',13,'bold'))
                        gen.place(x=150,y=210)

                        des_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                        des_ent.place(x=150,y=270)

                        sal_ent=Entry(f2,bd=3,relief=SUNKEN,font=('arial',15,'bold'))
                        sal_ent.place(x=150,y=330)
                        F12=Frame(sal,bd=5,relief=SUNKEN,bg=bg_color)
                        F12.place(x=1300,y=120,height=530,width=190)
                        B1=Button(F12,text="Add",command=add,height=2,width=14,font=('arial',15,'bold')).grid(row=0,column=0,pady=15)

                        B2=Button(F12,text="Update",command=add,height=2,width=14,font=('arial',15,'bold')).grid(row=1,column=0,pady=15)

                        B3=Button(F12,text="Clear",command=clear,height=2,width=14,font=('arial',15,'bold')).grid(row=2,column=0,pady=15)

                        B4=Button(F12,text="Fetch",command=fetch,height=2,width=14,font=('arial',15,'bold')).grid(row=3,column=0,pady=15)

                        B5=Button(F12,text="Exit",command=sal.destroy,height=2,width=14,font=('arial',15,'bold')).grid(row=4,column=0,pady=15)

                        F13=Frame(sal,bd=5,relief=SUNKEN,height=530,width=700)
                        F13.place(x=490,y=120)

                        scrol_y=Scrollbar(F13,orient=VERTICAL)
                        txtarea=Text(F13,yscrollcommand=scrol_y.set,font=('arial',15,'bold'),height=21,width=67)
                        scrol_y.pack(side=RIGHT,fill=Y)
                        scrol_y.config(command=txtarea.yview)
                        txtarea.pack()
                        txtarea.insert('1.0',"ID\tName\t\tContact\t\tDesigination\t\tSalary")
                        txtarea.insert('2.0',"\n  ")
                def budget():
                        F12=Frame(get,bd=5,relief=SUNKEN,bg='red')
                        F12.pack(fill=BOTH,expand=1)
                        def update():
                              db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                              con=db.cursor()
                              db.commit()
                        def  fetch():
                              db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                              con=db.cursor()
                              con.execute(f"SELECT * FROM bill_new where bill_date between '{st_ent.get()}' and '{ed_ent.get()} '")
                              res=con.fetchall()
                              for i in res:
                                  txtarea.insert(END,f"\n{i[5]} \t\t{i[6]}\t\t{i[3]}\t\t{i[4]}")
                                  txtarea.insert(END,"\n ")
                              con.execute(f'select sum(amount) from bill_new')
                              re=con.fetchall()
                              for j in re:
                                 sal_ent.config(text=f"{j[0]}")  
                              db.commit()

                        def clear():
                            txtarea.delete('3.0',END)
                            st_ent.delete(0,END)
                            ed_ent.delete(0,END)
                            sal_ent.config(text="")
                                
                           
                        
                        def MONTH():
                            db=pymysql.connect(host='localhost',user='harsh424',password='Hk@08052003',database='billing')
                            con=db.cursor()
                            yr=year_ent.get()
                            if month_ent.get() == 'January':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-01-01' and '{yr}-01-31' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-01-01" and "{yr}-01-31" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'February':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-02-01' and '{yr}-02-28' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-02-01" and "{yr}-02-28" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'March':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-03-01' and '{yr}-03-31' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-03-01" and "{yr}-03-31" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                                    
                            elif month_ent.get() == 'April':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-04-01' and '{yr}-04-30' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-04-01" and "{yr}-04-30" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'May':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-05-01' and '{yr}-05-31' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-05-01" and "{yr}-05-31" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'June':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-06-01' and '{yr}-06-30' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-06-01" and "{yr}-06-30" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'July':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-07-01' and '{yr}-07-31' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-07-01" and "{yr}-07-31" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'August':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-08-01' and '{yr}-08-30' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-08-01" and "{yr}-08-31" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'September':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-09-01' and '{yr}-09-31' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-09-01" and "{yr}-09-31" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'October':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-10-01' and '{yr}-10-30' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-10-01" and "{yr}-10-30" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'November':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-11-01' and '{yr}-11-31' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-11-01" and "{yr}-11-31" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                            elif month_ent.get() == 'December':
                                con.execute(f"select * from bill_new where bill_date between '{yr}-12-01' and '{yr}-12-30' ")
                                res=con.fetchall()
                                for i in res:
                                    txtarea.insert(END,f'\n{i[5]}\t\t{i[6]}\t\t{i[3]}\t\t{i[4]}')
                                con.execute(f'select sum(amount) from bill_new where bill_date between "{yr}-12-01" and "{yr}-12-30" ')
                                re=con.fetchall()
                                for j in re:
                                    sal_ent.config(text=f"{j[0]}")
                        f2=Frame(F12,bd=5,relief=GROOVE,bg=bg_color)
                        f2.place(x=30,y=120,height=530,width=400)
                        
                        st=Label(f2,text="Starting Day",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        st.place(x=10,y=30)

                        ed=Label(f2,text="Ending Day",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        ed.place(x=10,y=90)
                        
                        bud=Label(f2,text="Target",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        bud.place(x=10,y=150)

                        bud_ent=Label(f2,text="Rs 10000",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        bud_ent.place(x=150,y=150)

                        sale=Label(f2,text="Sales",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        sale.place(x=10,y=210)

                        sal_ent=Label(f2,text="",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        sal_ent.place(x=150,y=210)

                        month=Label(f2,text="Month",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        month.place(x=10,y=270)
                            
                        mon=['January','Febaury','March','April','May','June','July','August','Septmember','October','November','December']
                        
                        month_ent=ttk.Combobox(f2,values=mon,font=('arial',15,'bold'),height=5,width=17)
                        month_ent.place(x=150,y=270)

                        year=Label(f2,text="Year",font=('arial',15,'bold'),fg='gold',bg=bg_color)
                        year.place(x=10,y=330)
                        
                        yr=[]
                        for t in range(15):
                            y=2019
                            y+=t
                            yr.append(y)
                        
                            
                        year_ent=ttk.Combobox(f2,values=yr,font=('arial',15,'bold'),height=5,width=17)
                        year_ent.place(x=150,y=330)
                        
                        mth_btn=Button(f2,text="Get Monthly Sales",command=MONTH,font=('arial',15,'bold'),bg='white',fg='gold')
                        mth_btn.pack(side=BOTTOM,fill=X)
                        
                        st_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                        st_ent.place(x=150,y=30)

                        ed_ent=Entry(f2,bd=3,relief=GROOVE,font=('arial',15,'bold'))
                        ed_ent.place(x=150,y=90)

                        F13=Frame(F12,bd=5,relief=SUNKEN,height=530,width=700)
                        F13.place(x=490,y=120)
                        
                        scrol_y=Scrollbar(F13,orient=VERTICAL)
                        
                        txtarea=Text(F13,yscrollcommand=scrol_y.set,font=('arial',15,'bold'),fg='red',height=21,width=67)
                        scrol_y.pack(side=RIGHT,fill=Y)
                        scrol_y.config(command=txtarea.yview)
                        txtarea.pack()
                        txtarea.insert('1.0',"Date\t\tTime\t\tQty\t\tAmount")
                        txtarea.insert('2.0',"\n  ")
                        
                        F123=Frame(F12,bd=5,relief=SUNKEN,bg=bg_color)
                        F123.place(x=1300,y=120,height=530,width=190)

                        B3=Button(F123,text="Clear",command=clear,height=2,width=14,font=('arial',15,'bold')).grid(row=1,column=0,pady=15)

                        B4=Button(F123,text="Fetch",command=fetch,height=2,width=14,font=('arial',15,'bold')).grid(row=2,column=0,pady=15)

                        B5=Button(F123,text="Exit",command=F12.destroy,height=2,width=14,font=('arial',15,'bold')).grid(row=3,column=0,pady=15)
                        
                F=Frame(get,bd=5,relief=SUNKEN,bg='white',height=680,width=250)
                F.place(x=960,y=100)
                                                                                                                        
                B1=Button(F,text="Salary",command=salary,font=('arial',20,'bold'),height=2,width=11).grid(row=0,column=0,pady=15)

                B2=Button(F,text="Leave",font=('arial',20,'bold'),height=2,width=11).grid(row=1,column=0,pady=15)

                B3=Button(F,text="Budget",command=budget,font=('arial',20,'bold'),height=2,width=11).grid(row=2,column=0,pady=15)
                break
            elif uname.get() !=un and passwd.get() !=pas:
               continue 
    else:
            mb.showerror("alert","Invalid input")


    
        #===============variables===========================================
F121=Frame(get,bg='white',bd=3,relief=GROOVE,)
F121.place(x=0,y=0,width=1600,height=800)

title_image=ImageTk.PhotoImage(file="billing/login.jpg")
title_lbl=Label(F121,image=title_image).pack(fill=BOTH)
        
title=Label(F121,text="Login Panel",font=('arial',40,'bold'),bg="yellow",bd=10,relief=GROOVE)
title.place(x=0,y=0,relwidth=1)

user_image=ImageTk.PhotoImage(file="billing/hotspot_blue.png")
F131=Frame(F121,bg='white')
F131.place(x=600,y=100)

img=ImageTk.PhotoImage(file="billing/icon.jpg")    
logo_lbl=Label(F131,image=img,compound=TOP,bd=0).grid(row=0,columnspan=2,pady=20)

user=Label(F131,text="Username",image=user_image,font=('arial',15,'bold'),fg='gold',bg='white',compound=LEFT)
user.grid(row=1,column=0,padx=20,pady=10)

passw=Label(F131,text="Password",image=user_image,font=('arial',15,'bold'),fg='gold',compound=LEFT,bg='white')
passw.grid(row=2,column=0,padx=20,pady=10)

user_ent=Entry(F131,textvariable=uname,bd=5,relief=GROOVE,font=("arial",15)).grid(row=1,column=1)
pass_ent=Entry(F131,textvariable=passwd,bd=5,relief=GROOVE,font=("arial",15),show='*').grid(row=2,column=1)

btn_log=Button(F131,text="Login",width=15,command=login,font=('arial',14,'bold'),bg='yellow').grid(row=3,column=1,pady=10)

F213=Frame(F121,bg='white')
F213.place(x=610,y=530)

get.mainloop()
