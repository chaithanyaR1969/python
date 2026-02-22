a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
elif a==b and a>c and b>c:
    print("a and b is equal and greater than c")
elif b==c and b>a and c>a:
    print("b and c is equal and greater than a")
elif a==c and a>b and c>b:
    print("a and c is equal and greater than b")
else:
    print("all are equal")
