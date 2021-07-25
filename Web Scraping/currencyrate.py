# currencyrate.py

import requests # function การดึง code html ของเวปนั้นๆมาเลย 
from bs4 import BeautifulSoup 

def Currency(): 

	url = 'https://www.bot.or.th/thai/_layouts/application/exchangerate/exchangerate.aspx'
	rawdata = requests.get(url)
	rawdata = rawdata.content
	data = BeautifulSoup(rawdata,'html.parser')

	table = data.find('div',{'class':'table-foreignexchange2'})

	rows = table.find_all('tr',{'class':'bg-gray'})
	imgurl = 'https://www.bot.or.th/thai/_layouts/application/'

	allcurrency = {}

	for r in rows:
		column = r.find_all('td')
		# print(column[1].text, column[2].text, column[3].text, column[4].text, column[5].text)
		cc = {

				'Name':column[1].text,
				'Code':column[2].text.strip(),
				'Buy':float(column[3].text.strip()),
				'Sell':float(column[5].text),
		}
		# print(cc)
		allcurrency[cc['Code']] = cc


		'''
		# การ Dowload Image from url
		image_url = imgurl + r.img['src'][2:]
		image_name = image_url.split('/')[-1]
		img_data = requests.get(image_url).content
		# print(img_data)
		with open(image_name, 'wb') as handler:
			handler.write(img_data)

		'''
	return allcurrency

currency = Currency()
print(currency)
# print(currency['AUD'] ,currency['USD'])