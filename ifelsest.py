""" if (condition):
        statement
    else:
        statement """

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"
# The else keyword catches anything which isn't caught by the preceding conditions.


a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("if the previous conditions were not true, then try this condition")
else:
    print("catches anything which isn't caught by the preceding conditions")

d = 8
if (d < 15):
    if (d < 10):
        print("hey")
    if (d < 8):
        print("hello")
    else:
        print("inner loop")
else:
    print("outer loop")

"""Ternary Operators, or Conditional Expressions."""
a = 2
b = 25
print("A") if a > b else print("b")

a = 25
b = 25
print("A") if a > b else print("=") if a == b else print("B")


