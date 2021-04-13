# GUIstock.py

from tkinter import *
from tkinter import ttk, messagebox
import requests # function การดึง code html ของเวปนั้นๆมาเลย 
from bs4 import BeautifulSoup 

def Checkprice(QUOTE='EA'): # set ค่าไว้ว่าเริ่มต้นด้วย EA หากไม่ใส่ค่า

	url = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol={}&ssoPageId=9&selectPage=1'.format(QUOTE)

	rawdata = requests.get(url)
	rawdata = rawdata.content

	data = BeautifulSoup(rawdata, 'html.parser')

	# print(data.prettify()) # prettify() เพื่อให้ดูสวยงามและเห็นรายละเอียดต่างๆ

	# price = data.find_all('h1')
	price = data.find_all('div',{'class':'col-xs-6'})
	# print(price)

	name = price[0].text.strip()
	stprice = float(price[2].text.strip()) # float คือการทำค่าให้เป็นเลข
	change = float(price[3].text.split()[-1])
	percentchange = float(price[4].text.split()[-1].replace('%',''))

	# ----------- โซนวันที่ ---------------------- 

	date = data.find('div',{'class':'flex-item text-left padding-8'})
	date = date.find_all('span')
	update = date[0].text
	marketstatus = date[1].text

	# ----------- result ---------------------- 

	result = {'name':name,
			  'price':stprice,
			  'change':change,
			  '%'+'change':percentchange,
			  'update':update,
			  'status':marketstatus}

	# print(result)

	return result 

##################### GUI ####################################################

GUI = Tk()
GUI.geometry('600x700')
GUI.title('Check Stock By Plug')
GUI.iconbitmap('stock.ico')

# ------------ Font ---------------
FONT0 = ('Angsana New',15,)
FONT1 = ('Angsana New',20)
FONT2 = ('Angsana New',30,'bold')
# --------- Label ---------------
img = PhotoImage(file='Stockslogo.png')
LIMG = Label(GUI, image=img,)
LIMG.pack(pady=10)

L1 = Label(GUI, text='กรุณากรอกหุ้นที่ต้องการ', font=FONT2)
L1.pack(pady=10)


# ---------- ช่องกรอกข้อมูล -----------
v_quote = StringVar()
E1 = Entry(GUI, textvariable=v_quote, width=35)
E1.pack(pady=20)


# ----------Button -------------------
allresult = []

def CheckSrockPrice(event=None):
	# clear label
	global allresult
	for rs in allresult:
		rs.destroy() # ลบ label

	allresult = []

	# v_result.set('') # clear result
	quote = v_quote.get().split(',')
	print(quote)

	# สร้าง forloop เพื่อเปิดใช้งาน def Checkprice 
	for q in quote:
		try: # try , except = ให้ป้องกันการกรองข้อมูลผิด
			price = Checkprice(q.strip()) # strip() = ตัดข้อมูลไม่จำเป็น ตัดหน้า-ตัดหลัง
			print(price)
			text = '{} ราคา: {} บาท '.format(price['name'],price['price'])
			text = text + 'เปลี่ยนแปลง: {} บาท เปลี่ยนแปลง: {}%'.format(price['change'],price['%'+'change'])

			if price['%'+'change'] < 0:
				color = 'red'
			elif price['%'+'change'] == 0:
				color = 'black'
			elif price['%'+'change'] > 10:
				color = '#2cb3f2' # hex code color from googlr -> color picker
			else:
				color = 'green'
		except:
			text = 'หุ้น {} ไม่อยู่ในตลาดหุ้น'.format(q)
			color = 'orange'
		# --------- Result ------------
		L = Label(GUI, text=text, foreground=color, font=FONT0)
		allresult.append(L)
		L.pack(pady=10)


		# v_result.set(v_result.get() + text + '\n')



B1 = Button(GUI, text='Check Price', command=CheckSrockPrice)
B1.pack(ipadx=10,ipady=10)

E1.bind('<Return>',CheckSrockPrice)

# ----------- Result -----------------
# v_result = StringVar()
# v_result.set('----------Result----------')
# R1 = Label(GUI, textvariable=v_result, foreground='green',font=FONT0)
# R1.pack(pady=20)


statusbar = Label(GUI, text='กดปุ่ม <F1> เพื่อขอความช่วยเหลือ')
statusbar.pack(side=BOTTOM)

def Help(event=None):
	text = 'หากมีคำถามเพิ่มเติม กรุณาติดต่อ: รณกร ดำรงผล\nEmail: Plug8955@gmail.com\nFacebook: Ronnakorn Dumrongphol'
	messagebox.showinfo('Help',text)

GUI.bind('<F1>',Help)




GUI.mainloop()