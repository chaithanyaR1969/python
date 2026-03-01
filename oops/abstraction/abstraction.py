from abc import ABC, abstractmethod
class vehical(ABC):
    @abstractmethod
    def sound(self):
        pass
class car(vehical):
    def sound(self):
        print("car is making paw paw sound")
c1=car()
c1.sound()
