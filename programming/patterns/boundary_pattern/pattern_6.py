n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n//2+1 or i==n//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()