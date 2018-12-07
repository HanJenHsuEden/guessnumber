import random
r = random.randint(1,100)
while True:
	n = input('1~100,猜一個數字:')
	n = int(n)
	if n == r:
		print('終於猜對了')
		break
	elif n > r:
		print('猜得比答案大')
	elif n < r:
		print('猜得比答案小')

