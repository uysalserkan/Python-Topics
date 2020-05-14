""" 
* Custom Data Structure -> Stack
"""


class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def getStack(self):
        return self.items

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]


def main():
    myStack = CustomStack()
    myStack.push(2)
    myStack.push(5)
    myStack.push(12)
    myStack.push(15)
    myStack.push(-1)
    print(myStack.getStack())
    print(myStack.isEmpty())
    print(myStack.peek())


if __name__ == "__main__":
    main()
