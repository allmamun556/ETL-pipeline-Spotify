class Parent(object):
     def __init__(self):
         self.value = 4
     def get_value(self):
         return self.value
 
class Child(Parent):
     def get_value(self): #same method as parent class.
         return self.value + 1


c=Child()
print(c.get_value())

