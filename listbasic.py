a = ["deepali",'agarwal',10,2.4]
print(a,"can have multiple data")
print(a[1],'gives the values at postn 1')
#print(a[4],'gives index error')
print(a[1:],"prints from start index to end")
print(a[1:3],'prints from 1 to 3 index')
print(a[-1],'prints from the end')
print(a[:-1],'prints in reverse all the vals')

b = [30,40,'youtube']
print(b)

c = a+b 
print(c,'adds tow lists')

b.insert(3,10)
print(b)
b.insert(5,19)
print(b)
b.remove(30)
print(b)
b.append(56)
print(b)
b.append(58)
print(b)
b.pop()
print(b)
del b[2:4]
print(b)
b.extend([23,31,'pen'])
print(b)
d = [29,12,25,19,23,84]
print(max(d))
print(min(d))
d.sort()
print(d)