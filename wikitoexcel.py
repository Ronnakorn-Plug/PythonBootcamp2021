# wikitoexcel.py

import wikipedia
from openpyxl import Workbook

wikipedia.set_lang('th')
product = ['ทุเรียน','มังคุด','องุ่น','กล้วยหอม']

excelfile = Workbook()
sheet = excelfile.active # sheet 

sheet['B1'] = 'รายการผลไม้'

header = ['ลำดับ','สินค้า','ราคา','รายละเอียด']
sheet.append(header)

for i,pd in enumerate(product):
	content = wikipedia.summary(pd) # สรุปหลายรายการ
	# content = wikipedia.page(pd).content
	row = [i+1, pd, 1000, content]
	sheet.append(row)

excelfile.save('fruit.xlsx')
print('บันทึกสำเร็จ....')
