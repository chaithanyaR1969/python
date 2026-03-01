class A:
  def __init__(self):
    self.a=10
class B(A):
  def __init__(self):
    A.__init__(self)#PCN.__init__(self)(parent class name)
    self.b=20
b1=B()
print(b1.b)
print(b1.a)
    
    
  
