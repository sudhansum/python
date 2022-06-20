# strings built in function and methods
#acessing the function and method are different ex.length fn, method needs an object

s ="hello world"
dir(s) # it tells you number of methods with the string class
       # s.upper is a method only for string class
       # len(s) function used to find the length will work for all, independent of any class
       #funtion : len() str() ord() chr(),sorted()

x = len(s)
print(x)

k= 1234
p = str(k)
print(type(p),type(k))

r = input("enter any char")
print("char=",r,"UNICODE=",ord(r))

print(chr(65))