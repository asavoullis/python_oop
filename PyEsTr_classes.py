""" https://www.linkedin.com/learning/python-essential-training-2018/creating-a-class?autoplay=true&contextUrn=urn
%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=41294332 """


class Duck:
    # class variable - global
    # access using Duck.sound instead of self
    # values are same for all objects
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    # class constructor - special class method/function name __init__ - acts as initializer
    # the self points as the object
    def __init__(self, movement):
        # instance variables - because every object has a different value for this
        self.movement = movement

    # self is reference to the object - not the class
    # when an object is created from the class, self will reference that object
    def quack(self):
        print(self.sound)

    def move(self):
        # global class variable - value same for all objects
        Duck.movement = 'Walks like a dizzy duck. '
        print(Duck.movement)

        # instance variable - can be different for each object
        print('is', self.movement)


class Animal:
    # class constructor
    # we pass it parameters to initialise object variables - they are never initialised until after the object is defined
    # they don't exist in the class without having been constructed into an object
    def __init__(self, type, name, sound):
        # instance variables - because every object has a different value for this
        # __ for private / naming convention
        self._type = type
        self._name = name
        self._sound = sound

    # getters or accessors used to access those object variables
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


class Animal2:
    # alternative way - to pass multiple arguments
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name']
        self._sound = kwargs['sound']

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    """ Expects an Animal object and prints the animal """
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    print(' Donald')
    # we defined a variable donald from the class Duck
    # donald is the object because it was instantiated from the class
    # an instance of a class is called an object - donald
    donald = Duck('not dizzy')

    # invoke the object method quack on the object donald
    # the . dot operator dereferences the object so that we can get to the method - quack
    donald.quack()
    donald.move()

    print('\n', 'Daisy')

    daisy = Duck('dizzy')
    daisy.quack()
    daisy.move()

    print('')
    # an instance of a class is called an object = a0 & a1
    # we initialise them with various parameters
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')

    print_animal(a0)
    print_animal(a1)

    print_animal(Animal('velociraptor', 'veronica', 'hello'))
    print('')

    print('Jenny')
    a3 = Animal(type='cat', name='jenny', sound='meow')
    print(a3.sound())

    print('')
    print_animal(Animal2('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()
