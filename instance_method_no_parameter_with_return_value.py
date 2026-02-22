class calci:
    def __init__(self):
        self.brand="casio"
        self.color="black"
    def add(self):
        a=10
        b=20
        c=a+b
        return c

c1=calci()
print(c1.brand)
print(c1.color)
res=c1.add()
print(res)
