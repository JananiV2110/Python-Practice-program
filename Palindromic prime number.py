n=int(input())
temp=n
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n//=10
c=0
for i in range(1,temp+1):
    if temp%i==0:
        c+=1
if rev==temp and c==2:
    print("Palindromic prime number")
else:
    print("Not a palindromic prime number")
