x=float(input("Enter a number : "))
low = 0
high = max(x, 1)
ep=0.00001
guess = (low + high)/2.0
while abs(x-guess**2) > ep:
	if guess**2 < x:
		low = guess
	else:
		high = guess
	guess = (low + high)/2.0	
print 'The root is :  ', guess

