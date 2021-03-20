# GUIbasic.py ---> CSV

from tkinter import *
from tkinter import ttk, messagebox
import csv
import random


# CSV file
def WritetoCSV(data):
	with open('data.csv','a', newline='', encoding='utf-8') as file:
	# mode 'a' การใส่ค่าไปเรื่อยๆ 'w' มีข้อมูลอยุ่แล้วทับค่าไปเลย # newline คือการขึ้นบรรทัดใหม่ทุกครั้งที่เปิดfile
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('บันทึกไฟล์สำเร็จ')

def ReadCSV():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file) # fr = file reader
		data = list(fr)
	# print(data)
	return data # return คือ การส่งข้อมูลไปใช้งานต่อ


GUI = Tk()
GUI.title('โปรแกรมGUI By Plug')
GUI.geometry('700x700')

# font
FONT1 = ('Angsana New', 20, 'bold') # bold ตัวหนา
FONT2 = ('Angsana New', 20)


# Tab menu
Tab = ttk.Notebook(GUI) # Tab ในภาษา python เรียกว่า Notebook

T1 = Frame(Tab)
T2 = Frame(Tab)

Tab.add(T1,text='Add')
Tab.add(T2,text='Flash Card')

Tab.pack(fill=BOTH, expand=1) # fill=BOTHคำสั่งขยายทั้ง2ตัวเลยเต็มจอโปรแกรม



"""==========================================================="""

# Label 1
L1 = ttk.Label(T1, text='หัวข้อ', font=FONT1, foreground='green') #foreground คือการสร้างสี
L1.pack(pady=10)

# Entry 1
v_title = StringVar()
E1 = ttk.Entry(T1, textvariable=v_title, font=FONT2, width=30)
E1.pack()

# Label 2
L2 = ttk.Label(T1, text='รายละเอียด', font=FONT1, foreground='green')
L2.pack(pady=10)

# Entry2
v_detail = StringVar()
E2 = ttk.Entry(T1, textvariable=v_detail, font=FONT2, width=40)
E2.pack()

# สร้างฟังชั่น updateTable เพื่อหากเปิดไฟล์ให้ใช้ฟังชั่นนี้ทันที
def UpdateTable():
	table.delete(*table.get_children()) #clear ข้อมูลชุดเก่าแล้วจึงอัฟเดทชุดใหม่เข้าไป / get_children() - เป็นฟังชั่นข้อมูลที่อยุ่ใน Table / * เหมือนเป็นการรัน forloop
	alldata = ReadCSV() # เรียกฟังชั่นอ่าน CSV จากด้านบนมา
	for row in alldata:
		table.insert('','end',value=row)


# Button 1
def SaveButton(event=None): # event=None เป็นการเชื่องกับการกดปุ่ม enter 
	title = v_title.get()
	detail = v_detail.get() 
	print(title)
	print(detail)
	dt = [title,detail]
	WritetoCSV(dt)
	print('กำลังบันทึกข้อมูล...')
	# การ clear data
	v_title.set('')
	v_detail.set('') 
	E1.focus() # การทำให้เคอร์เซอรืไปอยู่ตำแหน่งช่อง Entry ที่ต้องการ
	UpdateTable() # จะทำการupdate ข้อมูลทุกครั้งที่บันทึก
	global allquestion
	allquestion = ReadCSV()

E2.bind('<Return>',SaveButton) # ใน python ปุ่ม Enter เรียกว่า Return
# E2.bind('<Control-s>',SaveButton)

B1 = ttk.Button(T1, text='Save', command=SaveButton)
B1.pack(ipadx=30, ipady=20,pady=20)


# table การสร้างตาราง

# Setting font for Table
style = ttk.Style()
style.configure('Treeview.Heading',font=('Angsana New',20))
style.configure('Treeview',font=('Angsana New',18),rowheight=30)

header = ['Title','Detail']

table = ttk.Treeview(T1, height=10, column=header, show='headings') # heighr คือระบุบรรทัด
table.place (x=20,y=300)

table.heading('Title', text='หัวข้อ')
table.column('Title', width=200)
table.heading('Detail', text='รายละเอียด')
table.column('Detail', width=460)


#  ทดลอง insert ข้อมูลเข้าไป
# row = ['GUI คืออะไร?','GUI : Graphical Iser Interface']
# table.insert('','end',value=row) # 'end' คือการแสดงข้อมูลบรรทัดสุดท้าย แต่หาก 0 จะไปแสดงข้างบน หากใส่เลขจะเรียงลำดับเหมือน List / 0,1,2
# row = ['.insert','คือการใส่ข้อมูลเข้าไป']
# table.insert('','0',value=row)

