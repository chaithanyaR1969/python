class animal:
    def eat(self):
        print("animals eat")
    def sleep(self):
        print("animals sleep")
    def hunt(self):
        print("animals hunt")
class lion(animal):
    pass
class cat(animal):
    pass
class whale(animal):
    pass
l1 = lion()
c1 = cat()
w1 = whale()
l1.eat()
l1.sleep()
l1.hunt()
c1.eat()
c1.sleep()
c1.hunt()
w1.eat()
w1.sleep()
w1.hunt()
