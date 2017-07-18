n=input("Enter the order of the matrix")
a=[[0 for i in range(0,n)] for j in range(0,n)]
b=[[0 for i in range(0,n)] for j in range(0,n)]
print "Enter first matrix : "
for i in range(0,n):
    print "\n"
    for j in range(0,n):
        a[i][j]=input()
print "Enter second matrix : "
for i in range(0,n):
    print "\n"
    for j in range(0,n):
        b[i][j]=input()
print "Resultant matrix is"
for i in range(0,n):
    print "\n"
    for j in range(0,n):
        print a[i][j]+b[i][j],
