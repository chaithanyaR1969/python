def fun1():
  print("inside fun1")
def fun2(ptr):
  print("inside fun2")
  ptr1=ptr
  ptr1()
fun1()
fun2(fun1)
