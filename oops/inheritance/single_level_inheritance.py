class A:
  def disp_A(self):
    print("inside A")
class B(A):
  def disp_B(self):
    print("inside B")

b1=B()
b1.disp_B()
b1.disp_A()
