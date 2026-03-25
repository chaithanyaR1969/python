n=3
x=1
for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print(x,end=" ")
        x=x+1
    print()
