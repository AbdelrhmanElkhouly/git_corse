# class Car:
#     name = 'toyota'
#     model = 'corolla'
#     year = 2020
#     def open(self):
#         print("car is open")
# c1 = Car()
# print(c1.name)
# print(c1.model)
# print(c1.year)  
# c1.opon()

# Example of a simple class with a class variable named x
class MyClass:
  x = 5 # class variable

p1 = MyClass()
print(p1.x)
#The examples above are classes and objects in their simplest form,
#  and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.
# The __init__() function is called automatically every time the class is being used to create a new object.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
      has_brain = True # class variable
      has_heart = True # class variable
      def __init__(self, name, age): # constructor with parameters
        self.name = name # instance variable
        self.age = age   # instance variable
      def __str__(self): # to print the object
        return f"name is {self.name} and have({self.age}) years old"
      #we can also create our own function 
      def age_in_days(self):
          return self.age * 365


p1 = Person("John", 36) # create object and pass values to the constructor
print(p1.name) # access instance variable
print(p1.age)  # access instance variable
print('class attribute ' , p1.has_brain) # access class variable
print('class attribute ' , p1.has_heart) # access class variable


p2 = Person("ali", 28) # create object and pass values to the constructor
print(p2.name) # access instance variable
print(p2.age)  # access instance variable
print('without str function ',p2)#before tr function 
print("age in days ",p2.age_in_days()) # call the method