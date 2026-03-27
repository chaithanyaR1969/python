n=int(input("enter number:"))
sqr=n**2
s=0
while sqr>0:
    d=sqr%10
    s=s+d
    sqr=sqr//10
if s==n:
    print("neon number")
else:
    print("not neon number")