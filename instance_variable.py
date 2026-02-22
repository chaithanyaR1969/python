class tv:
    def __init__(self):
        self.brand="samsung"
        self.color=("black")
    def display(self):
        self.cost=50000
        print(self.cost)
        print(self)
t1=tv()
print(t1.brand)
print(t1.color)
t1.display()
print(t1.cost)
print(t1)
