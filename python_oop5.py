# OOP - youtube - Corey Schafer - Python OOP Tutorial 1,2,3

#   Class
# Is basically a blueprint or the design of the entity for creating instances
# which defines the core properties and functions
# a logical definition or a type of object allowing new instances of that type to be made

#   Instance
# Each employee that we create using our employee class will be an instance of that class
#
# Instance variable contain data that is unique to each instance

# regular methods vs class methods vs static methods

#   Regular Methods:
# Regular methods in a class automatically take the instance as the first argument - self

#   Class Methods:
# A method which is bound to the class and NOT the object of the class - cls
# They have access to the state of the class as it takes a cass parameter that points to the class, not the object
# It can modify a class state that would apply across all the instances of the class

#   Static Methods:
# Don't operate on the instance or the class
# Can be called without an object for that class
# Cannot modify the state of an object as they are not bound to it

import datetime


class Employee:
    # create a class variable where it wouldn't make sense to use self
    # keep track of the number of employees that we have
    # the number of employees should be the same for all instances of our class
    nums_of_emps = 0

    # class variables are variables that are shared among all instances of a class
    # class's raise_amount
    raise_amt = 1.04

    # constructor - initialization of the class attributes
    # self is the instance
    # the __init__ method runs every time we create a new employee
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # each time we create a new employee we are going to increment that by one
        Employee.nums_of_emps += 1

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

    # using the class decorator
    @classmethod
    # here we are working with the class instead of the instance
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # using the class method as an alternative constructor
    # to allow them to pass in the string and we can create the employee for them
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # creates a new employee and return it
        return cls(first, last, pay)

    # static methods
    # don't take the instance or the class as first argument - they behave like regular functions
    # we include them in our classes because they have some logical connection with the class
    # a static method is if you don't access the instance or the class anywhere within the function
    @staticmethod
    def is_workday(day):
        # weekdays - Monday = 0 and Sunday = 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# 0 because we haven't instantiated the Employees yet
print(Employee.nums_of_emps)

# Unique instances of the class - instance variables
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)
print("\n")

print(emp_1.email)
print(emp_2.email)
print("\n")

# this is the manual way of the function fullname
print('{} {}'.format(emp_1.first, emp_1.last))
# this is the automatic way using the function fullname - this is a method so we need ()
print(emp_1.fullname())
# alternative way
print(Employee.fullname(emp_1))
print("\n")

# instance variables
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print("\n")

# Using a class - this changes the raise_amount for the class and all of the instances
# Employee.raise_amount = 1.05
# Using an instance assignment (instead of class) this changes the raise_amount for the emp_1
# also adds it to its own namespace and returns that value before going and searching for that class
emp_1.raise_amt = 1.05
print("\n")

# printing the namespace of emp_1
print(emp_1.__dict__)
print(Employee.__dict__)
print("\n")

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
# restoring the default value
emp_1.raise_amt = 1.04
print("\n")

# 2 because we instantiated 2 employees , emp_1 and emp_2
print(Employee.nums_of_emps)
print("\n")

Employee.set_raise_amt(1.05)
# alternative
# Employee.raise_amt = (1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("\n")

# some use class methods as alternative constructors
# this means that you can use these class methods in order to provide multiple ways of creating our objects

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# NOT needed because we created a class method as a constructor
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# from_string is a class method used as a constructor
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
print("\n")

# import datetime
# year, month, day - (ints) - in this case its a Sunday
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
print("\n")


##################################
class Calculator:

    def addNumbers(x, y):
        return x + y


# create addNumbers static method
Calculator.addNumbers = staticmethod(Calculator.addNumbers)

print('Product:', Calculator.addNumbers(15, 110))
print("\n")


class Calculator2:

    # create addNumbers static method
    @staticmethod
    def addNumbers(x, y):
        return x + y


print('Product:', Calculator2.addNumbers(15, 110))
