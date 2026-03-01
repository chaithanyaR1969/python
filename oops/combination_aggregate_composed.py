class car:
    def __init__(self,name):
        self.cname=name
    def getcar(self):
        print("car in in the road")

class brain:
    def __init__(self,status):
        self.bstatus=status
    def getbrain(self):
        print("everyone have brain")

class person:
    def __init__(self,name):
        self.pname=name
        self.b=brain("active")
        self.c=""
    def hascar(self,p):
        self.c=p

p1=person("harshi")
c1=car("maruthi")
p1.hascar(c1)
print(p1.b.bstatus)
p1.b.getbrain()
print(p1.c.cname)
p1.c.getcar()
del p1
print(c1.cname)
print(p1.b.bstatus)#gives error
