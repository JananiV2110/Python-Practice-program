n=int(input())
for i in range(n+1):
    if i*(i+1)==n:
        print("Pronic number")
        break
else:
    print("Not a pronic number")
