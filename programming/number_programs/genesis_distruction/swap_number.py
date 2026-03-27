#with temparary variable
n=int(input("enter number n:"))
m=int(input("enter number m:"))
temp=n
n=m
m=temp
print(n,m)


#without using temparary variable
n=int(input("enter number n:"))
m=int(input("enter number m:"))
n,m=m,n
print(n,m)

#or

n=int(input("enter number n:"))
m=int(input("enter number m:"))
n=n+m
m=n-m
n=n-m
print(n,m)