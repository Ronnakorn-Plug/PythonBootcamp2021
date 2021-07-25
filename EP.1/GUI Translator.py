# GUI Translator.py
from tkinter import *   # ดึงข้อมูลใน Libraly ชื่อ tkinter, * คือให้ดึงความสามารถหลักมาทั้งหมดเฉพาะ file main
from tkinter import ttk # ttk คือ theme of tk ทำให้ tk เราสวยงาม
# ----Google Translate----------
from googletrans import Translator # ดึงความสามารถของ Google Translate
translator = Translator()
    

GUI = Tk() # ใช้ในการสร้างหน้าต่างหลัก
GUI.geometry('500x300') # การขยายหน้าต่าง กว้างxสูง
GUI.title('โปรแกมแปลภาษา by Plug')
# -----Config------
FONT = ('Angsana New' ,15)

# -----Label-----------

L = Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT,foreground='red')
L.pack(pady=20)

# -----Entry-(ช่องกรองข้อความ)--------
v_vocab = StringVar() # กล่องเก็บข้อความ
FONT = ('Angsana New' ,15)
E1 = Entry(GUI,textvariable = v_vocab,font=FONT,width=40) 
E1.pack(pady=20)


# -----Button-(ปุ่มแปล)--------
def Translate():
    vocab = v_vocab.get() # .get คือการให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print( vocab + ' : ' + meaning.text)
    print( meaning.pronunciation)
    v_result.set( vocab + ' : ' + meaning.text) # Set สั่งโชว์ใน GUI Result

    
# B1 = Button(GUI,text='Translate') # สร้างปลุ่มขึ้นมา
# B1.pack() # show ปุ่มขึ้นมา วางจากบนลงล่าง

B1 = Button(GUI,text='Translate',command=Translate) # สร้างปลุ่มขึ้นมา
B1.pack(ipadx=20,ipady=10) # show ปุ่มขึ้นมา วางจากบนลงล่าง

# -----Label-----------

L = Label(GUI,text='คำแปล',font=FONT)
L.pack()

# -----Result--------
v_result = StringVar()
FONT = ('Angsana New',20)
R1 = Label(GUI,textvariable = v_result,font=FONT, foreground='green')
R1.pack()


GUI.mainloop() # ทำให้่โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด
