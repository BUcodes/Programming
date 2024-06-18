# Iheritance -an object feature that a class to be modeled after another class, called the parent class

# Example 1
class Person:           # parent class
    """Class representing one person"""
    
    def __init__(self, lastname, firstname):
        """Constructor our class"""
        self.lastname = lastname
        self.firstname = firstname
    
    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"{self.firstname} {self.lastname}"
    
class SpecialAgent(Person):  # <--- Inherits from Person
    """A class that defines a special agent.
    It inherits from the class Person."""
        
    def __init__(self, name, firstname, id_number):
        """An agent is defined by his name and personnel number"""
    
        Person.__init__(self, name, firstname) #explicitly call the Person constructor
        self.id_number = id_number

    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"Agent {self.lastname}. {self.firstname} {self.lastname}, ID {self.id_number}"
         
agent = Person("Femi", "Remi")
agent_007 = SpecialAgent("Do", "Lu", "007")
print(agent)
print(agent_007)
     
     
# Example 2
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"I am {self.name} and I am {self.age} years old.")


class Dog(Animal):
    def __init__(self, name, age):

        self.name = name
        self.age = age
        self.type = "dog"

# Call child class
t = Dog("Snoopy", 5)
t.speak()


## Super() function
"""allows us to refer the superclass implicitly, thereby making our task easier and comfortable"""

# Example 1:
# Parent Class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"I am {self.name} and I am {self.age} years old.")

# Child class
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)         #referring to the parent class implicitly
        self.type = "dog"

# Call child class
t = Dog("Snoopy", 5)
t.speak()

# Example 2:
class A:
    def __init__(self):
        print("Initializing: class A")

    def sub_method(self, b):
        print("Printing from class A:", b)
        
    def __new_method(self, n):
        print(f"This is new method {n}")


class B(A):  # <-- Inherits from A
    def __init__(self):
        print("Initializing: class B")
        super().__init__()

    def sub_method(self, b):
        print("Printing from class B:", b)
        super().sub_method(b + 1)


class C(B):  # <-- Inherits from B
    def __init__(self):
        print("Initializing: class C")
        super().__init__()

    def sub_method(self, b):
        print("Printing from class C:", b)
        super().sub_method(b + 1)


if __name__ == "__main__":
    c = C()
    c.sub_method(1)
    c._A__new_method(8) #access protected method from parent class
    
#self._Parent__private_method()


# Examplen 3 --> child class method overwrites parent class when super fn not used
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"I am {self.name} and I am {self.age} years old.")


# Child class
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    # This will override the speak() method of the parent class:
    def speak(self):
        print("I am a dog.")


# Call child class
t = Dog("tyson", 5)
t.speak()



