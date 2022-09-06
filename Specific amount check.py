import tkinter
frame=tkinter.Tk()
frame.geometry('400x400')
frame.configure(background="darkcyan")
frame.title("specific amount check")

def a12000():
    note=int(en.get())
    a=note//2000
    a2000.set(a)
a2000=tkinter.IntVar()

def a1500():
    note=int(en.get())
    a=note//500
    a500.set(a)
a500=tkinter.IntVar()

def a1200():
    note=int(en.get())
    a=note//200
    a200.set(a)
a200=tkinter.IntVar()

def a1100():
    note=int(en.get())
    a=note//100
    a100.set(a)
a100=tkinter.IntVar()

def a150():
    note=int(en.get())
    a=note//100
    a50.set(a)
a50=tkinter.IntVar()

def a120():
    note=int(en.get())
    a=note//20
    a20.set(a)
a20=tkinter.IntVar()

def a110():
    note=int(en.get())
    a=note//10
    a10.set(a)
a10=tkinter.IntVar()

def a15():
    note=int(en.get())
    a=note//5
    a5.set(a)
a5=tkinter.IntVar()

def a12():
    note=int(en.get())
    a=note//2
    a2.set(a)
a2=tkinter.IntVar()

def a11():
    note=int(en.get())
    a=note//1
    a1.set(a)
a1=tkinter.IntVar()
    


name=tkinter.Label(text="Enter Amount")
name.place(x=20,y=30)

en=tkinter.Entry()
en.place(x=130,y=30)

btn=tkinter.Button(text="2000",height=2,width=5,command=a12000)
btn.place(x=30,y=80)

btn1=tkinter.Button(text="500",height=2,width=5,command=a1500)
btn1.place(x=80,y=80)

btn2=tkinter.Button(text="200",height=2,width=5,command=a1200)
btn2.place(x=130,y=80)

btn3=tkinter.Button(text="100",height=2,width=5,command=a1100)
btn3.place(x=180,y=80)

btn4=tkinter.Button(text="50",height=2,width=5,command=a150)
btn4.place(x=230,y=80)

btn5=tkinter.Button(text="20",height=2,width=5,command=a120)
btn5.place(x=280,y=80)

btn6=tkinter.Button(text="10",height=2,width=5,command=a110)
btn6.place(x=330,y=80)

btn7=tkinter.Button(text="5",height=2,width=5,command=a15)
btn7.place(x=30,y=125)

btn8=tkinter.Button(text="2",height=2,width=5,command=a12)
btn8.place(x=80,y=125)

btn9=tkinter.Button(text="1",height=2,width=5,command=a11)
btn9.place(x=130,y=125)

name=tkinter.Label(text="List",height=2,width=7)
name.place(x=180,y=180)

en2000=tkinter.Entry(textvariable=a2000)
en2000.place(x=30,y=250)

en1=tkinter.Entry(textvariable=a500)
en1.place(x=30,y=275)

en2=tkinter.Entry(textvariable=a200)
en2.place(x=30,y=300)

en3=tkinter.Entry(textvariable=a100)
en3.place(x=30,y=325)

en4=tkinter.Entry(textvariable=a50)
en4.place(x=30,y=350)

en5=tkinter.Entry(textvariable=a20)
en5.place(x=200,y=250)

en6=tkinter.Entry(textvariable=a10)
en6.place(x=200,y=275)

en7=tkinter.Entry(textvariable=a5)
en7.place(x=200,y=300)

en8=tkinter.Entry(textvariable=a2)
en8.place(x=200,y=325)

en9=tkinter.Entry(textvariable=a1)
en9.place(x=200,y=350)











