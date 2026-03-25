n=int(input())
prod=1
while n>0:
    d=n%10
    prod*=d
    n=n//10
print(prod)

#OR

#using function
def mul(n):
    mul=1
    while n>0:
        d=n%10
        mul*=d
        n=n//10
    return mul
n=int(input())
print(mul(n))