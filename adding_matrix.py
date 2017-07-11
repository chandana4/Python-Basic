r=input("Enter number of rows :")
c=input("Enter number of columns : ")
m1=[]
m2=[]
i=0
print "Enter first matrix"
while(i<r):
    row=[]
    j=0
    while(j<c):
        print "Enter element of ",i+1,"row and ",j+1,"column"
        e=input()
        row.append(e)
        j+=1
    m1.append(row)
    i+=1
print "Enter second matrix"
i=0
while(i<r):
    row=[]
    j=0
    while(j<c):
        print "Enter element of ",i+1,"row and ",j+1,"column"
        e=input()
        row.append(e)
        j+=1
    m2.append(row)
    i+=1

i=0
j=0
sum=[]
while(i<r):
    row=[]
    j=0
    while(j<c):
        e=m1[i][j]+m2[i][j]
        row.append(e)
        j+=1
    sum.append(row)
    i+=1
print sum
