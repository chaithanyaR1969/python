class book:
  def __init__(self,pages):
    self.__pages=pages
  b1=book(100)
  print(b1.__pages)# it will give an error because to access this we have ti use setter() and getter().
