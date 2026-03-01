class plane:
    def takeoff(self):
        print("plane is takingoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
class passanger(plane):
    def carry_p(self):
        print("plane carries p")
class cargo(plane):
    def carry_g(self):
        print("plane carries g")
class fighter(plane):
    def carry_w(self):
        print("plane carries w")
p1=passanger()
c1=cargo()
f1=fighter()
p1.takeoff()
p1.fly()
p1.land()
p1.carry_p()
c1.takeoff()
c1.fly()
c1.land()
c1.carry_g()
f1.takeoff()
f1.fly()
f1.land()
f1.carry_w()
