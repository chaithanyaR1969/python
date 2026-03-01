class A:
  def disp_A(self):
    print("inside A")
class B(A):
  def disp_B(self):
    print("inside B")
class C(B):
  def disp_C(self):
    print("inside C")
c1=C()
c1.disp_A()
c1.disp_B()
c1.disp_C()
