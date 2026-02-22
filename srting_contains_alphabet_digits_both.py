str=input("enter a string:")
if str.isalpha():
    print("str contains only alpha")
elif str.isdigit():
    print("str contains only digits")
elif str.isalnum():
    print("str contains both")
else:
    print("contains other char")
