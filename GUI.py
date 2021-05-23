from tkinter import *
from func import cal_fuction

def errorCheck(ZL, Z0, Zs, Vs, L, z, alpha, f):
    try:
       complex(ZL)
       int(Z0)
       complex(Zs)
       complex(Vs)
       float(L)
       float(z)
       float(alpha)
       float(f)
    except ValueError:
        announce.config(text='ZL, Z0, Zs, Vs phải có kiểu: a+bj với a,b là số thực, L là số thực lớn hơn 0')
        return False
    else:
        if float(L)>0 and int(Z0)>0 and float(z)>0 and float(z)<=float(L) and float(alpha) >=0 and float(f)>0:
            return True
        elif float(L)<0 or int(Z0)<0 or float(z)<0 or float(z)>float(L):
            announce.config(text='0<z<L và Z0>0 và L>0')
            return False
    
def button_summit(ZL, Z0, Zs, Vs, L, z, alpha, f):
    announce.config(text='')
    if errorCheck(ZL, Z0, Zs, Vs, L, z, alpha, f) is True:
        V, I, Pinc, Pref, Ptrans = cal_fuction(complex(ZL), int(Z0), complex(Zs), complex(Vs), float(L), float(z), float(alpha), float(f))
        e_V.insert(0, V)
        e_I.insert(0, I)
        e_Pinc.insert(0, Pinc)
        e_Pref.insert(0, Pref)
        e_Ptran.insert(0, Ptrans)
        
    





root = Tk()
root.title('Btl1 Nhóm xxx')

label_1 = Label(root, text='Nhập các thông số')

label_z = Label(root, text='z:')
e_z = Entry(root, width=20)

label_ZL = Label(root, text='ZL:')
e_ZL = Entry(root, width=20)

label_Z0 = Label(root, text='Z0:')
e_Z0 = Entry(root, width=20)

label_Zs = Label(root, text='Zs:')
e_Zs = Entry(root, width=20)

label_Vs = Label(root, text='Vs:')
e_Vs = Entry(root, width=20)

label_L = Label(root, text='L (theo lamdba):')
e_L = Entry(root, width=20)

label_alpha = Label(root, text='alpha:')
e_alpha = Entry(root, width=20)

label_f = Label(root, text='f:')
e_f = Entry(root, width=20)


label_2 = Label(root, text='Các thông số cần tính toán')

label_V = Label(root, text='V:')
e_V = Entry(root, width=20)

label_I = Label(root, text='I:')
e_I = Entry(root, width=20)

label_Pinc = Label(root, text='Pinc:')
e_Pinc = Entry(root, width=20)

label_Pref = Label(root, text='Pref:')
e_Pref = Entry(root, width=20)

label_Ptran = Label(root, text='Ptran:')
e_Ptran = Entry(root, width=20)

button_calculate = Button(root, text='Caculate', 
    command=lambda: button_summit(e_ZL.get(), e_Z0.get(),
    e_Zs.get(), e_Vs.get(), e_L.get(), e_z.get(), e_alpha.get(), e_f.get()))

label_1.grid(row=0, column=0)

label_ZL.grid(row=1, column=0)
e_ZL.grid(row=1,column=1)

label_Z0.grid(row=1, column=2)
e_Z0.grid(row=1, column=3)

label_Zs.grid(row=2, column=0)
e_Zs.grid(row=2, column=1)

label_Vs.grid(row=2, column=2)
e_Vs.grid(row=2, column=3)

label_L.grid(row=3, column=0)
e_L.grid(row=3, column=1)

label_z.grid(row=3, column=2)
e_z.grid(row=3, column=3)

label_alpha.grid(row=4, column=0)
e_alpha.grid(row=4, column=1)

label_f.grid(row=4, column=2)
e_f.grid(row=4, column=3)

button_calculate.grid(row=5, column=3)

label_2.grid(row=6, column=0)

label_V.grid(row=7, column=0)
e_V.grid(row=7, column=1)

label_I.grid(row=7, column=2)
e_I.grid(row=7, column=3)

label_Pinc.grid(row=8, column=0)
e_Pinc.grid(row=8, column=1)

label_Pref.grid(row=8, column=2)
e_Pref.grid(row=8, column=3)

label_Ptran.grid(row=9, column=0)
e_Ptran.grid(row=9, column=1)

announce = Label(root, text='')
announce.grid(row=11, column=0, columnspan=4)


root.mainloop()

