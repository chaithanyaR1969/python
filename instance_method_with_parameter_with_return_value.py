class calci:
    def __init__(self):
        self.brand="casio"
        self.color="black"
    def add(self,a,b):
        c=a+b
        return(c)

c1=calci()
print(c1.brand)
print(c1.color)
x=10
y=20
res=c1.add(x,y)
print(res)
