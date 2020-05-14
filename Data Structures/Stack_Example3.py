from Stack import CustomStack


def convert_int_to_bin(dec_num):
    blankStack = CustomStack()
    while dec_num != 0:
        if(dec_num % 2 == 0):
            blankStack.push(0)
        else:
            blankStack.push(1)
        dec_num = dec_num // 2

    numberString = ""

    while not blankStack.isEmpty():
        numberString += str(blankStack.pop())

    return numberString


def main():
    print(convert_int_to_bin(25))


if __name__ == "__main__":
    main()