def DeleteQuestion(event=None):
	select = table.selection() # เป็นการช่วยดูว่ามีการเลือกคำถามข้อไหน?
	data = table.item(select)
	print(data['values'])

	# การสร้าง if เพื่อให้สามารถลบข้อมูลที่เป็นตัวเลขได้ โดยใช้หลัก if 
	datarow = data['values']
	if isinstance(datarow[-1],int) or isinstance(datarow[-1],float):
		allquestion.remove([datarow[0],str(datarow[-1])])
	else:
		allquestion.remove(data['values'])		
	print('Count:',len(allquestion))

	# กรณีที่ต้องการลบเฉพาะค่าในโปรแกรม
	table.delete(*table.get_children()) #clear ข้อมูลชุดเก่าแล้วจึงอัฟเดทชุดใหม่เข้าไป / get_children() - เป็นฟังชั่นข้อมูลที่อยุ่ใน Table / * เหมือนเป็นการรัน forloop
	alldata = allquestion # เรียกฟังชั่นอ่าน CSV จากด้านบนมา
	for row in alldata:
		table.insert('','end',value=row)

table.bind('<Delete>',DeleteQuestion)	

def SaveQuestion(event=None):
	check = messagebox.askquestion('ยืนยันการบันทึกข้อมูล','คุณต้องการบันทึกข้อมูลล่าสุดใช่หรือไม่? ข้อมูลเก่าจะหายไป! ')

	if check == 'yes':
		with open('data.csv','w', newline='', encoding='utf-8') as file:
		# mode 'a' การใส่ค่าไปเรื่อยๆ 'w' มีข้อมูลอยุ่แล้วทับค่าไปเลย # newline คือการขึ้นบรรทัดใหม่ทุกครั้งที่เปิดfile
			fw = csv.writer(file) # fw = file writer
			fw.writerows(allquestion) # writerows มี s เพราะเป็นloopซ้อน loops เป็นการบันทึกข้อมูลล่าสุด
		# print('บันทึกไฟล์สำเร็จ')
		# from tkinter import ttk, messagebox # ต้องการโชว์ปํอปอัพต้องดึง messagebox
		messagebox.showinfo('Saving...','บันทึกข้อมูลสำเร็จ')

GUI.bind('<F1>',SaveQuestion)
L = ttk.Label(T1,text='หากต้องการบันทึกค่าล่าสุด กรุณากดปุ่ม <F1>',font=('Angsana New',13),foreground='red')
L.place(x=20,y=640)





###################### TAB 2 #############################################
v_question = StringVar() # ใช้สำหรับเก็บคำถามใน TAB 2
v_question.set('----------- คำถาม (กดปุ่ม Next เพื่อเริ่ม) ---------------')
R1 = ttk.Label(T2,textvariable=v_question,font=FONT1)
R1.pack(pady=20)

v_answer = StringVar()
v_answer.set('------------- กดปุ่ม Show เพื่อแสดงคำตอบ ------------------')
R2 = ttk.Label(T2,textvariable=v_answer,font=FONT1)
R2.pack(pady=20)


# ----------------- Button -----------------------
BF1 = Frame(T2) # สร้าง Button ในกรอบ เพื่อใช่ .Grid ได้ **กฎการใช้ .pack .place .grid คือห้ามใช้ปนกัน ยกเว้น .place   
BF1.pack(pady=100)

allquestion = ReadCSV() # [[จะเป็นรายการ list ซ้อน list]]

v_current_ans = StringVar() # คำตอบที่ซ่อนอยู่
def Next():
	v_answer.set('------------- กดปุ่ม Show เพื่อแสดงคำตอบ ------------------') # เพื่อ reset คำตอบเมื่อกด Next
	q = random.choice(allquestion)
	v_question.set(q[0])
	v_current_ans.set(q[1])
	BC3['state'] = 'enabled' # set ว่าเมื่อกด score+1 และกด next แล้วกด score+1 ต่อได้

def Show():
	v_answer.set(v_current_ans.get()) # ดึงคำตอบล่าสุดที่ซ่อนอยู่ไปโชว์ที่ตำแหน่ง v_answer

# ------------ ตัววโชว์คะแนนที่ได้ -------------
score = 0
v_score = StringVar()
v_score.set('Score: {}'.format(score))
Score = ttk.Label(T2,textvariable=v_score,font=('Impact',20))
Score.place(x=20,y=20)

def ScoreUp():
	global score # การประกาศ global เพื่อให้ข้อมูลใน def สามารถ setting กับข้อมูลภายนอกได้ / ใน def จะเรียกกันว่า local แต่โซนนอก def จะเป็น global
	score += 1 # score = score + 1
	v_score.set('Score: {}'.format(score))
	BC3['state'] = 'disabled' # สร้างคำสั่งกด score ได้ครั้งเดียว



BC1 = ttk.Button(BF1,text='Next',command=Next)
BC2 = ttk.Button(BF1,text='Show',command=Show)
BC3 = ttk.Button(BF1,text='Score +1',command=ScoreUp)
BC1.grid(row=0,column=0,ipadx=20,ipady=30)
BC2.grid(row=0,column=1,ipadx=20,ipady=30)
BC3.grid(row=0,column=2,ipadx=20,ipady=30)






# เป็นการโหลดข้อมูล CSV เข้าไปในโปรแกรม
UpdateTable()













GUI.mainloop()
