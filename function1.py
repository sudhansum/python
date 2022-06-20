def greet():
    print("hello")
    print("good morning")


greet()


def add(x, y):
    s = x + y
    # print(s)
    return (s)


n = int(input('enter the number n'))
m = int(input('enter the number m'))
k = add(n, m)
print("the value of k is ",k)
