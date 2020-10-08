import fire


class Operations(object):

    @staticmethod
    def whack(n=1):
        """Prints "whack!" n times."""
        return ' '.join('whack!' for _ in range(n))

    @staticmethod
    def bang(noise='bang'):
        """Makes a loud noise."""
        return '{noise} bang!'.format(noise=noise)


def main():
    fire.Fire(Operations(), name='op')


if __name__ == '__main__':
    main()
