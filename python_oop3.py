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


class SoftwareEngineer:

    def __init__(self, name, age):

        # these can be accessed from the outside
        self.name = name
        self.age = age

        # these must be kept private
        # you can acess it using _salary but you shouldn't , use __ to make it fully private
        self._salary = None
        self._num_bugs_solved = 0
        # _x is called a "protected" attribute (one underscore)
        # __x is called a "private" attribute (double underscore)

    def code(self):
        self._num_bugs_solved += 1

    # these are the only ways to access this internal self._salary attribute
    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):

        # we can also check the value of salary or enforce constraints
        # if value < 1000:
        #     self._salary = 1000
        # if value > 20000:
        #     self._salary = 20000
        #
        self._salary = self._calculate_salary(base_value)

    # private function defined with _ at start (leading underscore)
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


# create an instance of the object
se = SoftwareEngineer("Max", 25)
# cannot use se.__salary but can use se._salary
print(se.age, se.name)

for i in range(70):
    se.code()

# print(se._num_bugs_solved)

# this is applying the abstraction principle
# only the hr department should only be able to set the salary but they don't care about
# the internal implementation and factor applyment
se.set_salary(6000)
print(se.get_salary())
