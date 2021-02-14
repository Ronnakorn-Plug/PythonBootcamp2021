#basic-ifelse.py

money = int(input('คุณมีเงินอยู่เท่าไหร่?: '))
from pprint import pprint #pretty print
import random

restaurant = {'hight': [{'name':'shitsuka sushi','price':700},
						{'name':'peprini','price':500}],
			  'medium':[{'name':'เสวย','price':200},
						{'name':'รสดี','price':250}],
			  'low':  [{'name':'ป้าส้ม','price':40},
					   {'name':'ป้าส้มกระเพรา','price':50}]}

# pprint(restaurant)

# money = 1000

if money >= 500:
	select = random.choice(restaurant['hight']) # choice จะใช้ได้ต่อเมื่อเป็น list[] เท่านั้น ในกรณีนี้ values เป็น list
	print('คุณลูกค้าทานร้าน {} ดีไหม? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))
elif money >= 200:
	select = random.choice(restaurant['medium']) 
	print('คุณลูกค้าทานร้าน {} ดีไหม? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))	 	
else:
	select = random.choice(restaurant['low']) 
	print('คุณลูกค้าทานร้าน {} ดีไหม? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))		