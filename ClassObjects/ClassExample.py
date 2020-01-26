class Box:
    width=10
    height=20


obj = Box()
print(obj.width)


#The __init__() function is called automatically every time the class is being used to create a new object.
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
