n=int(input("enter the number"))
while n>0:
    d=n%10
    n=n//10
    print("extracterd value is",d)
    print("remaining value is",n)