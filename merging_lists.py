l1=[1,11,3,9,5]
l2=[2,4]
print "First list is ",l1
print "Second list is ",l2
print "Merging first and second \n"
l=len(l2)
i=0
while(i<l):
	l1.append(l2[i])
	i+=1
print l1
