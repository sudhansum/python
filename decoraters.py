""" DECORATORS ARE FUNCTIONS USED TO MODIFY THE FUNCTIONS IN ANOTHER FILE"""


def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a > b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = smart_div(div)
div(2, 4)
