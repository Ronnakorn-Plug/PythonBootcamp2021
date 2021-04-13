# basic web scraping.py
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


# print(data)

'''
for p in price:
	print([p.text.strip()]) # strip() คือการตัดข้อมูลไม่จำตัดหน้า-หลัง
	# print(p.text.replace('\n','').replace('\r','').replace(' ','')) # การตัดข้อความนั้นๆ ผลลัพธ์เหมือน strip()
	print('-------')
'''

# mystock = ['DELTA']
mystock = ['DELTA','EA','GPSC','BGRIM','GULF','OSP','CKP']

for st in mystock:
	res = Checkprice(st)
	# print(res['name'],res['price'])
	print(res)

