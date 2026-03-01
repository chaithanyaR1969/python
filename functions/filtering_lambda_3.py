m=lambda x: x%2==0
res=list(filter(m,l))
print(res)

r=list(filter(lambda x:x%2==0,l))
print(r)
