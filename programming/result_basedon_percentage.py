per=float(input("enter a percentage:"))
if 0>per>100:
    print("invalide percentage")
elif per>=85:
    print("first class with distinction")
elif per>=75:
    print("first class")
elif per>=60:
    print("second class")
elif per>=35:
    print("just pass")
else:
    print("fail")