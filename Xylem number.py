n=input()
s1=int(n[0])+int(n[-1])
s2=(n[1:-1])
m=0
for i in s2:
    m=m+int(i)
if s1==m:
    print("Xylem number")
else:
    print("Not a xylem number")