# OOP - youtube - Corey Schafer - Python OOP Tutorial 4

#   Inheritance
# Allows us to inherit attributes and methods from a parent class
# We can create subclasses and get all the functionality of our parent class,
# then we can override or add new functionality without affecting the parent class


# parent class
class Employee:
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


# child class - inherits from the Employee class
class Developer(Employee):

    # override - doesn't affect parent class
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # lets the parent class - Employee - handle the first, last and pay arguments
        # calling the parent class init method
        super().__init__(first, last, pay)
        # alternarive way of calling the parent class init method
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


# subclass-child class that inherits from parent class
class Manager(Employee):

    # we used employees = None instead of an empty list [] because we don't want to pass in multiple data types
    def __init__(self, first, last, pay, employees = None):
        # lets the parent class - Employee - handle the first, last and pay arguments
        # calling the parent class init method
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # method to add employee in the list
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # method to remove employee from the list
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # method to print all employees that the manager supervises
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())



# Unique instances of the class - instance variables
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(help(Developer))
print("\n")

print(dev_1.email)
print(dev_1.prog_lang)
print("\n")

print(dev_2.email)
print(dev_2.prog_lang)
print("\n")

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print("\n")

print(mgr_1.email)
print("\n")

mgr_1.add_emp(dev_2)
mgr_1.print_emp()
print("\n")

# isinstance() issubclass()

#   isinstance()
# will tell us if an object is an instance of a class

# True mgr_1 is an instance of a Manager
print(isinstance(mgr_1, Manager))
# True mgr_1 is an instance of an Employee
print(isinstance(mgr_1, Employee))
# False because even though both mgr_1 and Developer inherit from Employee they aren't part of each others inheritance
print(isinstance(mgr_1, Developer))
# False - its a subclass
print(isinstance(Developer, Employee))
print("\n")

# subclass()
# returns true if Manager is a subclass of Employee
print(issubclass(Manager, Employee))
# True
print(issubclass(Developer, Employee))
# True
print(issubclass(Manager, Employee))
# False
print(issubclass(Manager, Developer))
print("\n")



