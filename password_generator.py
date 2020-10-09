# https://github.com/uysalserkan/

"""This scripts generate password.
Default state is State 4 and default length is 8.
State 1: Only lower characters are allowed.
State 2: Only lower and upper characters are allowed.
State 3: Only lower, upper characters and numbers are allowed.
State 4: Upper, lower and Special characters and numbers are allowed.
"""

import fire
import string
import random


class Password(object):
    """METHODS:
        generate_password(state, length)
    """

    @staticmethod
    def generate_password(state=4, length=8) -> None:
        """DESCRIPTION:
            You could generate a specified password on your local machine.

            State 1: Only lower characters are allowed.
            State 2: Only lower and upper characters are allowed.
            State 3: Only lower, upper characters and numbers are allowed.
            State 4: Upper, lower and Special characters and numbers are allowed.

            You can also select `python password_generator.py --state=3 --length=16`
            on commandline or directly write `python password_generator.py 3 16`.

        ARGUMENTS:
            state: Which state selected on commandline.
            length: Password length.
        """
        generated = []
        try:
            if state == 1:
                for i in range(length):
                    generated.append(string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase) - 1)])

            elif state == 2:
                for i in range(length):
                    generated.append(string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)])

            elif state == 3:
                passlist = string.ascii_letters + string.digits
                for i in range(length):
                    generated.append(passlist[random.randint(0, len(passlist) - 1)])

            elif state == 4:
                passlist = string.ascii_letters + string.digits + string.punctuation
                for i in range(length):
                    generated.append(passlist[random.randint(0, len(passlist) - 1)])

            else:
                raise Exception
        except Exception as e:
            print(
                "Please confirm your state value, max state value is 4 and min state value is 1, and program does not have any lenght limitation.")
            return

        random.shuffle(generated)
        generated = "".join(generated)

        print("Generated:", generated)


def main():
    fire.Fire(Password().generate_password, name='generate')


if __name__ == '__main__':
    main()
