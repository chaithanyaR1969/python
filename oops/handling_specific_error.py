try:
    a = int(input("enter first number"))
    b = input("enter second number")
    res = a / b
    print(res)
except ValueError as e:
    print("it is a value error")
except ZeroDivisionError as e:
    print("it is a zero division error")
except Exception as e:
    print("error occured")
