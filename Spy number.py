n=int(input())
s=0
m=1
while n!=0:
    digit=n%10
    s+=digit
    m*=digit
    n//=10
if s==m:
    print("Spy Number")
else:
    print("Not a spy number")