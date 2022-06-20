import sys


t = ("deepali",'agarwal',10,2.4)
print(t,"tuples are immutable")
print()
print(t[1],'prints the first element')
print()
print(len(t),'prints the length')
print()
print(dir(t))
print('dir(t) prints the fn we can use')
print()
print('tuples use less memory')
print(sys.getsizeof(t))
print()
lst = ["deepali",'agarwal',10,2.4]
print(sys.getsizeof(lst))
print("sys module used to get the size")
print()
t1 = tuple('agarwal')
print(t1,"converts into individual tuples")
print()
b =()
print(b,'creates a blank tuple')
print()
lst2 = []
print(lst2)
print()
t3 =(t,t1)
print(t3)
t4 = t+t1
print(t4)
print(t1[1:],"to access specific index value")
print(t[::-1],"to print in the reverse direction")



