import os
import pickle
import datetime

details_list=[]
l2=[]
G = []
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
    restart_program()


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)






class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)





import sys

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



class New_Toplevel:

    def __init__(self):
        def check_room():
            self.Text1.configure(font=font10)
            self.rom = str(self.data.get())
            if self.rom.isdigit() == True and len(self.rom) != 0:
                v = int(self.rom)
                f = open("hotel.dat", "rb")
                f1 = open("hote.dat", "ab")
                n = 0
                try:
                    while True:
                        s = pickle.load(f)
                        if s.room_no == v:
                            n = 1
                            name1 = s.name
                            add = s.address
                            mob = s.mobile_no
                            room = str(v)
                            p  = str(s.price)
                            print(" ")
                        else:
                            pickle.dump(s, f1)
                except EOFError:
                    if n == 0:
                        self.Text1.insert(INSERT, "NO GUEST FOUND""\n")

                    elif n == 1:
                        self.Text1.insert(INSERT,"\t\t\t\t*************     ### COMFORT INN ###    ***********\n\t\t\t\t***************   SERVING GUEST SINCE  *************\n\t\t\t\t*****************      ###2000###    ***************")
                        self.Text1.insert(INSERT,"\n\t\t\t\tCHECK OUT TIME:- "+datetime.datetime.now().strftime("%H:%M %p")+"\t\t\t\t\tDt."+datetime.datetime.now().strftime("%d/%m/%Y"))
                        #self.Text1.insert(INSERT,"\n\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        self.Text1.insert(INSERT,"\n\t\t\t\tNAME- "+name1.upper())
                        self.Text1.insert(INSERT,"\n\t\t\t\tADDRESS- "+add.upper())
                        self.Text1.insert(INSERT,"\n\t\t\t\tMOBILE NO.- "+mob)
                        self.Text1.insert(INSERT,"\n\t\t\t\tYOUR TOTAL BILL IS Rs.- "+p)
                        self.Text1.insert(INSERT,"\n\t\t\t\tYOUR ROOM NUMBER IS  "+room)
                        self.Text1.insert(INSERT, "\n\t\t\t               *** THANK YOU " + name1.upper() + " FOR VISTING US ***""\n")
                    pass
                f.close()
                f1.close()
                os.remove("hotel.dat")
                os.rename("hote.dat", "hotel.dat")

            else:
                self.Text1.insert(INSERT, "invalid input please input a valid ROOM NO.""\n")

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
        font13 = "-family {Courier New} -size 15 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 23 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1600x1000")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="dark blue")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="deepskyblue")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)
        self.Frame1.configure(pady=20,padx=20,bd=10)


        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.04, rely=0.0001, relheight=0.15, relwidth=0.91)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="deepskyblue")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(pady=16,padx=16,bd=8)
        self.Frame2.configure(width=995)


        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.0001, height=46, width=442)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="deepskyblue")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="navy")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''CHECK OUT TIME   :''')

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.51, rely=0.0001, height=46, width=442)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="deepskyblue")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="navy")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M %p"))

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.12, height=46, width=442)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="deepskyblue")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="navy")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ENTER THE ROOM NO.   :''')

        self.Entry1 = Entry(self.Frame1)
        self.data=StringVar()
        self.Entry1.place(relx=0.6, rely=0.12,height=54, relwidth=0.15)
        self.Entry1.configure(background="darkturquoise")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font13)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#ffffff")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#e6e6e6")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.data)
        self.Entry1.configure(bd=10)


        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.07, rely=0.54, relheight=0.4, relwidth=0.89)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=824)
        self.Text1.configure(wrap=WORD)
        self.Text1.configure(pady=20,padx=20,bd=10)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.20, rely=0.28, height=93, width=286)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="darkturquoise")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''CHECK OUT''')
        self.Button1.configure(command=check_room)
        self.Button1.configure(pady=20,padx=20,bd=10)


        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.55, rely=0.28, height=93, width=286)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="powder blue")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''BACK''')
        self.Button1.configure(command=root.destroy)
        self.Button1.configure(pady=20,padx=20,bd=10)


        
        root.mainloop()



if __name__ == '__main__':
    out=New_Toplevel()
