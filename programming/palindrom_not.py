str1=input("enter string")
out=("")
for i in str1:
    out = i+out
if str1==out:
    print("palindrom")
else:
    print("not palindrom")