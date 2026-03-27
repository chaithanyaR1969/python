#method 1
n=int(input("enter a number"))
sum=0
mul=1
while n>0:
    d=n%10
    sum=sum+d
    mul=mul*d
    n=n//10
if sum==mul:
    print("spy number")
else:
    print("not spy number")

#method 2
n=int(input("enter a number"))
sum=0
mul=1
for i in str(n):
    sum=sum+int(i)
    mul=mul*int(i)
if sum==mul:
    print("spy number")
else:
    print("not spy number")
