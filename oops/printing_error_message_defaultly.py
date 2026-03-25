try:
    a = int(input("enter first number"))
    b =input("enter second number")
    res = a / b
    print(res)

except Exception as e:
    print("error occured")
    print(e.__str__())

