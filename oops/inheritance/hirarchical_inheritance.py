class A:
  def disp_A(self):
    print("inside A")
class B(A):
  def disp_B(self):
    print("inside B")
class C(A):
  def disp_C(self):
    print("inside C")
b1=B()
c1=C()
b1.disp_A()
b1.disp_B()

c1.disp_A()
c1.disp_C()
