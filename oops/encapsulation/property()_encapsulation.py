class person:
  def __init__(self):
    self.__name=" "
  def getter(self):
    return self.__name
  def setter(self,val):
    self.__name=(val)
  getset=property(getter,setter)
p1=person()
p1.getset="chaithanya"
res=p1.getset
print(res)
