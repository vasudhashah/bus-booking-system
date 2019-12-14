from tkinter import *
import mysql.connector
import datetime
from tkinter import messagebox

def fun_t():
    root = Tk()
    root.geometry("1600x900")

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="panda")
    photo = PhotoImage(file="knv.png")
    photo1 = photo.subsample(3, 4)
    lb1 = Label(root, image=photo1).place(x=60, y=5)

    lb2 = Label(root, text=' GHAR-JANA TRAVELS', bg="#470938", padx=70, pady=10, fg="white",
                font="Verdana 30 bold").place(x=400, y=25)
    lb_big = Label(root,  bg="#470938", padx=200, pady=280, fg="white",
                font="Verdana 30 bold").place(x=850, y=155)
    customer_id=StringVar()
    seat_no = StringVar()
    name = StringVar()
    contact = StringVar()
    dep_time = StringVar()
    drop_time = StringVar()
    amount = StringVar()
    fromm_d=StringVar(root)
    to_d = StringVar(root)
    gender_d=StringVar(root)
    day_d=StringVar(root)
    #-----------------------------------------------------------------------------------------------
    from_list={'PUNE','AHMEDNAGAR','AURANGABAD','JALGAON','BHUSAWAL','BURHANPUR'}
    gender_list={'M','F','O'}
    day_list={'SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY'}
    fromm_d.set('SELECT CITY')
    to_d.set('SELECT CITY')
    gender_d.set('SELECT GENDER')
    day_d.set('SELECT DAY')
    popupMenu=OptionMenu(root,fromm_d,*from_list).place(x=280,y=180)
    popupMenu2= OptionMenu(root, to_d, *from_list).place(x=280, y=230)
    popupMenu3=OptionMenu(root, gender_d, *gender_list).place(x=280, y=630)
    popupMenu4= OptionMenu(root, day_d, *day_list).place(x=280, y=280)
    #-------------------------------------------------------------------------------------------------------
    def onclick_b1():
        seat_no.set(1)
    def onclick_b2():
        seat_no.set(2)
    def onclick_b3():
        seat_no.set(3)
    def onclick_b4():
        seat_no.set(4)
    def onclick_b5():
        seat_no.set(5)
    def onclick_b6():
        seat_no.set(6)
    def onclick_b7():
        seat_no.set(7)
    def onclick_b8():
        seat_no.set(8)
    def onclick_b9():
        seat_no.set(9)
    def onclick_b10():
        seat_no.set(10)
    def onclick_b11():
        seat_no.set(11)
    def onclick_b12():
        seat_no.set(12)
    def onclick_b13():
        seat_no.set(13)
    def onclick_b14():
        seat_no.set(14)
    def onclick_b15():
        seat_no.set(15)
    def onclick_b16():
        seat_no.set(16)
    def onclick_b17():
        seat_no.set(17)
    def onclick_b18():
        seat_no.set(18)
    def onclick_b19():
        seat_no.set(19)
    def onclick_b20():
        seat_no.set(20)
    def onclick_b21():
        seat_no.set(21)
    def onclick_b22():
        seat_no.set(22)
    def onclick_b23():
        seat_no.set(23)
    def onclick_b24():
        seat_no.set(24)
    def fix(day):
        v=[onclick_b1,onclick_b2,onclick_b3,onclick_b4,onclick_b5,onclick_b6,onclick_b7,onclick_b8,onclick_b9,onclick_b10,onclick_b11,onclick_b12,onclick_b13,onclick_b14,onclick_b15,onclick_b16,onclick_b17,onclick_b18,onclick_b19,onclick_b20,onclick_b21,onclick_b22,onclick_b23,onclick_b24]
        l=[b_s1,b_s2,b_s3,b_s4,b_s5,b_s6,b_s7,b_s8,b_s9,b_s10,b_s11,b_s11,b_s12,b_s13,b_s14,b_s15,b_s16,b_s17,b_s18,b_s19,b_s20,b_s21,b_s22,b_s23,b_s24]
        x_list = [875, 950, 1100, 1175, 875, 950, 1100, 1175, 875, 950, 1100, 1175, 875, 950, 1100, 1175, 875, 950,
                  1100, 1175, 875, 950, 1100, 1175]
        y_list = [180, 180, 180, 180, 280, 280, 280, 280, 380, 380, 380, 380, 480, 480, 480, 480, 580, 580, 580, 580,
                  680, 680, 680, 680]
        for j in range(0,24):
            l[j]=Button(root, bg="white",text=""+str(j+1), padx=15, pady=20,fg="black", font="Verdana 10 bold",state=NORMAL,command=v[j]).place(x=x_list[j], y=y_list[j])

        mycursor = mydb.cursor()
        mycursor.execute("use vsdbms")
        sql = "select seat_no from customer where date_j=%s"
        val=[day]
        mycursor.execute(sql,val)
        result = mycursor.fetchall()
        for i in result:
            l[i[0]-1]=Button(root, bg="#e6a400", padx=20, pady=20,font="Verdana 10 bold",state=DISABLED).place(x=x_list[i[0] - 1], y=y_list[i[0] - 1])

        mycursor.close()
    #----------------------------------------------------------------------------------------------------------------
    def b_allclr_f():
        mycursor = mydb.cursor()
        mycursor.execute("use vsdbms")
        sql="insert into journey_comp select * from customer"
        mycursor.execute(sql)
        sql1 = "truncate table customer"
        mycursor.execute(sql1)
        mycursor.close()
        messagebox.showinfo("Successful Completion","Data transfered to journey completed table")
    #------------------------------------------------------------------------------------------------------------------
    def b_new_f():
        mycursor = mydb.cursor()
        mycursor.execute("use vsdbms")
        seat_no.set("")
        name.set("")
        contact.set("")
        dep_time.set("")
        drop_time.set("")
        amount.set("")
        day_d.set('SELECT DAY')
        fromm_d.set('SELECT CITY')
        to_d.set('SELECT CITY')
        gender_d.set('SELECT GENDER')
        fix("koinhi")
    #---------------------------------------------------------------------------------------------------------------
    def b_book_f():
        if  (seat_no.get()!="") &(name.get()!="")&(contact.get()!="")&(gender_d.get()!='SELECT GENDER')&(day_d.get()!='SELECT DAY')&(fromm_d.get()!='SELECT CITY')&(to_d.get()!='SELECT CITY')&(amount.get()!=""):
            mycursor = mydb.cursor()
            mycursor.execute("use vsdbms")
            sql = "insert into customer(seat_no,name,mobile,gender,date_j,start,end,rate) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            val = [seat_no.get(), name.get(), contact.get(), gender_d.get(), day_d.get(), fromm_d.get(), to_d.get(),
                   amount.get()]
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()
            mycursor=mydb.cursor()
            mycursor.execute("use vsdbms")
            sql1="select cus_no from customer where name=%s and mobile=%s"
            val1=[name.get(),contact.get()]
            mycursor.execute(sql1, val1)
            result=mycursor.fetchall()
            messagebox.showinfo("TICKET CONFIRMED!",
                                "Your ticket has been confirmed ,your customer_id is "+str(result[0][0])+" you will shortly recieve message on your contact number")
            mydb.commit()
            mycursor.close()
            b_new_f()
        else:
            messagebox.showinfo("ERROR","Please provide all the information")



        '''
        val = [int(seat_no.get()), name.get(), contact.get(), gender_d.get(), fromm_d.get(), to_d.get(), dep_time.get(),
               drop_time.get(), amount.get()]
        print(val)'''
    #----------------------------------------------------------------------------------------------------------------
    def b_ok_f():
        try:
            if (fromm_d.get() != 'SELECT CITY') & (to_d.get() != 'SELECT CITY') & (day_d.get() != 'SELECT DAY'):
                mycursor = mydb.cursor()
                mycursor.execute("use vsdbms")
                sql = "select s_time,e_time,rate from journey where start=%s and end=%s"
                val = [fromm_d.get(), to_d.get()]
                mycursor.execute(sql, val)
                result = mycursor.fetchall()
                dep_time.set(result[0][0])
                drop_time.set(result[0][1])
                amount.set(result[0][2])
                fix(day_d.get())
                mycursor.close()

            else:
                messagebox.showinfo("ERROR", "PLEASE ENTER FROM, TO AND DAY OF JOURNEY")

        except:
            messagebox.showinfo("NO ROUTE FOUND","Route Available only for "
                                                "PUNE---->AHMEDNAGAR---->AURANGABAD---->JALGAON------->BHUSAWAL--->BURHANPUR")

    #----------------------------------------------------------------------------------------------------------
    def b_cancel_f():
        if (customer_id.get()!=""):
            mycursor = mydb.cursor()
            mycursor.execute("use vsdbms")
            sql="delete from customer where cus_no=%s"
            val=[customer_id.get(),]
            #print(val)
            mycursor.execute(sql,val)
            mydb.commit()

            messagebox.showinfo("Ticket cancelled", "Ticket canceled successfully")
            mycursor.close()
            b_new_f()




    b_ok = Button(root, bg="#470938", text="ok", fg="white", padx=20, pady=10, font="Verdana 15 bold",
                   command=b_ok_f).place(x=480, y=220)
    b_new= Button(root, bg="#470938",text="NEW",fg="white", padx=20, pady=10, font="Verdana 15 bold",command=b_new_f).place(x=100, y=700)
    b_allclr = Button(root, bg="#470938", text="ALL CLEAR", fg="white", padx=20, pady=10, font="Verdana 15 bold",command=b_allclr_f).place(x=280,
                                                                                                               y=700)
    b_book = Button(root, bg="#470938", text="BOOK", fg="white", padx=20, pady=10, font="Verdana 15 bold",command=b_book_f).place(x=520,y=700)
    b_cancel=Button(root, bg="#470938", text="CANCEL", fg="white", padx=20, pady=10, font="Verdana 15 bold",
                   command=b_cancel_f).place(x=680, y=700)
    b_s1 = Button(root, bg="white", padx=15, pady=20,text=1,fg="black", font="Verdana 10 bold",command=onclick_b1).place(x=875, y=180)
    b_s2 = Button(root, bg="white", padx=15, pady=20,text=2,fg="black", font="Verdana 10 bold",command=onclick_b2).place(x=950, y=180)
    b_s3= Button(root, bg="white", padx=15, pady=20, text=3,fg="black",font="Verdana 10 bold",command=onclick_b3).place(x=1100, y=180)
    b_s4 = Button(root, bg="white", padx=15, pady=20,text=4,fg="black", font="Verdana 10 bold",command=onclick_b4).place(x=1175, y=180)

    b_s5 = Button(root, bg="white", padx=15, pady=20,text=5,fg="black", font="Verdana 10 bold",command=onclick_b5).place(x=875, y=280)
    b_s6 = Button(root, bg="white", padx=15, pady=20,text=6,fg="black", font="Verdana 10 bold",command=onclick_b6).place(x=950, y=280)
    b_s7 = Button(root, bg="white", padx=15, pady=20,text=7,fg="black", font="Verdana 10 bold",command=onclick_b7).place(x=1100, y=280)
    b_s8 = Button(root, bg="white", padx=15, pady=20,text=8,fg="black", font="Verdana 10 bold",command=onclick_b8).place(x=1175, y=280)

    b_s9 = Button(root, bg="white", padx=15, pady=20,text=9,fg="black", font="Verdana 10 bold",command=onclick_b9).place(x=875, y=380)
    b_s10 = Button(root, bg="white", padx=10, pady=20,text=10,fg="black", font="Verdana 10 bold",command=onclick_b10).place(x=950, y=380)
    b_s11 = Button(root, bg="white", padx=10, pady=20,text=11,fg="black", font="Verdana 10 bold",command=onclick_b11).place(x=1100, y=380)
    b_s12 = Button(root, bg="white", padx=10, pady=20,text=12,fg="black", font="Verdana 10 bold",command=onclick_b12).place(x=1175, y=380)

    b_s13 = Button(root, bg="white", padx=10, pady=20,text=13,fg="black", font="Verdana 10 bold",command=onclick_b13).place(x=875, y=480)
    b_s14 = Button(root, bg="white", padx=10, pady=20,text=14,fg="black", font="Verdana 10 bold",command=onclick_b14).place(x=950, y=480)
    b_s15= Button(root, bg="white", padx=10, pady=20,text=15,fg="black", font="Verdana 10 bold",command=onclick_b15).place(x=1100, y=480)
    b_s16= Button(root, bg="white", padx=10, pady=20,text=16,fg="black", font="Verdana 10 bold",command=onclick_b16).place(x=1175, y=480)

    b_s17= Button(root, bg="white", padx=10, pady=20,text=17,fg="black", font="Verdana 10 bold",command=onclick_b17).place(x=875, y=580)
    b_s18= Button(root, bg="white", padx=10, pady=20,text=18,fg="black", font="Verdana 10 bold",command=onclick_b18).place(x=950, y=580)
    b_s19= Button(root, bg="white", padx=10, pady=20,text=19,fg="black", font="Verdana 10 bold",command=onclick_b19).place(x=1100, y=580)
    b_s20= Button(root, bg="white", padx=10, pady=20,text=20,fg="black", font="Verdana 10 bold",command=onclick_b20).place(x=1175, y=580)

    b_s21 = Button(root, bg="white", padx=10, pady=20,text=21,fg="black", font="Verdana 10 bold",command=onclick_b21).place(x=875, y=680)
    b_s22 = Button(root, bg="white", padx=10, pady=20,text=22,fg="black", font="Verdana 10 bold",command=onclick_b22).place(x=950, y=680)
    #b_s23 = Button(root, bg="white", padx=20, pady=20, font="Verdana 10 bold").place(x=1025, y=680)
    b_s23 = Button(root, bg="white", padx=10, pady=20,text=23,fg="black", font="Verdana 10 bold",command=onclick_b23).place(x=1100, y=680)
    b_s24 = Button(root, bg="white", padx=10, pady=20,text=24,fg="black", font="Verdana 10 bold",command=onclick_b24).place(x=1175, y=680)

    today = datetime.date.today()
    lb3 = Label(root, text=today, font="Verdana 17 bold").place(x=1200, y=50)
    lb4 = Label(root, text="SEAT NO. :", font="Verdana 17 bold",fg="#470938").place(x=100, y=480)
    lb12 = Label(root, text="DROP TIME :", font="Verdana 17 bold", fg="#470938").place(x=100, y=380)
    lb13 = Label(root, text="AMOUNT :", font="Verdana 17 bold", fg="#470938").place(x=100, y=430)
    lb7 = Label(root, text="GENDER :", font="Verdana 17 bold", fg="#470938").place(x=100, y=630)
    lb8 = Label(root, text="FROM :", font="Verdana 17 bold", fg="#470938").place(x=100, y=180)
    lb9 = Label(root, text="TO :", font="Verdana 17 bold", fg="#470938").place(x=100, y=230)
    lb10 = Label(root, text="JOURNEY DAY:", font="Verdana 15 bold", fg="#470938").place(x=100, y=280)
    lb11 = Label(root, text="DEP.TIME :", font="Verdana 17 bold", fg="#470938").place(x=100, y=330)
    lb5 = Label(root, text="NAME :", font="Verdana 17 bold", fg="#470938").place(x=100, y=530)
    lb6 = Label(root, text="CONTACT :", font="Verdana 17 bold", fg="#470938").place(x=100, y=580)
    lb14=Label(root, text="Customer_id :", font="Verdana 15 bold", fg="#470938").place(x=100, y=130)
    e1 = Entry(root, width=18, font="Verdana 17 bold", textvariable=seat_no,state="disabled").place(x=280, y=480)
    e2 = Entry(root, width=18, font="Verdana 17 bold", textvariable=name).place(x=280, y=530)
    e3 = Entry(root, width=18, font="Verdana 17 bold", textvariable=contact).place(x=280, y=580)
    e8 = Entry(root, width=18, font="Verdana 17 bold", textvariable=dep_time,state="disabled").place(x=280, y=330)
    e9 = Entry(root, width=18, font="Verdana 17 bold", textvariable=drop_time,state="disabled").place(x=280, y=380)
    e10 = Entry(root, width=18, font="Verdana 17 bold", textvariable=amount,state="disabled").place(x=280, y=430)
    e4= Entry(root, width=18, font="Verdana 17 bold", textvariable=customer_id).place(x=280, y=130)
    root.mainloop()

fun_t()

