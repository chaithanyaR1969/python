str=input("enter string:")
if "A"<=str[0]<="Z":
    if "1"<=str[-1]<="9":
        print(str[::-1])
    else:
        print("not ending with digit")
else:
    print("not starting with uppercase")