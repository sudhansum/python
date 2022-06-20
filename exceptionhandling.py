

a = int(input())
b = int(input())
try:
    c = a/b
    print("Div =",c)
except ZeroDivisionError as e:
    print(e)
# print("will this be executed if the denominator is 0")
# print("keywords-zero div erro, val error, index erro")
# print("try except else raise finally")
try:
    a = int(input())
    b = int(input())
    c = a/b
    print("Div =",c)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)


with open("demo.txt") as fr:
    print(fr.closed)
    print(fr.read())
print(fr.closed)
