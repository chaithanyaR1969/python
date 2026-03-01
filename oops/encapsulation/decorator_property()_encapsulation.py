class person:
  def __init__(self):
    self.__name=" "
  @property
  def dataAccess(self):
    return self.__name
  @dataAccess.setter
  def dataAccess(self,val):
    self.__name=(val)
p1=person()
p1.dataAccess="chaithanya"
res=p1.dataAccess
print(res)
