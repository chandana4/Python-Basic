ep=0.00001

x=input("Enter number : ")
guess=x
diff=guess**2-x
while abs(diff)>ep:
	guess=guess-diff/(2.0*guess)
	diff=guess**2-x
print "The root is : ",guess

