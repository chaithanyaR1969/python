n=int(input("enter the number:"))
sum=0
for i in str(n):
    num=int(i)
    sum=sum+num**len(str(n))
if sum==n:
    print("armstrong number")
else:
    print("not armstrong number")