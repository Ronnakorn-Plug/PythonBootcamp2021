# autoimagepost.py

import os
import wikipedia
import time
wikipedia.set_lang('th')

imgfile = os.listdir() # การดูว่าใน folder มี file อะไรบ้าง
# print(imgfile)
print('-------')

wordlist = []
pathlist = []
mainpath = os.getcwd()

for img in imgfile:
	if img[-4:] == 'jpeg' or img[-3:] == 'png':
	# [-4:]มากกว่าหรือเท่ากับ -4 เพื่อหาข้อมูลเพราะภาพจากนามสกุลfile .jpeg
		# print(img)
		fn = img.split('.')[0]
		wordlist.append(fn)
		path = os.path.join(mainpath,img)
		# print(path)
		pathlist.append(path)

"""
img[:] คือการตัดข้อความโดยการนับเลข , : = มากกว่าหรือเท่ากับ เช่น [1:5] = 1 ขึ้นไปแต่น้อยกว่า5 
โดย listเลขจะเริ่มจาก (ซ้ายไปขวา)0 1 2 3 ... แต่ (ขวาไปซ้าย(ย้อนกลับ)) -1 -2 -3 ... 
"""
 
alltitle = []
alldata = []
allprice = [100,45,55]

for wl in wordlist:
	try: # คือการลองให้คนหาแล้วหาก error จะแจ้งว่าไม่มีข้อมูล
		data = wikipedia.summary(wl)
		page = wikipedia.page(wl)
		title = page.title
	except:
		title = wl
		data = 'ไม่มีข้อมูล'

	alltitle.append(title)
	alldata.append(data)
	print('Topic: {}'.format(wl))
	print(data)
	print('---------')

# ====================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # เป็นคำสั่ง key 

driverpath = '/Users/ronnakorn/Desktop/Python Bootcamp 2021/EP.RPA with Python (Open by python 3.8)/chromedriver'
driver = webdriver.Chrome(driverpath)

url = 'http://www.uncle-machine.com/login/'

driver.get(url)


username = driver.find_element_by_id('username') # by_id or by_name ก้ได้ ขึ้นอยู่กับผู้พัฒนาเว็ปว่าจะใส่คำว่าอะไรมาให้ / ('') ในวงเล็บต้องตรงกับเว็ปตั้ง
username.send_keys("plug@gmail.com")			

password = driver.find_element_by_id('password') 
password.send_keys("0875058543")
# คือการสั่งให้ enter แทนการกดปุ่ม แต่ต้องimport key มาก่อน
password.send_keys(Keys.RETURN) 

# การส่งสำสั่งกดปุ่ม โดยวิธี xpath (ข้อเสียคือหารใช้ xpath เจ้าของเว็ปอาจเปลี่ยนแปลงคำสั่งได้ ทำให้โปรแกรมอาจerror)
# button = driver.find_element_by_xpath('/html/body/div[2]/form/button') 
# button.click()

addurl = 'http://www.uncle-machine.com/addproduct/'

driver.get(addurl) # go to addurl เพื่อเข้าไปในข้อมูลอื่นๆต่อไป

# ----------- Add Product ----------------------
for pn,pp,pd,pt in zip(alltitle,allprice,alldata,pathlist): # zip คือฟังชั่นการรวมข้อมูลในlistให้เป็นก้อนเดียวกัน 

	pdname = driver.find_element_by_id('name')
	pdprice = driver.find_element_by_id('price')
	pddetail = driver.find_element_by_id('detail')
	photo = driver.find_element_by_id('photo')

	pd1_name = pn
	pd1_price = pp
	pd1_detail = pd
	photopath = pt

	pdname.send_keys(pd1_name)
	pdprice.send_keys(pd1_price)
	pddetail.send_keys(pd1_detail)
	photo.send_keys(photopath)
	time.sleep(1)

	button = driver.find_element_by_xpath('/html/body/div[2]/form/button') 
	button.click()

print('Upload ข้อมูลสำเร็จ')
