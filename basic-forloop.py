# รันซ้ำตามตัวเลขที่ต้องการ
import time

for i in range(10):
	print(i)
	# time.sleep(1)
	print('----------')	
print('=================')	
for i in range(1,11):
	print(i)
	# time.sleep(1)
	print('----------')	
print('=================')	
for i in range(1,10,2):
	print(i)
	# time.sleep(1)
	print('----------')		
print('=================')
friends = ['Albert','Sreve','Aden','Elon']
for f in friends:
	print(f)
print('=================')	

# แสดงผลสิ่งที่อยู่ใน list เฉพาะตัว
friends = ['Albert','Sreve','Aden','Elon']
for f in friends:
	if f =='Albert':
		print(f)