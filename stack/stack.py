# LIFO Principle of Stack Datastructure

class Stack:
    # class variable - global
    # access using Stack.__array2 instead of self
    # values are same for all objects
    __array2 = []

    def __init__(self):
        # instance variables - because every object has a different value for this
        # __ for private
        self.__array = []

    def push(self, item):
        self.__array.append(item)

    def pop(self):
        if len(self.__array) > 0:
            last_item = self.__array[-1]
            del self.__array[-1]
            return last_item
        else:
            # raise Exception
            return None

    # the __str__ allows you to have a printable format for your object
    def __str__(self):
        # doesn't work if it's not strings in the array
        # return ",".join(self.__array)

        return self.__array.__str__()
