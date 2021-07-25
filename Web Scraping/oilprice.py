# Oilprice.py

import requests # function การดึง code html ของเวปนั้นๆมาเลย 
from bs4 import BeautifulSoup 

def Checkoil(): 

	url = 'https://www.shell.co.th/th_th/motorists/shell-fuels/fuel-price/app-fuel-prices.html'
	rawdata = requests.get(url)
	rawdata = rawdata.content
	data = BeautifulSoup(rawdata,'html.parser')

	oiltable = data.find('table',{'class':'cc_cursor'})
	# print(oiltable.find_all('tr')[3].text.strip())

	result = '' # ทำให้ข้อมูลเป็นข้อความ

	for oil in oiltable.find_all('tr')[1:]:
		text = oil.text.strip()
		# print(text)
		result += text + '\n'

	return result

print(Checkoil()) # ที่ต้องใส่ print เพราะใน Function ไม่ได้ใส่ค่าprintเลย
