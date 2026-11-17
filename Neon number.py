n=int(input())
temp=n
s=n*n
s1=0
while s!=0:
    digit=s%10
    s1+=digit
    s//=10
if s1==temp:
    print("Neon number")
else:
    print("Not a neon number")

