class A:
    def disp(self,a,b,c):
        print(a)
        print(b)
        print(c)
class B(A):
    def disp(self,a,b):
        print(a)
        print(b)
class C(B):
    def disp(self,a):
        print(a)
c1=C()
c1.disp(10)#gives 10 a output
c1.disp(10,20)#error
c1.disp(10,20,30)#error
