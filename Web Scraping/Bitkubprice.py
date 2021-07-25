# Bitkubprice.py

import requests
from pprint import pprint # print แบบสวยงาม
import time

API_URL = 'https://api.bitkub.com' # base url

endpoint = {
	'status':'/api/status',
	'timestamp':'/api/servertime',
	'symbols':'/api/market/symbols',
	'ticker':'/api/market/ticker',
	'trades':'/api/market/trades',


}

def status():
	# pprint(r.json())
	url = API_URL + endpoint['status']
	r = requests.get(url)
	if r.status_code == 200:
		print('เซิร์ฟเวอร์ทำงานปกติ')
		print(r.status_code)
	return r.status_code

def ServerTime():
	url = API_URL + endpoint['timestamp']
	comtime = time.time()
	print('Com:',comtime)
	print(time.ctime(comtime))
	# print(time.localtime(comtime)) # บอกเวลาอย่างละเอียดมาก

	r = requests.get(url)

	data = r.json()

	print('Server:',data)
	print(time.ctime(data))

def Allsymbol():
	url = API_URL + endpoint['symbols']
	r = requests.get(url)
	data = r.json()
	# pprint(r.json())
	count = len(data['result'])
	print('Count:',count)
	print(data['result'])

def Ticker(COIN='THB_BTC',ALL=False):
	url = API_URL + endpoint['ticker']

	if ALL == True:
		r = requests.get(url)
		data = r.json()
		pprint(data)
		return data
	else:
		r = requests.get(url,params={'sym':COIN}) # params = sym คือการดึงข้อมูลเป็นรายตัวออกมาจาก dic เลย โดยในเวปให้ใช้ คำสั่ง sym
		data = r.json()
		# pprint(data)
		print('--------------------------')
		print('ราคาล่าสุด : ',data[COIN]['last'])
		print('เปลี่ยนแปลง : ',data[COIN]['percentChange'])
		return data

def Trades():
	url = API_URL + endpoint['ticker']
	r = requests.get(url,params={'sym':COIN}) # params = sym คือการดึงข้อมูลเป็นรายตัวออกมาจาก dic เลย โดยในเวปให้ใช้ คำสั่ง sym
	data = r.json()
	pprint(data)


Ticker(ALL=True)


'''
for i in range(60):
	Ticker('THB_BTC')
	time.sleep(1)
'''
