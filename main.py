from tkinter import *
from tkinter.ttk import Button

win = Tk()
win.title("Сal3")

lblstr = "0"


lbl = Label(win, text=lblstr, font=("Arial Bont", 40))
lbl.grid(column=0, row=0)

def seven():
    global lblstr
    lblstr += "7"
    lbl.configure(text=lblstr)

def eight():
    global lblstr
    lblstr += "8"
    lbl.configure(text=lblstr)

def nine():
    global lblstr
    lblstr += "9"
    lbl.configure(text=lblstr)

def four():
    global lblstr
    lblstr += "4"
    lbl.configure(text=lblstr)

def five():
    global lblstr
    lblstr += "5"
    lbl.configure(text=lblstr)

def six():
    global lblstr
    lblstr += "6"
    lbl.configure(text=lblstr)

def one():
    global lblstr
    lblstr += "1"
    lbl.configure(text=lblstr)

def two():
    global lblstr
    lblstr += "2"
    lbl.configure(text=lblstr)

def three():
    global lblstr
    lblstr += "3"
    lbl.configure(text=lblstr)

def zero():
    global lblstr
    lblstr += "0"
    lbl.configure(text=lblstr)


bt7 = Button(win, text="7", command=seven)
bt7.grid(column=0, row=3)

bt8 = Button(win, text="8", command=eight)
bt8.grid(column=1, row=3)

bt9 = Button(win, text="9", command=nine)
bt9.grid(column=2, row=3)


bt4 = Button(win, text="4", command=four)
bt4.grid(column=0, row=4)

bt5 = Button(win, text="5", command=five)
bt5.grid(column=1, row=4)

bt6 = Button(win, text="6", command=six)
bt6.grid(column=2, row=4)


bt1 = Button(win, text="1", command=one)
bt1.grid(column=0, row=5)

bt2 = Button(win, text="2", command=two)
bt2.grid(column=1, row=5)

bt3 = Button(win, text="3", command=three)
bt3.grid(column=2, row=5)


bt0 = Button(win, text="0", command=zero)
bt0.grid(column=1, row=6)

def dellbl():
    global lblstr
    lblstr = "0"
    lbl.configure(text=lblstr)

dellbl = Button(win, text="del", command=dellbl)
dellbl.grid(column=0, row=1)

def pluslbl():
    global lblstr
    global c1
    c1 = int(lblstr)
    lblstr = "0"
    lbl.configure(text=lblstr)

pluslbl = Button(win, text="+/-/*///**", command=pluslbl)
pluslbl.grid(column=1, row=1)

def enterpluslbl():
    global lblstr
    c2 = int(lblstr)
    strlbl = c1 + c2
    lbl.configure(text=strlbl)

enterpluslbl = Button(win, text="+=", command=enterpluslbl)
enterpluslbl.grid(column=0, row=2)


def enterminuslbl():
    global lblstr
    c2 = int(lblstr)
    lblstr = c1 - c2
    lbl.configure(text=lblstr)

enterminuslbl = Button(win, text="-=", command=enterminuslbl)
enterminuslbl.grid(column=1, row=2)


def entermultiplaylbl():
    global lblstr
    c2 = int(lblstr)
    lblstr = c1 * c2
    lbl.configure(text=lblstr)
entermultiplaylbl = Button(win, text="*=", command=entermultiplaylbl)
entermultiplaylbl.grid(column=2, row=2)


def enterdividelbl():
    global lblstr
    c2 = int(lblstr)
    lblstr = c1 / c2
    lbl.configure(text=lblstr)

enterdividelbl = Button(win, text="/=", command=enterdividelbl)
enterdividelbl.grid(column=3, row=2)

def enterpowerlbl():
    global lblstr
    c2 = int(lblstr)
    lblstr = c1 ** c2
    lbl.configure(text=lblstr)

enterpowerlbl = Button(win, text="**=", command=enterpowerlbl)
enterpowerlbl.grid(column=3, row=3)


win.mainloop()
