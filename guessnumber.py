import random
r = random.randint(1,100)
count = 0
while True:
	count = count + 1
	n = input('1~100,猜一個數字:')
	n = int(n)
	if n == r:
		print('終於猜對了')
		break
	elif n > r:
		print('猜得比答案大')
		print('這是你猜的第',count,'次')
	elif n < r:
		print('猜得比答案小')
		print('這是你猜的第',count,'次')

