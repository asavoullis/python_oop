# inheritance
# a process by which one class takes on the attributes and methods of another class
# the newly formed class is then called child class
# and the other is called the parent class


# parent class
# can inherit, extend and override
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working ...")


# child class - inherits from Employee class
# inherits all of its attributes and functions from the employees
# inherits the init function from its parent class Employee
class SoftwareEngineer(Employee):

    # we are overwriting the init functionality of its parent class
    def __init__(self, name, age, salary, level):
        # super refers to its parent class
        super().__init__(name, age, salary)

        # extends the functionality
        self.level = level

    def work(self):
        print(f"{self.name} is coding...")

    def debug(self):
        print(f"{self.name} is debugging...")


# child class - inherits from Employee class
# inherits all of its attributes and functions from the employees
class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")


se = SoftwareEngineer("Max", 25, 6000, "Junior")
se.work()
print(se.level)
se.debug()


print("\n")
d = Designer("Philipp", 27, 7000)
print(d.name, d.age)
d.work()
d.draw()
print("\n")

# Polymorphism
# a way to use a class exactly like its parent but still each child just keeps its own methods as they are

employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
             SoftwareEngineer("Lisa", 30, 9000, "Senior"),
             Designer("Philipp", 27, 7000)]

# use of Polymorphism
def motivate_employees(listofemployees):
    for employee in listofemployees:
        employee.work()

motivate_employees(employees)

# Recap:
# inheritance: ChildClass(ParentClass)
# inherit, extend, override
# super().__init__
# polymorphism
