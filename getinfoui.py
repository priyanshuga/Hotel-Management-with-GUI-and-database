import os
import pickle

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


class HOTEL_MANAGEMENT:
    def __init__(self):
        def gotinfo():
            self.gettininfo = str(self.gather.get())
            self.Text1.configure(font=font10)
            self.Text1.configure(foreground="dark blue")
            if self.gettininfo.isdigit() == True:
                self.Text1.insert(INSERT, " Valid room number ""\n")
            else :
                self.Text1.insert(INSERT,"invalid room number""\n")
            try:
                n = 0
                f2 = open("hotel.dat", "rb")
                while True:
                    s = pickle.load(f2)
                    a = str(s.room_no)
                    if self.gettininfo == a:
                        n = 1
                        self.Text1.insert(INSERT,"\n")
                        self.Text1.insert(INSERT,"NAME-", "\t",s.name.upper())
                        self.Text1.insert(INSERT,"\n")
                        self.Text1.insert(INSERT,"ADDRESS-", "\t", s.address.upper())
                        self.Text1.insert(INSERT,"\n")
                        self.Text1.insert(INSERT,"MOBILE NO.-", "\t", s.mobile_no)
                        self.Text1.insert(INSERT,"\n")
                        self.Text1.insert(INSERT,"TOTAL BILL IS Rs.", "\t", s.price)
                    elif EOFError:
                        self.Text1.insert(INSERT,"  ")
                       
            except EOFError:
                pass
            f2.close()


        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 28 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 23 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        root.geometry("1600x1000")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="Dark blue")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="deepskyblue")
        self.Frame1.configure(width=825)
        self.Frame1.configure(pady=20,padx=20,bd=10)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=764)
        self.Text1.configure(wrap=WORD)
        self.Text1.configure(pady=20,padx=20,bd=10)



        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.12, rely=0.16, height=48, width=377)
        self.Label1.configure(background="deepskyblue")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="navy")
        self.Label1.configure(text='''ENTER THE ROOM NO.   :''')

        self.Entry1 = Entry(self.Frame1)
        self.gather=StringVar()
        self.Entry1.place(relx=0.65, rely=0.17,height=45, relwidth=0.20)
        self.Entry1.configure(background="darkturquoise")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font9)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=84)
        self.Entry1.configure(bd=10)
        self.Entry1.configure(textvariable=self.gather)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.25, rely=0.29, height=74, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="darkturquoise")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady=20,padx=20,bd=10)
        self.Button1.configure(text='''SUBMIT''')
        self.Button1.configure(width=197)
        self.Button1.configure(command=gotinfo)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.55, rely=0.29, height=74, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="powder blue")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady=20,padx=20,bd=10)
        self.Button1.configure(text='''BACK''')
        self.Button1.configure(width=197)
        self.Button1.configure(command=root.destroy)

        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.02, rely=0.0001, relheight=0.15, relwidth=0.94)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="deepskyblue")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(pady=16,padx=16,bd=8)
        self.Frame2.configure(width=995)

        self.Message1 = Message(self.Frame2)
        self.Message1.place(relx=0.2, rely=0.3, relheight=0.55, relwidth=0.56)
        self.Message1.configure(background="deepskyblue")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="navy")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''GET INFO HERE ..!!''')
        self.Message1.configure(width=460)
        root.mainloop()






if __name__ == '__main__':
    GETINFO=HOTEL_MANAGEMENT()
