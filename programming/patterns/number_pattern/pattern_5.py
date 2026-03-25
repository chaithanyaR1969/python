n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==3:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

    #OR
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print((j+1)%2,end=" ")
    print()