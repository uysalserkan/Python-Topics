import fire

r"""
Burası nereye gidiyor..


USAGE: 123123


OPTIONS: 123123asdasd
"""

def single(text: str, num: int):
    """Bu fonksiyon gelen texti gelen sayı kadar bastırır."""
    i = 0
    while i < num:
        print(str(text))
        i += 1
    print("End of function.")


def main():
    fire.Fire(single, name="--s")


if __name__ == '__main__':
    main()
