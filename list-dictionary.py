# list จะเป็นการเรียงลำดับจากข้อมูล โดยเริ่มจาก 0,1,2,.... โดย list จะใช้ []
# fruit = ['ส้ม','กล้วย','องุ่น']
# print(fruit[2]) # ค่าที่ได้จะออกลำดับ
# fruit.append('เงาะ') # คือการเพิ่มข้อมูลลงไปใน list 
# print(fruit)

# -------------------------------------------------------------------

# # dictionary จะสามารถกำหนดข้อมูลได้จากการกำหนดต่างๆ ทั้ง keys , values  
# fruits = {'Japan':'สตอเบอรี่','USA':'องุ่น','China':'กล้วย'}
# # print(fruits)
# # print(fruits['Japan']) # จะทำการกำหนดค่าที่ออกมาเป็น สตอเบอรี่ (เป็นข้อมูลใน values)
# fruits['Thanland'] = 'ทุเรียน' # เป็นการเพิ่มค่าทุเรียนลงไป
# # print(fruits)
# del fruits['USA'] # การลบค่าออกไปจาก dic
# print(fruits)



""" ----- ตัวอย่างการใช้งาน dictionary ------"""

mobile = {} # สร้าง dic เปล่า แล้วเพิ่มค่าไปทีหลัง
mobile['samsung'] = {'title':'samsung A51 2020 Ram 8/Rom 128GB','price':7660,'discount':2,'oriprice':7777,'star':5}
mobile['iphone7'] = {'title':'iphone7 128gb เครื่องแท้','price':10300,'color':['red','blue','yellow']}
# print(mobile)
{'samsung': {'title': 'samsung A51 2020 Ram 8/Rom 128GB', 'price': 7660, 'discount': 2, 'oriprice': 7777, 'star': 5}, 'iphone7': {'title': 'iphone7 128gb เครื่องแท้', 'price': 10300, 'color': ['red', 'blue', 'yellow']}}
for m,d in mobile.items(): # .items คือการดึงข้อมูลทั้ง keys,values โดยต้องกำหนดตัวแปล จากตย. m,d
 	print(f'Mobile: {m}') # f คือคล้าย .format 
 	print('Title: {}'.format(d['title']))
 	print('Price: {} Baht'.format(d['price']))
 	if 'color' in d: # เป็นการซ้อนloop ว่า หากเจอ values เป็น color ให้แสดงผลมาด้วย
 		for c in d['color']:
 			print('Color: {}'.format(c))
 	print('-------')