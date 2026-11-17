n=int(input())
m=int(input())
c1=0
c2=0
for i in range(1,n+1):
    if n%i==0:
        c1+=1
for i in range(1,m+1):
    if m%i==0:
        c2+=1
if c1==2 and c2==2 and abs(n-m)==2:
    print("Twin prime number")
else:
    print("Not a twin prime number")