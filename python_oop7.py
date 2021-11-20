# OOP - youtube - Corey Schafer - Python OOP Tutorial 5

#   Special methods - Magic methods
# Methods that we can use within our classes
# This is how we implement operator overloading


# parent class
class Employee:
    # class variables are variables that are shared among all instances of a class
    # class's raise_amount
    raise_amt = 1.04

    # constructor - initialization of the class attributes
    # self is the instance
    # the __init__ method runs every time we create a new employee

    # dunder init is a special method - the constructor
    def __init__(self, first, last, pay):
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # method
    # if we don't write self in brackets then error - 0 arguments needed 1 was passed - emp_1.fullname()
    # this is because the instance acts as an argument to the method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # using self.raise_amount will give us the ability to change that amount for a single instance
        # using the self here will allow any subclass to override that constant
        # instance.raise_amount
        self.pay = int(self.pay * self.raise_amt)
        # alternative
        # class.raise_amount
        # self.pay = int(self.pay * Employee.raise_amt)

    # Repr is meant to be an unambiguous representation of the object
    # Used for debugging and logging etc
    def __repr__(self):
        # return a string that we can use to recreate the object
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # Str is meant to be a more readable representation  of an object
    # Used as a display to the end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # method to add 2 employees together and have their result be their combined salaries
    def __add__(self, other):
        return self.pay + other.pay

    # method that returns the total number of characters in their full name
    def __len__(self):
        return len(self.fullname())

    # https://docs.python.org/3/reference/datamodel.html#special-method-names


# Unique instances of the class - instance variables
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# by using a method __repr__ we get a string that we specified there
print(emp_1)
print("\n")

print(repr(emp_1))
print(str(emp_1))
print("\n")

print(emp_1.__repr__())
print(emp_1.__str__())
print("\n")

print(emp_1 + emp_2)
print("\n")

print(len('test'))
print('test'.__len__())
print("\n")

print(len(emp_1))
print("\n")

# OOP - youtube - Corey Schafer - Python OOP Tutorial 6

# Property Decorator - Getters, Setters, and Deleters

class Employee2:
    # constructor
    def __init__(self, first, last):
        # instance variables
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@email.com'

    # no longer need to type .email() , just .email
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    # the method full name returns the current first and last name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_3 = Employee2('John', 'Smith')
emp_4 = Employee2('John', 'Smith')

# replacing an attribute will not change email
emp_3.first = 'Jim'


print(emp_3.first)
print(emp_3.email)
print(emp_3.fullname)
print('\n')

emp_4.fullname = ('Corey Scafer')
print(emp_4.first)
print(emp_4.email)
print(emp_4.fullname)
del emp_4.fullname
print("\n")


# What is the meaning of underscores ( _ and __ ) in Python variables when using OOP - classes
class Test:

    # the constructor of the class
    def __init__(self):
        # instance variables
        self.foo = 11
        # one underscore _ is not meant as part of the public interface of the class
        self._bar = 23
        # double underscore (or dunder) "private variable"
        self.__baz = 42


t = Test()

# Unique instances of the class - instance variables
print(t)

# if we go to the end of the dir we see that foo appears, and so does _bar
# _bar is indicated as a private variable - you should be careful when changing
# __baz is not shown in the dir but _Test__baz and this is the name mangling
# the python interpreter does this name mangling to prevent any collisions
# its more of a protection so that you don't have to worry about subclasses changing the attribute
print(dir(t))
print(t._bar)

# error
# print(t.__baz)

# AVOID THIS - ITS NOT MEANT TO BE USED - access them from the class only
print(t._Test__baz)




