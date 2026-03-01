class plane:
    def takeoff(self):
        print("plane is takingoff")
    def fly(self):
        print("plane is flying")
class passanger(plane):
    def land(self):
        print("plane is landing")
class cargo(plane):
    def land(self):
        print("plane is landing")
class fighter(plane):
    def land(self):
        print("plane is landing")
p1=passanger()
c1=cargo()
f1=fighter()
def allowanimal(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
allowanimal(p1)
allowanimal(c1)
allowanimal(f1)
