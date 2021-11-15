# Encapsulation and abstraction

# Encapsulation is the mechanism of hiding of data implementation
# this means instance variables are kept private and there is only one accessor method from the outside
# with which we can access or change these instance variable so with with this we restrict the access to public methods
# so called getter and setter methods and we can also do the same for methods so instance methods can be kept private
# so that they can only be used internally and not from the outside

# abstraction is a natural extension of encapsulation
# applying abstraction means that each object should only expose a high level mechanism for using it
# so this mechanism should hide internal implementation details
# it should only reveal the operations relevant for the other objects


# applying this encapsulation principle
class SoftwareEngineer:

    def __init__(self):
        # these must be kept private
        # you can acess it using _salary but you shouldn't , use __ to make it fully private
        self._salary = None
        self._num_bugs_solved = 0
        # _x is called a "protected" attribute (one underscore)
        # __x is called a "private" attribute (double underscore)

    # use of property decorator
    # getter
    @property
    def salary(self):
        # we can use checks or constraints or internal calculations
        return self._salary

    # setter
    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary


se = SoftwareEngineer()

# instead of calling this function we can:
#se._salary(6000)
se.salary = 6000

# you can use the del
#del se.salary

print(se.salary)

# Recap
# Encapsulation
# abstraction
# public, private methods and attributes
# _foo(), _x (function, attribute)
# getter / setter  - only way to access them from the outside
# getter -> @property
# setter -> @x.setter
