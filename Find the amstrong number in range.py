n=int(input())
for i in range(1,n+1):
    temp=i
    s=0
    c=0
    while temp!=0:
        c+=1
        temp//=10
    temp=i
    while temp!=0:
        d=temp%10
        s+=d**c
        temp//=10
    if s==i:
        print(i)