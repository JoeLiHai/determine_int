num = input('Please enter an integer: ')
if num.isdigit():
	if int(num) % 2 == 0:
		print('{} is an even. '.format(num))
	else:
		print('{} is an odd. '.format(num))
else:
	print('{} is not an integer. '.format(num))