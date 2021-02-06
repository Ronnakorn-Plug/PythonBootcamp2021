from tkinter import *
from tkinter import ttk

# ------รูปแบบ GUI------------
GUI = Tk()
GUI.geometry('500x700+100+100') # การ +100+100 คือการกำหนดจุดให้ GUI เปิดในตำแหน่งไหนบนจอ เช่น +0+0 จะชิดขอบ
GUI.title('โปรแกรมคำนวนภาษีมูลค่าเพิ่ม')

# -----Config------
FONT  = ('Angsana New' ,10)
FONT1 = ('Angsana New' ,15)
FONT2 = ('Angsana New' ,20)

# -------Label------------
L = ttk.Label(GUI, text='โปรแกรมคำนวนภาษีมูลค่าเพิ่ม',font=FONT2,foreground='red')
L.pack(pady=10)

# -------Logo Picture --------
LP = PhotoImage(file='logo7.png').subsample(18) # .subsample(18) การปรับขนาดภาพ / ใช้ Jpeg ไม่ได้
 
logopic = ttk.Label(GUI, image=LP)
logopic.pack()

# ------------------------------------------------------------------------------------ #

# -------Label & Entry 1-------------

L1 = ttk.Label(GUI, text='ชื่อสินค้า',font=FONT1)
L1.pack()

Cal1 = StringVar()
E1 = ttk.Entry(GUI, textvariable = Cal1, font=FONT1, width=40)
E1.pack(pady=5)


# -------Label & Entry 2-------------

L2 = ttk.Label(GUI, text='ราคา(บาท)',font=FONT1)
L2.pack()

Cal2 = StringVar()
E2 = ttk.Entry(GUI, textvariable = Cal2, font=FONT1, width=40)
E2.pack(pady=5)

# -------Label & Entry 3-------------

L3 = ttk.Label(GUI, text='จำนวนสินค้า',font=FONT1)
L3.pack()    

Cal3 = StringVar()
E3 = ttk.Entry(GUI, textvariable = Cal3, font=FONT1, width=40)
E3.pack(pady=5)


# --------Button-----------
def Calculator(event=None): # คำอธิบาย event=None ดู line 74
    C_C1 = Cal1.get()
    C_C2 = int(Cal2.get())
    C_C3 = int(Cal3.get())
    C_C4 = C_C2 * C_C3
    C_C5 = int(C_C4 * 0.07)
    textshow = 'สินค้า : {}\n'.format(C_C1) # \n คือการขึ้นบรรทัดใหม่ของข้อความ , 
    textshow1 = 'ราคา : {:,.2f} บาท/ถุง\n'.format(C_C2) # :,.2f คือการใส่ ทศนิยม 2 ตำแหน่งและ ,
    textshow2 = 'จำนวน : {:,.2f} ถุง\n'.format(C_C3)
    textshow3 = 'ราคารวมสุทธิ : {:,.2f} บาท\n'.format(C_C4)
    textshow4 = 'VAT(7%) : {:,.2f} บาท\n'.format(C_C5)
    textshow5 = 'ราคาก่อน VAT(7%) : {:,.2f} บาท'.format(C_C4-C_C5)
    r_result.set(textshow+textshow1+textshow2+textshow3+textshow4+textshow5)


B = ttk.Button(GUI,text='Calculator',command=Calculator)
B.pack(ipadx=10,ipady=5)

E3.bind('<Return>',Calculator) # bind คือการสร้างระบบ การกด Enter โดยใน def ต้องใส่ event ด้วยและ =None เพื่อจะได้ใช้ Enter ร่วมกับปุ่ม จะได้ไม่ Error

# -------Label Result------------
LR = ttk.Label(GUI, text='ผลการคำนวน',font=FONT1)
LR.pack(pady=15)

# -------Result-------------
r_result = StringVar()
R1 = ttk.Label(GUI,textvariable = r_result,font=FONT1, foreground='green')
R1.pack()

GUI.mainloop()

