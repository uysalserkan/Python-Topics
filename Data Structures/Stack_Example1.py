from Stack import *


def is_match(first, second):
    if first == "(" and second == ")":
        return True

    if first == "{" and second == "}":
        return True

    if first == "[" and second == "]":
        return True

    else:
        return False


def is_paranthesis_balanced(paren_str):
    checker = CustomStack()
    isBalanced = True
    index = 0

    while index < len(paren_str) and isBalanced:
        par = paren_str[index]
        if par in "([{":
            checker.push(par)
        else:
            if checker.isEmpty():
                isBalanced = False
            else:
                top = checker.pop()
                if not is_match(top, par):
                    isBalanced = False

        index += 1
    if checker.isEmpty() and isBalanced:
        return True
    else:
        return False


def main():
    print("String : (((({})))) Balanced or not?")
    print(is_paranthesis_balanced("(((({}))))"))
    print("String : [][]]] Balanced or not?")
    print(is_paranthesis_balanced("[][]]]"))
    print("String : [][] Balanced or not?")
    print(is_paranthesis_balanced("[][]"))


if __name__ == "__main__":
    main()
