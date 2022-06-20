

import operator

n =input("enter the value")
m =input("enter the value")
c = operator.add(n,m)
print(c)
# f = operator.truediv(n,m)
# print(f)
g = operator.floordiv(n,m)
print(g)
i = operator.mod(n,m)
print(i)
if(operator.lt(n,m)):
    print("lt is less than")
else:
    print("n is greater")
