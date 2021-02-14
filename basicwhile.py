# while คือ ทำซ้ำไปจนกว่าข้อมูลจะเป็น False หากเป็น True ก็จะวน loops 
money = 998
transfer = 2000
moneytransfer = 15

# print('Condition: ',money < transfer)
print('ต้องการโอน', transfer ,'(ค่าบริการโอนเงิน 15 บาท)')
while money < (transfer + moneytransfer ) :
	print('คุณมีเงิน', money)
	print('กรุณาโอนเงินเข้าบัญชี เงินไม่พอโอน')
	getmoney = int(input('ฝากเงินเท่าไหร่?: '))
	money = money + getmoney # 998 + xxx
	print('---') 

print('คุณมีเงิน', money)
print('โอนเงินได้เลย')
print('ค่าบริการโอนเงิน', moneytransfer)
print('เหลือเงินในบัญชี: ', money - (transfer + moneytransfer ))