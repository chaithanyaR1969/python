class farmer:
    def __init__(self,P,T,R):
        self.principle=P
        self.time=T
        self.rate=R
    def loan(self):
        si=(self.principle*self.time*self.rate)/100
        print(si)
f1=farmer(300000,5,2.5)
f2=farmer(400000,3,2.5)
f1.loan()
f2.loan()
