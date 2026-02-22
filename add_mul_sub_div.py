class calci:
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c2=a-b
        return c2
    def mul(self,a,b):
        c3=a*b
        return c3
    def div(self,a,b):
        c4=a/b
        return c4
c1=calci()
x=10
y=20
res1=c1.add(x,y)
print(res1)
res2=c1.sub(x,y)
print(res2)
res3=c1.mul(x,y)
print(res3)
res4=c1.div(x,y)
print(res4)
