import pytest
import os


def main():
    testdir = str(os.getcwd() + '\\tests\\')
    print(testdir)

    args = [testdir,
            '--verbose',  # detailed view
            '--capture=sys',
            '-s']  # print stdout
    pytest.main(args=args)


if __name__ == '__main__':
    main()
