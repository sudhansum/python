
a =10
b = 8

if(a>b and a==10):
    print("hello")
else:
    print("bye")

if(a>b and a!=10):
    print("hello")
else:
    print("not equal to bye")

a =12
b = 28

if(a>b and a==10):
    print("hello")
else:
    print("bye")

if(a>b or a!=12):
    print("hello or")
else:
    print("bye or")

if(not a>b):
    print("hello not")
else:
    print("bye not")


a = 5
b = 10
if(a is b):
    print("pointing same object")
else:
    print("not pointing same object")

a = 10
b = 10
if(a is not b):
    print("pointing same object is not")
else:
    print("not pointing same object else" )


a =[1,2,3,4,5]
if(2 not in a):
    print("is present")
else:
    print("not available")

a =[1,2,3,4,5]
if(2 in a):
    print("is present in a")
else:
    print("not available")

