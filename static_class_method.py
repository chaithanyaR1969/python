class Mobile:
    def __init__(self):
        self.brand="realme"
    def display(self):
        print("mobile display")
    @staticmethod
    def call():
        print("mobile call")
    @classmethod
    def game(cls):
        print("we can play games")

m1=Mobile()
print(m1.brand)
m1.display()
m1.call()
m1.game()
Mobile.call()
Mobile.game()
Mobile.display()
