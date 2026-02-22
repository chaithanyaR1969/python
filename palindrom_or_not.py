str=input("enter a string:")
rev=""
for i in str:
    rev=i+rev
if rev==str:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
