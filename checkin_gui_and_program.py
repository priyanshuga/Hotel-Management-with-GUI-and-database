import os
import pickle
import sys
import os
from subprocess import call
import datetime

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
details_list=[]


def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    listq=[str(NAME_PRO),str(ADDRESS_PRO),str(MOBILE_NO_PRO),str(ROOM_NO_PRO),str(PRICE_PRO)]
    myVars = {'A':NAME_PRO,"B":ADDRESS_PRO,"C":MOBILE_NO_PRO,"D":ROOM_NO_PRO,"E":PRICE_PRO }

    fo=open("recipt.txt","w+")
    for h in range(0,5):
        fo.write(listq[h]+"\r\n")
    fo.close()
    call(["python", "recipt.py"])


u = list()
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
m = [9]
G = []
class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO



class HOTEL_MANGMENT_checkin:


    def __init__(self):
        self.NAME=""
        self.ADDERESS=""
        self.MOBILE=""
        self.DAYS=0
        self.price=0
        self.room=0





        def chk_name():
            self.Text1.configure(font=font17)
            while True:

                self.k = str(self.name.get())

                a = self.k.isdigit()
                if len(self.k) != 0 and a != True:
                    self.NAME=self.k
                    self.Text1.insert(INSERT, "Name accepted""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "Invalid input please input a valid name""\n")

                    break

        def chk_add():
            self.Text1.configure(font=font17)
            while True:
                self.g = str(self.addr.get())


                ak = self.g.isdigit()
                if len(self.g)!= 0 and ak!=True:
                    self.ADDERESS=self.g
                    self.Text1.insert(INSERT, "Address accepted""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "Invalid input please input a valid address""\n")

                    break

        def chk_mo():
            self.Text1.configure(font=font17)
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.MOBILE = self.h
                    self.Text1.insert(INSERT, "Mobile number accepted""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "Invalid input please input a valid mobile number""\n")
                break

        def chk_day():
            self.Text1.configure(font=font17)
            while True:

                self.l = str(self.days.get())

                if self.l.isdigit() == True and len(self.l) != 0:
                    self.DAYS = int(self.l)
                    self.Text1.insert(INSERT, "Days accepted""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "Invalid input ""\n")
                    break

        def enter(self):
            self.name = self.NAME
            self.address = self.ADDERESS
            self.mobile_no = self.MOBILE
            self.no_of_days = int(self.DAYS)

        def tor(self):

            if self.ch == 1:
                self.price = self.price + (2000 * self.no_of_days)
                m[0] = 1
            elif self.ch == 2:
                self.price = self.price + (1500 * self.no_of_days)
                m[0] = 2
            elif self.ch == 3:
                self.price = self.price + (1000 * self.no_of_days)
                m[0] = 3
            elif self.ch == 4:
                self.price = self.price + (1700 * self.no_of_days)
                m[0] = 4

        def payment_option(self):
            op = self.p
            if op == 1:
                self.Text1.insert(INSERT, "no discount""\n")
            elif op == 2:
                self.price = self.price - ((self.price * 10) / 100)
                self.Text1.insert(INSERT, "10% discount""\n")

        def bill(self):

            if m[0] == 1:
                a = Delux
            elif m[0] == 2:
                a = Semi_Delux
            elif m[0] == 3:
                a = General
            elif m[0] == 4:
                a = Joint_Room

            G = []
            f2 = open("hotel.dat", "rb")
            try:
                while True:
                    s = pickle.load(f2)

                    k = s.room_no
                    G.append(k)
                    continue

            except EOFError:
                pass

            for r in a:
                if r not in G:
                    self.room = r
                    break
                else:
                    continue
            self.room = r
            f2.close()

            details_list.append(self.name)
            details_list.append(self.address)
            details_list.append(self.mobile_no)
            details_list.append(self.room)
            details_list.append(self.price)




            file_save()



        def submit_clicked():
            if self.var1.get()==1 and self.var2.get()==0 and self.var3.get()==0 and self.var4.get()==0 and self.var5.get()==1 and self.var6.get()==0:
                self.ch=1
                self.p=2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)


            elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 1
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 2
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() ==0 :
                self.ch = 2
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 3
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() == 0:
                self.ch = 3
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)

            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 4
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 1 and self.var6.get() == 0:
                self.ch = 4
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)

            else:
                self.Text1.insert(INSERT, "invalid choice please input a valid choice""\n")


        root = Tk()


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font17 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1600x1000")
        root.title("HOTEL MANGMENT")
        root.configure(background="Dark blue")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        self.Text1 = Text(root)
        self.Text1.place(relx=0.03, rely=0.73, relheight=0.19, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(pady=16,padx=16,bd=8)
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.02, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="deepskyblue")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(pady=16,padx=16,bd=8)
        self.Frame1.configure(width=995)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.05, rely=0.12,relheight=0.9)
        self.Message1.configure(background="deepskyblue")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="navy")
        self.Message1.configure(highlightbackground="#ffffff")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''CHECK IN TIME''')
        self.Message1.configure(width=496)

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.41, rely=0.01,relheight=0.9)
        self.Message2.configure(background="deepskyblue")
        self.Message2.configure(font=font11)
        self.Message2.configure(foreground="navy")
        self.Message2.configure(highlightbackground="#ffffff")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text=''':''')
        self.Message2.configure(width=66)

        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.5, rely=0.11,relheight=0.9)
        self.Message3.configure(background="deepskyblue")
        self.Message3.configure(font=font11)
        self.Message3.configure(foreground="navy")
        self.Message3.configure(highlightbackground="#ffffff")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M %p"))
        self.Message3.configure(width=900)

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.13, relheight=0.60, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(background="deepskyblue")
        self.Frame2.configure(pady=16,padx=16,bd=8)
        self.Frame2.configure(width=1000)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.05, rely=0.03)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="deepskyblue")
        self.Label3.configure(disabledforeground="#bfbfbf")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#ffffff")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''ENTER YOUR NAME''')

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.05, rely=0.29)
        self.Label4.configure(activebackground="#ffffff")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="deepskyblue")
        self.Label4.configure(disabledforeground="#bfbfbf")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#ffffff")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''ENTER YOUR NUMBER''')



        self.Entry3 = Entry(self.Frame2)
        self.name=StringVar()
        self.Entry3.place(relx=0.47, rely=0.05,height=34, relwidth=0.43)
        self.Entry3.configure(background="darkturquoise")
        self.Entry3.configure(disabledforeground="#bfbfbf")
        self.Entry3.configure(font=font16)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#ffffff")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#e6e6e6")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(textvariable=self.name)
        self.Entry3.configure(bd=8)
        
        self.Entry4 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry4.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
        self.Entry4.configure(background="darkturquoise")
        self.Entry4.configure(disabledforeground="#bfbfbf")
        self.Entry4.configure(font=font16)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#ffffff")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#e6e6e6")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.configure(textvariable=self.mobile)
        self.Entry4.configure(bd=8)


        self.Entry5 = Entry(self.Frame2)
        self.addr = StringVar()
        self.Entry5.place(relx=0.47, rely=0.18,height=34, relwidth=0.43)
        self.Entry5.configure(background="powder blue")
        self.Entry5.configure(disabledforeground="#bfbfbf")
        self.Entry5.configure(font=font16)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#ffffff")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#e6e6e6")
        self.Entry5.configure(selectforeground="black")
        self.Entry5.configure(textvariable=self.addr)
        self.Entry5.configure(bd=8)

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.05, rely=0.16)
        self.Label5.configure(activebackground="#ffffff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="deepskyblue")
        self.Label5.configure(disabledforeground="#bfbfbf")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#ffffff")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''ENTER YOUR ADDRESS''')

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.05, rely=0.43)
        self.Label1.configure(background="deepskyblue")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''NUMBER OF DAYS''')


        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.28, rely=0.52)
        self.Label6.configure(activebackground="#ffffff")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="deepskyblue")
        self.Label6.configure(disabledforeground="#bfbfbf")
        self.Label6.configure(font=font13)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#ffffff")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''CHOOSE YOUR ROOM''')

        self.Message4 = Message(self.Frame2)
        self.Message4.place(relx=0.41, rely=0.04)
        self.Message4.configure(background="deepskyblue")
        self.Message4.configure(font=font13)
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#ffffff")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(text=''':''')
        self.Message4.configure(width=46)

        self.Message5 = Message(self.Frame2)
        self.Message5.place(relx=0.41, rely=0.17)
        self.Message5.configure(background="deepskyblue")
        self.Message5.configure(font=font13)
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#ffffff")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(text=''':''')
        self.Message5.configure(width=26)

        self.Message6 = Message(self.Frame2)
        self.Message6.place(relx=0.41, rely=0.3)
        self.Message6.configure(background="deepskyblue")
        self.Message6.configure(font=font13)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#ffffff")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text=''':''')
        self.Message6.configure(width=36)

        self.Message8 = Message(self.Frame2)
        self.Message8.place(relx=0.41, rely=0.41)
        self.Message8.configure(background="deepskyblue")
        self.Message8.configure(font=font13)
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#ffffff")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(text=''':''')


        self.Checkbutton1 = Checkbutton(self.Frame2)
        self.var1 = IntVar()
        self.Checkbutton1.place(relx=0.15, rely=0.62)
        self.Checkbutton1.configure(activebackground="#ffffff")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="deepskyblue")
        self.Checkbutton1.configure(disabledforeground="#bfbfbf")
        self.Checkbutton1.configure(font=font13)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#ffffff")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''DELUXE(Rs.2000)''')
        self.Checkbutton1.configure(variable=self.var1)





        self.Checkbutton2 = Checkbutton(self.Frame2)
        self.var2 = IntVar()
        self.Checkbutton2.place(relx=0.15, rely=0.75)
        self.Checkbutton2.configure(activebackground="#ffffff")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="deepskyblue")
        self.Checkbutton2.configure(disabledforeground="#bfbfbf")
        self.Checkbutton2.configure(font=font13)
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#ffffff")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''SEMI DELUXE(Rs.1500)''')
        self.Checkbutton2.configure(variable=self.var2)

        self.Checkbutton3 = Checkbutton(self.Frame2)
        self.var3 = IntVar()
        self.Checkbutton3.place(relx=0.5, rely=0.62)
        self.Checkbutton3.configure(activebackground="#ffffff")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="deepskyblue")
        self.Checkbutton3.configure(disabledforeground="#bfbfbf")
        self.Checkbutton3.configure(font=font13)
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#ffffff")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''GENERAL(Rs1000)''')
        self.Checkbutton3.configure(variable=self.var3)

        self.Checkbutton4 = Checkbutton(self.Frame2)
        self.var4 = IntVar()
        self.Checkbutton4.place(relx=0.5, rely=0.75)
        self.Checkbutton4.configure(activebackground="#ffffff")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(background="deepskyblue")
        self.Checkbutton4.configure(disabledforeground="#bfbfbf")
        self.Checkbutton4.configure(font=font13)
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#ffffff")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text='''JOINT(Rs.1700)''')
        self.Checkbutton4.configure(variable=self.var4)

        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0.28, rely=0.85)
        self.Label7.configure(activebackground="#ffffff")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="deepskyblue")
        self.Label7.configure(disabledforeground="#bfbfbf")
        self.Label7.configure(font=font14)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#ffffff")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''CHOOSE PAYMENT METHOD''')

        self.Checkbutton5 = Checkbutton(self.Frame2)
        self.var5 = IntVar()
        self.Checkbutton5.place(relx=0.498, rely=0.93)
        self.Checkbutton5.configure(activebackground="#ffffff")
        self.Checkbutton5.configure(activeforeground="#000000")
        self.Checkbutton5.configure(background="deepskyblue")
        self.Checkbutton5.configure(disabledforeground="#bfbfbf")
        self.Checkbutton5.configure(font=font16)
        self.Checkbutton5.configure(foreground="#000000")
        self.Checkbutton5.configure(highlightbackground="#ffffff")
        self.Checkbutton5.configure(highlightcolor="black")
        self.Checkbutton5.configure(justify=LEFT)
        self.Checkbutton5.configure(text='''BY CARD(10% Discount)''')
        self.Checkbutton5.configure(variable=self.var5)

        self.Checkbutton6 = Checkbutton(self.Frame2)
        self.var6 = IntVar()
        self.Checkbutton6.place(relx=0.152, rely=0.93)
        self.Checkbutton6.configure(activebackground="#ffffff")
        self.Checkbutton6.configure(activeforeground="#000000")
        self.Checkbutton6.configure(background="deepskyblue")
        self.Checkbutton6.configure(disabledforeground="#bfbfbf")
        self.Checkbutton6.configure(font=font16)
        self.Checkbutton6.configure(foreground="#000000")
        self.Checkbutton6.configure(highlightbackground="#ffffff")
        self.Checkbutton6.configure(highlightcolor="black")
        self.Checkbutton6.configure(justify=LEFT)
        self.Checkbutton6.configure(text='''BY CASH''')
        self.Checkbutton6.configure(variable=self.var6)

        """self.Message7 = Message(self.Frame2)
        self.Message7.place(relx=0.28, rely=0.46, relheight=0.11, relwidth=0.04)
        self.Message7.configure(background="#ffffff")
        self.Message7.configure(font=font15)
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#ffffff")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(text='''-''')
        self.Message7.configure(width=41)"""

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.05,height=33, width=43)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="powder blue")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(command=chk_name)
        self.Button1.configure(pady=20,padx=20,bd=10)

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.18, height=33, width=43)
        self.Button2.configure(activebackground="#ffffff")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="darkturquoise")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#ffffff")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')
        self.Button2.configure(command=chk_add)
        self.Button2.configure(pady=20,padx=20,bd=10)

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.91, rely=0.31, height=33, width=43)
        self.Button3.configure(activebackground="#ffffff")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="powder blue")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#ffffff")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''OK''')
        self.Button3.configure(command=chk_mo)
        self.Button3.configure(pady=20,padx=20,bd=10)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.72, rely=0.66, height=83, width=156)
        self.Button4.configure(activebackground="#ffffff")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="darkturquoise")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font16)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#ffffff")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''SUBMIT''')
        self.Button4.configure(command=submit_clicked)
        self.Button4.configure(pady=20,padx=20,bd=10)

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.87, rely=0.66, height=83, width=156)
        self.Button5.configure(activebackground="#ffffff")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="powder blue")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font16)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#ffffff")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(text='''EXIT''')
        self.Button5.configure(command=root.destroy)
        self.Button5.configure(pady=20,padx=20,bd=10)


        self.Entry1 = Entry(self.Frame2)
        self.days=StringVar()
        self.Entry1.place(relx=0.47, rely=0.43, height=34, relwidth=0.43)
        self.Entry1.configure(background="powder blue")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font16)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=424)
        self.Entry1.configure(textvariable=self.days)
        self.Entry1.configure(bd=8)


        self.Button6 = Button(self.Frame2)
        self.Button6.place(relx=0.91, rely=0.43, height=33, width=43)
        self.Button6.configure(activebackground="#ffffff")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="darkturquoise")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#ffffff")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(text='''OK''')
        self.Button6.configure(command=chk_day)
        self.Button6.configure(pady=20,padx=20,bd=10)


        root.mainloop()


if __name__ == '__main__':
    hotel=HOTEL_MANGMENT_checkin()






