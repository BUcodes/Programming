
# Intro to Object-oriented Programming

## class is a blueprint for an object, the object is the actual item.
print (type(None))
print (type(type))

## creating car class

class Car:
    def __init__(self): # method that defines the attribute of the class
        '''start with a constructor. constructor is a method 
        of our object responsible for creating our attribute '''
        
        self.name = "Ferrari" # instatiation of our name attribute
        self.model = "F40" # instatiation of our model attribute
        self.year = "2020" # instatiation of our year attribute
        
# bombo is the name of my class instance. Class instance and object are synonyms.
bombo= Car()
bombo.model = "250"
bombo.year = "2020"
print(type(bombo))
print(bombo.name)

# You can create an attribute for your object at any time:
bombo.model = "250"
print(bombo.model)

## Creating person class

class Person:
  '''Class defining a person characterized by :
  - his name
  - his first name
  - his age
  - his place of residence'''

  def __init__(self, name, firstname):
      '''Constructor our class'''
      self.name = name
      self.firstname = firstname
      self.age = 34
      self.place_residence = "Brussels"
      self.birthday = ""


coach = Person("Patho", "Ludovic")
print(coach)
coach.birthday= "24/06/1984"
print(coach.birthday)

# count the number of objects created
class Counter:
  """This class has a class attribute (`objects_created`) that is incremented at each
  time you create an object of this type"""

  objects_created = 0  # The counter is 0 at the start
  # we define our class attribute directly before defining the constructor

  def __init__(self):
      """Each time we create an object, we increment the counter"""
      Counter.objects_created = Counter.objects_created + 1

print(Counter.objects_created)

# Create a first object
a = Counter()
# Let's check that the counter has been incremented correctly
print(Counter.objects_created)
b = Counter()
print(b.objects_created)  # You can also access it using the object
# NB: It can be useful to have class attributes, when all our 
# objects must have some identical data.


## Creating a Blackboard object which we can read and delete

# Attributes are variables specific to our object, used to xterize it. 
# Methods are actions acting on the object 

class Blackboard:
  """Class defining a surface on which to write, by a set of methods. 
  The modified attribute is `surface`"""

  def __init__(self):
      """By default, our surface is empty"""
      self.surface = ""
  def write(self, message_written):
      '''Method for writing on the surface of the table.
        If the surface is not empty, we skip a line before adding
        the message_written '''

      if self.surface:
          self.surface += "\n"
      self.surface += message_written


board = Blackboard()
# Check if blackboard is empty
print(board.surface)

## Notes

board = Blackboard()

# Check if blackboard is empty
print(board.surface)
board.write("Coooool ! I love this one") # same as Blackboard.write(board,...)
print(board.surface)
board.write("Have a good start of the school year!")
print(board.surface)

#create another instance of the class
b = Blackboard()
# same as Blackboard.write(b,...)
b.write("No gree for anybody!")
# b and board have different attributes
print(b.surface) 

# both do the same action
board.write("Hello Swartz")
Blackboard.write(board, "Hello Turing")
print(board.surface)

# And yes, the help comes from reading the docstring of the associated method
help(Blackboard.write)
Blackboard.write(board, "try")
print(board.surface)

board.write("Hello everyone")
board.write("How you dey")
board.read()
board.reset()

# It's worth the effort to get good documentation on ones classes, isn't it?
#help (Blackboard)

print (dir(Blackboard)) # returns list of attributes and object methods
print (Blackboard.__dict__) #contains dico: key-name of attributes, values- values of attributes