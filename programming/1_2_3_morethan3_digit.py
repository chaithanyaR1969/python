a=int(input("enter a number:"))
if 0<=a<=9:
    print("number is single digit")
elif 10<=a<=99:
    print("number is two digit")
elif 100<=a<=999:
    print("number is three digit")
else:
    print("number is more than three digit")