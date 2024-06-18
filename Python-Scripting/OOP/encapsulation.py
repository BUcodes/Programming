# Encapsulation is one of the fundamental concepts of object-oriented programming (OOP
# idea of data encapsulation and the methods that work with data within a unit
# limits direct access to variables and methods and can prevent accidental modification of data

# PUBLIC METHOD
"""All methods and attributes default to public in Python.
if you want to put your attributes and methods in public you don't have to do anything at all"""



# PROTECTED METHOD
"""accessible only from within the class and it`s subclasses
By prefixing the name of your member with a single underscore_"""

# Example:
class Blackboard:
    """Class defining a surface on which to write,
    that can be read and deleted, by a set of methods. The modified attribute
    is "surface" """

    def __init__(self):
        """By default, our surface is empty"""
        self._surface = ""

    def write(self, message_written):
        """Method for writing on the surface of the table.
        If the surface is not empty, we skip a line before adding
        the message to be written"""

        if self._surface != "":
            self._surface += "\n"
        self._surface += message_written

    def read(self):
        return self._surface
    
board = Blackboard()
board.write("another message")
board._surface = "Hello guys"
board.read()
     
     
     
# PRIVATE METHOD
"""make your methods and attributes inaccessible, even for child classes, then you must declare them privately using double underscore __"""


class Parent:
    def __init__(self):
        self.__private_method() # private method can be invoked during the initialization of an object

    def __private_method(self):
        print("This is a private method in the Parent class.")

class Child(Parent):
    def call_private_method(self):
        # Accessing the private method indirectly
        self._Parent__private_method()

# Example usage:
parent_obj = Parent()  # This will call the private method in the Parent class.

child_obj = Child()
child_obj.call_private_method()  # This will call the private method in the Parent class.


# A method can be called in the initialization of an object
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

        # Call a public method during initialization
        self.display_info()

    def display_info(self):
        """Display information about the car."""
        print(f"Car: {self.make} {self.model}")

    def start_engine(self):
        """Start the car's engine."""
        print("Engine started.")
        
my_car = Car(make="Toyota", model="Camry")
print(my_car)
