n=int(input("enter the number"))
i=1
s=0
while i<=n:
    s=s+i
    i=i+1
print(s)

#OR
n=int(input("enter the number"))
for i in range(1,n+1):
     s=s+i
print(s)