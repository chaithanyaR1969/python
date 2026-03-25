n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 and 1<j<n) or (j==1 and 1<i<n) or (i==n and 1<j<n) or (j==n and 1<i<n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()