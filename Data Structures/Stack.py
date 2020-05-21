""" 
* Custom Data Structure -> Stack
"""


class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def getStack(self):
        return self.items

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1].data  # data is optimization for Binary Tree

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def __str__(self):
        s = ""
        for i in range(self(self.items)):
            # data is optimization for Binary Tree
            s += str[self.items[i].data] + "->"
        return s


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
