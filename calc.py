def add():
    print('this is addition', __name__)


def sub():
    print('this is subtraction',__name__)


def main():
    print('in calc main')
    add()
    sub()


if __name__ == "__main__":
    main()
