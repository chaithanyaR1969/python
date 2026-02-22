import time
password=1234
balance=20000
print("welcome to pentagon atm")
print("insert the card")
print("1.yes 2.no")
card=int(input())
if card==1:
    print("select your language")
    print("1.english 2.kannada 3.malayalam")
    lang=int(input())
    if lang==1:
        print("please enter the pin:")
        pin=int(input())
        if pin==password:
            print("select the option:")
            print("1.check balance 2.withdraw")
            choice=int(input())
            if choice==1:
                print("The available balance is",balance)
                print("thank you visit again")
            elif choice==2:
                amount=int(input("enter the amount:"))
                print(amount)
                if amount%100==0:
                    if amount<=balance:
                        print("transaction is processing")
                        time.sleep(3)
                        print("collect you cash")
                        time.sleep(3)
                        print("do you want to check your balance")
                        print("1.yes 2.no")
                        option=int(input())
                        if option==1:
                            balance=balance-amount
                            print("your current balance is",balance)
                            print("thank you for visiting")
                        else:
                            print("thank you visit again")
                    else:
                        print("insufficient balance")
                else:
                    print("enter the amount in multiple of 100")
            else:
                print("please enter the correct option")
        else:
            print("wrong pin")
    else:
        print("please enter only english")
else:
    print("insert card properly")
