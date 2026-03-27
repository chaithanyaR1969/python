n=int(input("enter number:"))
s=set()
while n>1:
    if n in s:
        print("not a happy number")
        break
    s.add(n)
    sum=0
    for i in str(n):
        num=int(i)
        sum=sum+(num**2)
    n=sum
else:
    print("happy number")