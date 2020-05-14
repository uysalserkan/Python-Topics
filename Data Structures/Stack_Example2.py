from Stack import *


def reverse_string(stack, string):
    for index in range(len(string)):
        stack.push(string[index])
    reverse_string = ""

    while not stack.isEmpty():
        reverse_string += stack.pop()

    return reverse_string


def main():
    myString = "My name is Serkan"
    blankStack = CustomStack()
    print(reverse_string(blankStack, myString))


if __name__ == "__main__":
    main()
