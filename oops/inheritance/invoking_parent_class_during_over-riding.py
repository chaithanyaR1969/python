class A:
    def disp(self):
        print("inside A")
class B(A):
    def disp(self):
        print("inside B")
class C(B):
    def disp(self):
        print("inside C")
        B.disp(self)
        A.disp(self)
c1=C()
c1.disp()
