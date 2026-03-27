n=int(input("enter the number"))
s=0
for i in str(n):
    num=int(i)
    fact=1
    for j in range(1,num+1):
        fact=fact*j
    s=s+fact
if s==n:
    print("strong number")
else:
    print("not strong number")