#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    # class variable it is defined in the class - not in a method
    # you generally want to put immutable data in the class - not a list
    x = [1, 2, 3]

    def __init__(self, **kwargs):
        # underscore _ indicates it's a private variable and should not be set or retrieved outside the setter or getter
        # we are initialising 3 different variables - object variable
        # they only exist when an object is created from the class they do not exist in the class itself
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    # a function that is associated with a class is called a method
    # this provides the interface to the class and its objects

    # serves as both a getter and a setter - self makes it (type) a method instead of just a function
    # 2nd argument is t and has default value=None
    def type(self, t=None):
        # if there is a value for t (if we have given one) then it will set a type and return it
        if t: self._type = t
        return self._type

    def name(self, n=None):
        # you never want to set that directly from outside the class methods
        if n: self._name = n
        return self._name

    def sound(self, s=None):
        # if we have a value for s then  if s: = True
        if s:
            self._sound = s
        return self._sound

    # Special method which provides the string representation of the object
    # allows us to print it easil`y without needing a special function
    def __str__(self):
        # we read it using the getter method
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


def main():
    # we are creating 2 objects a0 a1 and printing them out.
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')

    print('a0', a0)

    # if we want to change the sound of the object then we call the method with a new input argument.
    a0.sound('bark')
    print('a0 after sound change to bark:', a0)

    print('a1:',a1)

    # shouldn't do that as its private object variable
    # they are bound to the object, not to the class itself.
    a0._name = 'Joe'
    print('a1._name:', a1._name)

    print('a0.x:', a0.x)

    # if we change the class variable like this all the objects get affected - as it's a class variable
    # x is not encapsulated - it is the same object for all objects of that class - in every instance of the class
    a1.x[0] =7
    print('a0.x:', a0.x)
    print('a1.x:', a1.x)

    # concept of Encapsulation:
    # if variables are encapsulated, that means that they belong to the object, and not to the class


if __name__ == '__main__':
    main()
