try:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    res = a / b
    print(res)
except (ValueError,ZeroDivisionError) as e:
    print("it is a value error or zero division error")

except Exception as e:
    print("error occured")
