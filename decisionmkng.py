
"""if():
    print("hello")
    print('bye')
else:
    print('hey')"""

a=50
b= 20
c =30

if(a<b):
    print('a is less than b')
else:
    print('a is greater than b')
print("bye")

if(a<b):
    print('a is less than b')
elif (a<c):
    print("a is less than c")
elif(b<c):
    print("b is less than c")
else:
    print('a is greater than b')


d = 12
if(d<15):
    if(d<10):
        print("less than")
    if(d<8):
        print("less than 20")
    else:
        print("less than d")
else:
        print('else block')

