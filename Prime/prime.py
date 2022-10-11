number = int(input())
if number < 0:
	print("Number is negative. It is not a prime number.")
elif number == 0:
	print("Number is zero, it is not a prime number.")
elif number == 1:
	print("Number is 1. It is not a prime number.")
else: 
	for i in range(2, int(number/2)+  1):
		if ((number % i) == 0):
			print( number, " is not a prime number.")
			break
	else:
		print( number, " is a prime number.")