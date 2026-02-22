print("welcome to canara bank")
print("please insert the card")
balance=10000
pin=1234
print(input("select a language:"))
pin1=int(input("please enter the pin:"))
if pin==pin1:
    print("1.check balance")
    print("2.withdraw")
    a=int(input("chose from above option:"))
    print(a)
    if a==1:
        print(balance)
    else:
        amount=int(input("please enter the amount:"))
        print(amount)
        balance=(balance-amount)
        b=input("do you want to check your balance:")
        print(b)
        if b=="yes":
            print(balance)
            print("thank you")
        else:
            print("thank you")
else:
    print("wrong pin")
    print("try again")
