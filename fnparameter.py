# def update(x):
#     x = 8
#     print("x",x)
# 
# a= 10
# update(a)
# print("a", a)

def add(a, b):
    c = a + b
    print(c)

add(4, 5)


def person(name, age):
    print(name)
    print(age)


person("test", 29)
person(age=28, name="test")


def variable_lengtharg(a, *b):  # to accept multiple values we use *b
    c = a
    for i in b:
        c = c+i
        print(c)


variable_lengtharg(4, 5, 6, 7, 8, )

def variable_lengthargs( *b):  # we can use one variable also with *b
    c = 0
    for i in b:
        c = c+i
        print(c)


variable_lengtharg(4, 5, 6, 7, 8, )
