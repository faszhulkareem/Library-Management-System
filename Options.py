
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
from Add_book import *
from Borrow_book import *
from Return_book import *


def add_book():
    addBook = Tk()
    application = Add_book(addBook)
    addBook.mainloop()


def borrow_book():
    borrowBook = Tk()
    application = Borrow_book(borrowBook)
    borrowBook.mainloop()


def return_book():
    returnBook = Tk()
    application = Return_book(returnBook)
    returnBook.mainloop()


class Options_Portal:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI Black} -size 16 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family Arial -size 17 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("962x609+300+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title('select any option')
        top.configure(background="#d9d9d9")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.001)
        self.Canvas1.configure(background="#efefed")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Labelframe1 = tk.LabelFrame(self.Canvas1)
        self.Labelframe1.place(relx=0.249, rely=0.394,
                               relheight=0.452, relwidth=0.55)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font=font9)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Select Any Option''')
        self.Labelframe1.configure(background="#efefed")

        self.Button1 = tk.Button(self.Labelframe1)
        self.Button1.place(relx=0.321, rely=0.218, height=33,
                           width=200, bordermode='ignore')
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Book''')
        self.Button1.configure(command=add_book)

        self.Button2 = tk.Button(self.Labelframe1)
        self.Button2.place(relx=0.321, rely=0.473, height=33,
                           width=200, bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Borrow Book''')
        self.Button2.configure(command=borrow_book)

        self.Button3 = tk.Button(self.Labelframe1)
        self.Button3.place(relx=0.321, rely=0.727, height=33,
                           width=200, bordermode='ignore')
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Return Book''')
        self.Button3.configure(command=return_book)

        self.Label1 = tk.Label(self.Canvas1)
        self.Label1.place(relx=0.291, rely=0.049, height=43, width=428)
        self.Label1.configure(background="#efefed")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''KCG COLLEGE OF TECHNOLOGY''')

        self.Label2 = tk.Label(self.Canvas1)
        self.Label2.place(relx=0.26, rely=0.181, height=80, width=500)
        self.Label2.configure(background="#efefed")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font13)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(
            text='''Department Of Information Technology\n\nLibrary Management System''')
