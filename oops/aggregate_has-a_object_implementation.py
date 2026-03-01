class charger:
    def __init__(self,name):
        self.cname=name
    def charging(self):
        print("mobile is charging")
class mobile:
    def __init__(self,name):
        self.mname=name
        self.c=""
    def hasMobile(self,p):
        self.c=p
m1=mobile("oppo")
c1=charger("cpin")
m1.hasMobile(c1)
print(m1.c.cname)
m1.c.charging()
del m1
print(c1.cname)
c1.charging()
