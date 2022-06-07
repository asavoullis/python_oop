#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Parent class
class Animal:
    # a base class that is going to be inherited in order to be used.
    def __init__(self, **kwargs):
        # we are no longer providing any default values
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t=None):
        # it attempts to return the value and if that fails, it returns none instead
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n: self._name = n
        try: return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError:
            return None


# Child class
class Duck(Animal):
    def __init__(self, **kwargs):
        # we set the type to duck
        self._type = 'duck'
        # we check if there is a type in the keyword arguments and if there is we delete it.
        if 'type' in kwargs: del kwargs['type']
        # through the super function we call the parent class initializer with our kwargs
        # super always calls the parent class
        super().__init__(**kwargs)


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    # s will be the string that will identify of its prey
    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')


""" Extending built-in class str """
# here we are inheriting from the class str - this is a built-in python class - we change the built-in class
class RevStr(str):
    # Overwriting the str representation method - instead of return the string its self we return its reverse
    def __str__(self):
        # slice of the string where the step goes backwards - we reverse the string
        return self[::-1]


# an iterator is a class that provides a sequence of items, generally used in a loop
class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'expected at most 3 arguments, got {numargs}')

        # we initialise the starting point of our iterator
        self._next = self._start

    # special iterator method - identifies this object as an iterator object
    def __iter__(self):
        return self

    # next function which is the iteration its self which is a construct like the for loop is going to look for this
    # next function in order to use it for iteration
    def __next__(self):
        # if we reach the stop we raise the StopIteration exception
        if self._next > self._stop:
            raise StopIteration
        else:
            # otherwise we go ahead and increment
            _r = self._next
            self._next += self._step
            return _r


class Random_repr:
    def __init__(self, n):
        self.n = n

    # it will print the value returned by the special method
    def __repr__(self):
        return f'repr: the number is {self.n}'


    def __str__(self):
        return f'str: the number is {self.n}'

def main():
    a0 = Kitten(name='fluffy', sound='rwar')
    a1 = Duck(name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    a0.kill('humans')
    print('')

    hello = RevStr('Hello, World.')
    print(hello, '\n')

    print('Inclusive Range:')
    for n in inclusive_range(25):
        print(n, end=' ')
    print()
    for n in inclusive_range(5, 25):
        print(n, end=' ')
    print('\n')

    print('Repr:')
    s = 'Hello World'
    # repr (representation) will print the best possible string representation of an object
    print(repr(s), '\n')
    n = Random_repr(47)
    print(repr(n))
    # same output
    # the repr function will either print the return from the repr of the class or if it doesn't have that
    # it will print the name of the class + object + memory location
    # now that we added the __str__ method it will print the str method and not the repr version
    print(n)
    print(repr(n))
    # so if you do have the string version it will default to the str version if you don't it will use the rpr version
    # if you don't have either of them it will print class+object+memory loc

    print('\n')
    # works just like repr - uses the repr method, but it will escape any special characters - like emojis
    print('ascii: ', ascii(n))
    # the chr function prints the character represented by that unicode position number - the character of a number
    print(chr(128406))
    # ord function gives you the unicode position number for that character
    print(ord('🖖'))


if __name__ == '__main__':
    main()
