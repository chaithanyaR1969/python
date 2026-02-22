class fan:
    def __init__(self):
        self.brand="usha"
        self.color="brown"
        self.cost=2000
        self.wings=3
    def on(self):
        print("fan is on")
    def rotate(self):
        print("fan is rotating")
    def off(self):
        print("fan is off")
f1=fan()
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.wings)
f1.on()
f1.rotate()
f1.off()
