n=5
for i in range(1,n+1):
    for space in range(1,i):
        print(" ",end=" ")
    x=76+i-1
    for j in range(1,n-i+2):
        print(chr(x),end=" ")
        x=x+1
    print()