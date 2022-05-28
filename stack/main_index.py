from stack import Stack


def main():
    stack1 = Stack()
    stack2 = Stack()

    stack1.push(1)
    stack1.push(2)
    print(stack1.pop())

    stack2.push(3)
    stack2.push(4)
    stack2.pop()
    stack2.push(5)
    stack2.push(6)

    print(stack1)
    print(stack2)


if __name__ == '__main__':
    main()
