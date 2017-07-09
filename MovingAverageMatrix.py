a=[[1,2,3,4],[10,20,1,1],[22,0,2,2],[1,1,2,2]]
r=4 #No of rows
c=4 #NO of columns
print a
ws=input("Enter the window size : ")
i=0
j=0
sum=0
k=0
while(i<r):
    while(j<c and j+ws <=c):
        while(k<ws):
            sum=a[i][j+k]+sum
            k=k+1
        print sum/ws
        sum=0
        k=0
        j=j+1
    i=i+1
    j=0
