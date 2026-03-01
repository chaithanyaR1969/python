class A:
    def disp_A(self):
        print("inside A")

class B(A):
    def disp_B(self):
        print("inside B")

class C(A):
    def disp_C(self):
        print("inside C")

class D(B, C):   # Multiple inheritance
    def disp_D(self):
        print("inside D")

d1 = D()

d1.disp_A()
d1.disp_B()
d1.disp_C()
d1.disp_D()
