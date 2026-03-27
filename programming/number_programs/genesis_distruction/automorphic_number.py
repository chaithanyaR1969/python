n=int(input('enter the value:'))
sqr=n**2
if str(sqr).endswith(str(n)):
    print("automorphic number")
else:
    print("not automorphic number")