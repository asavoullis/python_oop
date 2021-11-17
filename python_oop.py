# Principles of Object Oriented Programming:
#   Inheritance
#   Polymorphism
#   Encapsulation
#   Abstraction

# Lesson1
# create a class - blueprint
# create an instance - object
# instance attributes are defined in __init__(self) function
# class attributes

# Lesson2
# create instance method(self)
# methods can take arguments and can return values
# special "dunder" (__str__ and __eq__) methods
# @staticmethod


# 	CLASS
# a blueprint or the design of an entity
# which defines the core properties and functions
# a logical definition or a type
# Male is a class where Alkis is the object - object with the name Alkis

# 	Object
# An object is an instance of a class which has physical existance

#   position, name, age, level, salary
# software engineers
se1 = ['Software Enginer', 'Max', 20, 'Junior', 5000]
se2 = ['Software Engineer', 'Lisa', 25, 'Senior', 7000]
se3 = ['Software Engineer', 'Lisa', 27, 'Senior', 7000]

#  designer
d1 = ['Designer', 'Philipp']



# class - a blueprint of this data structure
class SoftwareEngineer:
    # class attribute
    alias = 'Keyboard Magician'

    # special method used to initialize our object
    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}')

    # def information(self):
    #     information = f'name = {self.name}, age = {self.age}, level ={self.level}'
    #     return information

    # dunder method
    # will be executed whenever our object is converted into string
    def __str__(self):
        information = f'name = {self.name}, age = {self.age}, level ={self.level}'
        return information

    # here we compare 2 objects
    def __eq__(self, other):
        # if both name and age of the 2 objects are the same it returns True otherwise False
        return self.name == other.name and self.age == other.age


    # decorator
    @staticmethod
    # we can only use this only function on the class but not on an instance
    # this is because we didn't use the self parameter
    # this is not tied in a specific instance - so you cannot access instance attributes
    def entry_salary(age):
        # you cannot use self.age
        # you cannot access the self attributes
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# instance se1
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
print(se1.name, se1.age)

# instance se2
se2 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)
print(se2.name, se2.age, se2.level)

# instance se3
se3 = SoftwareEngineer('Lisa', 27, 'Senior', 7000)
print(se3)

print(SoftwareEngineer.alias)

se1.code()
se2.code()

se1.code_in_language('Python')
se2.code_in_language('C++')

print(se1)

print(se2)

print(se2 == se3)

#this would crash without @staticmethod
print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))

#   Inheritance
# Is the process by which one class takes on the attributes and methods of another.
# Newly formed classes are called child classes, and the classes that child classes are derived from
# are called parent classes.

# Child Classes inherit all of the parent's attributes and methods but can also extend and override
# attributes and methods that are unique to themselves.

#   Polymorphism - Many Shapes
# We can write a code that works on the superclass, it will work with any subclass type as well.
# Give a way to use a class exactly like its parent, but each class keeps its own methods as they are.
#
# Concept that allows us to define more than one way to do something.
# Either by using a different process for it or by using different parts to do it.
# By overriding or overloading

#   Encapsulation
# Is the mechanism of hiding data implementation.
# Instance variables are kept private and accessor methods are made public to achieve this.
# With this, we restrict access to public methods (getter/setter).
# Instance methods are kept private
#
# Binding properties with functions in a class - leads to data hiding

#   Abstraction
# Can be thought as a natural extension of encapsulation.
# Applying abstraction means that each object should only expose a high-level mechanism for using it.
# This mechanism should hide internal implementation details.
# It should only reveal operations relevant for the other objects.

