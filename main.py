import pytest
import os


def main():
    testdir = os.getcwd() + '\\tests'
    print(testdir)

    args = ['--verbose',  # detailed view
            '-s',  # stdout view
            '--capture=sys',
            '-rp',
            testdir]  # tests location
    pytest.main(args=args)


if __name__ == '__main__':
    main()
