# switcher
def a():
    return "hello"
def b():
    return "hello b"
def xyz(x):
    switcher = {
        0: a(),
        1: b(),
        2: "two",
        3:"three"
        4:"four"
    }
    return switcher.get(x, "option not available")


n = int(input('enter the choice'))
c = xyz(n)
print(c)
