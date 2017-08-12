t=input()
l=[]
for i in range(0,t):
    (n,k)=map(int,raw_input().split())
    coin=0
    for j in range(2,k+1):
        r=(n%j)
        if(r>coin):
            coin=r
    l.append(coin)
print l
