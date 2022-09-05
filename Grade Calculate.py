from tkinter import*
frame=Tk()
frame.geometry('1200x600')
frame.configure(background='skyblue')
frame.title('Grade Calculate')

def tt():
    H=int(h1.get())
    E=int(e1.get())
    M=int(m1.get())
    SS=int(ss1.get())
    S=int(s1.get())
    D=int(d1.get())
    t=H+E+M+SS+S+D
    nn.set(t)

def per():
    T=int(t1.get())
    p=T/6
    np.set(p)

def print():
    H=int(h1.get())
    E=int(e1.get())
    M=int(m1.get())
    SS=int(ss1.get())
    S=int(s1.get())
    D=int(d1.get())
    t=H+E+M+SS+S+D
    p=t/6
    
    
    title=Label(text="Print Preview",font=("times",35,"bold"),fg="white",bg="skyblue")
    title.place(x=700,y=20)

    sub=Label(text="Sub",font=("times",25),fg="black",bg="skyblue")
    sub.place(x=600,y=80)

    obt_Marks=Label(text="Obt Marks",font=("times",25),fg="black",bg="skyblue")
    obt_Marks.place(x=800,y=80)

    Marks=Label(text="Marks",font=("times",25),fg="black",bg="skyblue")
    Marks.place(x=1050,y=80)
    
    h=Label(text="Hindi",font=('times',20),bg="skyblue")
    h.place(x=600,y=130)

    
    e=Label(text="English",font=('times',20),bg="skyblue")
    e.place(x=600,y=170)

    m=Label(text="Math",font=('times',20),bg="skyblue")
    m.place(x=600,y=210)

    ss=Label(text="Sst",font=('times',20),bg="skyblue")
    ss.place(x=600,y=250)

    s=Label(text="Science",font=('times',20),bg="skyblue")
    s.place(x=600,y=290)


    d=Label(text="Drawing",font=('times',20),bg="skyblue")
    d.place(x=600,y=330)

    om1=Label(text="100",font=('times',20),bg="skyblue")
    om1.place(x=850,y=130)

    om2=Label(text="100",font=('times',20),bg="skyblue")
    om2.place(x=850,y=170)

    om3=Label(text="100",font=('times',20),bg="skyblue")
    om3.place(x=850,y=210)

    om4=Label(text="100",font=('times',20),bg="skyblue")
    om4.place(x=850,y=250)

    om5=Label(text="100",font=('times',20),bg="skyblue")
    om5.place(x=850,y=290)


    om6=Label(text="100",font=('times',20),bg="skyblue")
    om6.place(x=850,y=330)

    m0=Label(textvariable=n1,font=('times',20),bg="skyblue")
    m0.place(x=1050,y=130)

    m2=Label(textvariable=n2,font=('times',20),bg="skyblue")
    m2.place(x=1050,y=170)

    m3=Label(textvariable=n3,font=('times',20),bg="skyblue")
    m3.place(x=1050,y=210)

    m4=Label(textvariable=n4,font=('times',20),bg="skyblue")
    m4.place(x=1050,y=250)

    m5=Label(textvariable=n5,font=('times',20),bg="skyblue")
    m5.place(x=1050,y=290)


    m6=Label(textvariable=n6,font=('times',20),bg="skyblue")
    m6.place(x=1050,y=330)

    tto=Label(text="Total Marks",font=('times',20),bg="skyblue")
    tto.place(x=600,y=400)
    
    to=Label(textvariable=t9,font=('times',20),bg="skyblue")
    to.place(x=800,y=400)

    tto=Label(text="Percentage",font=('times',20),bg="skyblue")
    tto.place(x=600,y=450)
    
    to=Label(textvariable=t10,font=('times',20),bg="skyblue")
    to.place(x=800,y=450)

    
    n1.set(H)
    n2.set(E)
    n3.set(M)
    n4.set(SS)
    n5.set(S)
    n6.set(D)
    t9.set(t)
    t10.set(p)
    

n1=IntVar()
n2=IntVar()
n3=IntVar()
n4=IntVar()
n5=IntVar()
n6=IntVar()
t9=IntVar()
t10=IntVar()

   
    

    

    

    
    
    

    
nn=IntVar()
np=IntVar()

mr=Label(text="Xth Marksheet",font=('times',25,'bold'),bg="skyblue",fg="red")
mr.place(x=180,y=20)

h=Label(text="Hindi",font=('times',20),bg="skyblue")
h.place(x=30,y=60)

h1=Entry()
h1.place(x=180,y=70)

e=Label(text="English",font=('times',20),bg="skyblue")
e.place(x=30,y=100)

e1=Entry()
e1.place(x=180,y=110)

m=Label(text="Math",font=('times',20),bg="skyblue")
m.place(x=30,y=140)

m1=Entry()
m1.place(x=180,y=150)

ss=Label(text="Sst",font=('times',20),bg="skyblue")
ss.place(x=30,y=180)

ss1=Entry()
ss1.place(x=180,y=190)

s=Label(text="Science",font=('times',20),bg="skyblue")
s.place(x=30,y=220)

s1=Entry()
s1.place(x=180,y=230)

d=Label(text="Drawing",font=('times',20),bg="skyblue")
d.place(x=30,y=260)

d1=Entry()
d1.place(x=180,y=270)


btn1=Button(text="Total",font=('times',20),bg="white",fg="red",command=tt)
btn1.place(x=60,y=350)

t1=Entry(textvariable=nn)
t1.place(x=200,y=360)

btn2=Button(text="Percentage",font=('times',20),bg="white",fg="red",command=per)
btn2.place(x=60,y=410)

p1=Entry(textvariable=np)
p1.place(x=210,y=440)

btn=Button(text="Print",font=('times',20),bg="Blue",fg="white",command=print)
btn.place(x=250,y=480)





