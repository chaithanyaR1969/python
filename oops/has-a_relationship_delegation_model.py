class Radio:
    def turnon(self,x):
        if x==1:
            print("radio is on")
        else:
            print("radio is off")
class Car:
    def __init__(self,min,max):
        self.cmin=min
        self.cmax=max
        self.r=Radio()#creating an object and self.r is instance variable
c1=Car(30,120)
print(c1.cmin)
print(c1.cmax)
c1.r.turnon(1)
c1.r.turnon(0)
