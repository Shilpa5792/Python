class Student:

   def __init__(self, name, id, marks):
      self.name = name
      self.id = id
      self.marks = marks

   def display(self):
      print("Name is " + str(self.name))
      print("Id is " + str(self.id))
      print("Marks are " + str(self.marks))


S1 = Student("Shilpa", 1, 88)
S1.display()


