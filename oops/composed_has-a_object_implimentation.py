class os:
    def __init__(self):
        self.status=True
        print("os is installing")
        print("os is ready")
    def hasmobile(self):
        print("mobile has os")
class mobile:
    def __init__(self,name):
        self.mname=name
        self.o=os()
        print("mobile is ready")
        print("with os installed")
m1=mobile("mi")
print(m1.mname)
print(m1.o.status)
m1.o.hasmobile()
del m1
print(m1.o.status)
