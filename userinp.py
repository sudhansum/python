# is used for single line comment
"""used for multiline
comments"""

x = int(input("enter the 1st number"))
print(x)
y = int(input("enter the 2nd number"))
print(y)

a,b,c = input("enter a b c ").split()
print("value of a =",a)
print("value of b =",b)
print("value of c =", c)
print("value of a is{} b is {} and c is {}".format(a,b,c))

a1,b1 = input("enter the 2 numbers").split()
a = int(a1)
b=int(b1)
print("addion is c is{} mul m is {} divn d is {}".format(a+b,a*b,a/b))
